#
# RPM spec file for php-guzzlehttp-psr7
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      psr7
%global github_version   1.0.0
%global github_commit    19e510056d8d671d9d9e25dc16937b3dd3802ae6

%global composer_vendor  guzzlehttp
%global composer_project psr7

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "psr/http-message": "^1.0"
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
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language)                  >= %{php_min_ver}
BuildRequires: php-composer(psr/http-message) >= %{psr_http_message_min_ver}
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php-hash
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-zlib
%endif

# composer.json
Requires:      php(language)                  >= %{php_min_ver}
Requires:      php-composer(psr/http-message) >= %{psr_http_message_min_ver}
Requires:      php-composer(psr/http-message) <  %{psr_http_message_max_ver}
# phpcompatinfo (computed from version 1.0.0)
Requires:      php-hash
Requires:      php-pcre
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/http-message-implementation)        = 1.0

%description
PSR-7 message implementation, several stream decorators, and some helpful
functionality like query string parsing.


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
(cat <<'AUTOLOAD'
<?php
/**
 * Autoloader created by %{name}-%{version}-%{release}
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once 'Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('GuzzleHttp\\Psr7', dirname(dirname(__DIR__)));

require_once __DIR__ . '/functions.php';
require_once 'Psr/Http/Message/autoload.php';

return $fedoraClassLoader;
AUTOLOAD
) | tee src/autoload.php


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp/Psr7
cp -rp src/* %{buildroot}%{phpdir}/GuzzleHttp/Psr7/


%check
%if %{with_tests}
sed "s#require.*autoload.*#require '%{buildroot}%{phpdir}/GuzzleHttp/Psr7/autoload.php';#" \
    -i tests/bootstrap.php

%{_bindir}/phpunit -v
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/GuzzleHttp
     %{phpdir}/GuzzleHttp/Psr7


%changelog
* Sun Jun 14 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-1
- Initial package
