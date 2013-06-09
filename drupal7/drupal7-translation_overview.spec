%{?drupal7_find_provides_and_requires}

%global module_name translation_overview
%global pre_release beta1

Name:          drupal7-%{module_name}
Version:       2.0
Release:       0.2.%{pre_release}%{?dist}
Summary:       Provides an overview of the translation status of site's content

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(translation)
# phpci
Requires:      php-pcre

%description
The Translation Overview page provides a table listing the site's nodes and
showing what's been translated into each language. It also lets you assign
priorities for translating nodes into the various languages.

For translations of taxonomy terms and menu items check out the Translation
table (http://drupal.org/project/translation_table) module.

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
* Sun Jun 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.2.beta1
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.1.beta1
- Initial package
