#
# Fedora spec file for php-robrichards-xmlseclibs3
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     robrichards
%global github_name      xmlseclibs
%global github_version   3.0.0
%global github_commit    a29eb3100eb6c5a427d6a3f9e61aff37492405ae

%global composer_vendor  robrichards
%global composer_project xmlseclibs

# "php": ">= 5.6"
%global php_min_ver 5.6

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}3
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A PHP library for XML Security (version 3)

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
BuildRequires: php-openssl
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-dom
BuildRequires: php-hash
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# composer.json: suggest
Requires:      php-openssl
# phpcompatinfo (computed from version 3.0.0)
Requires:      php-dom
Requires:      php-hash
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
xmlseclibs is a library written in PHP for working with XML Encryption and
Signatures.

Autoloader: %{phpdir}/RobRichards/XMLSecLibs3/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('RobRichards\\XMLSecLibs\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/RobRichards
cp -rp src %{buildroot}%{phpdir}/RobRichards/XMLSecLibs3


%check
%if %{with_tests}
: Use autoloader
sed 's#require.*xmlseclibs.*#require_once "%{buildroot}%{phpdir}/RobRichards/XMLSecLibs3/autoload.php";#' \
    -i tests/*.phpt

: Skip tests known to fail
rm -f tests/extract-win-cert.phpt

: Disable deprecation warning with php 7.1
#for test in tests/*phpt; do
#  echo -e "\n--INI--\nerror_reporting=24575" >>$test
#done

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose tests || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG.txt
%doc composer.json
%doc README.md
%dir %{phpdir}/RobRichards
     %{phpdir}/RobRichards/XMLSecLibs3


%changelog
* Wed Jul 12 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.0-1
- Initial package
