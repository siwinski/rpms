#
# Fedora spec file for php-cache-filesystem-common
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-cache
%global github_name      filesystem-adapter
%global github_version   0.4.0
%global github_commit    98ee81842156d18dade449f4dd5b3a89f9a9fcc9

%global composer_vendor  cache
%global composer_project filesystem-adapter

# "php": "^5.6 || ^7.0"
%global php_min_ver 5.6
# "cache/adapter-common": "^0.4"
%global cache_adapter_common_min_ver 0.4
%global cache_adapter_common_max_ver 1.0
# "cache/integration-tests": "^0.16"
%global cache_integration_tests_min_ver 0.16
%global cache_integration_tests_max_ver 1.0
# "league/flysystem": "^1.0"
%global league_flysystem_min_ver 1.0
%global league_flysystem_max_ver 2.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/simple-cache": "^1.0"
%global psr_simple_cache_min_ver 1.0
%global psr_simple_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       A PSR-6 cache implementation using filesystem

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(cache/adapter-common) <  %{cache_adapter_common_max_ver}
BuildRequires: php-composer(cache/adapter-common) >= %{cache_adapter_common_min_ver}
BuildRequires: php-composer(cache/integration-tests) <  %{cache_integration_tests_max_ver}
BuildRequires: php-composer(cache/integration-tests) >= %{cache_integration_tests_min_ver}
BuildRequires: php-composer(league/flysystem) <  %{league_flysystem_max_ver}
BuildRequires: php-composer(league/flysystem) >= %{league_flysystem_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
BuildRequires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
## phpcompatinfo (computed from version 0.4.0)
BuildRequires: php-date
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(cache/adapter-common) <  %{cache_adapter_common_max_ver}
Requires:      php-composer(cache/adapter-common) >= %{cache_adapter_common_min_ver}
Requires:      php-composer(league/flysystem) <  %{league_flysystem_max_ver}
Requires:      php-composer(league/flysystem) >= %{league_flysystem_min_ver}
Requires:      php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:      php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:      php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
Requires:      php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
# phpcompatinfo (computed from version 0.4.0)
Requires:      php-date
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/cache-implementation) = 1.0

%description
A PSR-6 cache implementation using filesystem. This implementation supports
tags.

Autoloader: %{phpdir}/Cache/Adapter/Filesystem/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Cache\\Adapter\\Filesystem\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/Adapter/Common/autoload.php',
    '%{phpdir}/League/Flysystem/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/SimpleCache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Cache/Adapter/Filesystem
cp -rp * %{buildroot}%{phpdir}/Cache/Adapter/Filesystem/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Cache/Adapter/Filesystem/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/IntegrationTests/autoload.php',
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
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
%{phpdir}/Cache/Adapter/Filesystem
%exclude %{phpdir}/Cache/Adapter/Filesystem/*.md
%exclude %{phpdir}/Cache/Adapter/Filesystem/composer.json
%exclude %{phpdir}/Cache/Adapter/Filesystem/LICENSE
%exclude %{phpdir}/Cache/Adapter/Filesystem/phpunit.*
%exclude %{phpdir}/Cache/Adapter/Filesystem/Tests


%changelog
* Tue May 30 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-2
- Fix directory ownership

* Fri Apr 14 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Initial package
