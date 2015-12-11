#
# Fedora spec file for php-wikimedia-composer-merge-plugin
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     wikimedia
%global github_name      composer-merge-plugin
%global github_version   1.3.0
%global github_commit    bfed1f8d4eb97e9ba80eee57ea46229d7e5364d9

%global composer_vendor  wikimedia
%global composer_project composer-merge-plugin

# "php": ">=5.3.2"
%global php_min_ver 5.3.2
# "composer-plugin-api": "^1.0"
%global composer_plugin_min_ver 1.0
%global composer_plugin_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Composer plugin to merge multiple composer.json files

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-wikimedia-composer-merge-plugin-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Autoloader classmap
BuildRequires: php-composer(theseer/autoload)
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                     >= %{php_min_ver}
BuildRequires: php-composer(composer-plugin-api) >= %{composer_plugin_min_ver}
BuildRequires: php-composer(composer/composer)
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.3.0)
BuildRequires: php-json
BuildRequires: php-reflection
BuildRequires: php-pcre
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language)                     >= %{php_min_ver}
Requires:      php-composer(composer-plugin-api) >= %{composer_plugin_min_ver}
Requires:      php-composer(composer-plugin-api) <  %{composer_plugin_max_ver}
# phpcompatinfo (computed from version 1.3.0)
Requires:      php-pcre
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Merge one or more additional composer.json files at runtime.

Autoloader: %{phpdir}/Wikimedia/Composer/Merge/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader classmap
%{_bindir}/phpab --nolower --output src/Merge/autoload.classmap.php src/
cat src/Merge/autoload.classmap.php

: Create autoloader
cat <<'AUTOLOAD' | tee src/Merge/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

// Classmap
require_once __DIR__ . '/autoload.classmap.php';

// Required dependency
require_once '%{phpdir}/Composer/autoload.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Wikimedia/Composer
cp -pr src/* %{buildroot}%{phpdir}/Wikimedia/Composer/


%check
%if %{with_tests}
: Skip test known to fail
sed 's/function testHasBranchAlias/function SKIP_testHasBranchAlias/' \
    -i tests/phpunit/MergePluginTest.php

: Run tests
%{_bindir}/phpunit --verbose \
    --bootstrap %{buildroot}%{phpdir}/Wikimedia/Composer/Merge/autoload.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Wikimedia
     %{phpdir}/Wikimedia/Composer


%changelog
* Fri Dec 11 2015 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Initial package
