%global module_name lang_dropdown

Name:          drupal7-%{module_name}
Version:       1.5
Release:       1%{?dist}
Summary:       Provides a dropdown select to switch between available languages

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
Language Switcher Dropdown is a very simple module that exposes a new block,
similar to the default Language Switcher block provided by Locale module.

The new block allows site visitors to switch languages using a drop-down
select list instead of using hyperlinks.

The module also integrates well with Language Icons
(http://drupal.org/project/languageicons) module if installed.

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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.5-1
- Initial package
