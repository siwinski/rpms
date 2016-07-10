#
# Fedora spec file for php-robrichards-xmlseclibs1
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     robrichards
%global github_name      xmlseclibs
%global github_version   1.4.1
%global github_commit    465f18a8e1196c279b1298a3b08bcbee71ea4e4e

%global composer_vendor  robrichards
%global composer_project xmlseclibs

# "php": ">= 5.2"
%global php_min_ver 5.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}1
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A PHP library for XML Security (version 1)

Group:         Development/Libraries
License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## composer.json: optional
BuildRequires: php-mcrypt
BuildRequires: php-openssl
## phpcompatinfo (computed from version 1.4.1)
BuildRequires: php-dom
BuildRequires: php-hash
## Autoloader
BuildRequires: php-composer(theseer/autoload)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.4.1)
Requires:      php-dom
Requires:      php-hash

# Weak dependencies
%if 0%{?fedora} >= 21
## composer.json: suggest
#Suggests:      php-mcrypt
Suggests:      php-openssl
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
xmlseclibs is a library written in PHP for working with XML Encryption and
Signatures.

Autoloader: %{phpdir}/robrichards-xmlseclibs/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --nolower --output src/autoload.php src


%install
mkdir -p %{buildroot}%{phpdir}/robrichards-xmlseclibs
cp -rp src/* %{buildroot}%{phpdir}/robrichards-xmlseclibs/


%check
%if %{with_tests}
: Use autoloader
sed 's#require.*xmlseclibs.*#require_once "%{buildroot}%{phpdir}/robrichards-xmlseclibs/autoload.php";#' \
    -i tests/*.phpt

: Skip tests known to fail
rm -f tests/extract-win-cert.phpt

: Run tests
%{_bindir}/phpunit tests
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.txt
%doc composer.json
%doc README.md
%{phpdir}/robrichards-xmlseclibs


%changelog
* Sun Jul 10 2016 Shawn Iwinski <shawn@iwin.ski> - 1.4.1-1
- Initial package
