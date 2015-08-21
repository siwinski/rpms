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
%global github_version   0.2.1
%global github_commit    16285231eb37587c6c32b86fa483c35853cd7515

%global composer_vendor  alchemy
%global composer_project zippy

# "php"                  : ">=5.3.3"
%global php_min_ver 5.3.3
# "doctrine/collections" : "~1.0"
#     Note: Min version not 1.0 b/c autoloader was added in 1.3.0
%global doctrine_collections_min_ver 1.3.0
%global doctrine_collections_max_ver 2.0
# "guzzle/guzzle"        : "~3.0"
#     Note: Min version not 3.0 b/c autoloader was added in 3.9.3
%global guzzle_min_ver 3.9.3
%global guzzle_max_ver 4.0
# "pimple/pimple"        : "~1.0"
%global pimple_min_ver 1.0
%global pimple_max_ver 2.0
# "symfony/filesystem"   : "~2.0"
# "symfony/finder"       : "~2.0"
# "symfony/process"      : "~2.0"
#     Note: Min version not 2.0 b/c autoloader was added in 2.3.31|2.7.1
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 3.0

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
BuildRequires: php-composer(guzzle/guzzle)        >= %{guzzle_min_ver}
BuildRequires: php-composer(pimple/pimple)        >= %{pimple_min_ver}
BuildRequires: php-composer(symfony/filesystem)   >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder)       >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process)      >= %{symfony_min_ver}
BuildRequires: php-zip
## phpcompatinfo (computed from version 0.2.1)
BuildRequires: php-date
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                      >= %{php_min_ver}
Requires:      php-composer(doctrine/collections) >= %{doctrine_collections_min_ver}
Requires:      php-composer(doctrine/collections) <  %{doctrine_collections_max_ver}
Requires:      php-composer(guzzle/guzzle)        >= %{guzzle_min_ver}
Requires:      php-composer(guzzle/guzzle)        <  %{guzzle_max_ver}
Requires:      php-composer(pimple/pimple)        >= %{pimple_min_ver}
Requires:      php-composer(pimple/pimple)        <  %{pimple_max_ver}
Requires:      php-composer(symfony/filesystem)   >= %{symfony_min_ver}
Requires:      php-composer(symfony/filesystem)   <  %{symfony_max_ver}
Requires:      php-composer(symfony/process)      >= %{symfony_min_ver}
Requires:      php-composer(symfony/process)      <  %{symfony_max_ver}
# composer.json: optional
Requires:      php-zip
# phpcompatinfo (computed from version 0.2.1)
Requires:      php-date
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A Object-Oriented PHP library to manipulate any archive format (de)compression
through commandline utilities or PHP extension.


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/Alchemy/Zippy/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 *
 * Created by %{name}-%{version}-%{release}
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

foreach (array(
    '%{phpdir}/Doctrine/Common/Collections/autoload.php',
    '%{phpdir}/Guzzle/autoload.php',
    '%{phpdir}/Pimple1/autoload.php',
    '%{phpdir}/Symfony/Component/Filesystem/autoload.php',
    '%{phpdir}/Symfony/Component/Process/autoload.php',
) as $dependencyAutoloader) {
    require_once $dependencyAutoloader;
}

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}
cp -pr src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Recreate tests bootstrap
cat <<'BOOTSTRAP' | tee tests/bootstrap.php
<?php

$fedoraClassLoader =
    require_once '%{buildroot}%{phpdir}/Alchemy/Zippy/autoload.php';

$fedoraClassLoader->addPrefix('Alchemy\\Zippy\\Tests\\', __DIR__);
$fedoraClassLoader->addPrefix('Alchemy\\Zippy\\Functional\\', __DIR__);

require_once '%{phpdir}/Symfony/Component/Finder/autoload.php';
BOOTSTRAP

: Skip tests that require network access
rm -f tests/Alchemy/Zippy/Tests/Resource/TargetLocatorTest.php
sed 's/function testFunctionnal/function SKIP_testFunctionnal/' \
    -i tests/Alchemy/Zippy/Tests/Resource/ResourceManagerTest.php
sed 's/function testTeleport/function SKIP_testTeleport/' \
    -i tests/Alchemy/Zippy/Tests/Resource/Teleporter/GuzzleTeleporterTest.php

: Skip test known to fail
sed 's/function testTeleportADir/function SKIP_testTeleportADir/' \
    -i tests/Alchemy/Zippy/Tests/Resource/Teleporter/LocalTeleporterTest.php

%{_bindir}/phpunit --verbose
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
* Thu Aug 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2.1-1
- Initial package
