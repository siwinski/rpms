#
# Fedora spec file for php-cache-integration-tests
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-cache
%global github_name      integration-tests
%global github_version   0.16.0
%global github_commit    a8d9538a44ed5a70d551f9b87f534c98dfe6b0ee

%global composer_vendor  cache
%global composer_project integration-tests

# "php": "^5.4|^7",
%global php_min_ver 5.4
# "psr/cache": "~1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "cache/tag-interop": "^1.0"
%global cache_tag_interop_min_ver 1.0
%global cache_tag_interop_max_ver 2.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Integration tests for PSR-6 and PSR-16 cache implementations

Group:         Development/Libraries
License:       MIT
URL:           http://www.php-cache.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Minimal autoloader test
BuildRequires: php-cli
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(cache/tag-interop) <  %{cache_tag_interop_max_ver}
BuildRequires: php-composer(cache/tag-interop) >= %{cache_tag_interop_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
## Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(cache/tag-interop) <  %{cache_tag_interop_max_ver}
Requires:      php-composer(cache/tag-interop) >= %{cache_tag_interop_min_ver}
Requires:      php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:      php-composer(psr/cache) >= %{psr_cache_min_ver}
# phpcompatinfo (computed from version 0.16.0)
Requires:      php-composer(phpunit/phpunit)
Requires:      php-date
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package contains integration tests to make sure your implementation of a
PSR-6 and/or PSR-16 cache follows the rules by PHP-FIG. It is a part of the PHP
Cache organization.

Autoloader: %{phpdir}/Cache/IntegrationTests/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove unnecessary exec bits
chmod a-x composer.json LICENSE


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Cache\\IntegrationTests\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/TagInterop/autoload.php',
    '%{phpdir}/PHPUnit/Autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Cache
cp -rp src %{buildroot}%{phpdir}/Cache/IntegrationTests


%check
: Minimal autoloader test
php -r '
    require_once "%{buildroot}%{phpdir}/Cache/IntegrationTests/autoload.php";
    exit(class_exists("Cache\\IntegrationTests\\CachePoolTest") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Cache/IntegrationTests


%changelog
* Fri Apr 14 2017 Shawn Iwinski <shawn@iwin.ski> - 0.16.0-1
- Initial package
