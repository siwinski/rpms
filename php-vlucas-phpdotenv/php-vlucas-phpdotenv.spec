#
# Fedora spec file for php-vlucas-phpdotenv
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     vlucas
%global github_name      phpdotenv
%global github_version   2.4.0
%global github_commit    3cc116adbe4b11be5ec557bf1d24dc5e3a21d18c

%global composer_vendor  vlucas
%global composer_project phpdotenv

# "php": ">=5.3.9"
%global php_min_ver 5.3.9

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Loads environment variables from .env

Group:         Development/Libraries
License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-vlucas-phpdotenv-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 2.4.0)
BuildRequires: php-ctype
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.4.0)
Requires:      php-ctype
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Loads environment variables from .env to getenv(), $_ENV and $_SERVER
automagically.

This is a PHP version of the original Ruby dotenv [1].

Autoloader: %{phpdir}/Dotenv/autoload.php

[1] https://github.com/bkeepers/dotenv


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

\Fedora\Autoloader\Autoload::addPsr4('Dotenv\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Dotenv


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        pwd
        ls
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Dotenv/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc *.md
%doc composer.json
%{phpdir}/Dotenv


%changelog
* Sat Oct 21 2017 Shawn Iwinski <shawn@iwin.ski> - 2.4.0-1
- Initial package
