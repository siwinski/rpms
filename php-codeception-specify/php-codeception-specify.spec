#
# Fedora spec file for php-codeception-specify
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Codeception
%global github_name      Specify
%global github_version   0.4.6
%global github_commit    21b586f503ca444aa519dd9cafb32f113a05f286

%global composer_vendor  codeception
%global composer_project specify

# "php": ">=5.4.0"
%global php_min_ver 5.4
# "myclabs/deep-copy": "~1.1"
%global myclabs_deep_copy_min_ver 1.1
%global myclabs_deep_copy_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       BDD code blocks for PHPUnit and Codeception

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
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(myclabs/deep-copy) <  %{myclabs_deep_copy_max_ver}
BuildRequires: php-composer(myclabs/deep-copy) >= %{myclabs_deep_copy_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.4.6)
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(myclabs/deep-copy) <  %{myclabs_deep_copy_max_ver}
Requires:      php-composer(myclabs/deep-copy) >= %{myclabs_deep_copy_min_ver}
# phpcompatinfo (computed from version 0.4.6)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer()
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
BDD style code blocks for PHPUnit / Codeception

Specify allows you to write your tests in more readable BDD style, the
same way you might have experienced with Jasmine. Inspired by MiniTest
of Ruby now you combine BDD and classical TDD style in one test.

Autoloader: %{phpdir}/Codeception/Specify/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/Codeception/Specify/autoload.php src/
cat <<'AUTOLOAD' | tee -a src/Codeception/Specify/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/DeepCopy/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Codeception %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Codeception/Specify/autoload.php';
\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/tests/_support/SpecifyUnitTest.php'
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
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
     %{phpdir}/Codeception/Specify
     %{phpdir}/Codeception/Specify.php


%changelog
* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-1
- Initial package
