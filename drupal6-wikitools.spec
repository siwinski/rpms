%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name wikitools

Name:      drupal6-%{module_name}
Version:   1.3
Release:   1%{?dist}
Summary:   Provides helper functionality to have wiki-like behaviour

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6

%description
The wikitools module provides some settings to get a more wiki-like behavior.
It aims to be lightweight; all features are optional, and it provides no
database tables of its own.

Some of the features of this module are:
* Node Creation: Let users create new nodes when they type in a node name which
  does not exist.
* Node Search: Let users search for nodes when they type in a node name which
  does not exist.
* Automatic Redirect: If a title of a moved page is entered, redirect
  automatically.
* Unique Titles: Enforce that titles are unique over all wiki node types
* Move Protection: Disallow change of node titles for users without administer
  nodes permission.
* Underscore as Space: Treat underscores as spaces when doing a node-lookup by
  title.
* Dash as Space: Treat dashes as spaces when doing a node-lookup by title.
* Custom wiki 404 pages: pick and choose from links to create, links to search,
  and an inline node add form.

The module can be used in conjunction with the flexifilter module (of course),
the freelinking module by hijacking freelinking links, or together with the
pearwiki filter module for various wiki formats.


%prep
%setup -qn %{module_name}

cp -p %{SOURCE1} .


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.3-1
- Initial package
