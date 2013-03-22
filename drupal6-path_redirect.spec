%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name path_redirect
%global pre_release rc2

Name:      drupal6-%{module_name}
Version:   1.0
Release:   0.1.%{pre_release}%{?dist}
Summary:   Redirect users from one URL to another

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}-%{pre_release}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
# phpci
Requires:  php-pcre

%description
This module allows you to specify a redirect from one path to another path
or an external URL, using any HTTP redirect status
(http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3).


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
