%{?drupal7_find_provides_and_requires}

%global module_name drush_language

Name:          drupal7-%{module_name}
Version:       1.2
Release:       2%{?dist}
Summary:       Drush language commands

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

%description
Drush commands allowing languages to be added, switched, enabled, disabled,
imported and exported from the commandline. This module only provides drush
commands, so you will see no functionality in the UI.

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
* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-2
- Updated for drupal7-rpmbuild 7.22-5

* Wed Apr 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-1
- Initial package
