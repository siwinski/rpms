#
# Fedora spec file for php-behat-mink-browserkit-driver
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     minkphp
%global github_name      MinkBrowserKitDriver
%global github_version   1.3.0
%global github_commit    da47df1593dac132f04d24e7277ef40d33d9f201

%global composer_vendor  behat
%global composer_project mink-browserkit-driver

# "php": ">=5.3.6"
%global php_min_ver 5.3.6
# "behat/mink": "~1.7@dev"
%global mink_min_ver 1.7
%global mink_max_ver 2.0
# "silex/silex": "~1.2"
%global silex_min_ver 1.2
%global silex_max_ver 2.0
# "symfony/browser-kit": "~2.3"
# "symfony/dom-crawler": "~2.3"
#     NOTE: Min version not 2.3 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%global phpdir   %{_datadir}/php
%global testsdir %{_datadir}/tests

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Symfony BrowserKit driver for Mink framework

Group:         Development/Libraries
License:       MIT
URL:           http://mink.behat.org/en/latest/drivers/browserkit.html
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-behat-mink-driver-testsuite
## composer.json
BuildRequires: php(language)                     >= %{php_min_ver}
BuildRequires: php-composer(behat/mink)          >= %{mink_min_ver}
BuildRequires: php-composer(silex/silex)         >= %{silex_min_ver}
BuildRequires: php-composer(symfony/browser-kit) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.3.0)
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                     >= %{php_min_ver}
Requires:      php-composer(behat/mink)          >= %{mink_min_ver}
Requires:      php-composer(behat/mink)          <  %{mink_max_ver}
Requires:      php-composer(symfony/browser-kit) >= %{symfony_min_ver}
Requires:      php-composer(symfony/browser-kit) <  %{symfony_max_ver}
Requires:      php-composer(symfony/dom-crawler) >= %{symfony_min_ver}
Requires:      php-composer(symfony/dom-crawler) <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.3.0)
Requires:      php-pcre
Requires:      php-reflection

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
BrowserKitDriver provides a bridge for the Symfony BrowserKit [1] component.
BrowserKit is a browser emulator provided by the Symfony project [2].

Autoloader: %{phpdir}/Behat/Mink/Driver/autoload-browserkit.php

[1] http://symfony.com/components/BrowserKit
[2] http://symfony.com/


%prep
%setup -qn %{github_name}-%{github_commit}

: Create library autoloader
cat <<'AUTOLOAD' | tee src/autoload-browserkit.php
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

$fedoraClassLoader->addPrefix(
    'Behat\\Mink\\Driver\\',
    dirname(dirname(dirname(__DIR__)))
);

require_once '%{phpdir}/Behat/Mink/autoload.php';
require_once '%{phpdir}/Symfony/Component/BrowserKit/autoload.php';
require_once '%{phpdir}/Symfony/Component/DomCrawler/autoload.php';

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p  %{buildroot}%{phpdir}/Behat/Mink/Driver
cp -pr src/* %{buildroot}%{phpdir}/Behat/Mink/Driver/


%check
%if %{with_tests}
: Setup driver testsuite
mkdir -p vendor/behat/mink/
ln -s %{testsdir}/php-behat-mink-driver-testsuite vendor/behat/mink/driver-testsuite

: Make PSR-0 tests
mkdir -p tests-psr0/Behat/Mink/Tests
ln -s ../../../../tests tests-psr0/Behat/Mink/Tests/Driver

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
$fedoraClassLoader =
    require '%{buildroot}%{phpdir}/Behat/Mink/Driver/autoload-browserkit.php';
$fedoraClassLoader->addPrefix('Behat\\Mink\\Tests\\Driver\\', __DIR__ . '/tests-psr0');

require_once '%{phpdir}/Silex/autoload.php';
require_once __DIR__ . '/vendor/behat/mink/driver-testsuite/bootstrap.php';
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
%{phpdir}/Behat/Mink/Driver/autoload-browserkit.php
%{phpdir}/Behat/Mink/Driver/BrowserKitDriver.php


%changelog
* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Initial package
