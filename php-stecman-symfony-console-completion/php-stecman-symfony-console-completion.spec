#
# Fedora spec file for php-stecman-symfony-console-completion
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     stecman
%global github_name      symfony-console-completion
%global github_version   0.7.0
%global github_commit    5461d43e53092b3d3b9dbd9d999f2054730f4bbb

%global composer_vendor  stecman
%global composer_project symfony-console-completion

# "php": ">=5.3.2"
%global php_min_ver 5.3.2
# "symfony/console": "~2.3 || ~3.0"
%global symfony_min_ver 2.3
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Automatic BASH completion for Symfony Console Component apps

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 0.7.0)
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 0.7.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package provides automatic (tab) completion in BASH and ZSH for Symfony
Console Component based applications. With zero configuration, this package
allows completion of available command names and the options they provide.
User code can define custom completion behavior for argument and option values.

Autoloader:
%{phpdir}/Stecman/Component/Symfony/Console/BashCompletion/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Fix license filename
mv LICENCE LICENSE


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4(
    'Stecman\\Component\\Symfony\\Console\\BashCompletion\\',
    __DIR__
);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ),
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Stecman/Component/Symfony/Console
cp -rp src %{buildroot}%{phpdir}/Stecman/Component/Symfony/Console/BashCompletion


%check
%if %{with_tests}
%if 0%{?el6}
# PHPUnit >= 4.4.0 required for these tests
: Skip tests requiring assertArraySubset
: PHPUnit >= 4.4.0 required
sed \
    -e 's/function testCompleteDoubleDash/function SKIP_testCompleteDoubleDash/' \
    -e 's/function testCompleteOptionFull/function SKIP_testCompleteOptionFull/' \
    -i tests/Stecman/Component/Symfony/Console/BashCompletion/CompletionHandlerTest.php
%endif

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose --bootstrap %{buildroot}%{phpdir}/Stecman/Component/Symfony/Console/BashCompletion/autoload.php || RETURN_CODE=1
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
%dir %{phpdir}/Stecman
%dir %{phpdir}/Stecman/Component
%dir %{phpdir}/Stecman/Component/Symfony
%dir %{phpdir}/Stecman/Component/Symfony/Console
     %{phpdir}/Stecman/Component/Symfony/Console/BashCompletion


%changelog
* Tue Mar 21 2017 Shawn Iwinski <shawn@iwin.ski> - 0.7.0-1
- Initial package
