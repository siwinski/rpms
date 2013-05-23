%{?drupal7_find_provides_and_requires}

%global module_name link

Name:          drupal7-%{module_name}
Version:       1.1
Release:       2%{?dist}
Summary:       Defines simple link field types

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
# phpci
Requires:      php-pcre

%description
The link module can be count to the top 50 modules in Drupal installations and
provides a standard custom content field for links. With this module links can
be added easily to any content types and profiles and include advanced
validating and different ways of storing internal or external links and URLs.
It also supports additional link text title, site wide tokens for titles and
title attributes, target attributes, CSS class attribution, static repeating
values, input conversion, and many more.

This package provides the following Drupal module:
* %{module_name}


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt


%changelog
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-2
- Updated for drupal7-rpmbuild auto-provides

* Mon Apr 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-1
- Initial package
