#
# Fedora spec file for php-henrikbjorn-lurker
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     flint
%global github_name      Lurker
%global github_version   1.2.0
%global github_commit    712d3ef19bef161daa2ba0e0237c6b875587a089

%global composer_vendor  henrikbjorn
%global composer_project lurker

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "symfony/config" : "^2.2|^3.0"
# "symfony/event-dispatcher" : "^2.2|^3.0"
#     NOTE: Min version not 2.2 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Resource watcher

Group:         Development/Libraries
License:       MIT
URL:           http://lurker.rtfd.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/config) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/config) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.2.0)
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/config) <  %{symfony_max_ver}
Requires:      php-composer(symfony/config) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 1.2.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Resource tracking for PHP. Watch files and/or directories.

Autoloader: %{phpdir}/Lurker/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Lurker/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Lurker\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Symfony3/Component/Config/autoload.php',
        '%{phpdir}/Symfony/Component/Config/autoload.php',
    ),
    array(
        '%{phpdir}/Symfony3/Component/EventDispatcher/autoload.php',
        '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    ),
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Lurker %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Lurker/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Lurker\\Tests\\', __DIR__.'/tests/Lurker/Tests');
BOOTSTRAP

: Skip tests known to fail
sed \
    -e 's/function testDoesNotTrackMissingFiles/function SKIP_testDoesNotTrackMissingFiles/' \
    -e 's/function testDoesNotTrackMissingDirectories/function SKIP_testDoesNotTrackMissingDirectories/' \
    -i tests/Lurker/Tests/Tracker/TrackerTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --bootstrap bootstrap.php --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Lurker


%changelog
* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Update to 1.2.0
- Add max version to BuildRequires
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
