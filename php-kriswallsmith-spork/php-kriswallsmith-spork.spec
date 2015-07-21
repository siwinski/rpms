#
# Fedora spec file for php-kriswallsmith-spork
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     kriswallsmith
%global github_name      spork
%global github_version   0.3
%global github_commit    530fcf57fce4d54806288547b22aa8dcbb4b6c96

%global composer_vendor  kriswallsmith
%global composer_project spork

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "symfony/event-dispatcher": "*"

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Asynchronous PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: %{_bindir}/phpunit
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher)
BuildRequires: php-pcntl
BuildRequires: php-posix
BuildRequires: php-shmop
## phpcompatinfo (computed from version 0.3)
BuildRequires: php-date
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/event-dispatcher)
Requires:      php-pcntl
Requires:      php-posix
Requires:      php-shmop
# phpcompatinfo (computed from version 0.3)
Requires:      php-date
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Optional:
* Mongo (php-pecl-mongo)


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/Spork/autoload.php
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

$fedoraClassLoader->addPrefix('Spork\\', dirname(__DIR__));

if (file_exists('%{phpdir}/Symfony/Component/EventDispatcher/autoload.php')) {
    require_once '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php';
} else {
    // Not all dependency autoloaders exist or are in every dist yet so fallback
    // to using include path for dependencies for now
    $fedoraClassLoader->setUseIncludePath(true);
}

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
%{_bindir}/phpunit --verbose --bootstrap %{buildroot}%{phpdir}/Spork/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Spork


%changelog
* Mon Jul 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3-1
- Initial package
