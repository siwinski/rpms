#
# Fedora spec file for php-cache-adapter-common
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-cache
%global github_name      adapter-common
%global github_version   0.4.0
%global github_commit    2adecd1375fe2ce15b1679349965d7fa73f2676b

%global composer_vendor  cache
%global composer_project adapter-common

# "php": "^5.6 || ^7.0"
%global php_min_ver 5.6
# "cache/tag-interop": "^1.0"
%global cache_tag_interop_min_ver 1.0
%global cache_tag_interop_max_ver 2.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/log": "^1.0"
%global psr_log_min_ver 1.0
%global psr_log_max_ver 2.0
# "psr/simple-cache": "^1.0"
%global psr_simple_cache_min_ver 1.0
%global psr_simple_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common classes for PSR-6 adapters

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(cache/tag-interop) <  %{cache_tag_interop_max_ver}
BuildRequires: php-composer(cache/tag-interop) >= %{cache_tag_interop_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
BuildRequires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
## phpcompatinfo (computed from version 0.4.0)
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(cache/tag-interop) <  %{cache_tag_interop_max_ver}
Requires:      php-composer(cache/tag-interop) >= %{cache_tag_interop_min_ver}
Requires:      php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires:      php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
Requires:      php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
# phpcompatinfo (computed from version 0.4.0)
Requires:      php-date
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Cache/Adapter/Common/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Cache\\Adapter\\Common\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/TagInterop/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/Psr/SimpleCache/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Cache/Adapter/Common
cp -rp * %{buildroot}%{phpdir}/Cache/Adapter/Common/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Cache/Adapter/Common/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Cache\\Adapter\\Common\\Tests\\', __DIR__.'/Tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php70 php71 php72; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose --bootstrap bootstrap.php \
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
%dir %{phpdir}/Cache/Adapter
     %{phpdir}/Cache/Adapter/Common
%exclude %{phpdir}/Cache/Adapter/Common/*.md
%exclude %{phpdir}/Cache/Adapter/Common/composer.json
%exclude %{phpdir}/Cache/Adapter/Common/LICENSE
%exclude %{phpdir}/Cache/Adapter/Common/phpunit.*
%exclude %{phpdir}/Cache/Adapter/Common/Tests


%changelog
* Fri Apr 14 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.0-1
- Initial package
