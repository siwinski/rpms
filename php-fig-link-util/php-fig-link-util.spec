#
# Fedora spec file for php-fig-link-util
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-fig
%global github_name      link-util
%global github_version   1.0.0
%global github_commit    1a07821801a148be4add11ab0603e4af55a72fac

%global composer_vendor  fig
%global composer_project link-util

# "php": ">=5.5.0"
%global php_min_ver 5.5.0
# "psr/link": "~1.0@dev"
%global psr_link_min_ver 1.0
%global psr_link_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common utility implementations for HTTP links

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-fig-link-util-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/link) <  %{psr_link_max_ver}
BuildRequires: php-composer(psr/link) >= %{psr_link_min_ver}
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/link) <  %{psr_link_max_ver}
Requires:      php-composer(psr/link) >= %{psr_link_min_ver}
# phpcompatinfo (computed from version 1.0.0)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package includes common utilities to assist with implementing
PSR-13 [1].

Note that it is not intended as a complete PSR-13 implementation, only
a partial implementation to make writing other implementations easier.

Autoloader: %{phpdir}/Fig/Link/autoload.php

[1] http://www.php-fig.org/psr/psr-13/


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

\Fedora\Autoloader\Autoload::addPsr4('Fig\\Link\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Psr/Link/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Fig
cp -rp src %{buildroot}%{phpdir}/Fig/Link


%check
%if %{with_tests}
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Fig/Link/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%doc composer.json
%dir %{phpdir}/Fig
     %{phpdir}/Fig/Link


%changelog
* Sun Jun 11 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
