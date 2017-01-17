Name:       php-evenement
Version:    2.0.0
Release:    1%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    Événement is a very simple event dispatching library for PHP
URL:        https://github.com/igorw/evenement
Source0:    %{url}/archive/v%{version}.tar.gz
# https://github.com/igorw/evenement/pull/33
Patch0:     0000-Fix-a-test-to-catch-TypeError-instead-of-Exception.patch

BuildRequires: phpunit
BuildRequires: php-composer(symfony/class-loader)

Requires:      php(language) >= 5.4.0
# This is for the autoloader
Requires:      php-composer(symfony/class-loader)

Provides:      php-composer(evenement/evenement) = %{version}


%description
Événement is a very simple event dispatching library for PHP.

It has the same design goals as Silex and Pimple, to empower the user
while staying concise and simple.

It is very strongly inspired by the EventEmitter API found in node.js.

Autoloader:    %{_datadir}/php/Evenement/Evenement/autoload.php


%prep
%setup -q -n evenement-%{version}

%patch0 -p1

# This was taken from the pho-doctrine-inflector spec file and modified for evenement.
: Create autoloader
cat <<'AUTOLOAD' | tee src/Evenement/autoload.php
<?php
/**
 * Autoloader for %{name} and it's dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '%{_datadir}/php/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('Evenement', dirname(__DIR__));

return $fedoraClassLoader;
AUTOLOAD


%install
install -d -p -m 0755 %{buildroot}/%{_datadir}/php
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Evenement

cp -a -r src/Evenement %{buildroot}/%{_datadir}/php/Evenement/


%check
: Create tests autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php

$fedoraClassLoader =
    require_once '%{buildroot}%{_datadir}/php/Evenement/Evenement/autoload.php';

$fedoraClassLoader->addPrefix('Evenement\\Tests', __DIR__ . '/tests');
AUTOLOAD

phpunit --bootstrap autoload.php


%files
%license LICENSE
%doc CHANGELOG.md composer.json README.md
%{_datadir}/php/Evenement


%changelog
* Sat Jan 14 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.0.0-1
- Initial release.
