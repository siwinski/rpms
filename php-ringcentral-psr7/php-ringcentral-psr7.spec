#
# Fedora spec file for php-ringcentral-psr7
#
# Copyright (c) 2018 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     ringcentral
%global github_name      psr7
%global github_version   1.2.1
%global github_commit    2594fb47cdc659f3fcf0aa1559b7355460555303

%global composer_vendor  ringcentral
%global composer_project psr7

# "php": ">=5.3"
%global php_min_ver 5.3
# "psr/http-message": "~1.0"
%global psr_http_message_min_ver 1.0
%global psr_http_message_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       PSR-7 message implementation

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
BuildRequires: php-composer(psr/http-message) <  %{psr_http_message_max_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
## phpcompatinfo for version 1.2.1
BuildRequires: php-hash
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/http-message) <  %{psr_http_message_max_ver}
Requires:      php-composer(psr/http-message) >= %{psr_http_message_min_ver}
# phpcompatinfo for version 1.2.1
Requires:      php-hash
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/http-message-implementation) = 1.0

%description
This repository contains a partial PSR-7 [1] message implementation, several
stream decorators, and some helpful functionality like query string parsing.
Currently missing ServerRequestInterface and UploadedFileInterface; a pull
request for these features is welcome.

Autoloader: %{phpdir}/RingCentral/Psr7/autoload.php

[1] http://www.php-fig.org/psr/psr-7/


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

\Fedora\Autoloader\Autoload::addPsr4('RingCentral\\Psr7\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Http/Message/autoload.php',
    __DIR__.'/functions_include.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/RingCentral
cp -rp src %{buildroot}%{phpdir}/RingCentral/Psr7


%check
%if %{with_tests}
: Create mock Composer autoloader for test bootstrap
mkdir vendor
ln -s %{buildroot}%{phpdir}/RingCentral/Psr7/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
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
%dir %{phpdir}/RingCentral
     %{phpdir}/RingCentral/Psr7


%changelog
* Wed Jan 03 2018 Shawn Iwinski <shawn@iwin.ski> - 1.2.1-1
- Initial package
