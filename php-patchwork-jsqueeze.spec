#
# RPM spec file for php-patchwork-jsqueeze
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     nicolas-grekas
%global github_name      JSqueeze
%global github_version   1.0.1
%global github_commit    95f014738f93b5e0cf855da3745e5f617c41bec6

%global composer_vendor  patchwork
%global composer_project jsqueeze

# "php": ">=5.1.4"
%global php_min_ver 5.1.4

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Efficient JavaScript minification in PHP

Group:         Development/Libraries
License:       ASL 2.0 or GPLv2
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests
BuildRequires: php-phpunit-PHPUnit
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
# For tests: phpcompatinfo (computed from version 1.0.1)
BuildRequires: php-pcre
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.1)
Requires:      php-pcre

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
JSqueeze shrinks / compresses / minifies / mangles JavaScript code.

It's a single PHP class licensed under Apache 2 and GPLv2 that is being
developed, maintained and thouroughly tested since 2003 on major JavaScript
frameworks (e.g. jQuery).

JSqueeze operates on any parse error free JavaScript code, even when
semi-colons are missing.

In term of compression ratio, it compares to YUI Compressor and UglifyJS.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}/%{_datadir}/php
cp -rp class/* %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
# Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{__phpunit} --include-path %{buildroot}%{_datadir}/php -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%doc README.md composer.json
%{_datadir}/php/JSqueeze.php


%changelog
* Thu Sep 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Initial package
