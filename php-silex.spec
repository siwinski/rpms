#
# RPM spec file for php-silex
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner          silexphp
%global github_name           Silex
%global github_version        1.2.2
%global github_commit         8c5e86eb97f3eee633729b22e950082fb5591328

%global composer_vendor       silex
%global composer_project      silex

%global php_min_ver           5.3.3
# "doctrine/dbal": "~2.2"
%global doctrine_dbal_min_ver 2.2.0
%global doctrine_dbal_max_ver 3.0.0
# "monolog/monolog": "~1.4,>=1.4.1"
%global monolog_min_ver       1.4.1
%global monolog_max_ver       2.0.0
# "phpunit/phpunit": "~3.7"
#     NOTE: Max version ignored on purpose
%global phpunit_min_ver       3.7.0
# "pimple/pimple": "~1.0"
%global pimple_min_ver        1.0.0
%global pimple_max_ver        2.0.0
# "swiftmailer/swiftmailer": "5.*"
%global swiftmailer_min_ver   5.0.0
%global swiftmailer_max_ver   6.0.0
# "symfony/*": ">=2.3,<2.6-dev"
%global symfony_min_ver       2.3.0
%global symfony_max_ver       2.6.0
# "twig/twig": ">=1.8.0,<2.0-dev"
%global twig_min_ver          1.8.0
%global twig_max_ver          2.0.0

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       1%{dist}
Summary:       PHP micro-framework based on the Symfony components

Group:         Development/Libraries
License:       MIT
URL:           http://silex.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# composer.json
BuildRequires: php(language)                          >= %{php_min_ver}
BuildRequires: php-composer(monolog/monolog)          >= %{monolog_min_ver}
BuildRequires: php-composer(monolog/monolog)          <  %{monolog_max_ver}
BuildRequires: php-composer(symfony/browser-kit)      >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/browser-kit)      <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/config)           >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/config)           <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/css-selector)     >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/css-selector)     <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/debug)            >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/debug)            <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/dom-crawler)      >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/dom-crawler)      <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder)           >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder)           <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/form)             >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/form)             <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-foundation)  >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-foundation)  <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/http-kernel)      >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/http-kernel)      <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/locale)           >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/locale)           <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/monolog-bridge)   >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/monolog-bridge)   <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/options-resolver) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/options-resolver) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/process)          >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process)          <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/routing)          >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/routing)          <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/security)         >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/security)         <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/serializer)       >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/serializer)       <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/translation)      >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/translation)      <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/twig-bridge)      >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/twig-bridge)      <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/validator)        >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/validator)        <  %{symfony_max_ver}
BuildRequires: php-composer(doctrine/dbal)            >= %{doctrine_dbal_min_ver}
BuildRequires: php-composer(doctrine/dbal)            <  %{doctrine_dbal_max_ver}
BuildRequires: php-phpunit-PHPUnit                    >= %{phpunit_min_ver}
BuildRequires: php-Pimple                             >= %{pimple_min_ver}
BuildRequires: php-Pimple                             <  %{pimple_max_ver}
BuildRequires: php-swift-Swift                        >= %{swiftmailer_min_ver}
BuildRequires: php-swift-Swift                        <  %{swiftmailer_max_ver}
BuildRequires: php-twig-Twig                          >= %{twig_min_ver}
BuildRequires: php-twig-Twig                          <  %{twig_max_ver}
# phpcompatinfo (computed from version 1.2.2)
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl
BuildRequires: php-tokenizer
%endif

# composer.json
Requires:      php(language)                          >= %{php_min_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/http-foundation)  >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-foundation)  <  %{symfony_max_ver}
Requires:      php-composer(symfony/http-kernel)      >= %{symfony_min_ver}
Requires:      php-composer(symfony/http-kernel)      <  %{symfony_max_ver}
Requires:      php-composer(symfony/routing)          >= %{symfony_min_ver}
Requires:      php-composer(symfony/routing)          <  %{symfony_max_ver}
Requires:      php-Pimple                             >= %{pimple_min_ver}
Requires:      php-Pimple                             <  %{pimple_max_ver}
# composer.json: Optional
Requires:      php-composer(symfony/browser-kit)      >= %{symfony_min_ver}
Requires:      php-composer(symfony/browser-kit)      <  %{symfony_max_ver}
Requires:      php-composer(symfony/css-selector)     >= %{symfony_min_ver}
Requires:      php-composer(symfony/css-selector)     <  %{symfony_max_ver}
Requires:      php-composer(symfony/dom-crawler)      >= %{symfony_min_ver}
Requires:      php-composer(symfony/dom-crawler)      <  %{symfony_max_ver}
Requires:      php-composer(symfony/form)             >= %{symfony_min_ver}
Requires:      php-composer(symfony/form)             <  %{symfony_max_ver}
# phpcompatinfo (computed from version 1.2.2)
Requires:      php-date
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl
Requires:      php-tokenizer

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Silex is a PHP micro-framework. It is built on the shoulders of Symfony and
Pimple and also inspired by Sinatra.

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
%if %{with_tests}
# Create custom bootstrap
cat > bootstrap.php <<'BOOTSTRAP'
<?php

// Add non-standard Pimple and Swift paths to include path
set_include_path(
    get_include_path()
    . PATH_SEPARATOR . '%{_datadir}/php/Pimple'
    . PATH_SEPARATOR . '%{_datadir}/php/Swift'
);

spl_autoload_register(function ($class) {
    $src = str_replace(array('\\', '_'), '/',  $class) . '.php';
    @include_once $src;
});
BOOTSTRAP

# Create PHPUnit config w/ colors turned off
sed 's/colors\s*=\s*"true"/colors="false"/' phpunit.xml.dist > phpunit.xml

# Skip tests known to fail
rm -f tests/Silex/Tests/Provider/SwiftmailerServiceProviderTest.php

%{__phpunit} \
    --bootstrap ./bootstrap.php \
    --include-path %{buildroot}%{_datadir}/php:./tests \
    -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.rst composer.json doc
%{_datadir}/php/Silex


%changelog
* Sat Oct 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.2-1
- Initial package
