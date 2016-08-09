#
# Fedora spec file for php-egulias-email-validator2
#
# Copyright (c) 2016 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     egulias
%global github_name      EmailValidator
%global github_version   2.1.1
%global github_commit    30562b69fc6c8e9740645877a98063b3842204b2

%global composer_vendor  egulias
%global composer_project email-validator

# "php": ">= 5.5"
%global php_min_ver 5.5
# "doctrine/lexer": "^1.0.1"
#     NOTE: Min version not 1.0.1 because autoloader required
%global doctrine_lexer_min_ver 1.0.1-4
%global doctrine_lexer_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}2
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A library for validating emails against several RFCs (version 2)

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-egulias-email-validator2-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language)                >= %{php_min_ver}
#BuildRequires: php-composer(doctrine/lexer) >= %%{doctrine_lexer_min_ver}
BuildRequires: php-doctrine-lexer           >= %{doctrine_lexer_min_ver}
BuildRequires: php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver}
BuildRequires: php-intl
## phpcompatinfo (computed from version 2.1.1)
BuildRequires: php-dom
BuildRequires: php-filter
BuildRequires: php-pcre
BuildRequires: php-spl
# Autoloader
## NOTE: Min version 2.5 because class
##       \Symfony\Component\ClassLoader\Psr4ClassLoader required
BuildRequires: php-composer(symfony/class-loader) >= 2.5
BuildRequires: php-composer(symfony/class-loader) <  3.0
%endif

# composer.json
Requires:      php(language)                >= %{php_min_ver}
#Requires:      php-composer(doctrine/lexer) >= %%{doctrine_lexer_min_ver}
Requires:      php-doctrine-lexer           >= %{doctrine_lexer_min_ver}
Requires:      php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver}
# composer.json: optional
Requires:      php-intl
# phpcompatinfo (computed from version 2.1.1)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
## NOTE: Min version 2.5 because class
##       \Symfony\Component\ClassLoader\Psr4ClassLoader required
Requires:      php-composer(symfony/class-loader) >= 2.5
Requires:      php-composer(symfony/class-loader) <  3.0

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Egulias/EmailValidator2/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee EmailValidator/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\Psr4ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\Psr4ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\Psr4ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/Psr4ClassLoader.php';
    }

    $fedoraPsr4ClassLoader = new \Symfony\Component\ClassLoader\Psr4ClassLoader();
    $fedoraPsr4ClassLoader->register();
}

$fedoraPsr4ClassLoader->addPrefix('Egulias\\EmailValidator\\', __DIR__);

// Required dependency
require_once '%{phpdir}/Doctrine/Common/Lexer/autoload.php';

return $fedoraPsr4ClassLoader;
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/Egulias/EmailValidator2
cp -rp EmailValidator/* %{buildroot}%{phpdir}/Egulias/EmailValidator2/

find %{buildroot}%{phpdir} | sort


%check
%if %{with_tests}
: Skip tests requiring network access
rm -f Tests/EmailValidator/Validation/DNSCheckValidationTest.php

: Run tests
%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/Egulias/EmailValidator2/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc documentation
%doc README.md
%dir %{phpdir}/Egulias
     %{phpdir}/Egulias/EmailValidator2


%changelog
* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.1-1
- Initial package
