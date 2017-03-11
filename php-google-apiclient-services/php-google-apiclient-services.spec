#
# Fedora spec file for php-google-apiclient-services
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     google
%global github_name      google-api-php-client-services
%global github_version   0.10
%global github_commit    8ec364f33a230d259b3a532edc875c102976f261

%global composer_vendor  google
%global composer_project apiclient-services

# "php": ">=5.4"
%global php_min_ver 5.4

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Client library for Google APIs

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.10)
##     <none>
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.10)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Conflicts:     php-google-apiclient < 2

%description
%{summary}.

Autoloader: %{phpdir}/Google/Service/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Google/Service/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr0('Google_Service_', dirname(dirname(__DIR__)));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
sed -e '/require_once/d' \
    -e 's#$path\s*=.*#$path="%{buildroot}%{phpdir}/Google/Service/";#' \
    -i tests/ServiceTest.php

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Google/Service/autoload.php';

// Mock "Google_Service_autoload" class for Google_Service_ServiceTest
// @see Google_Service_ServiceTest::serviceProvider()
class Google_Service_autoload {}
BOOTSTRAP

: Upstream tests
%{_bindir}/phpunit --verbose --bootstrap bootstrap.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Google
     %{phpdir}/Google/Service


%changelog
* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.10-1
- Initial package
