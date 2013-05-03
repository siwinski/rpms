%global module_name entity_translation
%global pre_release beta2

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Allows entities to be translated into different languages

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
Requires:      drupal7-i18n
#Requires:      drupal7(i18n)
#Requires:      drupal7(i18n_menu)
#Requires:      drupal7(locale)
# phpci
Requires:      php-date
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-spl

Provides:      drupal7(%{module_name}) = %{version}
Provides:      drupal7(%{module_name}_i18n_menu) = %{version}
Provides:      drupal7(%{module_name}_upgrade) = %{version}

%description
Allows (fieldable) entities to be translated into different languages,
by introducing entity/field translation for the new translatable fields
capability in Drupal 7. Maintained by the Drupal core i18n team.

This project does not replace the Internationalization
(http://drupal.org/project/i18n) project, which focuses on enabling a full
multilingual workflow for site admins/builders. Some features, e.g. content
language negotiation or taxonomy translation, might overlap but most of them
are unrelated.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_i18n_menu
* %{module_name}_upgrade


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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta2
- Initial package
