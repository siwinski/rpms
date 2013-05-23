%{?drupal7_find_provides_and_requires}

%global module_name boxes

Name:          drupal7-%{module_name}
Version:       1.1
Release:       2%{?dist}
Summary:       Provides exports for custom blocks and spaces integration

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
Requires:      drupal7-ctools
#Requires:      drupal7(ctools)
# phpci
Requires:      php-pcre
Requires:      php-spl

%description
Boxes module is a re-implementation of the custom blocks (boxes) that the core
block module provides. It is a proof of concept for what a re-worked block
module could do.

The module assumes that custom blocks are configuration, and not content. This
means that it is a reasonable action to ask for all blocks at one time, this is
in fact exactly what the core block module does.

Boxes provides an inline interface for editing blocks, allowing you to change
the contents of blocks without going to an admin page.

Boxes provides exportables for its blocks via the (required) Chaos tools module.
This allows modules to provide blocks in code that can be overwritten in the UI.

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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-2
- Updated for drupal7-rpmbuild auto-provides

* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-1
- Initial package
