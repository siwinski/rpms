#
# Fedora spec file for php-henrikbjorn-lurker
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     flint
%global github_name      Lurker
%global github_version   1.1.0
%global github_commit    ab45f9cefe600065cc3137a238217598d3a1d062

%global composer_vendor  henrikbjorn
%global composer_project lurker

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "symfony/config": "~2.2"
# "symfony/event-dispatcher": "~2.2"
#     NOTE: Min version not 2.2 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Resource watcher

Group:         Development/Libraries
License:       MIT
URL:           http://lurker.rtfd.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                          >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/config)           >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                          >= %{php_min_ver}
Requires:      php-composer(symfony/config)           >= %{symfony_min_ver}
Requires:      php-composer(symfony/config)           <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Resource tracking for PHP. Watch files and/or directories.

Autoloader: %{phpdir}/Lurker/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Lurker/autoload.php
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

$fedoraClassLoader->addPrefix('Lurker\\', dirname(__DIR__));

// Required dependencies
require_once '%{phpdir}/Symfony/Component/Config/autoload.php';
require_once '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php';

return $fedoraClassLoader;
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Lurker %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
$fedoraClassLoader =
    require '%{buildroot}%{phpdir}/Lurker/autoload.php';
$fedoraClassLoader->addPrefix('Lurker\\Tests\\', __DIR__.'/tests');
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
%{phpdir}/Lurker


%changelog
* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
