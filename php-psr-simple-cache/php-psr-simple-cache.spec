#
# Fedora spec file for php-psr-simple-cache
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-fig
%global github_name      simple-cache
%global github_version   1.0.0
%global github_commit    753fa598e8f3b9966c886fe13f370baa45ef0e24

%global composer_vendor  psr
%global composer_project simple-cache

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common interfaces for simple caching (PSR-16)

Group:         Development/Libraries
License:       MIT
URL:           http://www.php-fig.org/psr/psr-16/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Minimal autoloader test
BuildRequires: php-cli >= %{php_min_ver}
# Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This repository holds all interfaces related to PSR-16.

Note that this is not a cache implementation of its own. It is merely an
interface that describes a cache implementation. See the specification [1]
for more details.

You can find implementations of the specification by looking for packages
providing the psr/simple-cache-implementation [2] virtual package.

Autoloader: %{phpdir}/Psr/SimpleCache/autoload.php

[1] https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-16-simple-cache.md
[2] https://packagist.org/providers/psr/simple-cache-implementation


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

\Fedora\Autoloader\Autoload::addPsr4('Psr\\SimpleCache\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Psr
cp -rp src %{buildroot}%{phpdir}/Psr/SimpleCache


%check
: Minimal autoloader test
%{_bindir}/php -r '
    require "%{buildroot}%{phpdir}/Psr/SimpleCache/autoload.php";
    exit(interface_exists("Psr\\SimpleCache\\CacheInterface") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%doc composer.json
%dir %{phpdir}/Psr
     %{phpdir}/Psr/SimpleCache


%changelog
* Tue Mar 21 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
