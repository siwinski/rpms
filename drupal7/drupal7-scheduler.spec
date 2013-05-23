%{?drupal7_find_provides_and_requires}

%global module_name scheduler

Name:          drupal7-%{module_name}
Version:       1.0
Release:       2%{?dist}
Summary:       Allows nodes to be published/unpublished on specified dates and time

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
# phpci
Requires:      php-date
Requires:      php-pcre

%description
This module allows nodes to be published and unpublished on specified dates.

Notice:
* Please check if cron is running correctly if scheduler does not publish your
  scheduled nodes.
* Scheduler does only schedule publishing and unpublishing of nodes. If you want
  to schedule any other activity check out Workflow, Rules and Actions.

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
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt


%changelog
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2
- Updated for drupal7-rpmbuild auto-provides

* Sat Mar 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
