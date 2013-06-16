%{?drupal7_find_provides_and_requires}

%global module_name ds

Name:          drupal7-%{module_name}
Version:       2.4
Release:       1%{?dist}
Summary:       Extend the display options for every entity type

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7-cools
#Requires:      drupal7(ctools)
# phpci
Requires:      php-pcre

%description
Display Suite allows you to take full control over how your content is displayed
using a drag and drop interface. Arrange your nodes, views, comments, user data
etc. the way you want without having to work your way through dozens of template
files. A predefined list of layouts (D7 only) is available for even more drag
and drop fun!

By defining custom view modes (build modes in D6), you can define how one piece
of content should be displayed in different places such as teaser lists, search
results, the full node, views etc.

Watch a screen-cast (http://drupal.org/node/644706) to see it all in action!

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_ui
* %{module_name}_devel (NOTE: Requires install of the devel module)
* %{module_name}_format
* %{module_name}_extras
* %{module_name}_search
* %{module_name}_forms


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
* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4-1
- Updated to 2.4
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2-1
- Initial package
