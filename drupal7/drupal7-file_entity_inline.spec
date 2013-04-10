%global module_name file_entity_inline
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Makes field entities editable within other entities

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
Requires:      drupal7-ctools
Requires:      drupal7-file_entity
#Requires:      drupal7(ctools)
#Requires:      drupal7(field)
#Requires:      drupal7(file_entity)

Provides:      drupal7(%{module_name}) = %{version}

%description
This module aims to provide the ability to edit File entities [1] inline, as
part of another form (such as nodes). This should enable the ability for
reusable and site-wide editing of file properties, such as description,
alt text, captions, bylines, etc.

This package provides the following Drupal module:
* %{module_name}

[1] http://drupal.org/project/file_entity


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
* Wed Apr 10 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta1
- Initial package
