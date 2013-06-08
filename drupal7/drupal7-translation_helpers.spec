%{?drupal7_find_provides_and_requires}

%global module_name translation_helpers

Name:          drupal7-%{module_name}
Version:       1.0
Release:       3%{?dist}
Summary:       Provides methods for other modules to use with translated content

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(translation)

%description
Translation helpers enables other modules to respond to changes in the "source
translation" of a set of translated content. This functionality is useful for
modules that track data by the "source translation" (node.tnid value).

The module also provides other methods for modules to use with translated
content.

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
* Sat Jun 08 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-3
- Updated for drupal7-rpmbuild 7.22-5

* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2
- Updated for drupal7-rpmbuild auto-provides

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
