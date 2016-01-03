#
# Fedora spec file for php-container-interop
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     container-interop
%global github_name      container-interop
%global github_version   1.1.0
%global github_commit    fc08354828f8fd3245f77a66b9e23a6bca48297e

%global composer_vendor  container-interop
%global composer_project container-interop

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-%{composer_project}
Version:   %{github_version}
Release:   1%{?github_release}%{?dist}
Summary:   Promoting the interoperability of container objects (DIC, SL, etc.)

Group:     Development/Libraries
License:   MIT
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch

# composer.json
#     <none>
# phpcompatinfo (computed from version 1.1.0)
Requires:  php(language) >= 5.3.0
# Autoloader
Requires:  php-composer(symfony/class-loader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:  php-%{composer_vendor}-%{composer_project}           = %{version}-%{release}
# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
container-interop tries to identify and standardize features in container
objects (service locators, dependency injection containers, etc.) to achieve
interopererability.

Through discussions and trials, we try to create a standard, made of common
interfaces but also recommendations.

If PHP projects that provide container implementations begin to adopt these
common standards, then PHP applications and projects that use containers can
depend on the common interfaces instead of specific implementations. This
facilitates a high-level of interoperability and flexibility that allows users
to consume any container implementation that can be adapted to these interfaces.

The work done in this project is not officially endorsed by the PHP-FIG [1],
but it is being worked on by members of PHP-FIG and other good developers. We
adhere to the spirit and ideals of PHP-FIG, and hope this project will pave the
way for one or more future PSRs.

Autoloader: %{phpdir}/Interop/Container/autoload.php

[1] http://www.php-fig.org/


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/Interop/Container/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('Interop\\Container\\', dirname(dirname(__DIR__)));

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
: No tests provided upstream


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%doc docs
%dir %{phpdir}/Interop
     %{phpdir}/Interop/Container


%changelog
* Sun Jan 03 2016 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
