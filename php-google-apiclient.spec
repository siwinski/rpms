%global github_owner   google
%global github_name    google-api-php-client
%global github_version 1.0.3
%global github_commit  2b3b475e3ee52e92fc7b649138ef4f9da3d4f9b9
%global github_release .beta

# "php": ">=5.2.1"
%global php_min_ver    5.2.1

Name:          php-google-apiclient
Version:       %{github_version}
Release:       0.1%{?github_release}%{dist}
Summary:       Client library for Google APIs

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://developers.google.com/api-client-library/php/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from 1.0.3-beta)
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-reflection
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
Requires:      ca-certificates
# phpcompatinfo (computed from 1.0.3-beta)
Requires:      php-date
Requires:      php-json
Requires:      php-openssl
Requires:      php-reflection
Requires:      php-spl

%description
Google APIs Client Library for PHP provides access to many Google APIs.
It is designed for PHP client-application developers and offers simple,
flexible, powerful API access.

Optional:
* php-pecl-apcu
* php-pecl-memcache
* php-pecl-memcached


%prep
%setup -qn %{github_name}-%{github_commit}

# Remove bundled CA cert
rm -f src/Google/IO/cacerts.pem
sed "s#dirname(__FILE__)\s*.\s*'/cacerts.pem'#'%{_sysconfdir}/pki/tls/cert.pem'#" \
    -i src/Google/IO/Stream.php


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -rp src/* %{buildroot}%{_datadir}/php/


%check
# Turn off PHPUnit colors
sed 's/colors="true"/colors="false"/' -i tests/phpunit.xml

# Skip tests requiring network access
sed -e 's/function testBatchRequest/function SKIP_testBatchRequest/' \
    -e 's/function testInvalidBatchRequest/function SKIP_testInvalidBatchRequest/' \
    -i tests/general/ApiBatchRequestTest.php
sed 's/function testPageSpeed/function SKIP_testPageSpeed/' \
    -i tests/pagespeed/PageSpeedTest.php
sed -e 's/function testGetPerson/function SKIP_testGetPerson/' \
    -e 's/function testListActivities/function SKIP_testListActivities/' \
    -i tests/plus/PlusTest.php
sed 's/function testMissingFieldsAreNull/function SKIP_testMissingFieldsAreNull/' \
    -i tests/youtube/YouTubeTest.php

cd tests
%{_bindir}/phpunit -d date.timezone="UTC" .

# Ensure unbundled CA cert is referenced
grep '%{_sysconfdir}/pki/tls/cert.pem' --quiet \
    %{buildroot}%{_datadir}/php/Google/IO/Stream.php


%files
%doc LICENSE *.md composer.json examples
%{_datadir}/php/Google


%changelog
* Sat Feb 08 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.3-0.1.beta
- Initial package
