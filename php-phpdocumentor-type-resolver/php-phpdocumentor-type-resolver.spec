#
# Fedora spec file for php-phpdocumentor-type-resolver
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      TypeResolver
%global github_version   0.1.5
%global github_commit    83e31258fb03b9a27884a83b81501cb4cb297a81

%global composer_vendor  phpdocumentor
%global composer_project type-resolver

# "php": ">=5.5"
%global php_min_ver 5.5
# "phpdocumentor/reflection-common": "^1.0@dev"
#     NOTE: Min version not 1.0 because no official 1.0 release and
#           tests pass with packaged version 0.2
%global reflection_common_min_ver 0.2
%global reflection_common_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       TypeResolver and FqsenResolver

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader classmap
BuildRequires: php-composer(theseer/autoload)
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                                 >= %{php_min_ver}
BuildRequires: php-composer(mockery/mockery)
BuildRequires: php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 0.1.5)
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
%endif

# composer.json
Requires:      php(language)                                 >= %{php_min_ver}
Requires:      php-composer(phpdocumentor/reflection-common) >= %{reflection_common_min_ver}
Requires:      php-composer(phpdocumentor/reflection-common) <  %{reflection_common_max_ver}
# phpcompatinfo (computed from version 0.1.5)
Requires:      php-spl
Requires:      php-tokenizer

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The specification on types in DocBlocks (PSR-5) describes various keywords and
special constructs but also how to statically resolve the partial name of a
Class into a Fully Qualified Class Name (FQCN).

PSR-5 also introduces an additional way to describe deeper elements than
Classes, Interfaces and Traits called the Fully Qualified Structural Element
Name (FQSEN). Using this it is possible to refer to methods, properties and
class constants but also functions and global constants.

This package provides two Resolvers that are capable of:
* Returning a series of Value Object for given expression while resolving any
  partial class names, and
* Returning an FQSEN object after resolving any partial Structural Element Names
  into Fully Qualified Structural Element names.

Autoloader: %{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader classmap
# NOTE: Cannot simply use Symfony autoloader because of src/Types/*_.php classes
%{_bindir}/phpab --nolower --output src/autoload-type-resolver.classmap.php src/
cat src/autoload-type-resolver.classmap.php

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload-type-resolver.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

// Classmap
require_once __DIR__ . '/autoload-type-resolver.classmap.php';

// Required dependency
require_once '%{phpdir}/phpDocumentor/Reflection/autoload.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor/Reflection
cp -rp src/* %{buildroot}%{phpdir}/phpDocumentor/Reflection/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/phpDocumentor/Reflection/autoload-type-resolver.php';
require_once '%{phpdir}/Mockery/autoload.php';
BOOTSTRAP

: Modify Mockery path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' \
    phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/phpDocumentor/Reflection/


%changelog
* Wed Dec 09 2015 Shawn Iwinski <shawn@iwin.ski> - 0.1.5-1
- Initial package
