%global module_name domain_views

Name:          drupal7-%{module_name}
Version:       1.5
Release:       1%{?dist}
Summary:       Provides Views integration for Domain Access

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
Requires:      drupal7(domain)
Requires:      drupal7-views
#Requires:      drupal7(views)

Provides:      drupal7(%{module_name}) = %{version}

%description
%{summary}.

This package provides the following Drupal modules:
* %{module_name}


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .

# Remove executable bits
find . -type f | xargs chmod a-x


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
* Fri May 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.5-1
- Initial package
