#
# Fedora spec file for php-mnapoli-phpunit-easymock
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     mnapoli
%global github_name      phpunit-easymock
%global github_version   0.2.0
%global github_commit    65431d92ec3f11dcafd1f4304e38612e12987d4e

%global composer_vendor  mnapoli
%global composer_project phpunit-easymock

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "phpunit/phpunit-mock-objects": "~2.0"
%global phpunit_mock_objects_min_ver 2.0
%global phpunit_mock_objects_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Helpers to build PHPUnit mocks

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-mnapoli-phpunit-easymock-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(phpunit/phpunit-mock-objects) >= %{phpunit_mock_objects_min_ver}
## phpcompatinfo (computed from version 0.2.0)
BuildRequires: php-reflection
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                              >= %{php_min_ver}
Requires:      php-composer(phpunit/phpunit-mock-objects) >= %{phpunit_mock_objects_min_ver}
Requires:      php-composer(phpunit/phpunit-mock-objects) <  %{phpunit_mock_objects_max_ver}
# phpcompatinfo (computed from version 0.2.0)
#     <none>
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/EasyMock/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('EasyMock\\', dirname(__DIR__));

// Required dependency
require_once '%{phpdir}/PHPUnit/Framework/MockObject/Autoload.php';

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}/EasyMock
cp -rp src/* %{buildroot}%{phpdir}/EasyMock/


%check
%if %{with_tests}
: Make PSR-0 tests
mkdir -p tests-psr0/EasyMock
ln -s ../../tests tests-psr0/EasyMock/Test

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
$fedoraClassLoader = require '%{buildroot}%{phpdir}/EasyMock/autoload.php';
$fedoraClassLoader->addPrefix('EasyMock\\Test\\', __DIR__.'/tests-psr0');
BOOTSTRAP

: Run tests
%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/
     %{phpdir}/


%changelog
* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 0.2.0-1
- Initial package
