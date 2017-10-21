#
# Fedora spec file for php-goaop-parser-reflection
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     goaop
%global github_name      parser-reflection
%global github_version   1.4.0
%global github_commit    adfc38fee63014880932ebcc4810871b8e33edc9

%global composer_vendor  goaop
%global composer_project parser-reflection

# "php": ">=5.6.0"
%global php_min_ver 5.6.0
# "nikic/php-parser": "^1.2|^2.0|^3.0"
%global nikic_php_parser_min_ver 1.2
%global nikic_php_parser_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Provides reflection information, based on raw source

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Add LICENSE file
# https://github.com/goaop/parser-reflection/pull/85
Patch0:        %{name}-upstream-pull-request-85.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: composer
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(nikic/php-parser) <  %{nikic_php_parser_max_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{nikic_php_parser_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo for version 1.4.0
BuildRequires: php-date
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(nikic/php-parser) <  %{nikic_php_parser_max_ver}
Requires:      php-composer(nikic/php-parser) >= %{nikic_php_parser_min_ver}
# phpcompatinfo for version 1.4.0
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Go/ParserReflection/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Add LICENSE file
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Go\\ParserReflection\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/PhpParser3/autoload.php',
        '%{phpdir}/PhpParser2/autoload.php',
        '%{phpdir}/PhpParser/autoload.php',
    ],
    __DIR__.'/bootstrap.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Go
cp -rp src %{buildroot}%{phpdir}/Go/ParserReflection


%check
%if %{with_tests}
: Create Composer autoloader for tests/Locator/ComposerLocatorTest.php
composer dumpautoload

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Go/ParserReflection/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Go\\ParserReflection\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required([
    // Load Composer autoloader for tests/Locator/ComposerLocatorTest.php
    __DIR__.'/vendor/autoload.php',
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php70 php71 php72; do
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
%doc docs
%doc composer.json
%dir %{phpdir}/Go
     %{phpdir}/Go/ParserReflection


%changelog
* Sat Oct 21 2017 Shawn Iwinski <shawn@iwin.ski> - 1.4.0-1
- Initial package
