%{?drupal7_find_provides_and_requires}

%global module_name views_rss
%global pre_release rc3

Name:          drupal7-%{module_name}
Version:       2.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Provides a views plugin that allows fields in RSS feeds

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7-views
#Requires:      drupal7(views)
# phpci
Requires:      php-date
Requires:      php-pcre

%description
This module allows users to take control of their feeds by providing a
fields-based views style plugin for RSS.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_core
* %{module_name}_dc


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
* Tue Jun 11 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.1.rc3
- Initial package
