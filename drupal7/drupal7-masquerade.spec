%{?drupal7_find_provides_and_requires}

%global module_name masquerade
%global pre_release rc5

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Allows permitted users to masquerade as other users

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
# phpci
Requires:      php-session

%description
The masquerade module is designed as a tool for site designers and site
administrators. It allows a user with the right permissions to switch users.
While masquerading, a field is set on the $user object, and a menu item appears
allowing the user to switch back. Watchdog entries are made any time a user
masquerades or stops masquerading.

This package provides the following Drupal modules:
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
* Thu May 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.rc5
- Initial package
