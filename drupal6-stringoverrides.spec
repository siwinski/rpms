%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name stringoverrides

Name:      drupal6-%{module_name}
Version:   1.8
Release:   1%{?dist}
Summary:   Provides a quick and easy way of replacing text

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6

Provides:  drupal6(%{module_name}) = %{version}

%description
Provides a quick and easy way to replace any text on a site.

Features:
* Easily replace anything that's passed through t()
* Locale support, allowing you to override strings in any language
* Ability to import/export *.po files, for easy migration from the Locale module
* Note that this is not a replacement to Locale as having thousands of overrides
  can cause more pain then benefit. Use this only if you need a few easy text
  changes.

This package provides the following Drupal modules:
* %{module_name}


%prep
%setup -qn %{module_name}

cp -p %{SOURCE1} .


%build
# Empty build section, nothing required


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal6_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal6_modules}/%{module_name}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal6_modules}/%{module_name}
%exclude %{drupal6_modules}/%{module_name}/*.txt


%changelog
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.8-1
- Initial package
