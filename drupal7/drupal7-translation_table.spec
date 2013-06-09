%{?drupal7_find_provides_and_requires}

%global module_name translation_table
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.2.%{pre_release}%{?dist}
Summary:       UI for quick translation of dynamic strings

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7-i18n
#Requires:      drupal7(i18n_string)
Requires:      drupal7(locale)

%description
UI for quick translation of taxonomies and menus. The i18n module allows for
translation of taxonomy terms and menu items, but the process is tedious - you
need to look up strings you want to translate, there is no overview of what's
already translated etc.

This module presents your taxonomy terms or menu items in a table, and
each language has a corresponding column. Just fill out the translations
and click Save.

Requires the i18n module, and either taxonomy or menu string translation.

* menu item titles
* vocabulary names and taxonomy terms
* CCK field names and descriptions
* content type names and descriptions
* quick tab titles

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
* Sun Jun 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.2.beta1
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta1
- Initial package
