%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name vote_up_down

Name:      drupal6-%{module_name}
Version:   3.2
Release:   1%{?dist}
Summary:   Provides a configurable up/down voting widget for other modules

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
Requires:  drupal6-ctools
Requires:  drupal6-votingapi
# Requires:  drupal6(comment)
# Requires:  drupal6(ctools)
# Requires:  drupal6(taxonomy)
# Requires:  drupal6(votingapi)
# phpci
Requires:  php-date

Provides:  drupal6(vud) = %{version}
Provides:  drupal6(vud_comment) = %{version}
Provides:  drupal6(vud_node) = %{version}
Provides:  drupal6(vud_term) = %{version}

%description
Allows votes on some drupal entities and provides the base for implementing
votes on other entities.

Features:
* Vote on nodes, comments and taxonomy terms on a node
* Interchangeable voting widget themes
* Code voting support for your own objects
* Make your own widgets using ctools plugins
* And more!

This package provides the following Drupal modules:
* vud
* vud_comment
* vud_node
* vud_term


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.2-1
- Initial package