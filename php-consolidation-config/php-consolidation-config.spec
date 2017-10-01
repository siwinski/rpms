#
# Fedora spec file for php-consolidation-config
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      config
%global github_version   1.0.2
%global github_commit    bcff5f4057c6ece20794d58dfc9e56919e2b33b7

%global composer_vendor  consolidation
%global composer_project config

# "php": ">=5.4.0"
%global php_min_ver 5.4.0
# "dflydev/dot-access-data": "^1.1.0"
%global dflydev_dot_access_data_min_ver 1.1.0
%global dflydev_dot_access_data_max_ver 2.0
# "grasmash/yaml-expander": "^1.1"
%global grasmash_yaml_expander_min_ver 1.1
%global grasmash_yaml_expander_max_ver 2.0
# "symfony/console": "^2.5|^3"
#     NOTE: Min version not 2.5 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Provide configuration services for a command-line tool

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
BuildRequires: php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
BuildRequires: php-composer(grasmash/yaml-expander) <  %{grasmash_yaml_expander_max_ver}
BuildRequires: php-composer(grasmash/yaml-expander) >= %{grasmash_yaml_expander_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
## phpcompatinfo for version 1.0.2
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(dflydev/dot-access-data) <  %{dflydev_dot_access_data_max_ver}
Requires:      php-composer(dflydev/dot-access-data) >= %{dflydev_dot_access_data_min_ver}
Requires:      php-composer(grasmash/yaml-expander) <  %{grasmash_yaml_expander_max_ver}
Requires:      php-composer(grasmash/yaml-expander) >= %{grasmash_yaml_expander_min_ver}
# phpcompatinfo for version 1.0.2
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Manage configuration for a command-line tool.

This component is designed to provide the components needed to manage
configuration options from different sources, including:
* Commandline options
* Configuration files
* Alias files (special configuration files that identify a specific target site)
* Default values (provided by command)

Symfony Console is used to provide the framework for the command-line tool, and
the Symfony Configuration component is used to load and merge configuration
files. This project provides the glue that binds the components together in an
easy-to-use package.

Autoloader: %{phpdir}/Consolidation/Config/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\Config\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Dflydev/DotAccessData/autoload.php',
    '%{phpdir}/Grasmash/YamlExpander/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Consolidation
cp -rp src %{buildroot}%{phpdir}/Consolidation/Config


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Consolidation/Config/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Consolidation\\TestUtils\\', __DIR__.'/tests/src');

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/EventDispatcher/autoload.php',
        '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    ],
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php55} php56 php70 php71 php72; do
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
%doc composer.json
%dir %{phpdir}/Consolidation
     %{phpdir}/Consolidation/Config


%changelog
* Sun Oct 01 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.2-1
- Update to 1.0.2

* Mon Aug 21 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.1-1
- Initial package
