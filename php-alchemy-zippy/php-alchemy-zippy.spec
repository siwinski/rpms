#
# Fedora spec file for php-alchemy-zippy
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     alchemy-fr
%global github_name      Zippy
%global github_version   0.4.0
%global github_commit    28b7c0e9db9755889d1e6b3a3ca237abcbd98693

%global composer_vendor  alchemy
%global composer_project zippy

# "php": ">=5.5"
%global php_min_ver 5.5
# "doctrine/collections": "~1.0"
#     NOTE: Min version not 1.0 b/c autoloader required
%global doctrine_collections_min_ver 1.3.0
%global doctrine_collections_max_ver 2.0
# "guzzle/guzzle": "~3.0"
# "guzzlehttp/guzzle": "^6.0"
#     NOTE: Min version not 3.0 to force version 6
%global guzzle_min_ver 6.0
%global guzzle_max_ver 7.0
# "symfony/filesystem": "^2.0.5|^3.0"
# "symfony/finder": "^2.0.5|^3.0"
# "symfony/process": "^2.1|^3.0"
#     NOTE: Min version not 2.1 b/c autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Zippy, the archive manager companion

Group:         Development/Libraries
License:       MIT
URL:           https://zippy.readthedocs.org/

# GitHub export does not include docs or tests.
# Run php-alchemy-zippy-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language)                      >= %{php_min_ver}
BuildRequires: php-composer(doctrine/collections) >= %{doctrine_collections_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle)    >= %{guzzle_min_ver}
BuildRequires: php-composer(symfony/filesystem)   <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/filesystem)   >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder)       <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder)       >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process)      <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/process)      >= %{symfony_min_ver}
BuildRequires: php-mbstring
BuildRequires: php-zip
## phpcompatinfo (computed from version 0.4.0)
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                      >= %{php_min_ver}
Requires:      php-composer(doctrine/collections) >= %{doctrine_collections_min_ver}
Requires:      php-composer(doctrine/collections) <  %{doctrine_collections_max_ver}
Requires:      php-composer(symfony/filesystem)   >= %{symfony_min_ver}
Requires:      php-composer(symfony/filesystem)   <  %{symfony_max_ver}
Requires:      php-composer(symfony/process)      >= %{symfony_min_ver}
Requires:      php-composer(symfony/process)      <  %{symfony_max_ver}
Requires:      php-mbstring
# composer.json: optional
Requires:      php-zip
# phpcompatinfo (computed from version 0.4.0)
Requires:      php-date
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Weak dependencies
Suggests:      php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A Object-Oriented PHP library to manipulate any archive format (de)compression
through command-line utilities or PHP extension.


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove legacy Guzzle
rm -f \
    src/Resource/Reader/Guzzle/LegacyGuzzle* \
    src/Resource/Teleporter/LegacyGuzzle*


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

$fedoraClassLoader->addPrefix('Alchemy\\Zippy\\', dirname(dirname(__DIR__)));

// Dependencies (autoloader => required)
foreach(array(
    // Required dependencies
    '%{phpdir}/Doctrine/Common/Collections/autoload.php'  => true,
    '%{phpdir}/Symfony/Component/Filesystem/autoload.php' => true,
    '%{phpdir}/Symfony/Component/Process/autoload.php'    => true,
    // Optional dependency
    '%{phpdir}/GuzzleHttp6/autoload.php'                  => false,
) as $dependencyAutoloader => $required) {
    if ($required || file_exists($dependencyAutoloader)) {
        require_once $dependencyAutoloader;
    }
}

return $fedoraClassLoader;
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Alchemy/Zippy
cp -pr src/* %{buildroot}%{phpdir}/Alchemy/Zippy/


%check
%if %{with_tests}
: Mock tests PSR-0
mkdir -p tests-psr0/Alchemy/Zippy
ln -s ../../../tests/Functional tests-psr0/Alchemy/Zippy/Functional
ln -s ../../../tests/Tests tests-psr0/Alchemy/Zippy/Tests

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php

$fedoraClassLoader =
    require_once '%{buildroot}%{phpdir}/Alchemy/Zippy/autoload.php';

$fedoraClassLoader->addPrefix('Alchemy\\Zippy\\Functional\\', __DIR__.'/tests-psr0');
$fedoraClassLoader->addPrefix('Alchemy\\Zippy\\Tests\\', __DIR__.'/tests-psr0');

require_once '%{phpdir}/GuzzleHttp6/autoload.php';
require_once '%{phpdir}/Symfony/Component/Finder/autoload.php';
BOOTSTRAP

: Skip tests that require network access
rm -f tests/Tests/Resource/TargetLocatorTest.php
sed 's/function testFunctionnal/function SKIP_testFunctionnal/' \
    -i tests/Tests/Resource/ResourceManagerTest.php
sed 's/function testTeleport/function SKIP_testTeleport/' \
    -i tests/Tests/Resource/Teleporter/GuzzleTeleporterTest.php

: Skip test known to fail
rm -f tests/Tests/Resource/Teleporter/GuzzleTeleporterTest.php
sed 's/function testTeleportADir/function SKIP_testTeleportADir/' \
    -i tests/Tests/Resource/Teleporter/LocalTeleporterTest.php

%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Alchemy/
     %{phpdir}/Alchemy/Zippy


%changelog
* Tue Aug 02 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Initial package
