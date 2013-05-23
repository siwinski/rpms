%{?drupal7_find_provides_and_requires}

%global module_name crumbs

Name:          drupal7-%{module_name}
Version:       1.9
Release:       2%{?dist}
Summary:       The ultimate breadcrumbs module

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
Requires:      php-pcre
Requires:      php-spl

%description
Crumbs is a powerful breadcrumb-building machine, generating high-quality
breadcrumbs for most every page on your site, with minimal configuration.

The Crumbs engine takes advantage of the hierarchical nature inherent to
breadcrumbs: It calculates the parent of the current page, the parent of
the parent, etc, until it has the complete breadcrumb trail.

Crumbs uses plugins with fine-grained user-defined priorities, for each
step in this process. Plugins for most of your favorite modules are already
built-in, and you can add more.

A lot of stuff that would require laborious configuration with other
breadcrumb-building modules, does work out of the box with Crumbs. And if it
doesn't, there are powerful and ways to configure, customize and extend.

Where in other breadcrumb-customizing modules you need to define complete
breadcrumbs for various pages and their all their children, in Crumbs you
mostly just say "A is the parent of B", and it can solve all the rest of
the puzzle by itself.

This package provides the following Drupal module:
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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.9-2
- Updated for drupal7-rpmbuild auto-provides

* Sat May 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.9-1
- Initial package
