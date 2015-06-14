#
# RPM spec file for php-guzzlehttp-promises
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     guzzle
%global github_name      promises
%global github_version   1.0.0
%global github_commit    01abc3232138f330d8a1eaa808fcbdf9b4292f47

%global composer_vendor  guzzlehttp
%global composer_project promises

# "php": ">=5.5.0"
%global php_min_ver 5.5.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Guzzle promises library

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php-json
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.0)
Requires:      php-json
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Promises/A+ [1] implementation that handles promise chaining and resolution
interactively, allowing for "infinite" promise chaining while keeping the
stack size constant.

[1] https://promisesaplus.com/


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
(cat <<'AUTOLOAD'
<?php
/**
 * Autoloader created by %{name}-%{version}-%{release}
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once 'Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('GuzzleHttp\\Promise', dirname(dirname(__DIR__)));

require_once __DIR__ . '/functions.php';

return $fedoraClassLoader;
AUTOLOAD
) | tee src/autoload.php


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp/Promise
cp -rp src/* %{buildroot}%{phpdir}/GuzzleHttp/Promise/


%check
%if %{with_tests}
sed "s#require.*autoload.*#require '%{buildroot}%{phpdir}/GuzzleHttp/Promise/autoload.php';#" \
    -i tests/bootstrap.php

%{_bindir}/phpunit -v
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/GuzzleHttp
     %{phpdir}/GuzzleHttp/Promise


%changelog
* Sun Jun 14 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.0-1
- Initial package
