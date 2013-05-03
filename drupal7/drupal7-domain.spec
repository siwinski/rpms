%global module_name domain

Name:          drupal7-%{module_name}
Version:       3.9
Release:       1%{?dist}
Summary:       A domain-based access control system

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
# phpci
Requires:      php-hash
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-session
Requires:      php-spl

Provides:      drupal7(%{module_name}) = %{version}
Provides:      drupal7(%{module_name}_alias) = %{version}
Provides:      drupal7(%{module_name}_conf) = %{version}
Provides:      drupal7(%{module_name}_content) = %{version}
Provides:      drupal7(%{module_name}_nav) = %{version}
Provides:      drupal7(%{module_name}_settings) = %{version}
Provides:      drupal7(%{module_name}_source) = %{version}
Provides:      drupal7(%{module_name}_strict) = %{version}
Provides:      drupal7(%{module_name}_test) = %{version}
Provides:      drupal7(%{module_name}_theme) = %{version}

%description
The Domain Access project is a suite of modules that provide tools for running
a group of affiliated sites from one Drupal installation and a single shared
database. The module allows you to share users, content, and configurations
across a group of sites such as:
* example.com
* one.example.com
* two.example.com
* my.example.com
* thisexample.com <-- can use any domain string
* example.com:3000 <-- treats non-standard ports as unique

By default, these sites share all tables in your Drupal installation. The
Domain Prefix module (for Drupal 6) allows for selective, dynamic table
prefixing for advanced users.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_alias
* %{module_name}_conf
* %{module_name}_content
* %{module_name}_nav
* %{module_name}_settings
* %{module_name}_source
* %{module_name}_strict
* %{module_name}_test
* %{module_name}_theme


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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.9-1
- Initial package