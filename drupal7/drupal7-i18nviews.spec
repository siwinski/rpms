%{?drupal7_find_provides_and_requires}

%global module_name i18nviews

Name:          drupal7-%{module_name}
Version:       3.0
Release:       0.2.dev.20120725%{?dist}
Summary:       Translate views using Internationalization

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-3.x-dev.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
Requires:      drupal7-i18n
Requires:      drupal7-views
#Requires:      drupal7(i18n_string)
#Requires:      drupal7(views)

%description
%{summary}.

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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.0-0.2.dev.20120725
- Updated for drupal7-rpmbuild auto-provides

* Wed Apr 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.0-0.1.dev.20120725
- Initial package
