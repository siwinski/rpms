#
# Fedora spec file for php-grasmash-yaml-expander
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     grasmash
%global github_name      yaml-expander
%global github_version   1.1.1
%global github_commit    720c54b2c99b80d5d696714b6826183d34edce93

%global composer_vendor  grasmash
%global composer_project yaml-expander

# "php": ">=5.4"
%global php_min_ver 5.4
# "dflydev/dot-access-data": "^1.1.0"
%global dot_access_data_min_ver 1.1.0
%global dot_access_data_max_ver 2.0
# "symfony/yaml": "^2.8.11|^3"
%global symfony_min_ver 2.8.11
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Expands internal property references in a yaml file

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
BuildRequires: php-composer(dflydev/dot-access-data) <  %{dot_access_data_max_ver}
BuildRequires: php-composer(dflydev/dot-access-data) >= %{dot_access_data_min_ver}
BuildRequires: php-composer(symfony/yaml) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/yaml) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(dflydev/dot-access-data) <  %{dot_access_data_max_ver}
Requires:      php-composer(dflydev/dot-access-data) >= %{dot_access_data_min_ver}
Requires:      php-composer(symfony/yaml) <  %{symfony_max_ver}
Requires:      php-composer(symfony/yaml) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Grasmash/YamlExpander/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Grasmash\\YamlExpander\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Dflydev/DotAccessData/autoload.php',
    [
        '%{phpdir}/Symfony3/Component/Yaml/autoload.php',
        '%{phpdir}/Symfony/Component/Yaml/autoload.php',
    ],
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Grasmash
cp -rp src %{buildroot}%{phpdir}/Grasmash/YamlExpander


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Grasmash/YamlExpander/autoload.php';
//\Fedora\Autoloader\Autoload::addPsr4('xxxxx\\Test\\', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php55} php56 php70 php71 php72; do
    if which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Grasmash/YamlExpander/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%doc RELEASE.md
%doc composer.json
%dir %{phpdir}/Grasmash
     %{phpdir}/Grasmash/YamlExpander


%changelog
* Sun Aug 20 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Initial package
