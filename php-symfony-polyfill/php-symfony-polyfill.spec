#
# Fedora spec file for php-symfony-polyfill
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      polyfill
%global github_version   1.0.0
%global github_commit    fef21adc706d3bb8f31d37c503ded2160c76c64a

%global composer_vendor  symfony
%global composer_project polyfill

# "php": ">=5.3.3"
%global php_min_ver 5.3.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Symfony polyfills backporting features to lower PHP versions

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-composer(theseer/autoload)
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(ircmaxell/password-compat)
BuildRequires: php-composer(paragonie/random_compat)
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-ldap
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(ircmaxell/password-compat)
Requires:      php-composer(paragonie/random_compat)
# phpcompatinfo (computed from version 1.0.0)
Requires:      php-hash
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project})       = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-util)  = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php54) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php55) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php56) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php70) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Symfony/Polyfill/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Docs
mkdir -p docs/{Php54,Php55,Php56,Php70}
mv *.md composer.json docs/
mv src/Php54/{*.md,composer.json} docs/Php54/
mv src/Php55/{*.md,composer.json} docs/Php55/
mv src/Php56/{*.md,composer.json} docs/Php56/
mv src/Php70/{*.md,composer.json} docs/Php70/

: Remove unneeded polyfills
rm -rf {src,tests}/{Iconv,Intl,Mbstring,Xml}




%build
: Create autoloader classmap
%{_bindir}/phpab --nolower --tolerant --output src/autoload.classmap.php src/
cat src/autoload.classmap.php

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

// Classmap
require_once __DIR__ . '/autoload.classmap.php';

// Php54
require_once __DIR__ . '/Php54/bootstrap.php';

// Php55
require_once '%{phpdir}/password_compat/password.php';
require_once __DIR__ . '/Php55/bootstrap.php';

// Php56
require_once __DIR__ . '/Php56/bootstrap.php';

// Php70
require_once '%{phpdir}/random_compat/autoload.php';
require_once __DIR__ . '/Php70/bootstrap.php';
AUTOLOAD


%install
: Library
mkdir -p %{buildroot}%{phpdir}/Symfony/Polyfill
cp -rp src/* %{buildroot}%{phpdir}/Symfony/Polyfill/


%check
%if %{with_tests}
%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/Symfony/Polyfill/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc docs/*
%{phpdir}/Symfony/Polyfill
%exclude %{phpdir}/Symfony/Polyfill/*/LICENSE


%changelog
* Sun Dec 06 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-2
- Always include ALL polyfills

* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
