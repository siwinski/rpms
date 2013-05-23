%{?drupal7_find_provides_and_requires}

%global module_name tmgmt
%global pre_release alpha3

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.2.%{pre_release}%{?dist}
Summary:       Translation Management Tool

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
Requires:      drupal7-entity
Requires:      drupal7-i18n
Requires:      drupal7-rules
Requires:      drupal7-variable
Requires:      drupal7-views
Requires:      drupal7-views_bulk_operations
Requires:      drupal7(entity_translation)
#Requires:      drupal7(entity)
#Requires:      drupal7(i18n)
#Requires:      drupal7(i18n_string)
#Requires:      drupal7(locale)
#Requires:      drupal7(rules)
#Requires:      drupal7(translation)
#Requires:      drupal7(variable)
#Requires:      drupal7(views)
#Requires:      drupal7(views_bulk_operations)
# phpci
Requires:      php-date
Requires:      php-dom
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xmlwriter

%description
The Translation Management Tool (TMGMT) module provides a tool set for
translating content from different sources. The translation can be done
by people or translation services of all kinds. It builds on and uses
existing language tools and data structures in Drupal and can be used
in automated workflow scenarios.

This module does not make i18n or any other language module for Drupal
obsolete. It does only facilitate the translation process.

The second alpha has been released, huge improvements have been made
(see the release notes for details) and there's even more work to do.
Please test the new version and report any bugs that you can find.

Important: The external translator plugins (Microsoft, MyGengo, Nativy,
Supertext) have been moved to separate projects. When any of these plugins,
make sure to download them as well and then run update.php when updating.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_local
* %{module_name}_skills
* %{module_name}_file
* %{module_name}_entity
* %{module_name}_entity_ui
* %{module_name}_node
* %{module_name}_node_ui
* %{module_name}_field
* %{module_name}_i18n_string
* %{module_name}_ui


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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.2.alpha3
- Updated for drupal7-rpmbuild auto-provides

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.alpha3
- Initial package
