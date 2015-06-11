#
# RPM spec file for php-jdorn-sql-formatter
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     jdorn
%global github_name      sql-formatter
%global github_version   1.2.17
%global github_commit    64990d96e0959dff8e059dfcdc1af130728d92bc

%global composer_vendor  jdorn
%global composer_project sql-formatter

# "php": ">=5.2.4"
%global php_min_ver 5.2.4

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global libdir %{phpdir}/%{composer_vendor}-%{composer_project}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       PHP SQL highlighting library

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.2.17)
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.2.17)
Requires:      php-pcre
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A lightweight php class for formatting sql statements.

It can automatically indent and add line breaks in addition to syntax
highlighting.


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
(cat <<'AUTOLOAD'
<?php
/**
 * Autoloader created by %{name}-%{version}-%{release}
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once 'Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('SqlFormatter', __DIR__);

return $fedoraClassLoader;
AUTOLOAD
) | tee lib/autoload.php


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{libdir}
cp -pr lib/* %{buildroot}%{libdir}/


%check
%if %{with_tests}
%{_bindir}/phpunit --bootstrap %{buildroot}%{libdir}/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc *.md
%doc composer.json
%doc examples
%{libdir}


%changelog
* Thu Jun 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.17-1
- Initial package
