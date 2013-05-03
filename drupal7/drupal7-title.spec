%global module_name title
%global pre_release alpha7

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Replaces entity legacy fields with regular fields

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7

Provides:      drupal7(%{module_name}) = %{version}

%description
While working on the new content translation system
(http://api.drupal.org/api/group/field_language/7) for Drupal 7, we (the Drupal
core i18n team) faced the need to convert node titles to the Field API in order
to make nodes fully translatable.

We were not able to make this happen in Drupal 7 core so we decided to find a
solution for this in contrib: the idea is replacing node titles with fields à
la Automatic Nodetitles (http://drupal.org/project/auto_nodetitle).

This will be exploited by the related Entity Translation
(http://drupal.org/project/entity_translation) project.

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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.alpha7
- Initial package
