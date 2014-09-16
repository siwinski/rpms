#
# RPM spec file for php-ocramius-proxy-manager
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      Ocramius
%global github_name       ProxyManager
%global github_version    0.5.1
%global github_commit     eaaf10f9a24ffd79a3e388809f6d61f229e261bd

%global composer_vendor   ocramius
%global composer_project  proxy-manager

# "php": ">=5.3.3"
%global php_min_ver     5.3.3
# "phpunit/phpunit": "~3.7"
#     NOTE: Max version ignored on purpose
%global phpunit_min_ver 3.7
# "zendframework/zend-code": ">2.2.5,<3.0"
%global zf_code_min_ver 2.2.5
%global zf_code_max_ver 3.0

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Abstraction for generating various kinds of proxy classes

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests
# For tests: composer.json
BuildRequires: php(language)           >= %{php_min_ver}
BuildRequires: php-phpunit-PHPUnit     >= %{phpunit_min_ver}
BuildRequires: php-ZendFramework2-Code >= %{zf_code_min_ver}
BuildRequires: php-ZendFramework2-Code <  %{zf_code_max_ver}
# For tests: phpcompatinfo (computed from version 0.5.1)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language)           >= %{php_min_ver}
Requires:      php-ZendFramework2-Code >= %{zf_code_min_ver}
Requires:      php-ZendFramework2-Code <  %{zf_code_max_ver}
# phpcompatinfo (computed from version 0.5.1)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A library providing utilities to generate, instantiate and generally operate
with Object Proxies.

Optional:
* php-ZendFramework2-Json: To have the JsonRpc adapter (Remote Object feature)
* php-ZendFramework2-Soap: To have the Soap adapter (Remote Object feature)
* php-ZendFramework2-Stdlib: To use the hydrator proxy
* php-ZendFramework2-XmlRpc: To have the XmlRpc adapter (Remote Object feature)


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}/%{_datadir}/php
cp -rp src/* %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
# Create autoloader
cat > autoload.php <<'AUTOLOAD'
<?php

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD

# Create PHPUnit config with colors turned off
sed -e 's/colors="true"/colors="false"/' \
    phpunit.xml.dist > phpunit.xml

%{__phpunit} \
    --bootstrap autoload.php \
    --include-path %{buildroot}%{_datadir}/php:./tests \
    --exclude-group Performance \
    -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%{_datadir}/php/ProxyManager


%changelog
* Tue Sep 16 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.5.1-1
- Initial package
