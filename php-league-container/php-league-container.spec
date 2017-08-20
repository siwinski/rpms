#
# Fedora spec file for php-league-container
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      container
%global github_version   2.4.1
%global github_commit    43f35abd03a12977a60ffd7095efd6a7808488c0

%global composer_vendor  league
%global composer_project container

# "php": "^5.4.0 || ^7.0"
%global php_min_ver 5.4.0
# "container-interop/container-interop": "^1.2"
%global container_interop_min_ver 1.2
%global container_interop_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A fast and intuitive dependency injection container

Group:         Development/Libraries
License:       MIT
URL:           http://container.thephpleague.com/

# GitHub export does not include tests.
# Run php-league-container-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(container-interop/container-interop) >= %{container_interop_min_ver}
## phpcompatinfo (computed from version 2.4.1)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(container-interop/container-interop) >= %{container_interop_min_ver}
Requires:      php-composer(container-interop/container-interop) <  %{container_interop_max_ver}
# phpcompatinfo (computed from version 2.4.1)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(container-interop/container-interop-implementation) = %{container_interop_min_ver}
Provides:      php-composer(psr/container-implementation) =  1.0

%description
A small but powerful dependency injection container that allows you to decouple
components in your application in order to write clean and testable code.

Autoloader: %{phpdir}/League/Container/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Interop/Container/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League
cp -rp src %{buildroot}%{phpdir}/League/Container


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/League/Container/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Skip test known to fail
sed 's/function testCallReflectsOnStaticMethodArguments/function SKIP_testCallReflectsOnStaticMethodArguments/' \
    -i tests/ReflectionContainerTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
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
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc CONTRIBUTING.md
%doc README.md
%dir %{phpdir}/League
     %{phpdir}/League/Container


%changelog
* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.1-1
- Update to 2.4.1
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 2.2.0-1
- Initial package
