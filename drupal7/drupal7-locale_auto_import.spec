%{?drupal7_find_provides_and_requires}

%global module_name locale_auto_import

Name:          drupal7-%{module_name}
Version:       1.0
Release:       2%{?dist}
Summary:       Locale automatic import

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
#Requires:      drupal7(locale)
# phpci
Requires:      php-pcre

%description
Search within your modules/features for .po files and import them in the DB
within the right text group.

When you install a new module with translations, the Locale module
automatically imports them in the "Built-in interface" text group and chooses
the mode "Existing strings and the plural format are kept, only new strings
are added.". It's OK for mostly all modules but not for Features that can
contain Content types, Fields or Views.

This module recognizes the system name of the text group in the name of your
.po file and imports it to the right text group automatically.

The .po files will be searched in an "auto_translations" folder within your
modules/features instead of "translations".

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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2
- Updated for drupal7-rpmbuild auto-provides

* Thu Apr 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
