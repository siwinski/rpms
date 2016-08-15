#
# Fedora spec file for php-behat-gherkin
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Behat
%global github_name      Gherkin
%global github_version   4.4.1
%global github_commit    1576b485c0f92ef6d27da9c4bbfc57ee30cf6911

%global composer_vendor  behat
%global composer_project gherkin

# "php": ">=5.3.1"
%global php_min_ver 5.3.1
# "symfony/yaml": "~2.1"
#     NOTE: Min version not 2.1 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%global phpdir   %{_datadir}/php

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Gherkin DSL parser for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://behat.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
## phpcompatinfo (computed from version 4.4.1)
BuildRequires: php-date
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/yaml) >= %{symfony_min_ver}
Requires:      php-composer(symfony/yaml) <  %{symfony_max_ver}
# phpcompatinfo (computed from version 4.4.1)
Requires:      php-date
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create library autoloader
cat <<'AUTOLOAD' | tee src/Behat/Gherkin/autoload.php
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

$fedoraClassLoader->addPrefix('Behat\\Gherkin\\', dirname(dirname(__DIR__)));

// Optional dependency
if (file_exists('%{phpdir}/Symfony/Component/Yaml/autoload.php')) {
    require_once '%{phpdir}/Symfony/Component/Yaml/autoload.php';
}

return $fedoraClassLoader;
AUTOLOAD


%install
mkdir -p  %{buildroot}%{phpdir}
cp -pr src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Make PSR-0 tests
ln -s tests Tests

: Create tests bootstrap
cat <<'AUTOLOAD' | tee bootstrap.php
<?php
$fedoraClassLoader =
    require_once '%{buildroot}%{phpdir}/Behat/Gherkin/autoload.php';
$fedoraClassLoader->addPrefix('Tests\\Behat\\', __DIR__);
AUTOLOAD

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
%dir %{phpdir}/Behat
     %{phpdir}/Behat/Gherkin


%changelog
* Mon Aug 15 2016 Shawn Iwinski <shawn@iwin.ski> - 4.4.1-1
- Initial package
