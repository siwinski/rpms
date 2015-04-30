#
# RPM spec file for php-guzzlehttp-promises
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      promises
%global github_version   0.1.1
%global github_commit    89e850a66126a06a1088b9d47bc1d5761461dafe

%global composer_vendor  guzzlehttp
%global composer_project promises

# "php": ">=5.4.0"
%global php_min_ver 5.4.0

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Guzzle promises library

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
BuildRequires: %{_bindir}/phpab
%if %{with_tests}
BuildRequires: %{_bindir}/phpunit
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.1.1)
BuildRequires: php-json
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.1.1)
Requires:      php-json
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Promises/A+ [1] implementation that handles promise chaining and resolution
iteratively, allowing for "infinite" promise chaining while keeping the stack
size constant.

[1] https://promisesaplus.com/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
%{_bindir}/phpab --nolower --output src/autoload.php src

cat >> src/autoload.php <<'AUTOLOAD'

require __DIR__ . '/functions.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp/Promises
cp -rp src/* %{buildroot}%{phpdir}/GuzzleHttp/Promises/


%check
%if %{with_tests}
sed "s#.*autoload.*#require '%{buildroot}%{phpdir}/GuzzleHttp/Promises/autoload.php';#" \
    -i tests/bootstrap.php

%{_bindir}/phpunit
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc composer.json
%{phpdir}/GuzzleHttp/Promises


%changelog
* Wed Apr 29 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.1-1
- Initial package
