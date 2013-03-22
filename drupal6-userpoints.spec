%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name userpoints

Name:      drupal6-%{module_name}
Version:   1.2
Release:   1%{?dist}
Summary:   Provides an API for users to gain or lose points

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6

%description
This module provides an API for users to gain or lose points for performing
certain actions on your site.

In conjunction with other modules, such as the Userpoints Nodes and Comments
(http://drupal.org/project/userpoints_nc) users can accumulate points for
actions such as posting nodes, commenting or moderation duties.

Use one of the many contributed modules
(http://drupal.org/project/userpoints_contrib) to extend the functionality of
the module to include point accumulation on page views or votes, upgrade roles
based on point balance, or purchase goods from your store.

This module is useful in providing an incentive for users to participate in
the site, and be more active.


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-1
- Initial package
