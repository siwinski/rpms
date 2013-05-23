%{?drupal7_find_provides_and_requires}

%global module_name features_extra
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.2.%{pre_release}%{?dist}
Summary:       Provides faux exportables of several site-building components

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
Requires:      drupal7-ctools
Requires:      drupal7-features
#Requires:      drupal7(ctools)
#Requires:      drupal7(features)
#Requires:      drupal7(profile)
# phpci
Requires:      php-pcre

%description
Features Extra provides faux exportables (via Features) of several
site-building components

This package provides the following Drupal modules:
* fe_block (requires manual install of block_class module only if running tests)
* fe_nodequeue (requires manual install of the nodequeue module)
* fe_profile
* features_extra_test (requires manual install of block_class module)


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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.2.beta1
- Updated for drupal7-rpmbuild auto-provides

* Thu Apr 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta1
- Initial package
