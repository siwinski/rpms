#
# Fedora spec file for php-COMPOSER_VENDOR-COMPOSER_PROJECT
#
# Copyright (c) COPYRIGHT_YEAR Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner      xxxxx
%global github_name       xxxxx
%global github_version    GITHUB_VERSION
%global github_commit     xxxxx

%global composer_vendor   COMPOSER_VENDOR
%global composer_project  COMPOSER_PROJECT

%global namespace_vendor  xxxxx
%global namespace_project xxxxx
#%global namespace_version xxxxx

# Deprecate Symfony 2 on Fedora 32+ and EPEL 8+
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%global with_symfony2 0
%else
%global with_symfony2 1
%endif

# "php": ""
%global php_min_ver xxxxx
# xxxxx
%global _min_ver xxxxx
%global _max_ver xxxxx

# PHPUnit
## v9
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 8
%global phpunit_require phpunit9
%global phpunit_exec    phpunit9
%else
## v8
%if 0%{?fedora} >= 29
%global phpunit_require phpunit8
%global phpunit_exec    phpunit8
%else
## v7
%if 0%{?fedora} >= 28
%global phpunit_require phpunit7
%global phpunit_exec    phpunit7
%else
## v6
%if 0%{?fedora} >= 26
%global phpunit_require phpunit6
%global phpunit_exec    phpunit6
%else
## Pre-v6
%global phpunit_require php-composer(phpunit/phpunit)
%global phpunit_exec    phpunit
%endif
%endif
%endif
%endif

# Build using "--with tests" to enable tests
#%global with_tests 0%{?_with_tests:1}
# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

# Range dependencies supported?
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
%global with_range_dependencies 1
%else
%global with_range_dependencies 0
%endif

# Weak dependencies supported?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%global with_weak_dependencies 1
%else
%global with_weak_dependencies 0
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{?namespace_version}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       xxxxx

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# GitHub export does not include tests
# Run php-COMPOSER_VENDOR-COMPOSER_PROJECT-get-source.sh to create full source
#Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
#Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: %{phpunit_require}
%if %{with_range_dependencies}
BuildRequires: (php-composer() >= %{_min_ver} with php-composer() < %{_max_ver})
%else
BuildRequires: php-composer() >= %{_min_ver}
BuildRequires: php-composer() <  %{_max_ver}
%endif
## phpcompatinfo (computed from version GITHUB_VERSION)
BuildRequires: php-
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if %{with_range_dependencies}
Requires:      (php-composer() >= %{_min_ver} with php-composer() < %{_max_ver})
%else
Requires:      php-composer() >= %{_min_ver}
Requires:      php-composer() <  %{_max_ver}
%endif
# phpcompatinfo (computed from version GITHUB_VERSION)
Requires:      php-
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if %{with_weak_dependencies}
Suggests:      php-composer()
%endif

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{namespace_vendor}\\%{namespace_project}\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}///autoload.php',
));

\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}///autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/%{namespace_vendor}
cp -rp src %{buildroot}%{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{namespace_vendor}\\%{namespace_project}\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in "" %{?rhel:php54 php55 php56} php70 php71 php72 php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
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
%dir %{phpdir}/%{namespace_vendor}
     %{phpdir}/%{namespace_vendor}/%{namespace_project}%{?namespace_version}


%changelog
* CHANGELOG_DAY_NAME CHANGELOG_MONTH CHANGELOG_DAY CHANGELOG_YEAR Shawn Iwinski <shawn@iwin.ski> - GITHUB_VERSION-1
- Initial package
