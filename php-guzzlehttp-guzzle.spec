%global github_owner     guzzle
%global github_name      guzzle
%global github_version   4.1.0
%global github_commit    85a0ba7de064493c928a8bcdc5eef01e0bde9953

%global composer_vendor  guzzlehttp
%global composer_project guzzle

# "php": ">=5.4.0"
%global php_min_ver      5.4.0
# "guzzlehttp/streams": "~1.0"
%global streams_min_ver  1.0
%global streams_max_ver  2.0
# "psr/log": "~1.0"
%global psr_log_min_ver  1.0
%global psr_log_max_ver  2.0

# Build using "--without tests" to disable tests
%global with_tests       %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       PHP HTTP client and webservice framework

Group:         Development/Libraries
License:       MIT
URL:           http://guzzlephp.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests
BuildRequires: nodejs
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(guzzlehttp/streams) >= %{streams_min_ver}
BuildRequires: php-composer(guzzlehttp/streams) <  %{streams_max_ver}
BuildRequires: php-PsrLog >= %{psr_log_min_ver}
BuildRequires: php-PsrLog <  %{psr_log_max_ver}
BuildRequires: php-phpunit-PHPUnit
BuildRequires: php-curl
BuildRequires: php-json
# For tests: phpcompatinfo (computed from version 4.1.0)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(guzzlehttp/streams) >= %{streams_min_ver}
Requires:      php-composer(guzzlehttp/streams) <  %{streams_max_ver}
Requires:      php-json
# phpcompatinfo (computed from version 4.1.0)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl

Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

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
* Fri Jun 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.0-1
- Updated to 4.1.0
- Require php-composer virtual provides instead of direct pkgs
- Added php-PsrLog and nodejs build requires
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.0.2-1
- Initial package
