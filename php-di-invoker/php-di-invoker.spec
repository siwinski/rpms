#
# Fedora spec file for php-di-invoker
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     PHP-DI
%global github_name      Invoker
%global github_version   1.2.0
%global github_commit    9949fff87fcf14e8f2ccfbe36dac1e5921944c48

%global composer_vendor  php-di
%global composer_project invoker

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "container-interop/container-interop": "~1.1"
%global container_interop_min_ver 1.1
%global container_interop_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Generic and extensible callable invoker

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-di-invoker-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(container-interop/container-interop) >= %{container_interop_min_ver}
## phpcompatinfo (computed from version 1.2.0)
BuildRequires: php-reflection
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                                     >= %{php_min_ver}
Requires:      php-composer(container-interop/container-interop) >= %{container_interop_min_ver}
Requires:      php-composer(container-interop/container-interop) <  %{container_interop_max_ver}
# phpcompatinfo (computed from version 1.2.0)
Requires:      php-reflection
# Autoloader
Requires:      php-composer(symfony/class-loader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project}           = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Invoker/autoload.php


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

$fedoraClassLoader->addPrefix('Invoker\\', dirname(__DIR__));

// Required dependency
require_once '%{phpdir}/Interop/Container/autoload.php';

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}/Invoker
cp -rp src/* %{buildroot}%{phpdir}/Invoker/


%check
%if %{with_tests}
: Make PSR-0 tests
mkdir -p tests-psr0/Invoker
ln -s ../../tests tests-psr0/Invoker/Test

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
$fedoraClassLoader = require '%{buildroot}%{phpdir}/Invoker/autoload.php';
$fedoraClassLoader->addPrefix('Invoker\\Test\\', __DIR__.'/tests-psr0');
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
%{phpdir}/Invoker


%changelog
* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 1.2.0-1
- Initial package
