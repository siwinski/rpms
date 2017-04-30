#
# Fedora spec file for php-league-event
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      event
%global github_version   2.1.2
%global github_commit    e4bfc88dbcb60c8d8a2939a71f9813e141bbe4cd

%global composer_vendor  league
%global composer_project event

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "phpspec/phpspec": "~2.0.0"
%global phpspec_min_ver 2.0.0
%global phpspec_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Event package for your app and domain

Group:         Development/Libraries
License:       MIT
URL:           http://event.thephpleague.com/

# GitHub export does not include tests.
# Run php-league-event-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpspec/phpspec) <  %{phpspec_max_ver}
BuildRequires: php-composer(phpspec/phpspec) >= %{phpspec_min_ver}
## phpcompatinfo (computed from version 2.1.2)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.1.2)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The `league/event` package provides a versatile tool to manage events in your
app or domain. The package supports string based and class based events, as
well as Closure or class based listeners. This makes the package ideal for
regular event management but also allows for a clean event-driven style of
programming.

Autoloader: %{phpdir}/League/Event/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Fix license filename
mv LICENCE LICENSE


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\Event\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League
cp -rp src %{buildroot}%{phpdir}/League/Event


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/League/Event/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('League\\Event\\Stub\\', __DIR__.'/stubs');
BOOTSTRAP

: Rewrite phpspec config
mv phpspec.yml phpspec.yml.dist
cat <<'PHPSPEC' | tee phpspec.yml
bootstrap: bootstrap.php
formatter.name: pretty
PHPSPEC

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpspec run --verbose || RETURN_CODE=1
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
     %{phpdir}/League/Event


%changelog
* Sun Apr 30 2017 Shawn Iwinski <shawn@iwin.ski> - 2.1.2-1
- Initial package
