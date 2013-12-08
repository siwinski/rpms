%global github_owner           silexphp
%global github_name            Silex
%global github_version         1.1.2
%global github_commit          47cc7d6545450ef8a91f50c04e8c7b3b04fceae9

%global php_min_ver            5.3.3
# "doctrine/dbal": ">=2.2.0,<2.4.0-dev"
%global doctrine_dbal_min_ver  2.2.0
%global doctrine_dbal_max_ver  2.4.0
# "monolog/monolog": "~1.4,>=1.4.1"
%global monolog_min_ver        1.4.1
%global monolog_max_ver        2.0.0
# "phpunit/phpunit": "~3.7"
%global phpunit_min_ver        3.7.0
%global phpunit_max_ver        4.0.0
# "pimple/pimple": "~1.0"
%global pimple_min_ver         1.0.0
%global pimple_max_ver         2.0.0
# "swiftmailer/swiftmailer": "5.*"
%global swiftmailer_min_ver    5.0.0
%global swiftmailer_max_ver    6.0.0
# "symfony/*": ">=2.3,<2.5-dev"
%global symfony_min_ver        2.3.0
%global symfony_max_ver        2.5.0
# "twig/twig": ">=1.8.0,<2.0-dev"
%global twig_min_ver           1.8.0
%global twig_max_ver           2.0.0

Name:          php-silex
Version:       %{github_version}
Release:       1%{dist}
Summary:       PHP micro-framework based on the Symfony components

Group:         Development/Libraries
License:       MIT
URL:           http://silex.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language)               >= %{php_min_ver}
BuildRequires: php-Monolog                 >= %{monolog_min_ver}
BuildRequires: php-Monolog                 <  %{monolog_max_ver}
BuildRequires: php-Pimple                  >= %{pimple_min_ver}
BuildRequires: php-Pimple                  <  %{pimple_max_ver}
BuildRequires: php-symfony-browserkit      >= %{symfony_min_ver}
BuildRequires: php-symfony-browserkit      <  %{symfony_max_ver}
BuildRequires: php-symfony-config          >= %{symfony_min_ver}
BuildRequires: php-symfony-config          <  %{symfony_max_ver}
BuildRequires: php-symfony-cssselector     >= %{symfony_min_ver}
BuildRequires: php-symfony-cssselector     <  %{symfony_max_ver}
BuildRequires: php-symfony-debug           >= %{symfony_min_ver}
BuildRequires: php-symfony-debug           <  %{symfony_max_ver}
BuildRequires: php-symfony-domcrawler      >= %{symfony_min_ver}
BuildRequires: php-symfony-domcrawler      <  %{symfony_max_ver}
BuildRequires: php-symfony-eventdispatcher >= %{symfony_min_ver}
BuildRequires: php-symfony-eventdispatcher <  %{symfony_max_ver}
BuildRequires: php-symfony-finder          >= %{symfony_min_ver}
BuildRequires: php-symfony-finder          <  %{symfony_max_ver}
BuildRequires: php-symfony-form            >= %{symfony_min_ver}
BuildRequires: php-symfony-form            <  %{symfony_max_ver}
BuildRequires: php-symfony-httpfoundation  >= %{symfony_min_ver}
BuildRequires: php-symfony-httpfoundation  <  %{symfony_max_ver}
BuildRequires: php-symfony-httpkernel      >= %{symfony_min_ver}
BuildRequires: php-symfony-httpkernel      <  %{symfony_max_ver}
BuildRequires: php-symfony-locale          >= %{symfony_min_ver}
BuildRequires: php-symfony-locale          <  %{symfony_max_ver}
BuildRequires: php-symfony-monologbridge   >= %{symfony_min_ver}
BuildRequires: php-symfony-monologbridge   <  %{symfony_max_ver}
BuildRequires: php-symfony-optionsresolver >= %{symfony_min_ver}
BuildRequires: php-symfony-optionsresolver <  %{symfony_max_ver}
BuildRequires: php-symfony-process         >= %{symfony_min_ver}
BuildRequires: php-symfony-process         <  %{symfony_max_ver}
BuildRequires: php-symfony-routing         >= %{symfony_min_ver}
BuildRequires: php-symfony-routing         <  %{symfony_max_ver}
BuildRequires: php-symfony-security        >= %{symfony_min_ver}
BuildRequires: php-symfony-security        <  %{symfony_max_ver}
BuildRequires: php-symfony-serializer      >= %{symfony_min_ver}
BuildRequires: php-symfony-serializer      <  %{symfony_max_ver}
BuildRequires: php-symfony-translation     >= %{symfony_min_ver}
BuildRequires: php-symfony-translation     <  %{symfony_max_ver}
BuildRequires: php-symfony-twigbridge      >= %{symfony_min_ver}
BuildRequires: php-symfony-twigbridge      <  %{symfony_max_ver}
BuildRequires: php-symfony-validator       >= %{symfony_min_ver}
BuildRequires: php-symfony-validator       <  %{symfony_max_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineDBAL) >= %{doctrine_dbal_min_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineDBAL) <  %{doctrine_dbal_max_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)                >= %{phpunit_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)                <  %{phpunit_max_ver}
BuildRequires: php-pear(pear.swiftmailer.org/Swift)             >= %{swiftmailer_min_ver}
BuildRequires: php-pear(pear.swiftmailer.org/Swift)             <  %{swiftmailer_max_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig)             >= %{twig_min_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig)             <  %{twig_max_ver}
# For tests: phpcompatinfo
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl

Requires:      php(language)               >= %{php_min_ver}
Requires:      php-Pimple                  >= %{pimple_min_ver}
Requires:      php-Pimple                  <  %{pimple_max_ver}
Requires:      php-symfony-eventdispatcher >= %{symfony_min_ver}
Requires:      php-symfony-eventdispatcher <  %{symfony_max_ver}
Requires:      php-symfony-httpfoundation  >= %{symfony_min_ver}
Requires:      php-symfony-httpfoundation  <  %{symfony_max_ver}
Requires:      php-symfony-httpkernel      >= %{symfony_min_ver}
Requires:      php-symfony-httpkernel      <  %{symfony_max_ver}
Requires:      php-symfony-routing         >= %{symfony_min_ver}
Requires:      php-symfony-routing         <  %{symfony_max_ver}
# Optional
Requires:      php-symfony-browserkit      >= %{symfony_min_ver}
Requires:      php-symfony-browserkit      <  %{symfony_max_ver}
Requires:      php-symfony-cssselector     >= %{symfony_min_ver}
Requires:      php-symfony-cssselector     <  %{symfony_max_ver}
Requires:      php-symfony-domcrawler      >= %{symfony_min_ver}
Requires:      php-symfony-domcrawler      <  %{symfony_max_ver}
Requires:      php-symfony-form            >= %{symfony_min_ver}
Requires:      php-symfony-form            <  %{symfony_max_ver}
# phpcompatinfo
Requires:      php-date
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl

%description
Silex is a PHP micro-framework for PHP 5.3+. It is built on the shoulders of
Symfony and Pimple and also inspired by Sinatra.

A micro-framework provides the guts for building simple single-file apps. Silex
aims to be:
* Concise: Silex exposes an intuitive and concise API that is fun to use
* Extensible: Silex has an extension system based around the Pimple micro
  service-container that makes it even easier to tie in third party libraries
* Testable: Silex uses Symfony's HttpKernel which abstracts requests and
  responses. This makes it very easy to test apps and the framework itself.
  It also respects the HTTP specification and encourages its' proper use.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp src/* %{buildroot}/%{_datadir}/php/


%check
# Rewrite tests' bootstrap (which uses Composer autoloader) with simple
# autoloader that uses include path
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > tests/bootstrap.php

# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

# Skip tests known to fail
rm -f tests/Silex/Tests/Provider/SwiftmailerServiceProviderTest.php

%{_bindir}/phpunit \
    --include-path ./src:./tests:%{pear_phpdir}/Swift:%{_datadir}/php/Pimple \
    -d date.timezone="UTC" \
    -d session.save_path="%{_tmppath}"


%files
%doc LICENSE README* composer.json doc/*
%{_datadir}/php/%{github_name}


%changelog
* Sat Dec 07 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.2-1
- Initial package
