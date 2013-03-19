%global module_name profiler
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       2.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Allows an install profile to be defined as a Drupal .info file

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7

%description
Profiler provides a new way to write install profiles. Gone are the days where
you needed to know all the quirks of Drupal's APIs in order to write a solid
install profile. Profiler allows you to quickly and easily create new install
profiles, as well as have 'Sub' Install Profiles, where one Install Profile
inherits from and extends another Install Profile.


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
* Tue Mar 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.1.beta1
- Initial package
