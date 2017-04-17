#
# Fedora spec file for php-league-flysystem-memory
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      flysystem-memory
%global github_version   1.0.1
%global github_commit    1cabecd08a8caec92a96a953c0d93b5ce83b07a2

%global composer_vendor  league
%global composer_project flysystem-memory

# "league/flysystem": "~1.0"
%global league_flysystem_min_ver 1.0
%global league_flysystem_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       An in-memory adapter for Flysystem

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-league-flysystem-memory-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(league/flysystem) <  %{league_flysystem_max_ver}
BuildRequires: php-composer(league/flysystem) >= %{league_flysystem_min_ver}
## phpcompatinfo (computed from version 1.0.1)
BuildRequires: php(language) >= 5.4.0
BuildRequires: php-date
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php-composer(league/flysystem) <  %{league_flysystem_max_ver}
Requires:      php-composer(league/flysystem) >= %{league_flysystem_min_ver}
# phpcompatinfo (computed from version 1.0.1)
Requires:      php(language) >= 5.4.0
Requires:      php-date
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

This adapter keeps the filesystem in memory. It's useful when you need a
filesystem, but do not need it persisted.

Autoloader: %{phpdir}/League/Flysystem/Memory/autoload.php


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

\Fedora\Autoloader\Autoload::addPsr4('League\\Flysystem\\Memory\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/League/Flysystem/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/League/Flysystem
cp -rp src %{buildroot}%{phpdir}/League/Flysystem/Memory


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose \
            --bootstrap %{buildroot}%{phpdir}/League/Flysystem/Memory/autoload.php \
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
%{phpdir}/League/Flysystem/Memory


%changelog
* Sun Apr 16 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.1-1
- Initial package
