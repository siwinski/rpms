#
# Fedora spec file for php-google-auth
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     google
%global github_name      google-auth-library-php
%global github_version   0.11.1
%global github_commit    a240674b08a09949fd5597f7590b3ed83663a12d

%global composer_vendor  google
%global composer_project auth

# "php": ">=5.4"
%global php_min_ver 5.4
# "firebase/php-jwt": "~2.0|~3.0|~4.0"
%global firebase_jwt_min_ver 4.0
%global firebase_jwt_max_ver 5.0
# "guzzlehttp/guzzle": "~5.3|~6.0"
%global guzzle_min_ver 6.0
%global guzzle_max_ver 7.0
# "guzzlehttp/psr7": "~1.2"
%global guzzle_psr7_min_ver 1.2
%global guzzle_psr7_max_ver 2.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/http-message": "^1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Google Auth Library for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
## phpcompatinfo (computed from version 0.11.1)
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:     php(language) >= %{php_min_ver}
Requires:     php-composer(firebase/php-jwt) <  %{firebase_jwt_max_ver}
Requires:     php-composer(firebase/php-jwt) >= %{firebase_jwt_min_ver}
Requires:     php-composer(guzzlehttp/guzzle) <  %{guzzle_max_ver}
Requires:     php-composer(guzzlehttp/guzzle) >= %{guzzle_min_ver}
Requires:     php-composer(guzzlehttp/psr7) <  %{guzzle_psr7_max_ver}
Requires:     php-composer(guzzlehttp/psr7) >= %{guzzle_psr7_min_ver}
Requires:     php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:     php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:     php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:     php-composer(psr/http-message) >= %{psr_http_message_min_ver}
# phpcompatinfo (computed from version 0.11.1)
Requires:      php-date
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Conflicts:     php-google-apiclient < 2

%description
This is Google's officially supported PHP client library for using OAuth 2.0
authorization and authentication with Google APIs.

Autoloader: %{phpdir}/Google/Auth/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Google\\Auth\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Firebase/JWT/autoload.php',
    '%{phpdir}/GuzzleHttp/Psr7/autoload.php',
    '%{phpdir}/GuzzleHttp6/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/Http/Message/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Google/Auth
cp -rp src/* %{buildroot}%{phpdir}/Google/Auth/


%check
%if %{with_tests}
: Mock composer autoloader
mkdir vendor
ln -s %{buildroot}%{phpdir}/Google/Auth/autoload.php vendor/autoload.php

: Upstream tests
%{_bindir}/phpunit --verbose

: Upstream tests with SCLs if available
SCL_RETURN_CODE=0
for SCL in php55 php56 php70 php71; do
    if which $SCL; then
        $SCL %{_bindir}/phpunit --verbose || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Google
     %{phpdir}/Google/Auth


%changelog
* Thu Jan 05 2017 Shawn Iwinski <shawn@iwin.ski> - 0.11.1-1
- Initial package
