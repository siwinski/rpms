%{?drupal7_find_provides_and_requires}

%global module_name domain_menu_access

Name:          drupal7-%{module_name}
Version:       1.2
Release:       1%{?dist}
Summary:       Allows restricting access to menu items per domain

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(domain)

%description
Domain Menu Access is an extension to Domain [1] module, allowing administrators
to configure visitors' access to selected menu items based on current domain
they are viewing.

It lets administrators decide whether a specific menu item should be hidden on
selected domains (regardless of it being enabled by default using standard
Drupal functionality), or should it be displayed on selected domains even if
disabled by default.

This package provides the following Drupal module:
* %{module_name}

[1] http://drupal.org/project/domain


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
* Wed Jun 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-1
- Initial package
