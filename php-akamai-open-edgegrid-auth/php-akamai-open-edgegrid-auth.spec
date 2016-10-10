#
# Fedora spec file for php-akamai-open-edgegrid-auth
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     akamai-open
%global github_name      AkamaiOPEN-edgegrid-php
%global github_version   0.6.0
%global github_commit    1617cf4bdeba7b5c46a1d55bb969d0e45c7f52f5

%global composer_vendor  akamai-open
%global composer_project edgegrid-auth

# "php": ">=5.3"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Implements the Akamai {OPEN} EdgeGrid Authentication

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: %{_bindir}/phpab
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.6.0)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.6.0)
Requires:      php-date
Requires:      php-hash
Requires:      php-pcre

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer(akamai-open/edgegrid-client)
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Broken out from client as of version 0.6.0
Conflicts:     php-akamai-open-edgegrid-client < 0.6.0

%description
This library implements the Akamai {OPEN} EdgeGrid Authentication scheme.

For more information visit the Akamai {OPEN} Developer Community [1].

Autoloader: %{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php

[1] https://developer.akamai.com/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --output src/autoload-auth.php src/


%install
mkdir -p %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid
cp -rp src/* %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid/


%check
%if %{with_tests}
: Remove logging from PHPUnit config
sed '/log/d' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Akamai
%dir %{phpdir}/Akamai/Open
%dir %{phpdir}/Akamai/Open/EdgeGrid
     %{phpdir}/Akamai/Open/EdgeGrid/Authentication
     %{phpdir}/Akamai/Open/EdgeGrid/Authentication.php
     %{phpdir}/Akamai/Open/EdgeGrid/autoload-auth.php


%changelog
* Mon Oct 10 2016 Shawn Iwinski <shawn@iwin.ski> - 0.6.0-1
- Initial package
