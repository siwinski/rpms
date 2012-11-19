%global libname Pimple

Name:      php-%{libname}
Version:   1.0.0
Release:   1%{?dist}
Summary:   A simple Dependency Injection Container for PHP 5.3

Group:     Development/Libraries
License:   MIT
URL:       http://pimple.sensiolabs.org
# To create source tarball:
# 1) Clone git repo:
#    git clone https://github.com/fabpot/Pimple.git
# 2) Checkout version tag (note "v" prefix before version):
#    cd Pimple && git checkout v%%{version} && cd ..
# 2) Create tarball:
#    tar --exclude-vcs -czf Pimple-%%{version}.tar.gz Pimple
#
# NOTE: https://github.com/fabpot/%%{libname}/archive/v%%{version}.tar.gz
#       downloads as "v%%{version}" instead of "v%%{version}.tar.gz"
Source0:   %{libname}-%{version}.tar.gz


BuildArch: noarch
# Test requires
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# Test requires: phpci
BuildRequires: php-spl

Requires:  php-common >= 5.3.0
# phpci requires
Requires:  php-spl

%description
Pimple is a small Dependency Injection Container for PHP 5.3 that consists of
just one file and one class.


%prep
%setup -q -n %{libname}

# Update tests' require
sed -e "s#.*require.*Pimple.php.*#require_once '%{_datadir}/php/%{libname}/Pimple.php';#" \
    -i tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{libname}
cp -pr lib/* %{buildroot}%{_datadir}/php/%{libname}/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -p phpunit.xml.dist %{buildroot}%{_datadir}/tests/%{name}/
cp -pr tests %{buildroot}%{_datadir}/tests/%{name}/


%check
# Update tests' require to use buildroot
sed 's#%{_datadir}#%{buildroot}%{_datadir}#' -i tests/bootstrap.php

%{_bindir}/phpunit .


%files
%doc LICENSE README.rst composer.json
%{_datadir}/php/%{libname}
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Mon Nov 19 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-1
- Initial package
