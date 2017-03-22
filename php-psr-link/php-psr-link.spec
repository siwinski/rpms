#
# Fedora spec file for php-psr-link
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-fig
%global github_name      link
%global github_version   1.0.0
%global github_commit    eea8e8662d5cd3ae4517c9b864493f59fca95562

%global composer_vendor  psr
%global composer_project link

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common interfaces for HTTP links (PSR-13)

Group:         Development/Libraries
License:       MIT
URL:           http://www.php-fig.org/psr/psr-13/
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
This package holds all interfaces/classes/traits related to PSR-13 [1].

Note that this is not an HTTP link implementation of its own. It is merely an
interface that describes an HTTP link. See the specification for more details.

Autoloader: %{phpdir}/Psr/Link/autoload.php

[1] https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-13-links.md


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

\Fedora\Autoloader\Autoload::addPsr4('Psr\\Link\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Psr
cp -rp src %{buildroot}%{phpdir}/Psr/Link


%check
: Minimal autoloader test
%{_bindir}/php -r '
    require "%{buildroot}%{phpdir}/Psr/Link/autoload.php";
    exit(interface_exists("Psr\\Link\\LinkInterface") ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%doc composer.json
%dir %{phpdir}/Psr
     %{phpdir}/Psr/Link


%changelog
* Tue Mar 21 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
