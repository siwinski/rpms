#
# Fedora spec file for php-dflydev-dot-access-data
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     dflydev
%global github_name      dflydev-dot-access-data
%global github_version   1.1.0
%global github_commit    3fbd874921ab2c041e899d044585a2ab9795df8a

%global composer_vendor  dflydev
%global composer_project dot-access-data

# "php": ">=5.3.2"
%global php_min_ver 5.3.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Given a deep data structure, access data by dot notation

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
## phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Dflydev/DotAccessData/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Dflydev/DotAccessData/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Dflydev\\DotAccessData\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Dflydev
cp -rp src/Dflydev/DotAccessData %{buildroot}%{phpdir}/Dflydev/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose \
            --bootstrap %{buildroot}%{phpdir}/Dflydev/DotAccessData/autoload.php \
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
%dir %{phpdir}/Dflydev
     %{phpdir}/Dflydev/DotAccessData


%changelog
* Tue Apr 25 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
