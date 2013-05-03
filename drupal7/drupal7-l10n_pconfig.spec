%global module_name l10n_pconfig

Name:          drupal7-%{module_name}
Version:       1.2
Release:       1%{?dist}
Summary:       Plural formula configurator

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
#Requires:      drupal7(locale)

Provides:      drupal7(%{module_name}) = %{version}

%description
The plural formula configurator sets sensible defaults for plural forms when
adding languages and lets you edit the plural formula for all languages on the
web interface.

Drupal does not expose these fields for editing due to the complexity of plural
forms. You should make sure to only give permissions to edit language details
to those, who will likely not screw up your plural formulas.

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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-1
- Initial package
