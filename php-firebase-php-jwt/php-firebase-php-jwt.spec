#
# Fedora spec file for php-firebase-php-jwt
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     firebase
%global github_name      php-jwt
%global github_version   4.0.0
%global github_commit    dccf163dc8ed7ed6a00afc06c51ee5186a428d35

%global composer_vendor  firebase
%global composer_project php-jwt

# "php": ">= 5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A simple library to encode and decode JSON Web Tokens (JWT)

Group:         Development/Libraries
License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-firebase-php-jwt-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 4.0.0)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 4.0.0)
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-mbstring
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A simple library to encode and decode JSON Web Tokens (JWT) in PHP, conforming
to RFC 7519 [1].

Autoloader: %{phpdir}/Firebase/JWT/autoload.php

[1] https://tools.ietf.org/html/rfc7519


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

\Fedora\Autoloader\Autoload::addPsr4('Firebase\\JWT\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Firebase/JWT
cp -rp src/* %{buildroot}%{phpdir}/Firebase/JWT/


%check
%if %{with_tests}
BOOTSTRAP=%{buildroot}%{phpdir}/Firebase/JWT/autoload.php

: Upstream tests
%{_bindir}/phpunit --verbose --bootstrap $BOOTSTRAP

: Upstream tests with SCLs if available
SCL_RETURN_CODE=0
for SCL in php54 php55 php56 php70 php71; do
    if which $SCL; then
        $SCL %{_bindir}/phpunit --bootstrap $BOOTSTRAP || SCL_RETURN_CODE=1
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
%dir %{phpdir}/Firebase
     %{phpdir}/Firebase/JWT


%changelog
* Thu Jan 05 2017 Shawn Iwinski <shawn@iwin.ski> - 4.0.0-1
- Initial package
