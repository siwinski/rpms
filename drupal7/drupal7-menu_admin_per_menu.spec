%{?drupal7_find_provides_and_requires}

%global module_name menu_admin_per_menu

Name:          drupal7-%{module_name}
Version:       1.0
Release:       1%{?dist}
Summary:       Allows menu admin permissions per role and menu

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(menu)
# phpci
Requires:      php-pdo

%description
By default, Drupal allows only users with "administer menu permission"
to add, modify or delete menu items.

In case you want for instance to let certain users manage primary links
or secondary links but not navigation menu, this module provides this
functionality.

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
* Wed Jul 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
