%global github_owner   google
%global github_name    google-api-php-client
%global github_version 1.0.0
%global github_commit  889aa1e32d8d4ca5c747154aef5d9e8649ff1d0a
%global github_release alpha

# "php": ">=5.2.1"
%global php_min_ver    5.2.1

Name:          php-google
Version:       %{github_version}
Release:       1.%{github_release}%{dist}
Summary:       Google APIs Client Library for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://developers.google.com/api-client-library/php/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from v1.0.0-alpha)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-openssl
BuildRequires: php-session
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
Requires:      ca-certificates
# phpcompatinfo (computed from v1.0.0-alpha)
Requires:      php-date
Requires:      php-json
Requires:      php-openssl
Requires:      php-spl

%description
Google APIs Client Library for PHP provides access to many Google APIs.
It is designed for PHP client-application developers and offers simple,
flexible, powerful API access.


%prep
%setup -q -n %{github_name}-%{github_commit}

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
sed 's/colors="true"/colors="false"/' \
    -i tests/phpunit.xml

# Skip tests requiring network access
sed 's/function testBatchRequest/function SKIP_testBatchRequest/' \
    -i tests/general/ApiBatchRequestTest.php
sed 's/function testPageSpeed/function SKIP_testPageSpeed/' \
    -i tests/pagespeed/PageSpeedTest.php
sed -e 's/function testGetPerson/function SKIP_testGetPerson/' \
    -e 's/function testListActivities/function SKIP_testListActivities/' \
    -i tests/plus/PlusTest.php

cd tests
%{_bindir}/phpunit -d date.timezone="UTC" .

# Ensure unbundled CA cert is referenced
grep '%{_sysconfdir}/pki/tls/cert.pem' --quiet \
    %{buildroot}%{_datadir}/php/Google/IO/Stream.php


%files
%doc LICENSE *.md composer.json examples
%{_datadir}/php/Google


%changelog
* Mon Dec 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-1.alpha
- Initial package
