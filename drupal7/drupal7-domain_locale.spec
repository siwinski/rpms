%global module_name domain_locale
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Adds language handling functionality per domain basis

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
Requires:      drupal7(domain)
Requires:      drupal7(domain_conf)
#Requires:      drupal7(locale)

Provides:      drupal7(%{module_name}) = %{version}

%description
Domain Locale allows to customize language sets per domain for Drupal installs
using Domain Access and core Locale module. This module also offers drush
integration.

You need this module if:
* you want a different default language on different domains
* you want a different language set for each different domain

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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta1
- Initial package
