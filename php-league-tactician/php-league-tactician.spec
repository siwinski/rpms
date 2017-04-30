#
# Fedora spec file for php-league-tactician
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      tactician
%global github_version   1.0.2
%global github_commit    1f3aaad497f07a8bef147a37c7e3f2f7c23fcd21

%global composer_vendor  league
%global composer_project tactician

# "php": ">=5.5"
%global php_min_ver 5.5
# "mockery/mockery": "~0.9"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A small, flexible command bus. Handy for building service layers

Group:         Development/Libraries
License:       MIT
URL:           http://tactician.thephpleague.com/

# GitHub export does not include tests.
# Run php-league-tactician-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.0.2)
BuildRequires: php-date
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.2)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Tactician is a command bus library. It tries to make using the command pattern
in your application easy and flexible.

You can use Tactician for all types of command inputs but it especially targets
service layers.

Autoloader: %{phpdir}/League/Tactician/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\Tactician\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League
cp -rp src %{buildroot}%{phpdir}/League/Tactician


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/League/Tactician/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\Tactician\\Tests\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required([
    __DIR__.'/tests/Fixtures/Command/CommandWithoutNamespace.php',
    '%{phpdir}/Mockery/autoload.php',
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
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
%dir %{phpdir}/League
     %{phpdir}/League/Tactician


%changelog
* Sun Apr 30 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.2-1
- Initial package
