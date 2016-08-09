#
# Fedora spec file for php-consolidation-log
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation-org
%global github_name      log
%global github_version   1.0.3
%global github_commit    74ba81b4edc585616747cc5c5309ce56fec41254

%global composer_vendor  consolidation
%global composer_project log

# "php": ">=5.5.0"
%global php_min_ver 5.5.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.0-8
%global psr_log_max_ver 2.0
# "symfony/console": "~2.5|~3.0"
#     NOTE: Min version not 2.5 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Improved Psr-3 / Psr\\Log logger based on Symfony Console components

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                 >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
#BuildRequires: php-composer(psr/log)         >= %%{psr_log_min_ver}
BuildRequires: php-PsrLog                    >= %{psr_log_min_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.0.3)
### <none>
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
#Requires:      php-composer(psr/log)         >= %%{psr_log_min_ver}
Requires:      php-PsrLog                    >= %{psr_log_min_ver}
Requires:      php-composer(psr/log)         <  %{psr_log_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.0.3)
## <none>
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Consolidation\Log provides a Psr-3 compatible logger that provides styled log
output to the standard error (stderr) stream. By default, styling is provided
by the SymfonyStyle class from the Symfony Console component; however,
alternative stylers may be provided if desired.

Autoloader: %{phpdir}/Consolidation/Log/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
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

$fedoraClassLoader->addPrefix('Consolidation\\Log\\', dirname(dirname(__DIR__)));

// Required dependencies
require_once '%{phpdir}/Psr/Log/autoload.php';
require_once '%{phpdir}/Symfony/Component/Console/autoload.php';

return $fedoraClassLoader;
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation/Log
cp -rp src/* %{buildroot}%{phpdir}/Consolidation/Log/


%check
%if %{with_tests}
: Mock PSR-0 tests
mkdir -p tests-psr0/Consolidation
ln -s ../../tests/src tests-psr0/Consolidation/TestUtils

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
$fedoraClassLoader =
    require '%{buildroot}%{phpdir}/Consolidation/Log/autoload.php';
$fedoraClassLoader->addPrefix('Consolidation\\TestUtils\\', __DIR__.'/tests-psr0');
BOOTSTRAP

%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Consolidation
     %{phpdir}/Consolidation/Log


%changelog
* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.0.3-1
- Initial package
