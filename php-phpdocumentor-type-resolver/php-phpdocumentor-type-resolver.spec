#
# Fedora spec file for php-phpdocumentor-type-resolver
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      TypeResolver
%global github_version   0.2.1
%global github_commit    e224fb2ea2fba6d3ad6fdaef91cd09a172155ccb

%global composer_vendor  phpdocumentor
%global composer_project type-resolver

# "php": ">=5.5"
%global php_min_ver 5.5
# "mockery/mockery": "^0.9.4"
%global mockery_min_ver 0.9.4
%global mockery_max_ver 1.0
# "phpdocumentor/reflection-common": "^1.0"
%global reflection_common_min_ver 1.0
%global reflection_common_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A PSR-5 based resolver of Class names, Types and Structural Element Names

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
BuildRequires: php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver}
BuildRequires: php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.2.1)
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver}
Requires:      php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver}
# phpcompatinfo (computed from version 0.2.1)
Requires:      php-spl
Requires:      php-tokenizer
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The specification on types in DocBlocks (PSR-5) describes various keywords
and special constructs but also how to statically resolve the partial name
of a Class into a Fully Qualified Class Name (FQCN).

PSR-5 also introduces an additional way to describe deeper elements than
Classes, Interfaces and Traits called the Fully Qualified Structural Element
Name (FQSEN). Using this it is possible to refer to methods, properties and
class constants but also functions and global constants.

This package provides two Resolvers that are capable of:
1. Returning a series of Value Object for given expression while resolving any
  partial class names, and
2. Returning an FQSEN object after resolving any partial Structural Element
  Names into Fully Qualified Structural Element names.

Autoloader: %{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Update examples autoload require
sed "s#.*require.*vendor.*/autoload.php.*#require_once '%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php';#" \
    -i examples/*


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-type-resolver.php src
cat <<'AUTOLOAD' | tee -a src/autoload-type-resolver.php

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/phpDocumentor/Reflection/autoload-common.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor/Reflection
cp -rp src/* %{buildroot}%{phpdir}/phpDocumentor/Reflection/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\Reflection\\', __DIR__.'/tests/unit');

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Mockery/autoload.php',
]);
BOOTSTRAP

: Adjust listener path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php56 php70 php71; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose --bootstrap bootstrap.php || RETURN_CODE=1
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
%doc examples
%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php
%{phpdir}/phpDocumentor/Reflection/FqsenResolver.php
%{phpdir}/phpDocumentor/Reflection/Type.php
%{phpdir}/phpDocumentor/Reflection/TypeResolver.php
%{phpdir}/phpDocumentor/Reflection/Types


%changelog
* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 0.2.1-1
- Initial package
