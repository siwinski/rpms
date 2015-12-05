#
# Fedora spec file for php-symfony3
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#                    Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      symfony
%global github_version   3.0.0
%global github_commit    eb2a4f5f7a09fc4ce7a74ae883a8cf8a279614f5

%global composer_vendor  symfony
%global composer_project symfony

# "php": ">=5.5.9"
%global php_min_ver 5.5.9
# "doctrine/annotations": "~1.0"
#     src/Symfony/Bundle/FrameworkBundle/composer.json
#     src/Symfony/Component/PropertyInfo/composer.json
#     src/Symfony/Component/Routing/composer.json
#     src/Symfony/Component/Serializer/composer.json
#     src/Symfony/Component/Validator/composer.json
%global doctrine_annotations_min_ver 1.0
%global doctrine_annotations_max_ver 2.0
# "doctrine/cache": "~1.0"
#     src/Symfony/Bundle/FrameworkBundle/composer.json
#     src/Symfony/Component/Serializer/composer.json
#     src/Symfony/Component/Validator/composer.json
%global doctrine_cache_min_ver 1.0
%global doctrine_cache_max_ver 2.0
# "doctrine/common": "~2.4"
%global doctrine_common_min_ver 2.4
%global doctrine_common_max_ver 3.0
# "doctrine/data-fixtures": "1.0.*"
%global doctrine_datafixtures_min_ver 1.0.0
%global doctrine_datafixtures_max_ver 1.1.0
# "doctrine/dbal": "~2.4"
%global doctrine_dbal_min_ver 2.4
%global doctrine_dbal_max_ver 3.0
# "doctrine/doctrine-bundle": "~1.4"
%global doctrine_bundle_min_ver 1.4
%global doctrine_bundle_max_ver 2.0
# "doctrine/orm": "~2.4,>=2.4.5"
%global doctrine_orm_min_ver 2.4.5
%global doctrine_orm_max_ver 3.0
# "egulias/email-validator": "~1.2"
%global email_validator_min_ver 1.2
%global email_validator_max_ver 2.0
# "monolog/monolog": "~1.11"
%global monolog_min_ver 1.11
%global monolog_max_ver 2.0
# "ocramius/proxy-manager": "~0.4|~1.0"
%global proxy_manager_min_ver 1.0
%global proxy_manager_max_ver 2.0
# "phpdocumentor/reflection": "^1.0.7"
%global phpdocumentor_reflection_min_ver 1.0.7
%global phpdocumentor_reflection_max_ver 2.0
# "psr/log": "~1.0"
%global psrlog_min_ver 1.0
%global psrlog_max_ver 2.0
# "symfony/polyfill-intl-icu": "~1.0"
# "symfony/polyfill-mbstring": "~1.0"
# "symfony/polyfill-php54": "~1.0"
# "symfony/polyfill-php55": "~1.0"
# "symfony/polyfill-php56": "~1.0"
# "symfony/polyfill-php70": "~1.0"
# "symfony/polyfill-util": "~1.0"
%global symfony_polyfill_min_ver 1.0
%global symfony_polyfill_max_ver 2.0
# "symfony/security-acl": "~2.8|~3.0"
%global symfony_security_acl_min_ver 2.8
%global symfony_security_acl_max_ver 4.0
# "twig/twig": "~1.23|~2.0"
%global twig_min_ver 1.23
%global twig_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests   0%{!?_without_tests:1}

%global php_version_id %(%{_bindir}/php -r "echo PHP_VERSION_ID;")

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global symfony3_dir %{phpdir}/Symfony3

Name:          php-%{composer_project}3
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Symfony PHP framework (version 3)

Group:         Development/Libraries
License:       MIT
URL:           http://symfony.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-generate-autoloaders.php

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
### Force version to 4.8 for autoloader
BuildRequires: php-composer(phpunit/phpunit)          >= 4.8
BuildRequires: php(language)                          >= %{php_min_ver}
BuildRequires: php-composer(doctrine/annotations)     >= %{doctrine_annotations_min_ver}
BuildRequires: php-composer(doctrine/cache)           >= %{doctrine_cache_min_ver}
BuildRequires: php-composer(doctrine/common)          >= %{doctrine_common_min_ver}
BuildRequires: php-composer(doctrine/data-fixtures)   >= %{doctrine_datafixtures_min_ver}
BuildRequires: php-composer(doctrine/dbal)            >= %{doctrine_dbal_min_ver}
BuildRequires: php-composer(doctrine/doctrine-bundle) >= %{doctrine_bundle_min_ver}
BuildRequires: php-composer(doctrine/orm)             >= %{doctrine_orm_min_ver}
BuildRequires: php-composer(egulias/email-validator)  >= %{email_validator_min_ver}
BuildRequires: php-composer(monolog/monolog)          >= %{monolog_min_ver}
BuildRequires: php-composer(ocramius/proxy-manager)   >= %{proxy_manager_min_ver}
BuildRequires: php-composer(psr/log)                  >= %{psrlog_min_ver}
BuildRequires: php-composer(symfony/polyfill)         >= %{symfony_polyfill_min_ver}
#BuildRequires: php-composer(symfony/security-acl)     >= %{symfony_security_acl_min_ver}
BuildRequires: php-composer(twig/twig)                >= %{twig_min_ver}
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-ctype
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-fileinfo
BuildRequires: php-filter
BuildRequires: php-gd
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-json
BuildRequires: php-ldap
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-pdo_sqlite
BuildRequires: php-posix
BuildRequires: php-readline
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-simplexml
BuildRequires: php-sockets
BuildRequires: php-spl
BuildRequires: php-tokenizer
BuildRequires: php-xml
%endif

# Bridges
Requires:      php-composer(%{composer_vendor}/doctrine-bridge)      = %{version}
Requires:      php-composer(%{composer_vendor}/monolog-bridge)       = %{version}
Requires:      php-composer(%{composer_vendor}/phpunit-bridge)       = %{version}
Requires:      php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bridge)          = %{version}
# Bundles
Requires:      php-composer(%{composer_vendor}/debug-bundle)         = %{version}
Requires:      php-composer(%{composer_vendor}/framework-bundle)     = %{version}
Requires:      php-composer(%{composer_vendor}/security-bundle)      = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bundle)          = %{version}
Requires:      php-composer(%{composer_vendor}/web-profiler-bundle)  = %{version}
# Components
Requires:      php-composer(%{composer_vendor}/asset)                = %{version}
Requires:      php-composer(%{composer_vendor}/browser-kit)          = %{version}
Requires:      php-composer(%{composer_vendor}/class-loader)         = %{version}
Requires:      php-composer(%{composer_vendor}/config)               = %{version}
Requires:      php-composer(%{composer_vendor}/console)              = %{version}
Requires:      php-composer(%{composer_vendor}/css-selector)         = %{version}
Requires:      php-composer(%{composer_vendor}/debug)                = %{version}
Requires:      php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires:      php-composer(%{composer_vendor}/dom-crawler)          = %{version}
Requires:      php-composer(%{composer_vendor}/event-dispatcher)     = %{version}
Requires:      php-composer(%{composer_vendor}/expression-language)  = %{version}
Requires:      php-composer(%{composer_vendor}/filesystem)           = %{version}
Requires:      php-composer(%{composer_vendor}/finder)               = %{version}
Requires:      php-composer(%{composer_vendor}/form)                 = %{version}
Requires:      php-composer(%{composer_vendor}/http-foundation)      = %{version}
Requires:      php-composer(%{composer_vendor}/http-kernel)          = %{version}
Requires:      php-composer(%{composer_vendor}/intl)                 = %{version}
Requires:      php-composer(%{composer_vendor}/ldap)                 = %{version}
Requires:      php-composer(%{composer_vendor}/options-resolver)     = %{version}
Requires:      php-composer(%{composer_vendor}/process)              = %{version}
Requires:      php-composer(%{composer_vendor}/property-access)      = %{version}
Requires:      php-composer(%{composer_vendor}/property-info)        = %{version}
Requires:      php-composer(%{composer_vendor}/routing)              = %{version}
Requires:      php-composer(%{composer_vendor}/security)             = %{version}
Requires:      php-composer(%{composer_vendor}/serializer)           = %{version}
Requires:      php-composer(%{composer_vendor}/stopwatch)            = %{version}
Requires:      php-composer(%{composer_vendor}/templating)           = %{version}
Requires:      php-composer(%{composer_vendor}/translation)          = %{version}
Requires:      php-composer(%{composer_vendor}/validator)            = %{version}
Requires:      php-composer(%{composer_vendor}/var-dumper)           = %{version}
Requires:      php-composer(%{composer_vendor}/yaml)                 = %{version}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project})  = %{version}

%description
%{summary}

# ##############################################################################

%package   common

Summary:   Symfony common (version 3)

Requires:  php(language)                                 >= %{php_min_ver}
# Autoloader
Requires:  php-composer(%{composer_vendor}/class-loader) =  %{version}-%{release}

%description common
%{summary}.

# ------------------------------------------------------------------------------

%package  doctrine-bridge

Summary:  Symfony Doctrine Bridge (version 3)

Requires: %{name}-common                                 =  %{version}-%{release}
# composer.json
Requires: php-composer(doctrine/common)                  >= %{doctrine_common_min_ver}
Requires: php-composer(doctrine/common)                  <  %{doctrine_common_max_ver}
# composer.json: optional
Suggests: php-composer(%{composer_vendor}/form)          =  %{version}
Suggests: php-composer(%{composer_vendor}/validator)     =  %{version}
Suggests: php-composer(%{composer_vendor}/property-info) =  %{version}
Suggests: php-composer(doctrine/data-fixtures)           >= %{doctrine_datafixtures_min_ver}
Suggests: php-composer(doctrine/data-fixtures)           <  %{doctrine_datafixtures_max_ver}
Suggests: php-composer(doctrine/dbal)                    >= %{doctrine_dbal_min_ver}
Suggests: php-composer(doctrine/dbal)                    <  %{doctrine_dbal_max_ver}
Suggests: php-composer(doctrine/orm)                     >= %{doctrine_orm_min_ver}
Suggests: php-composer(doctrine/orm)                     <  %{doctrine_orm_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-date
Requires: php-hash
Requires: php-iconv
Requires: php-json
Requires: php-pcre
Requires: php-pdo_sqlite
Requires: php-reflection
Requires: php-session
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/doctrine-bridge) = %{version}

%description doctrine-bridge
Provides integration for Doctrine (http://www.doctrine-project.org/) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/doctrine.html

# ------------------------------------------------------------------------------

%package  monolog-bridge

Summary:  Symfony Monolog Bridge (version 3)

Requires: %{name}-common                                    =  %{version}-%{release}
# composer.json
Requires: php-composer(monolog/monolog)                     >= %{monolog_min_ver}
Requires: php-composer(monolog/monolog)                     <  %{monolog_max_ver}
# composer.json: optional
Suggests: php-composer(%{composer_vendor}/console)          =  %{version}
Suggests: php-composer(%{composer_vendor}/event-dispatcher) =  %{version}
Suggests: php-composer(%{composer_vendor}/http-kernel)      =  %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-pcre

# Composer
Provides: php-composer(%{composer_vendor}/monolog-bridge) = %{version}

%description monolog-bridge
Provides integration for Monolog (https://github.com/Seldaek/monolog) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/monolog.html

# ------------------------------------------------------------------------------

%package  phpunit-bridge

Summary:  Symfony PHPUnit Bridge (version 3)

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
Suggests: php-composer(%{composer_vendor}/debug) = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-date
Requires: php-pcre
Requires: php-posix
Requires: php-reflection

# Composer
Provides: php-composer(%{composer_vendor}/phpunit-bridge) = %{version}

%description phpunit-bridge
Provides utilities for PHPUnit, especially user deprecation notices management.

It comes with the following features:
* disable the garbage collector
* auto-register class_exists to load Doctrine annotations
* print a user deprecation notices summary at the end of the test suite.

# ------------------------------------------------------------------------------

%package  proxy-manager-bridge

Summary:  Symfony ProxyManager Bridge (version 3)

# composer.json
Requires: php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires: php-composer(ocramius/proxy-manager)                  >= %{proxy_manager_min_ver}
Requires: php-composer(ocramius/proxy-manager)                  <  %{proxy_manager_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}

%description proxy-manager-bridge
Provides integration for ProxyManager [1] with various Symfony components.

[1] http://ocramius.github.io/ProxyManager/

# ------------------------------------------------------------------------------

%package  twig-bridge

Summary:  Symfony Twig Bridge (version 3)

Requires: %{name}-common                                       =  %{version}-%{release}
# composer.json
Requires: php-composer(twig/twig)                              >= %{twig_min_ver}
Requires: php-composer(twig/twig)                              <  %{twig_max_ver}
# composer.json: optional
Suggests: php-composer(%{composer_vendor}/asset)               =  %{version}
Suggests: php-composer(%{composer_vendor}/expression-language) =  %{version}
Suggests: php-composer(%{composer_vendor}/finder)              =  %{version}
Suggests: php-composer(%{composer_vendor}/form)                =  %{version}
Suggests: php-composer(%{composer_vendor}/http-kernel)         =  %{version}
Suggests: php-composer(%{composer_vendor}/routing)             =  %{version}
Suggests: php-composer(%{composer_vendor}/security)            =  %{version}
Suggests: php-composer(%{composer_vendor}/stopwatch)           =  %{version}
Suggests: php-composer(%{composer_vendor}/templating)          =  %{version}
Suggests: php-composer(%{composer_vendor}/translation)         =  %{version}
Suggests: php-composer(%{composer_vendor}/var-dumper)          =  %{version}
Suggests: php-composer(%{composer_vendor}/yaml)                =  %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/twig-bridge) = %{version}

%description twig-bridge
Provides integration for Twig (http://twig.sensiolabs.org/) with various
Symfony components.

# ------------------------------------------------------------------------------

%package  debug-bundle

Summary:  Symfony Debug Bundle (version 3)

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel)          = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge)          = %{version}
Requires: php-composer(%{composer_vendor}/var-dumper)           = %{version}
# composer.json: optional
Suggests: php-composer(%{composer_vendor}/config)               = %{version}
Suggests: php-composer(%{composer_vendor}/dependency-injection) = %{version}
# phpcompatinfo (computed from version 3.0.0)
#     <none>

# Composer
Provides: php-composer(%{composer_vendor}/debug-bundle) = %{version}

%description debug-bundle
%{summary}.

# ------------------------------------------------------------------------------

%package  framework-bundle

Summary:  Symfony Framework Bundle (version 3)

# composer.json
Requires: php-composer(%{composer_vendor}/asset)                =  %{version}
Requires: php-composer(%{composer_vendor}/class-loader)         =  %{version}
Requires: php-composer(%{composer_vendor}/config)               =  %{version}
Requires: php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires: php-composer(%{composer_vendor}/event-dispatcher)     =  %{version}
Requires: php-composer(%{composer_vendor}/filesystem)           =  %{version}
Requires: php-composer(%{composer_vendor}/http-foundation)      =  %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)          =  %{version}
Requires: php-composer(%{composer_vendor}/routing)              =  %{version}
Requires: php-composer(%{composer_vendor}/security-core)        =  %{version}
Requires: php-composer(%{composer_vendor}/security-csrf)        =  %{version}
Requires: php-composer(%{composer_vendor}/stopwatch)            =  %{version}
Requires: php-composer(%{composer_vendor}/templating)           =  %{version}
Requires: php-composer(%{composer_vendor}/translation)          =  %{version}
Requires: php-composer(doctrine/annotations)                    >= %{doctrine_annotations_min_ver}
Requires: php-composer(doctrine/annotations)                    <  %{doctrine_annotations_max_ver}
Requires: php-composer(doctrine/cache)                          >= %{doctrine_cache_min_ver}
Requires: php-composer(doctrine/cache)                          <  %{doctrine_cache_max_ver}
# composer.json: optional
Suggests: php-composer(%{composer_vendor}/console)              =  %{version}
Suggests: php-composer(%{composer_vendor}/finder)               =  %{version}
Suggests: php-composer(%{composer_vendor}/form)                 =  %{version}
Suggests: php-composer(%{composer_vendor}/property-info)        =  %{version}
Suggests: php-composer(%{composer_vendor}/serializer)           =  %{version}
Suggests: php-composer(%{composer_vendor}/validator)            =  %{version}
Suggests: php-composer(%{composer_vendor}/yaml)                 =  %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-dom
Requires: php-fileinfo
Requires: php-filter
Requires: php-hash
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-reflection
Requires: php-spl
Requires: php-tokenizer
Suggests: php-pcntl

# Composer
Provides: php-composer(%{composer_vendor}/framework-bundle) = %{version}

%description framework-bundle
The FrameworkBundle contains most of the "base" framework functionality and can
be configured under the framework key in your application configuration. This
includes settings related to sessions, translation, forms, validation, routing
and more.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/framework.html

# ------------------------------------------------------------------------------

%package  security-bundle

Summary:  Symfony Security Bundle (version 3)

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel)    =  %{version}
Requires: php-composer(%{composer_vendor}/security)       =  %{version}
Requires: php-composer(%{composer_vendor}/security-acl)   >= %{symfony_security_acl_min_ver}
Requires: php-composer(%{composer_vendor}/security-acl)   <  %{symfony_security_acl_max_ver}
Requires: php-composer(%{composer_vendor}/polyfill)       >= %{symfony_polyfill_min_ver}
Requires: php-composer(%{composer_vendor}/polyfill)       <  %{symfony_polyfill_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/security-bundle) = %{version}

%description security-bundle
%{summary}

# ------------------------------------------------------------------------------

%package  twig-bundle

Summary:  Symfony Twig Bundle (version 3)

# composer.json
Requires: php-composer(%{composer_vendor}/asset)           = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)     = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge)     = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-ctype
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/twig-bundle) = %{version}

%description twig-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/current/reference/configuration/twig.html

# ------------------------------------------------------------------------------

%package  web-profiler-bundle

Summary:  Symfony WebProfiler Bundle (version 3)

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/routing)     = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge) = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/web-profiler-bundle) = %{version}

%description web-profiler-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/current/reference/configuration/web_profiler.html

# ------------------------------------------------------------------------------

%package   asset

Summary:   Symfony Asset Component (version 3)

Requires: %{name}-common                                    = %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/http-foundation) = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-hash
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/asset) = %{version}

%description asset
The Asset component manages asset URLs.

# ------------------------------------------------------------------------------

%package   browser-kit

Summary:   Symfony BrowserKit Component (version 3)

# composer.json
Requires:  php-composer(%{composer_vendor}/dom-crawler) = %{version}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/process)     = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/browser-kit) = %{version}

%description browser-kit
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

# ------------------------------------------------------------------------------

%package   class-loader

Summary:   Symfony ClassLoader Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-hash
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer
Suggests:  php-pecl(apcu)
Suggests:  php-xcache

# Composer
Provides:  php-composer(%{composer_vendor}/class-loader) = %{version}

%description class-loader
The ClassLoader Component loads your project classes automatically if they
follow some standard PHP conventions.

Whenever you use an undefined class, PHP uses the autoloading mechanism
to delegate the loading of a file defining the class. Symfony provides
a "universal" autoloader, which is able to load classes from files that
implement one of the following conventions:
* The technical interoperability standards [1] for PHP 5.3 namespaces
  and class names
* The PEAR naming convention [2] for classes

If your classes and the third-party libraries you use for your project follow
these standards, the Symfony autoloader is the only autoloader you will ever
need.

[1] http://symfony.com/PSR0
[2] http://pear.php.net/manual/en/standards.php

# ------------------------------------------------------------------------------

%package   config

Summary:   Symfony Config Component (version 3)

# composer.json
Requires:  php-composer(%{composer_vendor}/filesystem) = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/config) = %{version}

%description config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

# ------------------------------------------------------------------------------

%package   console

Summary:   Symfony Console Component (version 3)

Requires: %{name}-common                                     =  %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/event-dispatcher) =  %{version}
Suggests:  php-composer(%{composer_vendor}/process)          =  %{version}
Suggests:  php-composer(psr/log)                             >= %{psrlog_min_ver}
Suggests:  php-composer(psr/log)                             <  %{psrlog_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-date
Requires:  php-dom
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-posix
Requires:  php-readline
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/console) = %{version}

%description console
The Console component eases the creation of beautiful and testable command line
interfaces.

The Console component allows you to create command-line commands. Your console
commands can be used for any recurring task, such as cronjobs, imports, or
other batch jobs.

# ------------------------------------------------------------------------------

%package   css-selector

Summary:   Symfony CssSelector Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-pcre

# Composer
Provides:  php-composer(%{composer_vendor}/css-selector) = %{version}

%description css-selector
The CssSelector Component converts CSS selectors to XPath expressions.

# ------------------------------------------------------------------------------

%package  debug

Summary:  Symfony Debug Component (version 3)

Requires: %{name}-common                                   =  %{version}-%{release}
# composer.json
Requires:  php-composer(psr/log)                           >= %{psrlog_min_ver}
Requires:  php-composer(psr/log)                           <  %{psrlog_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-reflection
Requires: php-pcre
Requires: php-spl
Suggests: php-pecl(Xdebug)

# Composer
Provides: php-composer(%{composer_vendor}/debug) = %{version}

%description debug
The Debug Component provides tools to ease debugging PHP code.

# ------------------------------------------------------------------------------

%package   dependency-injection

Summary:   Symfony DependencyInjection Component (version 3)

Requires: %{name}-common                                         = %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/config)               = %{version}
Suggests:  php-composer(%{composer_vendor}/yaml)                 = %{version}
Suggests:  php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-dom
Requires:  php-hash
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/dependency-injection) = %{version}

%description dependency-injection
The Dependency Injection component allows you to standardize and centralize
the way objects are constructed in your application.

# ------------------------------------------------------------------------------

%package   dom-crawler

Summary:   Symfony DomCrawler Component (version 3)

Requires: %{name}-common                                 = %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/css-selector) = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-dom
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/dom-crawler) = %{version}

%description dom-crawler
The DomCrawler Component eases DOM navigation for HTML and XML documents.

# ------------------------------------------------------------------------------

%package   event-dispatcher

Summary:   Symfony EventDispatcher Component (version 3)

Requires: %{name}-common                                         = %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/dependency-injection) = %{version}
Suggests:  php-composer(%{composer_vendor}/http-kernel)          = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}

%description event-dispatcher
The Symfony Event Dispatcher component implements the Observer [1] pattern in
a simple and effective way to make all these things possible and to make your
projects truly extensible.

[1] http://en.wikipedia.org/wiki/Observer_pattern

# ------------------------------------------------------------------------------

%package   expression-language

Summary:   Symfony ExpressionLanguage Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/expression-language) = %{version}

%description expression-language
The ExpressionLanguage component provides an engine that can compile and
evaluate expressions. An expression is a one-liner that returns a value
(mostly, but not limited to, Booleans).

# ------------------------------------------------------------------------------

%package   filesystem

Summary:   Symfony Filesystem Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-hash
Requires:  php-pcre
Requires:  php-posix
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/filesystem) = %{version}

%description filesystem
The Filesystem component provides basic utilities for the filesystem.

# ------------------------------------------------------------------------------

%package   finder

Summary:   Symfony Finder Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/finder) = %{version}

%description finder
The Finder Component finds files and directories via an intuitive fluent
interface.

# ------------------------------------------------------------------------------

%package   form

Summary:   Symfony Form Component (version 3)

# composer.json
Requires:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires:  php-composer(%{composer_vendor}/intl)             = %{version}
Requires:  php-composer(%{composer_vendor}/options-resolver) = %{version}
Requires:  php-composer(%{composer_vendor}/property-access)  = %{version}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/framework-bundle) = %{version}
Suggests:  php-composer(%{composer_vendor}/security-csrf)    = %{version}
Suggests:  php-composer(%{composer_vendor}/twig-bridge)      = %{version}
Suggests:  php-composer(%{composer_vendor}/validator)        = %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-date
Requires:  php-hash
Requires:  php-intl
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/form) = %{version}

%description form
Form provides tools for defining forms, rendering and mapping request data
to related models. Furthermore it provides integration with the Validation
component.

# ------------------------------------------------------------------------------

%package   http-foundation

Summary:   Symfony HttpFoundation Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-date
Requires:  php-fileinfo
Requires:  php-filter
Requires:  php-hash
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-session
Requires:  php-sockets
Requires:  php-spl
Suggests:  php-pecl(mongo)

# Composer
Provides:  php-composer(%{composer_vendor}/http-foundation) = %{version}

%description http-foundation
The HttpFoundation Component defines an object-oriented layer for the HTTP
specification.

In PHP, the request is represented by some global variables ($_GET, $_POST,
$_FILES, $_COOKIE, $_SESSION, ...) and the response is generated by some
functions (echo, header, setcookie, ...).

The Symfony HttpFoundation component replaces these default PHP global
variables and functions by an Object-Oriented layer.

# ------------------------------------------------------------------------------

%package   http-kernel

Summary:   Symfony HttpKernel Component (version 3)

# composer.json
Requires:  php-composer(%{composer_vendor}/debug)                =  %{version}
Requires:  php-composer(%{composer_vendor}/event-dispatcher)     =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)      =  %{version}
Requires:  php-composer(psr/log)                                 >= %{psrlog_min_ver}
Requires:  php-composer(psr/log)                                 <  %{psrlog_max_ver}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/browser-kit)          =  %{version}
Suggests:  php-composer(%{composer_vendor}/class-loader)         =  %{version}
Suggests:  php-composer(%{composer_vendor}/config)               =  %{version}
Suggests:  php-composer(%{composer_vendor}/console)              =  %{version}
Suggests:  php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Suggests:  php-composer(%{composer_vendor}/finder)               =  %{version}
Suggests:  php-composer(%{composer_vendor}/var-dumper)           =  %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-date
Requires:  php-hash
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl
Requires:  php-tokenizer
Suggests:  php-pecl(apcu)
Suggests:  php-pecl(Xdebug)
Suggests:  php-xcache
# TODO!!!!!!!!!!!!!!
#%%if 0%%{?rhel} >= 6
#* Zend OPcache (php-pecl-zendopcache)
#%%else
#* Zend OPcache (php-opcache)
#%%endif

# Composer
Provides:  php-composer(%{composer_vendor}/http-kernel) = %{version}

%description http-kernel
The HttpKernel Component provides a structured process for converting a Request
into a Response by making use of the event dispatcher. It's flexible enough to
create a full-stack framework (Symfony), a micro-framework (Silex) or an
advanced CMS system (Drupal).

Configuration reference:
http://symfony.com/doc/current/reference/configuration/kernel.html

# ------------------------------------------------------------------------------

%package   intl

Summary:   Symfony Intl Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# composer.json: optional
Requires:  php-intl
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-date
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/intl) = %{version}

%description intl
A PHP replacement layer for the C intl extension [1] that also provides access
to the localization data of the ICU library [2].

[1] http://www.php.net/manual/en/book.intl.php
[2] http://site.icu-project.org/

# ------------------------------------------------------------------------------

%package   ldap

Summary:   An abstraction in front of PHP's LDAP functions (version 3)

Requires: %{name}-common                             =  %{version}-%{release}
# composer.json
Requires:  php-ldap
Requires:  php-composer(%{composer_vendor}/polyfill) >= %{symfony_polyfill_min_ver}
Requires:  php-composer(%{composer_vendor}/polyfill) >= %{symfony_polyfill_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ldap
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/ldap)     =  %{version}

%description ldap
%{summary}.

# ------------------------------------------------------------------------------

%package   options-resolver

Summary:   Symfony OptionsResolver Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/options-resolver) = %{version}

%description options-resolver
The OptionsResolver Component helps you configure objects with option arrays.
It supports default values, option constraints and lazy options.

# ------------------------------------------------------------------------------

%package   process

Summary:   Symfony Process Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/process) = %{version}

%description process
The Process component executes commands in sub-processes.

# ------------------------------------------------------------------------------

%package   property-access

Summary:   Symfony PropertyAccess Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/property-access) = %{version}

%description property-access
The PropertyAccess component provides function to read and write from/to an
object or array using a simple string notation.

# ------------------------------------------------------------------------------

%package   property-info

Summary:   Symfony PropertyInfo Component (version 3)

Requires:  %{name}-common                                   =  %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/doctrine-bridge) =  %{version}
Suggests:  php-composer(%{composer_vendor}/serializer)      =  %{version}
Suggests:  php-composer(phpdocumentor/reflection)           >= %{phpdocumentor_reflection_min_ver}
Suggests:  php-composer(phpdocumentor/reflection)           <  %{phpdocumentor_reflection_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/property-info) = %{version}

%description property-info
%{summary}.

# ------------------------------------------------------------------------------

%package   routing

Summary:   Symfony Routing Component (version 3)

Requires:  %{name}-common                                        =  %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/config)               =  %{version}
Suggests:  php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Suggests:  php-composer(%{composer_vendor}/expression-language)  =  %{version}
Suggests:  php-composer(%{composer_vendor}/yaml)                 =  %{version}
Suggests:  php-composer(doctrine/annotations)                    >= %{doctrine_annotations_min_ver}
Suggests:  php-composer(doctrine/annotations)                    <  %{doctrine_annotations_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/routing) = %{version}

%description routing
The Routing Component maps an HTTP request to a set of configuration variables.

# ------------------------------------------------------------------------------

%package   security

Summary:   Symfony Security Component (version 3)

# composer.json
Requires:  php-composer(%{composer_vendor}/event-dispatcher)    =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)     =  %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel)         =  %{version}
Requires:  php-composer(%{composer_vendor}/polyfill)            >= %{symfony_polyfill_min_ver}
Requires:  php-composer(%{composer_vendor}/polyfill)            >= %{symfony_polyfill_max_ver}
Requires:  php-composer(%{composer_vendor}/property-access)     =  %{version}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/expression-language) =  %{version}
Suggests:  php-composer(%{composer_vendor}/form)                =  %{version}
Suggests:  php-composer(%{composer_vendor}/ldap)                =  %{version}
Suggests:  php-composer(%{composer_vendor}/routing)             =  %{version}
Suggests:  php-composer(%{composer_vendor}/validator)           =  %{version}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-reflection
Requires:  php-ctype
Requires:  php-date
Requires:  php-hash
Requires:  php-json
Requires:  php-ldap
Requires:  php-pcre
Requires:  php-session
Requires:  php-spl
############ TODO: WITHOUT SUB-PKG TESTS!!!!!!!!!!!!!!!!!!!!!

# Composer
Provides: php-composer(%{composer_vendor}/security)       = %{version}
Provides: php-composer(%{composer_vendor}/security-core)  = %{version}
Provides: php-composer(%{composer_vendor}/security-csrf)  = %{version}
Provides: php-composer(%{composer_vendor}/security-guard) = %{version}
Provides: php-composer(%{composer_vendor}/security-http)  = %{version}
# Composer sub-packages
Provides: %{name}-security-core  = %{version}-%{release}
Provides: %{name}-security-csrf  = %{version}-%{release}
Provides: %{name}-security-guard = %{version}-%{release}
Provides: %{name}-security-http  = %{version}-%{release}

%description security
The Security Component provides a complete security system for your web
application. It ships with facilities for authenticating using HTTP basic
or digest authentication, interactive form login or X.509 certificate login,
but also allows you to implement your own authentication strategies.
Furthermore, the component provides ways to authorize authenticated users
based on their roles, and it contains an advanced ACL system.

# ------------------------------------------------------------------------------

%package   serializer

Summary:   Symfony Serializer Component (version 3)

Requires:  %{name}-common                                   =  %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/config)          =  %{version}
Suggests:  php-composer(%{composer_vendor}/property-access) =  %{version}
Suggests:  php-composer(%{composer_vendor}/yaml)            =  %{version}
Suggests:  php-composer(doctrine/annotations)               >= %{doctrine_annotations_min_ver}
Suggests:  php-composer(doctrine/annotations)               <  %{doctrine_annotations_max_ver}
Suggests:  php-composer(doctrine/cache)                     >= %{doctrine_cache_min_ver}
Suggests:  php-composer(doctrine/cache)                     <  %{doctrine_cache_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/serializer) = %{version}

%description serializer
The Serializer Component is meant to be used to turn objects into a specific
format (XML, JSON, Yaml, ...) and the other way around.

# ------------------------------------------------------------------------------

%package  stopwatch

Summary:  Symfony Stopwatch Component (version 3)

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/stopwatch) = %{version}

%description stopwatch
Stopwatch component provides a way to profile code.

# ------------------------------------------------------------------------------

%package   templating

Summary:   Symfony Templating Component (version 3)

Requires:  %{name}-common        =  %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(psr/log) >= %{psrlog_min_ver}
Suggests:  php-composer(psr/log) <  %{psrlog_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-hash
Requires:  php-iconv
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/templating) = %{version}

%description templating
Templating provides all the tools needed to build any kind of template system.

It provides an infrastructure to load template files and optionally monitor
them for changes. It also provides a concrete template engine implementation
using PHP with additional tools for escaping and separating templates into
blocks and layouts.

# ------------------------------------------------------------------------------

%package   translation

Summary:   Symfony Translation Component (version 3)

Requires:  %{name}-common                          =  %{version}-%{release}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/config) =  %{version}
Suggests:  php-composer(%{composer_vendor}/yaml)   =  %{version}
Suggests:  php-composer(psr/log)                   >= %{psrlog_min_ver}
Suggests:  php-composer(psr/log)                   <  %{psrlog_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-dom
Requires:  php-intl
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/translation) = %{version}

%description translation
Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

# ------------------------------------------------------------------------------

%package   validator

Summary:   Symfony Validator Component (version 3)

# composer.json
Requires:  php-composer(%{composer_vendor}/translation)         =  %{version}
# composer.json: optional
Suggests:  php-composer(%{composer_vendor}/config)              =  %{version}
Suggests:  php-composer(%{composer_vendor}/expression-language) =  %{version}
Suggests:  php-composer(%{composer_vendor}/http-foundation)     =  %{version}
Suggests:  php-composer(%{composer_vendor}/intl)                =  %{version}
Suggests:  php-composer(%{composer_vendor}/property-access)     =  %{version}
Suggests:  php-composer(%{composer_vendor}/yaml)                =  %{version}
Suggests:  php-composer(doctrine/annotations)                   >= %{doctrine_annotations_min_ver}
Suggests:  php-composer(doctrine/annotations)                   <  %{doctrine_annotations_max_ver}
Suggests:  php-composer(doctrine/cache)                         >= %{doctrine_cache_min_ver}
Suggests:  php-composer(doctrine/cache)                         <  %{doctrine_cache_max_ver}
Suggests:  php-composer(egulias/email-validator)                >= %{email_validator_min_ver}
Suggests:  php-composer(egulias/email-validator)                <  %{email_validator_max_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-date
Requires:  php-filter
Requires:  php-iconv
Requires:  php-intl
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/validator) = %{version}

%description validator
This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

# ------------------------------------------------------------------------------

%package  var-dumper

Summary:  Symfony mechanism for exploring and dumping PHP variables (version 3)

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
## ext-symfony_debug
# phpcompatinfo (computed from version 3.0.0)
Requires: php-curl
Requires: php-date
Requires: php-dom
Requires: php-gd
Requires: php-iconv
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-reflection
Requires: php-spl
Requires: php-xml
Suggests: php-mysql
Suggests: php-pecl(amqp)
Suggests: php-pgsql
## symfony_debug

# Composer
Provides: php-composer(%{composer_vendor}/var-dumper) = %{version}

%description var-dumper
This component provides a mechanism that allows exploring then dumping any PHP
variable.

It handles scalars, objects and resources properly, taking hard and soft
references into account. More than being immune to infinite recursion problems,
it allows dumping where references link to each other. It explores recursive
structures using a breadth-first algorithm.

The component exposes all the parts involved in the different steps of cloning
then dumping a PHP variable, while applying size limits and having specialized
output formats and methods.

# ------------------------------------------------------------------------------

%package   yaml

Summary:   Symfony Yaml Component (version 3)

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-ctype
Requires:  php-date
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/yaml) = %{version}

%description yaml
The YAML Component loads and dumps YAML files.

# ##############################################################################


%prep
%setup -qn %{github_name}-%{github_commit}
cp %{SOURCE1} .

: Remove unnecessary files
find src -name '.git*' -delete


%build
: Create common autoloader
cat <<'AUTOLOAD' | tee src/Symfony/autoload-common.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

if (!isset($fedoraPsr4ClassLoader) || !($fedoraPsr4ClassLoader instanceof \Symfony\Component\ClassLoader\Psr4ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\Psr4ClassLoader', false)) {
        require_once __DIR__.'/Component/ClassLoader/Psr4ClassLoader.php';
    }

    $fedoraPsr4ClassLoader = new \Symfony\Component\ClassLoader\Psr4ClassLoader();
    $fedoraPsr4ClassLoader->register();
}

$fedoraSymfony3PhpDir = '%{phpdir}';
$fedoraSymfony3Dir    = __DIR__;

$fedoraPsr4ClassLoader->addPrefix('Symfony\\Bridge\\',    $fedoraSymfony3Dir.'/Bridge'   );
$fedoraPsr4ClassLoader->addPrefix('Symfony\\Bundle\\',    $fedoraSymfony3Dir.'/Bundle'   );
$fedoraPsr4ClassLoader->addPrefix('Symfony\\Component\\', $fedoraSymfony3Dir.'/Component');
AUTOLOAD

: Create autoloaders
for AUTOLOADER in `./%{name}-generate-autoloaders.php`
do
    sed -e 's/__VERSION__/%{version}/' \
        -e 's/__RELEASE__/%{release}/' \
        -i $AUTOLOADER;

    cat $AUTOLOADER
done


%install
mkdir -p %{buildroot}%{symfony3_dir}
cp -rp src/Symfony/* %{buildroot}%{symfony3_dir}/

# Symlink main package docs to common sub-package docs
mkdir -p %{buildroot}%{_docdir}
%if 0%{?fedora} >= 20
ln -s %{name}-common %{buildroot}%{_docdir}/%{name}
%else
ln -s %{name}-common-%{version} %{buildroot}%{_docdir}/%{name}-%{version}
%endif


%check
%if %{with_tests}
: Modify PHPUnit config
sed -e 's#vendor/autoload\.php#bootstrap.php#' \
    -e 's#\./src/Symfony/#%{buildroot}%{phpdir}/Symfony3/#' \
    phpunit.xml.dist > phpunit.xml

: Run tests
RET=0
for PKG in %{buildroot}%{phpdir}/Symfony3/*/*; do
    echo -e "\n>>>>>>>>>>>>>>>>>>>>>>> ${PKG}\n"

    : Create tests bootstrap
    cat << BOOTSTRAP | tee bootstrap.php
<?php

require_once '${PKG}/autoload.php';
require_once '%{buildroot}%{phpdir}/Symfony3/Bridge/PhpUnit/bootstrap.php';
BOOTSTRAP

    %{_bindir}/php -d include_path=.:%{buildroot}%{phpdir}:%{phpdir} \
        %{_bindir}/phpunit --exclude-group benchmark $PKG || RET=1
done
exit $RET
%else
: Tests skipped
%endif


%{!?_licensedir:%global license %%doc}

%files
%if 0%{?fedora} >= 20
%doc %{_docdir}/%{name}
%else
%doc %{_docdir}/%{name}-%{version}
%endif


# ##############################################################################

%files common

%doc *.md composer.json
%license LICENSE

%dir %{symfony3_dir}
     %{symfony3_dir}/autoload.php
%dir %{symfony3_dir}/Bridge
%dir %{symfony3_dir}/Bundle
%dir %{symfony3_dir}/Component

# ------------------------------------------------------------------------------

%files doctrine-bridge

%license src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/*.md
%doc src/Symfony/Bridge/Doctrine/composer.json

%{symfony3_dir}/Bridge/Doctrine
%exclude %{symfony3_dir}/Bridge/Doctrine/LICENSE
%exclude %{symfony3_dir}/Bridge/Doctrine/*.md
%exclude %{symfony3_dir}/Bridge/Doctrine/composer.json
%exclude %{symfony3_dir}/Bridge/Doctrine/phpunit.*
%exclude %{symfony3_dir}/Bridge/Doctrine/Tests

# ------------------------------------------------------------------------------

%files monolog-bridge

%license src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/*.md
%doc src/Symfony/Bridge/Monolog/composer.json

%{symfony3_dir}/Bridge/Monolog
%exclude %{symfony3_dir}/Bridge/Monolog/LICENSE
%exclude %{symfony3_dir}/Bridge/Monolog/*.md
%exclude %{symfony3_dir}/Bridge/Monolog/composer.json
%exclude %{symfony3_dir}/Bridge/Monolog/phpunit.*
%exclude %{symfony3_dir}/Bridge/Monolog/Tests

# ------------------------------------------------------------------------------

%files phpunit-bridge

%license src/Symfony/Bridge/PhpUnit/LICENSE
%doc src/Symfony/Bridge/PhpUnit/*.md
%doc src/Symfony/Bridge/PhpUnit/composer.json

%{symfony3_dir}/Bridge/PhpUnit
%exclude %{symfony3_dir}/Bridge/PhpUnit/LICENSE
%exclude %{symfony3_dir}/Bridge/PhpUnit/*.md
%exclude %{symfony3_dir}/Bridge/PhpUnit/composer.json
%exclude %{symfony3_dir}/Bridge/PhpUnit/phpunit.*
#%%exclude %%{symfony3_dir}/Bridge/PhpUnit/Tests

# ------------------------------------------------------------------------------

%files proxy-manager-bridge

%license src/Symfony/Bridge/ProxyManager/LICENSE
%doc src/Symfony/Bridge/ProxyManager/*.md
%doc src/Symfony/Bridge/ProxyManager/composer.json

%{symfony3_dir}/Bridge/ProxyManager
%exclude %{symfony3_dir}/Bridge/ProxyManager/LICENSE
%exclude %{symfony3_dir}/Bridge/ProxyManager/*.md
%exclude %{symfony3_dir}/Bridge/ProxyManager/composer.json
%exclude %{symfony3_dir}/Bridge/ProxyManager/phpunit.*
%exclude %{symfony3_dir}/Bridge/ProxyManager/Tests

# ------------------------------------------------------------------------------

%files twig-bridge

%license src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/*.md
%doc src/Symfony/Bridge/Twig/composer.json

%{symfony3_dir}/Bridge/Twig
%exclude %{symfony3_dir}/Bridge/Twig/LICENSE
%exclude %{symfony3_dir}/Bridge/Twig/*.md
%exclude %{symfony3_dir}/Bridge/Twig/composer.json
%exclude %{symfony3_dir}/Bridge/Twig/phpunit.*
%exclude %{symfony3_dir}/Bridge/Twig/Tests

# ------------------------------------------------------------------------------

%files debug-bundle

#%%doc src/Symfony/Bundle/DebugBundle/*.md
%doc src/Symfony/Bundle/DebugBundle/composer.json
%license src/Symfony/Bundle/DebugBundle/Resources/meta/LICENSE

%{symfony3_dir}/Bundle/DebugBundle
#%%exclude %%{symfony3_dir}/Bundle/DebugBundle/*.md
%exclude %{symfony3_dir}/Bundle/DebugBundle/composer.json
%exclude %{symfony3_dir}/Bundle/DebugBundle/phpunit.*
%exclude %{symfony3_dir}/Bundle/DebugBundle/Tests
%exclude %{symfony3_dir}/Bundle/DebugBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files framework-bundle

%doc src/Symfony/Bundle/FrameworkBundle/*.md
%doc src/Symfony/Bundle/FrameworkBundle/composer.json
%license src/Symfony/Bundle/FrameworkBundle/Resources/meta/LICENSE

%{symfony3_dir}/Bundle/FrameworkBundle
%exclude %{symfony3_dir}/Bundle/FrameworkBundle/*.md
%exclude %{symfony3_dir}/Bundle/FrameworkBundle/composer.json
%exclude %{symfony3_dir}/Bundle/FrameworkBundle/phpunit.*
%exclude %{symfony3_dir}/Bundle/FrameworkBundle/Tests
%exclude %{symfony3_dir}/Bundle/FrameworkBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files security-bundle

%doc src/Symfony/Bundle/SecurityBundle/*.md
%doc src/Symfony/Bundle/SecurityBundle/composer.json
%license src/Symfony/Bundle/SecurityBundle/Resources/meta/LICENSE

%{symfony3_dir}/Bundle/SecurityBundle
%exclude %{symfony3_dir}/Bundle/SecurityBundle/*.md
%exclude %{symfony3_dir}/Bundle/SecurityBundle/composer.json
%exclude %{symfony3_dir}/Bundle/SecurityBundle/phpunit.*
%exclude %{symfony3_dir}/Bundle/SecurityBundle/Tests
%exclude %{symfony3_dir}/Bundle/SecurityBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files twig-bundle

%doc src/Symfony/Bundle/TwigBundle/*.md
%doc src/Symfony/Bundle/TwigBundle/composer.json
%license src/Symfony/Bundle/TwigBundle/Resources/meta/LICENSE

%{symfony3_dir}/Bundle/TwigBundle
%exclude %{symfony3_dir}/Bundle/TwigBundle/*.md
%exclude %{symfony3_dir}/Bundle/TwigBundle/composer.json
%exclude %{symfony3_dir}/Bundle/TwigBundle/phpunit.*
%exclude %{symfony3_dir}/Bundle/TwigBundle/Tests
%exclude %{symfony3_dir}/Bundle/TwigBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files web-profiler-bundle

%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%doc src/Symfony/Bundle/WebProfilerBundle/composer.json
%license src/Symfony/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%license src/Symfony/Bundle/WebProfilerBundle/Resources/meta/LICENSE

%{symfony3_dir}/Bundle/WebProfilerBundle
%exclude %{symfony3_dir}/Bundle/WebProfilerBundle/*.md
%exclude %{symfony3_dir}/Bundle/WebProfilerBundle/composer.json
%exclude %{symfony3_dir}/Bundle/WebProfilerBundle/phpunit.*
%exclude %{symfony3_dir}/Bundle/WebProfilerBundle/Tests
%exclude %{symfony3_dir}/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%exclude %{symfony3_dir}/Bundle/WebProfilerBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files asset

%license src/Symfony/Component/Asset/LICENSE
%doc src/Symfony/Component/Asset/*.md
%doc src/Symfony/Component/Asset/composer.json

%{symfony3_dir}/Component/Asset
%exclude %{symfony3_dir}/Component/Asset/LICENSE
%exclude %{symfony3_dir}/Component/Asset/*.md
%exclude %{symfony3_dir}/Component/Asset/composer.json
%exclude %{symfony3_dir}/Component/Asset/phpunit.*
%exclude %{symfony3_dir}/Component/Asset/Tests

# ------------------------------------------------------------------------------

%files browser-kit

%license src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/*.md
%doc src/Symfony/Component/BrowserKit/composer.json

%{symfony3_dir}/Component/BrowserKit
%exclude %{symfony3_dir}/Component/BrowserKit/LICENSE
%exclude %{symfony3_dir}/Component/BrowserKit/*.md
%exclude %{symfony3_dir}/Component/BrowserKit/composer.json
%exclude %{symfony3_dir}/Component/BrowserKit/phpunit.*
%exclude %{symfony3_dir}/Component/BrowserKit/Tests

# ------------------------------------------------------------------------------

%files class-loader

%license src/Symfony/Component/ClassLoader/LICENSE
%doc src/Symfony/Component/ClassLoader/*.md
%doc src/Symfony/Component/ClassLoader/composer.json

%{symfony3_dir}/Component/ClassLoader
%exclude %{symfony3_dir}/Component/ClassLoader/LICENSE
%exclude %{symfony3_dir}/Component/ClassLoader/*.md
%exclude %{symfony3_dir}/Component/ClassLoader/composer.json
%exclude %{symfony3_dir}/Component/ClassLoader/phpunit.*
%exclude %{symfony3_dir}/Component/ClassLoader/Tests

# ------------------------------------------------------------------------------

%files config

%license src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/*.md
%doc src/Symfony/Component/Config/composer.json

%{symfony3_dir}/Component/Config
%exclude %{symfony3_dir}/Component/Config/LICENSE
%exclude %{symfony3_dir}/Component/Config/*.md
%exclude %{symfony3_dir}/Component/Config/composer.json
%exclude %{symfony3_dir}/Component/Config/phpunit.*
%exclude %{symfony3_dir}/Component/Config/Tests

# ------------------------------------------------------------------------------

%files console

%license src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/*.md
%doc src/Symfony/Component/Console/composer.json

%{symfony3_dir}/Component/Console
%exclude %{symfony3_dir}/Component/Console/LICENSE
%exclude %{symfony3_dir}/Component/Console/*.md
%exclude %{symfony3_dir}/Component/Console/composer.json
%exclude %{symfony3_dir}/Component/Console/phpunit.*
%exclude %{symfony3_dir}/Component/Console/Tests

# ------------------------------------------------------------------------------

%files css-selector

%license src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/*.md
%doc src/Symfony/Component/CssSelector/composer.json

%{symfony3_dir}/Component/CssSelector
%exclude %{symfony3_dir}/Component/CssSelector/LICENSE
%exclude %{symfony3_dir}/Component/CssSelector/*.md
%exclude %{symfony3_dir}/Component/CssSelector/composer.json
%exclude %{symfony3_dir}/Component/CssSelector/phpunit.*
%exclude %{symfony3_dir}/Component/CssSelector/Tests

# ------------------------------------------------------------------------------

%files debug

%license src/Symfony/Component/Debug/LICENSE
%doc src/Symfony/Component/Debug/*.md
%doc src/Symfony/Component/Debug/composer.json

%{symfony3_dir}/Component/Debug
%exclude %{symfony3_dir}/Component/Debug/LICENSE
%exclude %{symfony3_dir}/Component/Debug/*.md
%exclude %{symfony3_dir}/Component/Debug/composer.json
%exclude %{symfony3_dir}/Component/Debug/phpunit.*
%exclude %{symfony3_dir}/Component/Debug/Tests
%exclude %{symfony3_dir}/Component/Debug/Resources/ext

# ------------------------------------------------------------------------------

%files dependency-injection

%license src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/*.md
%doc src/Symfony/Component/DependencyInjection/composer.json

%{symfony3_dir}/Component/DependencyInjection
%exclude %{symfony3_dir}/Component/DependencyInjection/LICENSE
%exclude %{symfony3_dir}/Component/DependencyInjection/*.md
%exclude %{symfony3_dir}/Component/DependencyInjection/composer.json
%exclude %{symfony3_dir}/Component/DependencyInjection/phpunit.*
%exclude %{symfony3_dir}/Component/DependencyInjection/Tests

# ------------------------------------------------------------------------------

%files dom-crawler

%license src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/*.md
%doc src/Symfony/Component/DomCrawler/composer.json

%{symfony3_dir}/Component/DomCrawler
%exclude %{symfony3_dir}/Component/DomCrawler/LICENSE
%exclude %{symfony3_dir}/Component/DomCrawler/*.md
%exclude %{symfony3_dir}/Component/DomCrawler/composer.json
%exclude %{symfony3_dir}/Component/DomCrawler/phpunit.*
%exclude %{symfony3_dir}/Component/DomCrawler/Tests

# ------------------------------------------------------------------------------

%files event-dispatcher

%license src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/*.md
%doc src/Symfony/Component/EventDispatcher/composer.json

%{symfony3_dir}/Component/EventDispatcher
%exclude %{symfony3_dir}/Component/EventDispatcher/LICENSE
%exclude %{symfony3_dir}/Component/EventDispatcher/*.md
%exclude %{symfony3_dir}/Component/EventDispatcher/composer.json
%exclude %{symfony3_dir}/Component/EventDispatcher/phpunit.*
%exclude %{symfony3_dir}/Component/EventDispatcher/Tests

# ------------------------------------------------------------------------------

%files expression-language

%license src/Symfony/Component/ExpressionLanguage/LICENSE
%doc src/Symfony/Component/ExpressionLanguage/*.md
%doc src/Symfony/Component/ExpressionLanguage/composer.json

%{symfony3_dir}/Component/ExpressionLanguage
%exclude %{symfony3_dir}/Component/ExpressionLanguage/LICENSE
%exclude %{symfony3_dir}/Component/ExpressionLanguage/*.md
%exclude %{symfony3_dir}/Component/ExpressionLanguage/composer.json
%exclude %{symfony3_dir}/Component/ExpressionLanguage/phpunit.*
%exclude %{symfony3_dir}/Component/ExpressionLanguage/Tests

# ------------------------------------------------------------------------------

%files filesystem

%license src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/*.md
%doc src/Symfony/Component/Filesystem/composer.json

%{symfony3_dir}/Component/Filesystem
%exclude %{symfony3_dir}/Component/Filesystem/LICENSE
%exclude %{symfony3_dir}/Component/Filesystem/*.md
%exclude %{symfony3_dir}/Component/Filesystem/composer.json
%exclude %{symfony3_dir}/Component/Filesystem/phpunit.*
%exclude %{symfony3_dir}/Component/Filesystem/Tests

# ------------------------------------------------------------------------------

%files finder

%license src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/*.md
%doc src/Symfony/Component/Finder/composer.json

%{symfony3_dir}/Component/Finder
%exclude %{symfony3_dir}/Component/Finder/LICENSE
%exclude %{symfony3_dir}/Component/Finder/*.md
%exclude %{symfony3_dir}/Component/Finder/composer.json
%exclude %{symfony3_dir}/Component/Finder/phpunit.*
%exclude %{symfony3_dir}/Component/Finder/Tests

# ------------------------------------------------------------------------------

%files form

%license src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/*.md
%doc src/Symfony/Component/Form/composer.json

%{symfony3_dir}/Component/Form
%exclude %{symfony3_dir}/Component/Form/LICENSE
%exclude %{symfony3_dir}/Component/Form/*.md
%exclude %{symfony3_dir}/Component/Form/composer.json
%exclude %{symfony3_dir}/Component/Form/phpunit.*
%exclude %{symfony3_dir}/Component/Form/Tests

# ------------------------------------------------------------------------------

%files http-foundation

%license src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/*.md
%doc src/Symfony/Component/HttpFoundation/composer.json

%{symfony3_dir}/Component/HttpFoundation
%exclude %{symfony3_dir}/Component/HttpFoundation/LICENSE
%exclude %{symfony3_dir}/Component/HttpFoundation/*.md
%exclude %{symfony3_dir}/Component/HttpFoundation/composer.json
%exclude %{symfony3_dir}/Component/HttpFoundation/phpunit.*
%exclude %{symfony3_dir}/Component/HttpFoundation/Tests

# ------------------------------------------------------------------------------

%files http-kernel

%license src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/*.md
%doc src/Symfony/Component/HttpKernel/composer.json

%{symfony3_dir}/Component/HttpKernel
%exclude %{symfony3_dir}/Component/HttpKernel/LICENSE
%exclude %{symfony3_dir}/Component/HttpKernel/*.md
%exclude %{symfony3_dir}/Component/HttpKernel/composer.json
%exclude %{symfony3_dir}/Component/HttpKernel/phpunit.*
%exclude %{symfony3_dir}/Component/HttpKernel/Tests

# ------------------------------------------------------------------------------

%files intl

%license src/Symfony/Component/Intl/LICENSE
%doc src/Symfony/Component/Intl/*.md
%doc src/Symfony/Component/Intl/composer.json

%{symfony3_dir}/Component/Intl
%exclude %{symfony3_dir}/Component/Intl/LICENSE
%exclude %{symfony3_dir}/Component/Intl/*.md
%exclude %{symfony3_dir}/Component/Intl/composer.json
%exclude %{symfony3_dir}/Component/Intl/phpunit.*
%exclude %{symfony3_dir}/Component/Intl/Tests

# ------------------------------------------------------------------------------

%files ldap

%license src/Symfony/Component/Ldap/LICENSE
%doc src/Symfony/Component/Ldap/*.md
%doc src/Symfony/Component/Ldap/composer.json

%{symfony3_dir}/Component/Ldap
%exclude %{symfony3_dir}/Component/Ldap/LICENSE
%exclude %{symfony3_dir}/Component/Ldap/*.md
%exclude %{symfony3_dir}/Component/Ldap/composer.json
%exclude %{symfony3_dir}/Component/Ldap/phpunit.*
%exclude %{symfony3_dir}/Component/Ldap/Tests

# ------------------------------------------------------------------------------

%files options-resolver

%license src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/*.md
%doc src/Symfony/Component/OptionsResolver/composer.json

%{symfony3_dir}/Component/OptionsResolver
%exclude %{symfony3_dir}/Component/OptionsResolver/LICENSE
%exclude %{symfony3_dir}/Component/OptionsResolver/*.md
%exclude %{symfony3_dir}/Component/OptionsResolver/composer.json
%exclude %{symfony3_dir}/Component/OptionsResolver/phpunit.*
%exclude %{symfony3_dir}/Component/OptionsResolver/Tests

# ------------------------------------------------------------------------------

%files process

%license src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/*.md
%doc src/Symfony/Component/Process/composer.json

%{symfony3_dir}/Component/Process
%exclude %{symfony3_dir}/Component/Process/LICENSE
%exclude %{symfony3_dir}/Component/Process/*.md
%exclude %{symfony3_dir}/Component/Process/composer.json
%exclude %{symfony3_dir}/Component/Process/phpunit.*
%exclude %{symfony3_dir}/Component/Process/Tests

# ------------------------------------------------------------------------------

%files property-access

%license src/Symfony/Component/PropertyAccess/LICENSE
%doc src/Symfony/Component/PropertyAccess/*.md
%doc src/Symfony/Component/PropertyAccess/composer.json

%{symfony3_dir}/Component/PropertyAccess
%exclude %{symfony3_dir}/Component/PropertyAccess/LICENSE
%exclude %{symfony3_dir}/Component/PropertyAccess/*.md
%exclude %{symfony3_dir}/Component/PropertyAccess/composer.json
%exclude %{symfony3_dir}/Component/PropertyAccess/phpunit.*
%exclude %{symfony3_dir}/Component/PropertyAccess/Tests

# ------------------------------------------------------------------------------

%files property-info

%license src/Symfony/Component/PropertyInfo/LICENSE
%doc src/Symfony/Component/PropertyInfo/*.md
%doc src/Symfony/Component/PropertyInfo/composer.json

%{symfony3_dir}/Component/PropertyInfo
%exclude %{symfony3_dir}/Component/PropertyInfo/LICENSE
%exclude %{symfony3_dir}/Component/PropertyInfo/*.md
%exclude %{symfony3_dir}/Component/PropertyInfo/composer.json
%exclude %{symfony3_dir}/Component/PropertyInfo/phpunit.*
%exclude %{symfony3_dir}/Component/PropertyInfo/Tests

# ------------------------------------------------------------------------------

%files routing

%license src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/*.md
%doc src/Symfony/Component/Routing/composer.json

%{symfony3_dir}/Component/Routing
%exclude %{symfony3_dir}/Component/Routing/LICENSE
%exclude %{symfony3_dir}/Component/Routing/*.md
%exclude %{symfony3_dir}/Component/Routing/composer.json
%exclude %{symfony3_dir}/Component/Routing/phpunit.*
%exclude %{symfony3_dir}/Component/Routing/Tests

# ------------------------------------------------------------------------------

%files security

%license src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/*.md
%doc src/Symfony/Component/Security/composer.json

%{symfony3_dir}/Component/Security
%exclude %{symfony3_dir}/Component/Security/LICENSE
%exclude %{symfony3_dir}/Component/Security/*.md
%exclude %{symfony3_dir}/Component/Security/composer.json
%exclude %{symfony3_dir}/Component/Security/phpunit.*
%exclude %{symfony3_dir}/Component/Security/*/phpunit.*
#exclude %{symfony3_dir}/Component/Security/Tests
%exclude %{symfony3_dir}/Component/Security/*/Tests
%exclude %{symfony3_dir}/Component/Security/*/LICENSE
%exclude %{symfony3_dir}/Component/Security/*/*.md
%exclude %{symfony3_dir}/Component/Security/*/composer.json

# ------------------------------------------------------------------------------

%files serializer

%license src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/*.md
%doc src/Symfony/Component/Serializer/composer.json

%{symfony3_dir}/Component/Serializer
%exclude %{symfony3_dir}/Component/Serializer/LICENSE
%exclude %{symfony3_dir}/Component/Serializer/*.md
%exclude %{symfony3_dir}/Component/Serializer/composer.json
%exclude %{symfony3_dir}/Component/Serializer/phpunit.*
%exclude %{symfony3_dir}/Component/Serializer/Tests

# ------------------------------------------------------------------------------

%files stopwatch

%license src/Symfony/Component/Stopwatch/LICENSE
%doc src/Symfony/Component/Stopwatch/*.md
%doc src/Symfony/Component/Stopwatch/composer.json

%{symfony3_dir}/Component/Stopwatch
%exclude %{symfony3_dir}/Component/Stopwatch/LICENSE
%exclude %{symfony3_dir}/Component/Stopwatch/*.md
%exclude %{symfony3_dir}/Component/Stopwatch/composer.json
%exclude %{symfony3_dir}/Component/Stopwatch/phpunit.*
%exclude %{symfony3_dir}/Component/Stopwatch/Tests

# ------------------------------------------------------------------------------

%files templating

%license src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/*.md
%doc src/Symfony/Component/Templating/composer.json

%{symfony3_dir}/Component/Templating
%exclude %{symfony3_dir}/Component/Templating/LICENSE
%exclude %{symfony3_dir}/Component/Templating/*.md
%exclude %{symfony3_dir}/Component/Templating/composer.json
%exclude %{symfony3_dir}/Component/Templating/phpunit.*
%exclude %{symfony3_dir}/Component/Templating/Tests

# ------------------------------------------------------------------------------

%files translation

%license src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/*.md
%doc src/Symfony/Component/Translation/composer.json

%{symfony3_dir}/Component/Translation
%exclude %{symfony3_dir}/Component/Translation/LICENSE
%exclude %{symfony3_dir}/Component/Translation/*.md
%exclude %{symfony3_dir}/Component/Translation/composer.json
%exclude %{symfony3_dir}/Component/Translation/phpunit.*
%exclude %{symfony3_dir}/Component/Translation/Tests

# ------------------------------------------------------------------------------

%files validator

%license src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/*.md
%doc src/Symfony/Component/Validator/composer.json

%{symfony3_dir}/Component/Validator
%exclude %{symfony3_dir}/Component/Validator/LICENSE
%exclude %{symfony3_dir}/Component/Validator/*.md
%exclude %{symfony3_dir}/Component/Validator/composer.json
%exclude %{symfony3_dir}/Component/Validator/phpunit.*
%exclude %{symfony3_dir}/Component/Validator/Tests

# ------------------------------------------------------------------------------

%files var-dumper

%license src/Symfony/Component/VarDumper/LICENSE
%doc src/Symfony/Component/VarDumper/*.md
%doc src/Symfony/Component/VarDumper/composer.json

%{symfony3_dir}/Component/VarDumper
%exclude %{symfony3_dir}/Component/VarDumper/LICENSE
%exclude %{symfony3_dir}/Component/VarDumper/*.md
%exclude %{symfony3_dir}/Component/VarDumper/composer.json
%exclude %{symfony3_dir}/Component/VarDumper/phpunit.*
%exclude %{symfony3_dir}/Component/VarDumper/Tests

# ------------------------------------------------------------------------------

%files yaml

%license src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/*.md
%doc src/Symfony/Component/Yaml/composer.json

%{symfony3_dir}/Component/Yaml
%exclude %{symfony3_dir}/Component/Yaml/LICENSE
%exclude %{symfony3_dir}/Component/Yaml/*.md
%exclude %{symfony3_dir}/Component/Yaml/composer.json
%exclude %{symfony3_dir}/Component/Yaml/phpunit.*
%exclude %{symfony3_dir}/Component/Yaml/Tests

# ##############################################################################

%changelog
* Thu Dec 03 2015 Shawn Iwinski <shawn@iwin.ski> - 3.0.0-1
- Initial package
