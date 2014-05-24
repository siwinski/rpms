%global github_owner     guzzle
%global github_name      guzzle
%global github_version   4.0.2
%global github_commit    40db53833aaea528347994acd4578d7b9b2211ee

%global composer_vendor  guzzlehttp
%global composer_project guzzle

# "php": ">=5.4.0"
%global php_min_ver      5.4.0
# "guzzlehttp/streams": "~1.0"
%global streams_min_ver  1.0
%global streams_max_ver  2.0

# Build using "--without tests" to disable tests
%global with_tests       %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       PHP HTTP client and webservice framework

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests: composer.json
BuildRequires: php(language)          >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/streams) or php-packagist(guzzlehttp/streams) instead
BuildRequires: php-guzzlehttp-streams >= %{streams_min_ver}
BuildRequires: php-guzzlehttp-streams <  %{streams_max_ver}
BuildRequires: php-phpunit-PHPUnit
# For tests: phpcompatinfo (computed from version 4.0.2)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-simplexml
BuildRequires: php-spl
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language)          >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/streams) or php-packagist(guzzlehttp/streams) instead
Requires:      php-guzzlehttp-streams >= %{streams_min_ver}
Requires:      php-guzzlehttp-streams <  %{streams_max_ver}
# phpcompatinfo (computed from version 4.0.2)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl

# TODO: Provide whichever virtual provide that gets approved in Fedora PHP packaging guidelines
#Provides:      php-composer(%%{composer_vendor}/%%{composer_project}) = %%{version}
#Provides:      php-packagist(%%{composer_vendor}/%%{composer_project}) = %%{version}

%description
Guzzle is a PHP HTTP client that makes it easy to work with HTTP/1.1 and takes
the pain out of consuming web services.

* Pluggable HTTP adapters that can send requests serially or in parallel
* Doesn't require cURL, but uses cURL by default
* Streams data for both uploads and downloads
* Provides event hooks & plugins for cookies, caching, logging, OAuth, mocks,
  etc
* Keep-Alive & connection pooling
* SSL Verification
* Automatic decompression of response bodies
* Streaming multipart file uploads
* Connection timeouts


%prep
%setup -qn %{github_name}-%{github_commit}

# Remove bundled cert
rm -f src/cacert.pem
sed "s#__DIR__ . '/cacert.pem'#'%{_sysconfdir}/pki/tls/cert.pem'#" \
    -i src/Client.php
sed "s#cacert.pem#%{_sysconfdir}/pki/tls/cert.pem#" \
    -i tests/ClientTest.php
sed "s#__DIR__ . '/../../src/cacert.pem'#'%{_sysconfdir}/pki/tls/cert.pem'#" \
    -i tests/Adapter/StreamAdapterTest.php



%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/GuzzleHttp
cp -pr src/* %{buildroot}%{_datadir}/php/GuzzleHttp/


%check
%if %{with_tests}
# Ensure no bundled cert
for DIR in src tests
do
    find $DIR | grep 'cacert.pem' && exit 1
    grep -r 'cacert.pem' $DIR && exit 1
done

# Create autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php

require_once '%{_datadir}/php/GuzzleHttp/Stream/functions.php';
require_once __DIR__ . '/../src/functions.php';

spl_autoload_register(function ($class) {
    $src = str_replace(array('\\', '_'), '/', $class).'.php';
    if (!@include_once $src) {
        $psr4_class = preg_replace('#^GuzzleHttp\\\?#', '', $class);
        $psr4_src = str_replace(array('\\', '_'), '/', $psr4_class).'.php';
        @include_once $psr4_src;
    }
});
AUTOLOAD

# Create PHPUnit config w/ colors turned off
sed 's/colors\s*=\s*"true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --include-path="./src:./tests" -d date.timezone="UTC"
%endif


%files
%doc LICENSE *.md composer.json
%{_datadir}/php/GuzzleHttp/*


%changelog
* Sat May 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-2
- Added option to build without tests

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.0.2-1
- Initial package
