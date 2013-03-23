%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name notifications

Name:      drupal6-%{module_name}
Version:   2.3
Release:   1%{?dist}
Summary:   The basic notifications framework

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
Requires:  drupal6-token
Requires:  drupal6-views
Requires:  drupal6(messaging)
#Requires:  drupal6(taxonomy)
#Requires:  drupal6(token)
#Requires:  drupal6(views)
# phpci
Requires:  php-date
Requires:  php-ereg
Requires:  php-pcre

Provides:  drupal6(%{module_name}) = %{version}
Provides:  drupal6(%{module_name}_autosubscribe) = %{version}
Provides:  drupal6(%{module_name}_content) = %{version}
Provides:  drupal6(%{module_name}_lite) = %{version}
Provides:  drupal6(%{module_name}_tags) = %{version}
Provides:  drupal6(%{module_name}_ui) = %{version}
Provides:  drupal6(%{module_name}_views) = %{version}

%description
This is a complete Subscriptions/Notifications Framework aiming at extendability
and scalability. It allows any number of plug-ins defining new event types or
subscription types or a different user interface.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_autosubscribe
* %{module_name}_content
* %{module_name}_lite
* %{module_name}_tags
* %{module_name}_ui
* %{module_name}_views


%prep
%setup -qn %{module_name}

cp -p %{SOURCE1} .

# Remove executable bits
chmod a-x translations/*


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.3-1
- Initial package
