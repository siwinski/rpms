%{?drupal7_find_provides_and_requires}

%global module_name admin_views

Name:          drupal7-%{module_name}
Version:       1.2
Release:       1%{?dist}
Summary:       Replaces all system object management pages in core with views

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7-views
Requires:      drupal7-views_bulk_operations
#Requires:      drupal7(views)
#Requires:      drupal7(views_bulk_operations)
# phpci
Requires:      php-pcre

%description
Replaces administrative overview/listing pages with actual views for superior
usability.

Features:
* Filter all administrative views via AJAX.
* Perform any kind of bulk/mass operations on items in administrative views.
* Filter content by title, node type, author, published status, and/or
  vocabulary.
* Filter comments by title, author, node title, or published status.
* Filter users by name, ban/blocked status, or user roles.

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
* Wed Jun 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2-1
- Initial package
