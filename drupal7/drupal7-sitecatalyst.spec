%{?drupal7_find_provides_and_requires}

%global module_name sitecatalyst
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Adds SiteCatalyst JavaScript tracking code to your site's pages

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

# phpci
Requires:      php-date
Requires:      php-pcre

%description
This module integrates the Site Catalyst analytics software into a Drupal site.

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
* Mon Jun 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta1
- Initial package
