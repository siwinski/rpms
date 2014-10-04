#
# RPM spec file for php-stack-builder
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     stackphp
%global github_name      builder
%global github_version   1.0.2
%global github_commit    b4af43e7b7f3f7fac919ff475b29f7c5dc7b23b7

%global composer_vendor  stack
%global composer_project builder

# "php": ">= 5.3.0"
%global php_min_ver      5.3.3
# "silex/silex": "~1.0"
%global silex_min_ver    1.0
%global silex_max_ver    2.0
# "symfony/http-kernel": "~2.1"
%global symfony_min_ver  2.1
%global symfony_max_ver  3.0

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Builder for stack middlewares based on HttpKernelInterface

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
BuildRequires: php-phpunit-PHPUnit
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(symfony/http-foundation) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-foundation) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-kernel)     >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-kernel)     <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.0.2)
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/http-foundation) >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-foundation) <  %{symfony_max_ver}
Requires:      php-composer(symfony/http-kernel)     >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-kernel)     <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.0.2)
Requires:      php-reflection
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Builder for stack middlewares based on HttpKernelInterface.

Stack/Builder is a small library that helps you construct a nested
HttpKernelInterface decorator tree. It models it as a stack of middlewares.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}/%{_datadir}/php
cp -rp src/* %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
# Create bootstrap
cat > bootstrap.php <<'BOOTSTRAP'
<?php

// Add non-standard Pimple path to include path
set_include_path(get_include_path() . PATH_SEPARATOR . '%{_datadir}/php/Pimple');

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});
BOOTSTRAP

# Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{__phpunit} \
    --bootstrap ./bootstrap.php \
    --include-path %{buildroot}%{_datadir}/php \
    -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%dir %{_datadir}/php/Stack
     %{_datadir}/php/Stack/Builder.php
     %{_datadir}/php/Stack/StackedHttpKernel.php


%changelog
* Sat Oct 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Initial package
