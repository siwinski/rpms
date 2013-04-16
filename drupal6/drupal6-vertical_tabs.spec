%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name vertical_tabs
%global pre_release rc2

Name:      drupal6-%{module_name}
Version:   1.0
Release:   0.1.%{pre_release}%{?dist}
Summary:   Provides vertical tabs for supported forms like the node edit page

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

Provides:  drupal6(%{module_name}) = %{version}

%description
Provides vertical tabs like the node add form here:
http://drupal.geek.nz/static/node-form/default/summaries2.html

This module provides the following features:
* Vertical tabifying all node forms
* Vertical tabifying the content type forms
* Vertical tabifying the block forms
* Specialized CSS for Garland, as well as generic CSS for other themes
* Color module support when both Garland and color.module are used
* Vertical tabbed forms and fieldsets are over-ridable by using your site's
  settings.php and $conf
* When used in combination with Form module allows you to configure vertical
  tabs on all possible forms

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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.rc2
- Initial package