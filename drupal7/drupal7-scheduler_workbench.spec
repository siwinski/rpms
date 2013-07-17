%{?drupal7_find_provides_and_requires}

%global module_name scheduler_workbench

Name:          drupal7-%{module_name}
Version:       1.2
Release:       1%{?dist}
Summary:       Integrates the Scheduler with the Workbench Moderation

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

# Write simpletests: https://drupal.org/node/1966814
Patch0:        http://drupal.org/files/1966814-1-scheduler_workbench-tests.patch
# Publish only "approved" nodes: https://drupal.org/node/1955938
Patch1:        http://drupal.org/files/1955938-12-scheduler_workbench-only_publish_approved.patch

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

# phpcompatinfo
Requires:      php-date
Requires:      php-spl

Requires:      drupal7-workbench_moderation
Requires:      drupal7(scheduler) >= 1.1
#Requires:      drupal7(workbench_moderation)

%description
Provides integration between the Scheduler module and the Workbench Moderation
module to set a moderation state when Scheduler triggers automatic publication
unpublication of a module. It also adds a field to capture a default value for
unpublication and adds a permission to determine which users can override this
default value.

This package provides the following Drupal module:
* %{module_name}


%prep
%setup -q -n %{module_name}

cp -p %{SOURCE1} .

%patch0 -p1 -F3
%patch1 -p1


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
* Wed Jul 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-1
- Initial package
