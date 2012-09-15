%global libname lessphp

Name:          php-%{libname}
Version:       0.3.6
Release:       1%{?dist}
Summary:       A compiler for LESS written in PHP

Group:         Development/Libraries
License:       MIT or GPLv3
URL:           http://leafo.net/lessphp/
Source0:       http://leafo.net/lessphp/src/%{libname}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: help2man

Requires:      php-common
# phpci requires
Requires:      php-ctype
Requires:      php-date
Requires:      php-pcre

%description
lessphp is a compiler that generates CSS from a superset language which
adds a collection of convenient features often seen in other languages.
All CSS is compatible with LESS, so you can start using new features
with your existing CSS.

It is designed to be compatible with less.js (http://lesscss.org/), and
suitable as a drop in replacement for PHP projects.


%prep
%setup -q -c

# Remove unnecessary files
rm -f %{libname}/Makefile

# Move docs
mkdir -p %{libname}-docs/tests
mv -f \
    %{libname}/LICENSE \
    %{libname}/README.md \
    %{libname}/composer.json \
    %{libname}/docs \
    %{libname}-docs/
mv -f %{libname}/tests/README.md %{libname}-docs/tests/

# Update path in bin file
sed -i \
    's#^\s*$path\s*=.*#$path = "%{_datadir}/php/%{libname}/";#' \
    %{libname}/plessc

# Move bin
mkdir %{libname}-bin
mv -f %{libname}/plessc %{libname}-bin/

# Add shebang to bootstrap script
# NOTE: To be fixed upstream
sed -i '1i\
#!/bin/bash\
' %{libname}/tests/bootstrap.sh


%build
# Create man page for bin
#help2man --version-string=%{version} --no-info \
help2man --version-option='-v' --no-info \
    %{libname}-bin/plessc | gzip > plessc.1.gz


%check
cd %{libname}
%{_bindir}/phpunit tests


%install
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
cp -rp %{libname}/* $RPM_BUILD_ROOT%{_datadir}/php/%{libname}/

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -rp %{libname}-bin/* $RPM_BUILD_ROOT%{_bindir}/

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p plessc.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/


%files
%doc %{libname}-docs/*
%doc %{_mandir}/man1/plessc.1.gz
%{_datadir}/php/%{libname}
%{_bindir}/plessc


%changelog
* Mon Aug 13 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.6-1
- Updated to upstream version 0.3.6

* Thu Jul 12 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.5-1
- Initial package
