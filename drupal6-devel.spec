%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name devel

Name:      drupal6-%{module_name}
Version:   1.27
Release:   1%{?dist}
Summary:   Various blocks, pages, and functions for developers

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
#Requires:  drupal6(menu)
# phpci
Requires:  php-date
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session

Provides:  drupal6(%{module_name}) = %{version}
Provides:  drupal6(%{module_name}_generate) = %{version}
Provides:  drupal6(%{module_name}_node_access) = %{version}

%description
A suite of modules containing fun for module developers and themers.

Devel
* Helper functions for Drupal developers and inquisitive admins. This module can
  print a summary of all database queries for each page request at the bottom of
  each page. The summary includes how many times each query was executed on a
  page (shouldn't run same query multiple times), and how long each query took
  (short is good - use cache for complex queries).
* Also a dprint_r($array) function is provided, which pretty prints arrays.
  Useful during development. Similarly, a ddebug_backtrace() is offerred.
* much more. See this helpful demo page.

Generate content
* Accelerate development of your site or module by quickly generating nodes,
  comments, terms, users, and more.

Devel Node Access (DNA)
* View the node access entries for the node(s) that are shown on a page.
  Essential for developers of node access modules and useful for site admins in
  debugging problems with those modules.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_generate
* %{module_name}_node_access


%prep
%setup -qn %{module_name}

cp -p %{SOURCE1} .

# Remove executable bits
find krumo -type f | xargs chmod a-x

# Fix wrong-script-end-of-line-encoding
find krumo -type f | xargs sed -i 's/\r//'


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.27-1
- Initial package
