%global module_name l10n_update
%global pre_release beta3 

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Provides automatic downloads and updates for translations

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
#Requires:      drupal7(locale)
# phpci
Requires:      php-date
Requires:      php-pcre
Requires:      php-xml

Provides:      drupal7(%{module_name}) = %{version}

%description
Automatically download and update your translations fetching them from
localize.drupal.org (http://localize.drupal.org/) or any other
Localization server (http://drupal.org/project/l10n_server).

This package provides the following Drupal modules:
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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta3
- Initial package
