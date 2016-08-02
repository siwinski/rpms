#
# Fedora spec file for php-sentry
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     getsentry
%global github_name      sentry-php
%global github_version   1.1.0
%global github_commit    33fbf98955cdfe34e99fe43ef8bdd874253675dd

%global composer_vendor  sentry
%global composer_project sentry

# "php": ">=5.2.4"
%global php_min_ver      5.2.4
# "monolog/monolog": "*"
#     NOTE: Min version because autoloader required
%global monolog_min_ver  1.15.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       PHP client for Sentry

Group:         Development/Libraries
License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-sentry-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                 >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(monolog/monolog) >= %{monolog_min_ver}
BuildRequires: php-curl
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
# Conflicts
BuildConflicts: php-Raven
%endif

Requires:      ca-certificates
# composer.json
Requires:      php(language)                 >= %{php_min_ver}
Requires:      php-composer(monolog/monolog) >= %{monolog_min_ver}
Requires:      php-curl
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl
Requires:      php-zlib
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Rename
Obsoletes:     php-Raven < %{version}
Provides:      php-Raven = %{version}-%{release}
Provides:      php-composer(raven/raven) = %{version}


%description
%{summary} (http://getsentry.com).

Autoloader: %{phpdir}/Raven/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove bundled cert
rm -rf lib/Raven/data
sed "/return.*cacert\.pem/s#.*#        return '%{_sysconfdir}/pki/tls/cert.pem';#" \
    -i lib/Raven/Client.php

: Update autoloader require in bin
sed "/require.*Autoloader/s#.*#require_once '%{phpdir}/Raven/Autoloader.php';#" \
    -i bin/sentry


%build
: Create autoloader
cat <<'AUTOLOAD' | tee lib/Raven/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

require_once dirname(__FILE__).'/Autoloader.php';
Raven_Autoloader::register();

require_once '%{phpdir}/Monolog/autoload.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/sentry %{buildroot}%{_bindir}/
: Compat bin
ln -s sentry %{buildroot}%{_bindir}/raven


%check
: Library version value check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Raven/Client.php";
    $version = Raven_Client::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
session_start();
require_once '%{buildroot}%{phpdir}/Raven/autoload.php';
BOOTSTRAP

: Run tests
%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.rst
%doc AUTHORS
%doc CHANGES
%doc composer.json
%{phpdir}/Raven
%{_bindir}/raven
%{_bindir}/sentry


%changelog
* Mon Aug 01 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
