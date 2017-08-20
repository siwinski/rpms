#
# Fedora spec file for php-behat-gherkin
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Behat
%global github_name      Gherkin
%global github_version   4.4.5
%global github_commit    5c14cff4f955b17d20d088dec1bde61c0539ec74

%global composer_vendor  behat
%global composer_project gherkin

# "php": ">=5.3.1"
%global php_min_ver 5.3.1
# "symfony/yaml": "~2.3|~3"
#     NOTE: Min version not 2.1 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%global phpdir   %{_datadir}/php

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Gherkin DSL parser for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://behat.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
## phpcompatinfo (computed from version 4.4.5)
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/yaml) >= %{symfony_min_ver}
Requires:      php-composer(symfony/yaml) <  %{symfony_max_ver}
# phpcompatinfo (computed from version 4.4.5)
Requires:      php-date
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Behat/Gherkin/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create library autoloader
cat <<'AUTOLOAD' | tee src/Behat/Gherkin/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Behat\\Gherkin\\', __DIR__);

\Fedora\Autoloader\Dependencies::optional(array(
    array(
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony/Component/Yaml/autoload.php',
    ),
));
AUTOLOAD


%install
mkdir -p  %{buildroot}%{phpdir}/Behat
cp -pr src/Behat/Gherkin %{buildroot}%{phpdir}/Behat/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'AUTOLOAD' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Behat/Gherkin/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Tests\\Behat\\', __DIR__.'/tests/Behat');
AUTOLOAD

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
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
%dir %{phpdir}/Behat
     %{phpdir}/Behat/Gherkin


%changelog
* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 4.4.5-1
- Update to 4.4.5
- Switch autoloader to fedora/autoloader
- Test with SCLs if available

* Mon Aug 15 2016 Shawn Iwinski <shawn@iwin.ski> - 4.4.1-1
- Initial package
