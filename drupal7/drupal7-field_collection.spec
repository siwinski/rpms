%{?drupal7_find_provides_and_requires}

%global module_name field_collection
%global pre_release beta5

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Provides a field collection field

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3

Requires:      drupal7-entity
#Requires:      drupal7(entity)
# phpcompatinfo
# --- none ---

%description
Provides a field-collection field, to which any number of fields can
be attached.

A field collection is internally represented as an entity, which is
embedded in the host entity. Thus, if desired field collections may
be viewed and edited separately too.

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
* Tue Nov 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta5
- Initial package
