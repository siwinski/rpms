%{?drupal7_find_provides_and_requires}

%global module_name any_menu_path

Name:          drupal7-%{module_name}
Version:       1.1
Release:       1%{?dist}
Summary:       Allows to add menu paths that don't exist on the site

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

%description
This module allows you to put any relative path you'd like for a menu entry,
even if the path doesn't exist on your site.

You might need this module for two reasons:

1) You either need to create menu items before the pages/paths are created.
   Helpful when you are building out new sites for which you haven't actually
   created the secondary pages yet, or if you want your menu to point to some
   path that will actually be redirected somewhere else (for which you've
   already set up a redirect).

   This actually isn't why this module was created, but it will work for this.

2) You have a distributed system, with some paths being on one (non-Drupal,
   or different Drupal install) server, and the other on your current Drupal
   system. It's assumed that you have some sort of path redirection mechanism
   in place such as Varnish, nginx or The Big IP to redirect your request to
   the proper path. But you need to serve your menu from Drupal.

   Why not just put an absolute path, you ask? When you put absolute paths,
   not only does it make it a pain for moving your Drupal site to other
   environments - but it also doesn't keep the proper base url when your site
   is serving up translated content. Ideally,
   http://example.com/your_sneaky_path would change to
   http://example.co.uk/your_sneaky_path when you changed to UK English
   (as an example).

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
* Wed Jun 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-1
- Initial package
