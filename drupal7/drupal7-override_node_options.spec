%{?drupal7_find_provides_and_requires}

%global module_name override_node_options

Name:          drupal7-%{module_name}
Version:       1.12
Release:       1%{?dist}
Summary:       Allow non-admins to override default node publishing options

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

%description
The Override Node Options module allows permissions to be set to each field
within the Authoring information and Publishing options field sets on the
node form. It also allows selected field sets to be set as collapsed and/or
collapsible.

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
* Mon Jun 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.12-1
- Initial package
