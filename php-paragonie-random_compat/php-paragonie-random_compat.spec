#
# Fedora spec file for php-paragonie-random_compat
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     paragonie
%global github_name      random_compat
%global github_version   1.1.0
%global github_commit    19f765b66c6fbb56ee3b11bc16d52e38eebdc295

%global composer_vendor  paragonie
%global composer_project random_compat

# "php": ">=5.2.0"
%global php_min_ver 5.2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       PHP 5.x polyfill for random_bytes() and random_int() from PHP 7

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.1.0)
##     <none except weak dependencies>
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.0)
#     <none except weak dependencies>
# Weak dependencies
%if 0%{?fedora} > 21
Suggests:      php-mbstring
Suggests:      php-mcrypt
Suggests:      php-openssl
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/random_compat/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Autoloader compat
ln -s random.php lib/autoload.php


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}/random_compat
cp -rp lib/* %{buildroot}%{phpdir}/random_compat/


%check
%if %{with_tests}
%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/random_compat/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/random_compat


%changelog
* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
