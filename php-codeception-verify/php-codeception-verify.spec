#
# Fedora spec file for php-codeception-verify
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Codeception
%global github_name      Verify
%global github_version   0.4.0
%global github_commit    8a17273017e23a866df3fa2ad2b4182b7ce354f0

%global composer_vendor  codeception
%global composer_project verify

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       BDD assertion library for PHPUnit

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.4.0)
BuildRequires: php(language) >= 5.3.0
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-reflection
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# phpcompatinfo (computed from version 0.4.0)
Requires:      php(language) >= 5.3.0
Requires:      php-reflection
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
BDD Assertions for PHPUnit and Codeception

This is very tiny wrapper for PHPUnit assertions, that are aimed to make tests
a bit more readable. With BDD assertions influenced by Chai, Jasmine, and
RSpec your assertions would be a bit closer to natural language.

Autoloader: %{phpdir}/Codeception/autoload-verify.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/Codeception/autoload-verify.php src/
cat <<'AUTOLOAD' | tee -a src/Codeception/autoload-verify.php

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/function.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Codeception
cp -rp src/Codeception/* %{buildroot}%{phpdir}/Codeception/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Codeception/autoload-verify.php \
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
%dir %{phpdir}/Codeception
     %{phpdir}/Codeception/Verify.php
     %{phpdir}/Codeception/autoload-verify.php
     %{phpdir}/Codeception/function.php


%changelog
* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Initial package
