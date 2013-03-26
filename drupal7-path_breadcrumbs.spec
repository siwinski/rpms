%global module_name path_breadcrumbs
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       3.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Allows creation of custom breadcrumbs for any page using contexts

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
Requires:      drupal7-entity
#Requires:      drupal7(ctools)
#Requires:      drupal7(entity_token)
# phpci
Requires:      php-pcre

Provides:      drupal7(%{module_name}) = %{version}
Provides:      drupal7(%{module_name}_ui) = %{version}
Provides:      drupal7(%{module_name}_i18n) = %{version}

%description
Path breadcrumbs module helps you to create breadcrumbs for any page with any
selection rules and load any entity from the URL.

Features
* Breadcrumbs navigation may be added to any kind of page: static
  (example: node/1) or dynamic (example: node/NID).
* You can load contexts from URL and use it like tokens for breadcrumb path or
  title.
* You can use selection rules for every breadcrumbs navigation.
* Supports ALL tokens from Entity tokens module (part of Entity module).
* You can import/export breadcrumbs (supports single operations, Features and
  Ctools bulk export).
* Breadcrumbs can be cloned to save you time while building navigation.
* Module provides rich snippets support for breadcrumbs (RDFa and Microdata).
* Module provides first/last/odd/even classes to every breadcrumb link.
* You can change breadcrumbs delimiter.
* Breadcrumbs could be hidden if they contain only one element.
* You can disable breadcrumbs and enable them later.
* All breadcrumb titles are translatable.
* Usable interface.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_ui
* %{module_name}_i18n (Requires manual install of the i18n module)


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
* Mon Mar 26 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.0-0.1.beta1
- Initial package