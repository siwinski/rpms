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

%global github_owner     xxxxx
%global github_name      xxxxx
%global github_version   GITHUB_VERSION
%global github_commit    xxxxx

%global composer_vendor  COMPOSER_VENDOR
%global composer_project COMPOSER_PROJECT

# "php": ">= 5.3.3"
%global php_min_ver xxxxx
# xxxxx
%global _min_ver xxxxx
%global _max_ver xxxxx

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       xxxxx

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# GitHub export does not include tests.
# Run php-COMPOSER_VENDOR-COMPOSER_PROJECT-get-source.sh to create full source.
#Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
#Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer() >= %{_min_ver} with php-composer() < %{_max_ver})
%else
BuildRequires: php-composer() >= %{_min_ver}
BuildRequires: php-composer() <  %{_max_ver}
%endif
## phpcompatinfo for version GITHUB_VERSION
BuildRequires: php-
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer() >= %{_min_ver} with php-composer() < %{_max_ver})
%else
Requires:      php-composer() >= %{_min_ver}
Requires:      php-composer() <  %{_max_ver}
%endif
# phpcompatinfo for version GITHUB_VERSION
Requires:      php-
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-composer()
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}///autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('xxxxx\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}///autoload.php',
));

\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}///autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/xxxxx/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('xxxxx\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
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
%dir %{phpdir}/
     %{phpdir}/


%changelog
* CHANGELOG_DAY_NAME CHANGELOG_MONTH CHANGELOG_DAY CHANGELOG_YEAR Shawn Iwinski <shawn@iwin.ski> - GITHUB_VERSION-1
- Initial package
