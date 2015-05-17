#
# RPM spec file for php-pimple1
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     silexphp
%global github_name      Pimple
%global github_version   1.1.1
%global github_commit    2019c145fe393923f3441b23f29bbdfaa5c58c4d

%global composer_vendor  pimple
%global composer_project pimple

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}1
Version:       %{github_version}
Release:       1%{?dist}
Summary:       A simple dependency injection container for PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}/tree/1.1
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: %{_bindir}/phpunit
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.1.1)
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.1)
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# Rename
Obsoletes:     php-Pimple < 2
Provides:      php-Pimple = %{version}

# Newer releases
Conflicts:     php-Pimple >= 2

%description
Pimple is a small dependency injection container for PHP that consists of
just one file and one class.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Generate autoloader
%{_bindir}/phpab --nolower --output lib/autoload.php lib


%install
mkdir -p  %{buildroot}%{phpdir}/Pimple
cp -pr lib/* %{buildroot}%{phpdir}/Pimple/


%check
%if %{with_tests}
: Recreate test bootstrap
rm -f tests/bootstrap.php
%{_bindir}/phpab --nolower --output tests/bootstrap.php tests
cat >> tests/bootstrap.php <<'BOOTSTRAP'

require '%{buildroot}%{phpdir}/Pimple/autoload.php';
BOOTSTRAP

: Run tests
%{_bindir}/phpunit
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.rst
%doc composer.json
%{phpdir}/Pimple


%changelog
* Sun May 17 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Rename of php-Pimple version 1 to php-pimple1
