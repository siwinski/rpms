#
# Fedora spec file for php-tedivm-stash
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     tedious
%global github_name      Stash
%global github_version   0.14.1
%global github_commit    bcb739b08b22571e35589ebe5403af9b89a33394

%global composer_vendor  tedivm
%global composer_project stash

# "php": "^5.4|^7.0"
%global php_min_ver 5.4
# "psr/cache": "~1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A PHP caching library

Group:         Development/Libraries
License:       BSD
URL:           http://www.stashphp.com/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# [Driver/Composite] Fix PHP 7.2 failure
# https://github.com/tedious/Stash/pull/356
# https://github.com/tedious/Stash/pull/356.patch
Patch0:        %{name}-pull-356.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
## phpcompatinfo (computed from version 0.14.1)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:      php-composer(psr/cache) <  %{psr_cache_max_ver}
# phpcompatinfo (computed from version 0.14.1)
Requires:      php-ctype
Requires:      php-date
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-session
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/cache-implementation) = 1.0.0

%description
Stash makes it easy to speed up your code by caching the results of expensive
functions or code. Certain actions, like database queries or calls to external
APIs, take a lot of time to run but tend to have the same results over short
periods of time. This makes it much more efficient to store the results and
call them back up later.

Autoloader: %{phpdir}/Stash/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: [Driver/Composite] Fix PHP 7.2 failure
: https://github.com/tedious/Stash/pull/356
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Stash/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Stash\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Cache/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/Stash %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Rewrite tests bootstrap
# (because it assumes Composer autoloader is returned)
mv tests/bootstrap.php tests/bootstrap.php.dist
cat <<'BOOTSTRAP' | tee tests/bootstrap.php
<?php
define('TESTING', true);
define('TESTING_DIRECTORY', __DIR__);
error_reporting(-1);
date_default_timezone_set('UTC');

require '%{buildroot}%{phpdir}/Stash/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Stash\\Test\\', __DIR__.'/Stash/Test');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose || RETURN_CODE=1
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
%{phpdir}/Stash


%changelog
* Sun Apr 30 2017 Shawn Iwinski <shawn@iwin.ski> - 0.14.1-1
- Initial package
