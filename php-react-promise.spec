#
# RPM spec file for php-react-promise
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      promise
%global github_version   2.0.0
%global github_commit    58129a9cb9da88f2055309a805e2696b06928bb0

%global composer_vendor  react
%global composer_project promise

# "php": ">=5.4.0"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%global with_tests %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:     %global phpdir     %{_datadir}/php}
%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A lightweight implementation of CommonJS Promises/A for PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
BuildRequires: php-phpunit-PHPUnit
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.0)
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.0)
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A lightweight implementation of CommonJS Promises/A [1] for PHP.

[1] http://wiki.commonjs.org/wiki/Promises/A


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
# Create bootstrap
cat > bootstrap.php <<'BOOTSTRAP'
<?php

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});

require_once '%{buildroot}%{phpdir}/React/Promise/functions.php';
BOOTSTRAP

# Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{__phpunit} \
    --bootstrap ./bootstrap.php \
    --include-path %{buildroot}%{phpdir}:./tests \
    -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%dir %{phpdir}/React
     %{phpdir}/React/Promise


%changelog
* Wed Oct 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0.0-1
- Initial package
