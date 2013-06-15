%{?drupal7_find_provides_and_requires}

%global module_name admin_language

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.2.dev.20130226%{?dist}
Summary:       Displays administration pages in preferred language

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-1.x-dev.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(locale)

%description
This module lets the administrator see all administration pages in her
preferred language.

You can use this to display the front-end of the site in one language and still
keep most of the back-end in English (or another language of your choice).

You can use the standard Languages page to choose the language of the admin
pages.

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
* Sun Jun 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.2.dev.20130226
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.dev.20130226
- Initial package
