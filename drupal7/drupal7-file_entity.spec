%{?drupal7_find_provides_and_requires}

%global module_name file_entity
%global pre_release unstable7

Name:          drupal7-%{module_name}
Version:       2.0
Release:       0.2.%{pre_release}%{?dist}
Summary:       File entity (fieldable files)

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
Requires:      drupal7-ctools
#Requires:      drupal7(field)
#Requires:      drupal7(file)
#Requires:      drupal7(ctools)
# phpci
Requires:      php-spl

%description
File entity provides interfaces for managing files. It also extends the core
file entity, allowing files to be fieldable, grouped into types, viewed (using
display modes) and formatted using field formatters. File entity integrates
with a number of modules, exposing files to Views, Entity API, Token and more.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_test


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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.2.unstable7
- Updated for drupal7-rpmbuild auto-provides

* Wed Apr 10 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.1.unstable7
- Initial package
