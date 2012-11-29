%global libname jsonlint

Name:          php-%{libname}
Version:       1.0.1
Release:       1%{?dist}
Summary:       JSON Lint for PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/Seldaek
Source0:       %{url}/%{libname}/archive/%{version}.tar.gz

BuildArch:     noarch

Requires:      php-common >= 5.3.0
# phpci requires
Requires:      php-pcre

%description
%{summary}.


%prep
%setup -q -n %{libname}-%{version}


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/* %{buildroot}%{_datadir}/php/


%files
%doc LICENSE README.mdown composer.json
%dir %{_datadir}/php/Seld
     %{_datadir}/php/Seld/JsonLint


%changelog
* Thu Nov 29 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.1-1
- Initial package
