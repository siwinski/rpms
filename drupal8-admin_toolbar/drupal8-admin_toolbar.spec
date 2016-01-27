#
# Fedora spec file for drupal8-admin_toolbar
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global drupal8_type module

Name:          drupal8-admin_toolbar
Version:       1.11
Release:       1%{drupal8_release}
Summary:       Improves the default Drupal Toolbar

Group:         Applications/Publishing
License:       GPLv2+
URL:           %{drupal8_url}
Source0:       %{drupal8_source_url}

BuildArch:     noarch
BuildRequires: drupal8-rpmbuild

%description
Admin Toolbar intends to improve the default Drupal Toolbar (the administration
menu at the top of your site) to transform it into a drop-down menu, providing
a fast a full access of all the administration links.

The module works on the top of the default toolbar core module and is therefore
a very light module and keeps all the toolbar functionalities (shortcut / media
responsive).


%prep
%{drupal8_prep}


%build
# Empty build section, nothing to build


%install
%{drupal8_install}


%files -f .rpm/files.txt


%changelog
* Sat Jan 23 2016 Shawn Iwinski <shawn@iwin.ski> - 1.11-1
- Initial package
