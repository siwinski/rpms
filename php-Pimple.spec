%global libname     Pimple
%global php_min_ver 5.3.0

Name:          php-%{libname}
Version:       1.0.0
Release:       1%{?dist}
Summary:       A simple Dependency Injection Container for PHP 5.3

Group:         Development/Libraries
License:       MIT
URL:           http://pimple.sensiolabs.org
Source0:       https://github.com/fabpot/%{libname}/archive/v%{version}.tar.gz


BuildArch: noarch
# Test requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# Test requires: phpci
BuildRequires: php-spl

Requires:      php-common >= %{php_min_ver}
# phpci requires
Requires:      php-spl

%description
Pimple is a small Dependency Injection Container for PHP 5.3 that consists of
just one file and one class.


%prep
%setup -q -n %{libname}-%{version}

# Update and move tests' PHPUnit config
sed 's#tests/##' -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Update tests' require
sed "s#.*require.*Pimple.php.*#require_once '%{_datadir}/php/%{libname}/Pimple.php';#" \
    -i tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{libname}
cp -pr lib/* %{buildroot}%{_datadir}/php/%{libname}/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -pr tests/* %{buildroot}%{_datadir}/tests/%{name}/


%check
# Update tests' require to use buildroot
sed 's#%{_datadir}#%{buildroot}%{_datadir}#' -i tests/bootstrap.php

%{_bindir}/phpunit -c tests/phpunit.xml.dist


%files
%doc LICENSE README.rst composer.json
%{_datadir}/php/%{libname}
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Fri Nov 30 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-1
- Initial package
