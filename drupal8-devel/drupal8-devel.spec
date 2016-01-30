#
# Fedora spec file for drupal8-devel
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global drupal8_project     devel
%global drupal8_type        module
#%%global drupal8_pre_release
%global drupal8_commit      03e2e3c67747918208d8862d6925540dd500eacb
%global drupal8_commit_date 20160130

Name:          %{drupal8_name}
Version:       0
Release:       0.1%{drupal8_release}
Summary:       Various blocks, pages, and functions for developers

License:       GPLv2+
URL:           %{drupal8_url}
Source0:       %{drupal8_source}

BuildArch:     noarch
BuildRequires: drupal8-rpmbuild

# phpcompatinfo (computed from 0-0.1.20160130git03e2e3c)
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-date
Requires:      php-iconv
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-session
Requires:      php-spl
Requires:      php-tokenizer
## Weak dependencies
Suggests:      php-pecl(apcu)
Suggests:      php-pecl(xdebug)
Suggests:      php-xcache

%description
A suite of modules containing fun for module developers and themers.

Devel
* Helper functions for Drupal developers and inquisitive admins.
* Enable the included Kint submodule as for pretty print of variables.
  kint($array) function is provided, which pretty prints arrays. Useful
  during development. Similarly, a ddebug_backtrace() is offered.
* much more. See this helpful demo page:
  http://ratatosk.net/drupal/tutorials/debugging-drupal.html

Generate content
* Accelerate development of your site or module by quickly generating nodes,
comments, terms, users, and more.

WebProfiler
* Add a powerful footer to all pages of your site. There, admins can review
resource utilization, cache effectiveness, database queries, Views, and so
much more. Sponsored by Wellnet

Devel Node Access (DNA)
* View the node access entries for the node(s) that are shown on a page.
  Essential for developers of node access modules and useful for site admins
  in debugging problems with those modules.


%prep
%{drupal8_prep}


%build
# Empty build section, nothing to build


%install
%{drupal8_install}


%files -f %{drupal8_files}


%changelog
* Sat Jan 30 2016 Shawn Iwinski <shawn@iwin.ski> - 0-0.1.20160130git03e2e3c
- Initial package
