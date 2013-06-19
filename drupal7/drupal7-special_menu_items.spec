%{?drupal7_find_provides_and_requires}

%global module_name special_menu_items

Name:          drupal7-%{module_name}
Version:       2.0
Release:       1%{?dist}
Summary:       Allow users to add placeholder and/or separator menu items

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(menu)
# phpci
Requires:      php-pcre

%description
Special menu items is a Drupal module that provides placeholder and separator
menu items.

A placeholder is a menu item which is not a link. It is useful with dynamic
drop down menus where we want to have a parent menu item which is not linking
to a page but just acting as a parent grouping some menu items below it.

A separator menu item is something like "-------" which is not linking anywhere
but merely a mean to structure menus and "separate" menu items visually.

Menu item container [1] provides similar functionality.

Shane Thomas made a video about special menu item [2].

Features:
* User can create a new menu item and place either "<nolink>" or "<separator>"
  to the Path field, without quotes.
* "<nolink>" item will be rendered similar to a normal menu link item but there
  will be no link just the title.
* You can change HTML tag used for menu item
* "<separator>" item will be rendered to an item which is no link and by default
  title will be "-------".
* Breadcrumb of "<nolink>" will be rendered same as "<nolink>" menu item.
* CSS class "nolink" is added to "nolink" menu item.
* CSS class "separator" is added to "separator" menu item.

This package provides the following Drupal module:
* %{module_name}

[1] https://drupal.org/project/menu_item_container
[2] https://www.youtube.com/watch?v=sSY8tu7shd0


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
* Wed Jun 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-1
- Initial package
