#
# Fedora spec file for php-guzzlehttp-guzzle5
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      guzzle
%global github_version   5.3.0
%global github_commit    f3c8c22471cb55475105c14769644a49c3262b93

%global composer_vendor  guzzlehttp
%global composer_project guzzle

# "php": ">=5.4.0"
%global php_min_ver      5.4.0
# "guzzlehttp/ringphp": "^1.1"
#     Note: Min version not "1.1" because autoloader required
%global ring_min_ver     1.1.0-3
%global ring_max_ver     2.0
# "psr/log": "^1.0"
%global psr_log_min_ver  1.0
%global psr_log_max_ver  2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:    %global phpdir    %{_datadir}/php}
%{!?testsdir:  %global testsdir  %{_datadir}/tests}

Name:          php-%{composer_vendor}-%{composer_project}5
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       PHP HTTP client and webservice framework

Group:         Development/Libraries
License:       MIT
URL:           http://guzzlephp.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: nodejs
BuildRequires: %{_bindir}/phpunit
BuildRequires: php-guzzlehttp-ringphp-tests
## composer.json
BuildRequires: php(language)                    >= %{php_min_ver}
#BuildRequires: php-composer(guzzlehttp/ringphp) >= %%{ring_min_ver}
BuildRequires: php-guzzlehttp-ringphp           >= %{ring_min_ver}
## phpcompatinfo (computed from version 5.3.0)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language)                    >= %{php_min_ver}
#Requires:      php-composer(guzzlehttp/ringphp) >= %%{ring_min_ver}
Requires:      php-guzzlehttp-ringphp           >= %{ring_min_ver}
Requires:      php-composer(guzzlehttp/ringphp) <  %{ring_max_ver}
# phpcompatinfo (computed from version 5.3.0)
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

Obsoletes:     php-%{composer_vendor}-%{composer_project} <= 5.3.0-3
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Conflicts:     php-composer(%{composer_vendor}/%{composer_project}) >= 6.0

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

**** NOTE: This is major version 5.x of php-guzzlehttp-guzzle.  If you need a
****       newer major version, install php-guzzlehttp-guzzle instead.


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader created by %{name}-%{version}-%{release}
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

require_once '%{phpdir}/GuzzleHttp/Ring/autoload.php';

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('GuzzleHttp\\', dirname(__DIR__));

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp
cp -pr src/* %{buildroot}%{phpdir}/GuzzleHttp/


%check
%if %{with_tests}
: Create tests autoloader
cat <<'AUTOLOAD' | tee tests/autoload.php
<?php

require_once 'GuzzleHttp/autoload.php';

$fedoraClassLoader->addPrefix('GuzzleHttp\\Tests', __DIR__);
AUTOLOAD

: Modify tests bootstrap
sed -e "s#.*require.*autoload.*#require __DIR__ . '/autoload.php';#" \
    -e "s#.*require.*Server.php.*#require '%{testsdir}/php-guzzlehttp-ringphp/autoload.php';#" \
    -i tests/bootstrap.php

: Mock tests PSR-0
mkdir tests/GuzzleHttp
ln -s .. tests/GuzzleHttp/Tests

%{_bindir}/phpunit --include-path %{buildroot}%{phpdir} --verbose
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/GuzzleHttp/*


%changelog
* Sat Sep 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.0-4
- Renamed from php-guzzlehttp-guzzle to php-guzzlehttp-guzzle5

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.0-3
- Autoloader updates

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.3.0-1
- Updated to 5.3.0 (BZ #1140134)
- Added autoloader
- Re-added tests

* Sun Feb 08 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.1.0-1
- Updated to 5.1.0 (BZ #1140134)
- CA cert no longer bundled (see
  https://github.com/guzzle/guzzle/blob/5.1.0/docs/clients.rst#verify)
- No tests because dependency package does not provide required test file

* Mon Jan 12 2015 Remi Collet <remi@fedoraproject.org> - 4.1.8-3
- Upstream patch for PHP behavior change, thanks Koschei

* Tue Aug 26 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.8-2
- Fix test suite when previous version installed

* Sat Aug 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.8-1
- Updated to 4.1.8 (BZ #1126611)

* Wed Jul 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.4-1
- Updated to 4.1.4 (BZ #1124226)
- Added %%license usage

* Sun Jun 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.2-1
- Updated to 4.1.2

* Fri Jun 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.1.0-1
- Updated to 4.1.0
- Require php-composer virtual provides instead of direct pkgs
- Added php-PsrLog and nodejs build requires
- Added php-composer(%%{composer_vendor}/%%{composer_project}) virtual provide
- Added option to build without tests

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.0.2-1
- Initial package
