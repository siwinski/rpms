%global module_name taxonomy_access_fix

Name:          drupal7-%{module_name}
Version:       1.1
Release:       1%{?dist}
Summary:       Fixes the crooked access checks for Taxonomy pages

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
# Since Drupal 7 only requires PHP >= 5.2.5, we must must specify greater PHP min ver
Requires:      php-common >= 5.3.0

%description
This module:
* adds 1 permission per vocabulary: "add terms in X"
* changes the way vocabulary specific permissions are handled
* changes the Taxonomy admin pages' access checks
* alters the vocabularies overview table to show only what you have access to
  edit or delete

The module does what native Taxonomy lacks: more specific Taxonomy permissions
(and checking them correctly).

Note: In order to access the admin/structure/taxonomy page, you must first set
permissions for the desired vocabularies.

Note: A module can't add permissions to another module, so the extra "add terms
in X" permissions are located under "Taxonomy access fix" and not under
"Taxonomy".


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt


%changelog
* Tue Mar 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-1
- Initial package
