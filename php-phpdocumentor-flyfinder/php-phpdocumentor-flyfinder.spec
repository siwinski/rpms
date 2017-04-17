#
# Fedora spec file for php-phpdocumentor-flyfinder
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      FlyFinder
%global github_version   1.0.0
%global github_commit    47e21713bc6d0619ae6bb511ae981af7be1e8ac7
%global github_release   .alpha1

%global composer_vendor  phpdocumentor
%global composer_project flyfinder

# "php": ">=5.5"
%global php_min_ver 5.5
# "league/flysystem": "~1.0.8"
%global league_flysystem_min_ver 1.0.8
%global league_flysystem_max_ver 1.1.0
# "league/flysystem-memory": "^1.0"
%global league_flysystem_memory_min_ver 1.0
%global league_flysystem_memory_max_ver 2.0
# "mockery/mockery":  "~0.9@dev"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       0.1%{?github_release}%{?dist}
Summary:       Flysystem plugin to add file finding capabilities

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
BuildRequires: php-composer(league/flysystem) >= %{league_flysystem_min_ver}
BuildRequires: php-composer(league/flysystem) <  %{league_flysystem_max_ver}
BuildRequires: php-composer(league/flysystem-memory) >= %{league_flysystem_memory_min_ver}
BuildRequires: php-composer(league/flysystem-memory) <  %{league_flysystem_memory_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php-pcre
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(league/flysystem) >= %{league_flysystem_min_ver}
Requires:      php-composer(league/flysystem) <  %{league_flysystem_max_ver}
# phpcompatinfo (computed from version 1.0.0)
Requires:      php-pcre
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Flyfinder/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('Flyfinder\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/League/Flysystem/autoload.php',
]);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Flyfinder


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/Flyfinder/autoload.php';

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/League/Flysystem/Memory/autoload.php',
    '%{phpdir}/Mockery/autoload.php',
]);
BOOTSTRAP

: Update Mockery path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php56 php70 php71 php72; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose --bootstrap bootstrap.php \
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
%{phpdir}/Flyfinder


%changelog
* Sun Apr 16 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-0.1.alpha1
- Initial package
