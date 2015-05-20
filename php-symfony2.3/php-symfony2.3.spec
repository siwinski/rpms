#
# RPM spec file for php-symfony2.3
#
# Copyright (c) 2014-2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      symfony
%global github_version   2.3.25
%global github_commit    959733dc4b1da99b9e93a1762f4217eee20fc933

%global composer_vendor  symfony
%global composer_project symfony

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "doctrine/common": "~2.2"
%global doctrine_common_min_ver 2.2
%global doctrine_common_max_ver 3.0
# "doctrine/data-fixtures": "1.0.*"
%global doctrine_datafixtures_min_ver 1.0.0
%global doctrine_datafixtures_max_ver 1.1.0
# "doctrine/dbal": "~2.2"
%global doctrine_dbal_min_ver 2.2
%global doctrine_dbal_max_ver 3.0
# "doctrine/orm": "~2.2,>=2.2.3"
%global doctrine_orm_min_ver 2.2.3
%global doctrine_orm_max_ver 3.0
# "ircmaxell/password-compat": "~1.0"
%global password_compat_min_ver 1.0
%global password_compat_max_ver 2.0
# "monolog/monolog": "~1.3"
%global monolog_min_ver 1.3
%global monolog_max_ver 2.0
# "psr/log": "~1.0"
%global psrlog_min_ver 1.0
%global psrlog_max_ver 2.0
# "swiftmailer/swiftmailer": ">=4.2.0,<6.0-dev" (src/Symfony/Bridge/Swiftmailer/composer.json)
%global swift_min_ver 4.2.0
%global swift_max_ver 6.0.0
# "symfony/icu": "~1.0"
#%global symfony_icu_min_ver 1.0
#%global symfony_icu_max_ver 2.0
# "twig/twig": "~1.12,>=1.12.3"
%global twig_min_ver 1.12.3
%global twig_max_ver 2.0

%{!?phpdir:     %global phpdir     %{_datadir}/php}
%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

%global symfony_dir  %{phpdir}/Symfony
%global pear_channel pear.symfony.com

# Build using "--without tests" to disable tests
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_project}2.3
Version:       %{github_version}
Release:       1%{?dist}
Summary:       PHP framework for web projects

Group:         Development/Libraries
License:       MIT
URL:           http://symfony.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Run this command to download the PEAR packages
# and retrieve files missing from github archive
#
# NOTE: PEAR channel deprecated after 2.3.13
Source2:       %{name}-pear-autoloader.sh
Source3:       %{name}-pear-autoloader-2.3.13.tgz

BuildArch:     noarch
%if %{with_tests}
# composer.json
BuildRequires: php(language)                        >= %{php_min_ver}
BuildRequires: php-composer(doctrine/common)        >= %{doctrine_common_min_ver}
BuildRequires: php-composer(doctrine/common)        <  %{doctrine_common_max_ver}
BuildRequires: php-composer(doctrine/data-fixtures) >= %{doctrine_datafixtures_min_ver}
BuildRequires: php-composer(doctrine/data-fixtures) <  %{doctrine_datafixtures_max_ver}
BuildRequires: php-composer(doctrine/dbal)          >= %{doctrine_dbal_min_ver}
BuildRequires: php-composer(doctrine/dbal)          <  %{doctrine_dbal_max_ver}
BuildRequires: php-composer(doctrine/orm)           >= %{doctrine_orm_min_ver}
BuildRequires: php-composer(doctrine/orm)           <  %{doctrine_orm_max_ver}
BuildRequires: php-composer(monolog/monolog)        >= %{monolog_min_ver}
BuildRequires: php-composer(monolog/monolog)        <  %{monolog_max_ver}
BuildRequires: php-composer(psr/log)                >= %{psrlog_min_ver}
BuildRequires: php-composer(psr/log)                <  %{psrlog_max_ver}
BuildRequires: php-composer(twig/twig)              >= %{twig_min_ver}
BuildRequires: php-composer(twig/twig)              <  %{twig_max_ver}
BuildRequires: php-phpunit-PHPUnit
%if 0%{?el6}%{?el7}
BuildRequires: php-password-compat                  >= %{password_compat_min_ver}
BuildRequires: php-password-compat                  <  %{password_compat_max_ver}
%endif
## TODO: "propel/propel1"
## TODO: "ocramius/proxy-manager"
# phpcompatinfo (computed from version 2.3.25)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-fileinfo
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-openssl
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-posix
BuildRequires: php-readline
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-simplexml
BuildRequires: php-sockets
BuildRequires: php-spl
BuildRequires: php-sqlite3
BuildRequires: php-tokenizer
BuildRequires: php-xml
%endif

# Bridges
Requires:      php-composer(%{composer_vendor}/doctrine-bridge)      = %{version}
Requires:      php-composer(%{composer_vendor}/monolog-bridge)       = %{version}
#Requires:      php-composer(%%{composer_vendor}/propel1-bridge)       = %%{version}
#Requires:      php-composer(%%{composer_vendor}/proxy-manager-bridge) = %%{version}
Requires:      php-composer(%{composer_vendor}/swiftmailer-bridge)   = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bridge)          = %{version}
# Bundles
Requires:      php-composer(%{composer_vendor}/framework-bundle)     = %{version}
Requires:      php-composer(%{composer_vendor}/security-bundle)      = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bundle)          = %{version}
Requires:      php-composer(%{composer_vendor}/web-profiler-bundle)  = %{version}
# Components
Requires:      php-composer(%{composer_vendor}/browser-kit)          = %{version}
Requires:      php-composer(%{composer_vendor}/class-loader)         = %{version}
Requires:      php-composer(%{composer_vendor}/config)               = %{version}
Requires:      php-composer(%{composer_vendor}/console)              = %{version}
Requires:      php-composer(%{composer_vendor}/css-selector)         = %{version}
Requires:      php-composer(%{composer_vendor}/debug)                = %{version}
Requires:      php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires:      php-composer(%{composer_vendor}/dom-crawler)          = %{version}
Requires:      php-composer(%{composer_vendor}/event-dispatcher)     = %{version}
Requires:      php-composer(%{composer_vendor}/filesystem)           = %{version}
Requires:      php-composer(%{composer_vendor}/finder)               = %{version}
Requires:      php-composer(%{composer_vendor}/form)                 = %{version}
Requires:      php-composer(%{composer_vendor}/http-foundation)      = %{version}
Requires:      php-composer(%{composer_vendor}/http-kernel)          = %{version}
Requires:      php-composer(%{composer_vendor}/intl)                 = %{version}
Requires:      php-composer(%{composer_vendor}/locale)               = %{version}
Requires:      php-composer(%{composer_vendor}/options-resolver)     = %{version}
Requires:      php-composer(%{composer_vendor}/process)              = %{version}
Requires:      php-composer(%{composer_vendor}/property-access)      = %{version}
Requires:      php-composer(%{composer_vendor}/routing)              = %{version}
Requires:      php-composer(%{composer_vendor}/security)             = %{version}
Requires:      php-composer(%{composer_vendor}/serializer)           = %{version}
Requires:      php-composer(%{composer_vendor}/stopwatch)            = %{version}
Requires:      php-composer(%{composer_vendor}/templating)           = %{version}
Requires:      php-composer(%{composer_vendor}/translation)          = %{version}
Requires:      php-composer(%{composer_vendor}/validator)            = %{version}
Requires:      php-composer(%{composer_vendor}/yaml)                 = %{version}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project})  = %{version}

%description
%{summary}

# ##############################################################################

%package   common

Summary:   Symfony common files

Requires:  php(language) >= %{php_min_ver}

Obsoletes: php-channel-symfony2

Conflicts: %{name}-common >= 2.4.0

%description common
%{summary}

# ------------------------------------------------------------------------------

%package   doctrine-bridge

Summary:   Symfony Doctrine Bridge

# composer.json
Requires:  php-composer(doctrine/common)              >= %{doctrine_common_min_ver}
Requires:  php-composer(doctrine/common)              <  %{doctrine_common_max_ver}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/form)      =  %{version}
Requires:  php-composer(%{composer_vendor}/validator) =  %{version}
Requires:  php-composer(doctrine/data-fixtures)       >= %{doctrine_datafixtures_min_ver}
Requires:  php-composer(doctrine/data-fixtures)       <  %{doctrine_datafixtures_max_ver}
Requires:  php-composer(doctrine/dbal)                >= %{doctrine_dbal_min_ver}
Requires:  php-composer(doctrine/dbal)                <  %{doctrine_dbal_max_ver}
Requires:  php-composer(doctrine/orm)                 >= %{doctrine_orm_min_ver}
Requires:  php-composer(doctrine/orm)                 <  %{doctrine_orm_max_ver}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl

Conflicts: %{name}-doctrine-bridge >= 2.4.0

# Composer
Provides: php-composer(%{composer_vendor}/doctrine-bridge) = %{version}

%description doctrine-bridge
Provides integration for Doctrine (http://www.doctrine-project.org/) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/doctrine.html

# ------------------------------------------------------------------------------

%package   monolog-bridge

Summary:   Symfony Monolog Bridge

# composer.json
Requires:  php-composer(%{composer_vendor}/http-kernel) =  %{version}
Requires:  php-composer(monolog/monolog)                >= %{monolog_min_ver}
Requires:  php-composer(monolog/monolog)                <  %{monolog_max_ver}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcre

# Composer
Provides:  php-composer(%{composer_vendor}/monolog-bridge) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/MonologBridge) = %{version}
# Rename
Obsoletes: %{name}-monologbridge < %{version}
Provides:  %{name}-monologbridge = %{version}

Conflicts: %{name}-monolog-bridge >= 2.4.0

%description monolog-bridge
Provides integration for Monolog (https://github.com/Seldaek/monolog) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/monolog.html

# ------------------------------------------------------------------------------

#%%package  propel1-bridge

#Summary:  Symfony Propel 1 Bridge

#Requires: php-composer(%%{composer_vendor}/http-foundation) = %%{version}
#Requires: php-composer(%%{composer_vendor}/http-kernel)     = %%{version}
#Requires: php-composer(%%{composer_vendor}/form)            = %%{version}
## TODO: "propel/propel1"

# Composer
#Provides: php-composer(%%{composer_vendor}/propel1-bridge) = %%{version}

#Conflicts: %%{name}-propel1-bridge >= 2.4.0

#%%description propel1-bridge
#Provides integration for Propel 1 (http://propelorm.org/) with various
#Symfony components.

# ------------------------------------------------------------------------------

#%%package  proxy-manager-bridge

#Summary:  Symfony ProxyManager Bridge

#Requires: php-composer(%%{composer_vendor}/dependency-injection) = %%{version}
## TODO: "ocramius/proxy-manager"

# Composer
#Provides: php-composer(%%{composer_vendor}/proxy-manager-bridge) = %%{version}

#Conflicts: %%{name}-proxy-manage-bridge >= 2.4.0

#%%description proxy-manager-bridge
#Provides integration for ProxyManager (https://github.com/Ocramius/ProxyManager)
#with various Symfony components.

# ------------------------------------------------------------------------------

%package   swiftmailer-bridge

Summary:   Symfony Swiftmailer Bridge

# composer.json
Requires:  php-swift-Swift >= %{swift_min_ver}
Requires:  php-swift-Swift <  %{swift_max_ver}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/http-kernel) = %{version}
# phpcompatinfo (computed from version 2.3.25)
# <none>

# Composer
Provides:  php-composer(%{composer_vendor}/swiftmailer-bridge) = %{version}
# Rename
Obsoletes: %{name}-swiftmailerbridge < %{version}
Provides:  %{name}-swiftmailerbridge = %{version}

Conflicts: %{name}-swiftmailer-bridge >= 2.4.0

%description swiftmailer-bridge
Provides integration for Swift Mailer (http://swiftmailer.org/) with various
Symfony components.

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/swiftmailer.html

NOTE: Deprecated since version 2.4, to be removed in 3.0. Use SwiftmailerBundle
instead.

# ------------------------------------------------------------------------------

%package   twig-bridge

Summary:   Symfony Twig Bridge

# composer.json
Requires:  php-composer(twig/twig) >= %{twig_min_ver}
Requires:  php-composer(twig/twig) <  %{twig_max_ver}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/finder)      = %{version}
Requires:  php-composer(%{composer_vendor}/form)        = %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires:  php-composer(%{composer_vendor}/routing)     = %{version}
Requires:  php-composer(%{composer_vendor}/security)    = %{version}
Requires:  php-composer(%{composer_vendor}/templating)  = %{version}
Requires:  php-composer(%{composer_vendor}/translation) = %{version}
Requires:  php-composer(%{composer_vendor}/yaml)        = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/twig-bridge) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/TwigBridge) = %{version}
# Rename
Obsoletes: %{name}-twigbridge < %{version}
Provides:  %{name}-twigbridge = %{version}

Conflicts: %{name}-twig-bridge >= 2.4.0

%description twig-bridge
Provides integration for Twig (http://twig.sensiolabs.org/) with various
Symfony components.

# ------------------------------------------------------------------------------

%package   framework-bundle

Summary:   Symfony Framework Bundle

# composer.json
Requires:  php-composer(%{composer_vendor}/config)               =  %{version}
Requires:  php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires:  php-composer(%{composer_vendor}/event-dispatcher)     =  %{version}
Requires:  php-composer(%{composer_vendor}/filesystem)           =  %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel)          =  %{version}
Requires:  php-composer(%{composer_vendor}/routing)              =  %{version}
Requires:  php-composer(%{composer_vendor}/stopwatch)            =  %{version}
Requires:  php-composer(%{composer_vendor}/templating)           =  %{version}
Requires:  php-composer(%{composer_vendor}/translation)          =  %{version}
Requires:  php-composer(doctrine/common)                         >= %{doctrine_common_min_ver}
Requires:  php-composer(doctrine/common)                         <  %{doctrine_common_max_ver}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/console)              =  %{version}
Requires:  php-composer(%{composer_vendor}/finder)               =  %{version}
Requires:  php-composer(%{composer_vendor}/form)                 =  %{version}
Requires:  php-composer(%{composer_vendor}/validator)            =  %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-fileinfo
Requires:  php-filter
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/framework-bundle) = %{version}
# Rename
Obsoletes: %{name}-frameworkbundle < %{version}
Provides:  %{name}-frameworkbundle = %{version}

Conflicts: %{name}-framework-bundle >= 2.4.0

%description framework-bundle
The FrameworkBundle contains most of the "base" framework functionality and can
be configured under the framework key in your application configuration. This
includes settings related to sessions, translation, forms, validation, routing
and more.

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/framework.html

# ------------------------------------------------------------------------------

%package   security-bundle

Summary:   Symfony Security Bundle

# composer.json
Requires:  php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires:  php-composer(%{composer_vendor}/security)    = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/security-bundle) = %{version}
# Rename
Obsoletes: %{name}-securitybundle < %{version}
Provides:  %{name}-securitybundle = %{version}

Conflicts: %{name}-security-bundle >= 2.4.0

%description security-bundle
%{summary}

# ------------------------------------------------------------------------------

%package   twig-bundle

Summary:   Symfony Twig Bundle

# composer.json
Requires:  php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires:  php-composer(%{composer_vendor}/twig-bridge) = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/twig-bundle) = %{version}
# Rename
Obsoletes: %{name}-twigbundle < %{version}
Provides:  %{name}-twigbundle = %{version}

Conflicts: %{name}-twig-bundle >= 2.4.0

%description twig-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/twig.html

# ------------------------------------------------------------------------------

%package   web-profiler-bundle

Summary:   Symfony WebProfiler Bundle

# composer.json
Requires:  php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires:  php-composer(%{composer_vendor}/routing)     = %{version}
Requires:  php-composer(%{composer_vendor}/twig-bridge) = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/web-profiler-bundle) = %{version}
# Rename
Obsoletes: %{name}-webprofilerbundle < %{version}
Provides:  %{name}-webprofilerbundle = %{version}

Conflicts: %{name}-web-profiler-bundle >= 2.4.0

%description web-profiler-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/web_profiler.html

# ------------------------------------------------------------------------------

%package   browser-kit

Summary:   Symfony BrowserKit Component

# composer.json
Requires:  php-composer(%{composer_vendor}/dom-crawler) = %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/process)     = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/browser-kit) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/BrowserKit) = %{version}
# Rename
Obsoletes: %{name}2-BrowserKit < %{version}
Provides:  %{name}2-BrowserKit = %{version}
Obsoletes: %{name}-browserkit  < %{version}
Provides:  %{name}-browserkit  = %{version}

Conflicts: %{name}-browser-kit >= 2.4.0

%description browser-kit
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

# ------------------------------------------------------------------------------

%package   class-loader

Summary:   Symfony ClassLoader Component
URL:       http://symfony.com/doc/2.3/components/class_loader/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/class-loader) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/ClassLoader) = %{version}
# Rename
Obsoletes: %{name}2-ClassLoader < %{version}
Provides:  %{name}2-ClassLoader = %{version}
Obsoletes: %{name}-classloader  < %{version}
Provides:  %{name}-classloader  = %{version}

Conflicts: %{name}-class-loader >= 2.4.0

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

Optional:
* APC (php-pecl-apcu)
* XCache (php-xcache)

[1] http://symfony.com/PSR0
[2] http://pear.php.net/manual/en/standards.php

# ------------------------------------------------------------------------------

%package   config

Summary:   Symfony Config Component
URL:       http://symfony.com/doc/2.3/components/config/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/filesystem) = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/config) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Config) = %{version}
# Rename
Obsoletes: %{name}2-Config < %{version}
Provides:  %{name}2-Config = %{version}

Conflicts: %{name}-config >= 2.4.0

%description config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

# ------------------------------------------------------------------------------

%package   console

Summary:   Symfony Console Component
URL:       http://symfony.com/doc/2.3/components/console/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-dom
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-posix
Requires:  php-readline
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/console) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Console) = %{version}
# Rename
Obsoletes: %{name}2-Console < %{version}
Provides:  %{name}2-Console = %{version}

Conflicts: %{name}-console >= 2.4.0

%description console
The Console component eases the creation of beautiful and testable command line
interfaces.

The Console component allows you to create command-line commands. Your console
commands can be used for any recurring task, such as cronjobs, imports, or
other batch jobs.

# ------------------------------------------------------------------------------

%package   css-selector

Summary:   Symfony CssSelector Component
URL:       http://symfony.com/doc/2.3/components/css_selector.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcre

# Composer
Provides:  php-composer(%{composer_vendor}/css-selector) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/CssSelector) = %{version}
# Rename
Obsoletes: %{name}2-CssSelector < %{version}
Provides:  %{name}2-CssSelector = %{version}
Obsoletes: %{name}-cssselector  < %{version}
Provides:  %{name}-cssselector  = %{version}

Conflicts: %{name}-css-selector >= 2.4.0

%description css-selector
The CssSelector Component converts CSS selectors to XPath expressions.

# ------------------------------------------------------------------------------

%package  debug

Summary:  Symfony Debug Component
URL:      http://symfony.com/doc/2.3/components/debug/index.html

# composer.json: optional
Requires: php-composer(%{composer_vendor}/class-loader)    = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel)     = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/debug) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/Debug) = %{version}

Conflicts: %{name}-debug >= 2.4.0

%description debug
The Debug Component provides tools to ease debugging PHP code.

Optional:
* Xdebug (php-pecl-xdebug)

# ------------------------------------------------------------------------------

%package   dependency-injection

Summary:   Symfony DependencyInjection Component
URL:       http://symfony.com/doc/2.3/components/dependency_injection/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config) = %{version}
#Requires:  php-composer(%%{composer_vendor}/proxy-manager-bridge) = %%{version}
Requires:  php-composer(%{composer_vendor}/yaml)   = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-dom
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/dependency-injection) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/DependencyInjection) = %{version}
# Rename
Obsoletes: %{name}2-DependencyInjection < %{version}
Provides:  %{name}2-DependencyInjection = %{version}
Obsoletes: %{name}-dependencyinjection  < %{version}
Provides:  %{name}-dependencyinjection  = %{version}

Conflicts: %{name}-dependency-injection >= 2.4.0

%description dependency-injection
The Dependency Injection component allows you to standardize and centralize
the way objects are constructed in your application.

# ------------------------------------------------------------------------------

%package   dom-crawler

Summary:   Symfony DomCrawler Component
URL:       http://symfony.com/doc/2.3/components/dom_crawler.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/css-selector) = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-dom
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/dom-crawler) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/DomCrawler) = %{version}
# Rename
Obsoletes: %{name}2-DomCrawler < %{version}
Provides:  %{name}2-DomCrawler = %{version}
Obsoletes: %{name}-domcrawler  < %{version}
Provides:  %{name}-domcrawler  = %{version}

Conflicts: %{name}-dom-crawler >= 2.4.0

%description dom-crawler
The DomCrawler Component eases DOM navigation for HTML and XML documents.

# ------------------------------------------------------------------------------

%package   event-dispatcher

Summary:   Symfony EventDispatcher Component
URL:       http://symfony.com/doc/2.3/components/event_dispatcher/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel)          = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/EventDispatcher) = %{version}
# Rename
Obsoletes: %{name}2-EventDispatcher < %{version}
Provides:  %{name}2-EventDispatcher = %{version}
Obsoletes: %{name}-eventdispatcher  < %{version}
Provides:  %{name}-eventdispatcher  = %{version}

Conflicts: %{name}-event-dispatcher >= 2.4.0

%description event-dispatcher
The Symfony Event Dispatcher component implements the Observer [1] pattern in
a simple and effective way to make all these things possible and to make your
projects truly extensible.

[1] http://en.wikipedia.org/wiki/Observer_pattern

# ------------------------------------------------------------------------------

%package   filesystem

Summary:   Symfony Filesystem Component
URL:       http://symfony.com/doc/2.3/components/filesystem.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/filesystem) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Filesystem) = %{version}
# Rename
Obsoletes: %{name}2-Filesystem < %{version}
Provides:  %{name}2-Filesystem = %{version}

Conflicts: %{name}-filesystem >= 2.4.0

%description filesystem
The Filesystem component provides basic utilities for the filesystem.

# ------------------------------------------------------------------------------

%package   finder

Summary:   Symfony Finder Component
URL:       http://symfony.com/doc/2.3/components/finder.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/finder) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Finder) = %{version}
# Rename
Obsoletes: %{name}2-Finder < %{version}
Provides:  %{name}2-Finder = %{version}

Conflicts: %{name}-finder >= 2.4.0

%description finder
The Finder Component finds files and directories via an intuitive fluent
interface.

# ------------------------------------------------------------------------------

%package   form

Summary:   Symfony Form Component

# composer.json
Requires:  php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires:  php-composer(%{composer_vendor}/intl)             = %{version}
Requires:  php-composer(%{composer_vendor}/options-resolver) = %{version}
Requires:  php-composer(%{composer_vendor}/property-access)  = %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/http-foundation)  = %{version}
Requires:  php-composer(%{composer_vendor}/validator)        = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-date
Requires:  php-hash
Requires:  php-intl
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-session
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/form) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Form) = %{version}
# Rename
Obsoletes: %{name}2-Form < %{version}
Provides:  %{name}2-Form = %{version}

Conflicts: %{name}-form >= 2.4.0

%description form
Form provides tools for defining forms, rendering and mapping request data
to related models. Furthermore it provides integration with the Validation
component.

# ------------------------------------------------------------------------------

%package   http-foundation

Summary:   Symfony HttpFoundation Component
URL:       http://symfony.com/doc/2.3/components/http_foundation/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-fileinfo
Requires:  php-filter
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-session
Requires:  php-sockets
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/http-foundation) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/HttpFoundation) = %{version}
# Rename
Obsoletes: %{name}2-HttpFoundation < %{version}
Provides:  %{name}2-HttpFoundation = %{version}
Obsoletes: %{name}-httpfoundation  < %{version}
Provides:  %{name}-httpfoundation  = %{version}

Conflicts: %{name}-http-foundation >= 2.4.0

%description http-foundation
The HttpFoundation Component defines an object-oriented layer for the HTTP
specification.

In PHP, the request is represented by some global variables ($_GET, $_POST,
$_FILES, $_COOKIE, $_SESSION, ...) and the response is generated by some
functions (echo, header, setcookie, ...).

The Symfony HttpFoundation component replaces these default PHP global
variables and functions by an Object-Oriented layer.

Optional:
* Memcache (php-pecl-memcache)
* Memcached (php-pecl-memcached)
* Mongo (php-pecl-mongo)

# ------------------------------------------------------------------------------

%package   http-kernel

Summary:   Symfony HttpKernel Component
URL:       http://symfony.com/doc/2.3/components/http_kernel/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/debug)                =  %{version}
Requires:  php-composer(%{composer_vendor}/event-dispatcher)     =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)      =  %{version}
Requires:  php-composer(psr/log)                                 >= %{psrlog_min_ver}
Requires:  php-composer(psr/log)                                 <  %{psrlog_max_ver}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/browser-kit)          =  %{version}
Requires:  php-composer(%{composer_vendor}/class-loader)         =  %{version}
Requires:  php-composer(%{composer_vendor}/config)               =  %{version}
Requires:  php-composer(%{composer_vendor}/console)              =  %{version}
Requires:  php-composer(%{composer_vendor}/dependency-injection) =  %{version}
Requires:  php-composer(%{composer_vendor}/finder)               =  %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-hash
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-reflection
Requires:  php-spl
Requires:  php-sqlite3
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/http-kernel) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/HttpKernel) = %{version}
# Rename
Obsoletes: %{name}2-HttpKernel < %{version}
Provides:  %{name}2-HttpKernel = %{version}
Obsoletes: %{name}-httpkernel  < %{version}
Provides:  %{name}-httpkernel  = %{version}

Conflicts: %{name}-http-kernel >= 2.4.0

%description http-kernel
The HttpKernel Component provides a structured process for converting a Request
into a Response by making use of the event dispatcher. It's flexible enough to
create a full-stack framework (Symfony), a micro-framework (Silex) or an
advanced CMS system (Drupal).

Configuration reference:
http://symfony.com/doc/2.3/reference/configuration/kernel.html

Optional:
* Memcache (php-pecl-memcache)
* Memcached (php-pecl-memcached)
* Mongo (php-pecl-mongo)
* Redis (php-pecl-redis)
%if 0%{?rhel} >= 6
* Zend OPcache (php-pecl-zendopcache)
%else
* Zend OPcache (php-opcache)
%endif

# ------------------------------------------------------------------------------

%package   intl

Summary:   Symfony Intl Component
URL:       http://symfony.com/doc/2.3/components/intl.html

Requires:  %{name}-common = %{version}-%{release}
# composer.json: optional
Requires:  php-intl
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-date
Requires:  php-intl
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/intl) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Intl) = %{version}
# Rename
Obsoletes: %{name}2-Intl < %{version}
Provides:  %{name}2-Intl = %{version}

Conflicts: %{name}-intl >= 2.4.0

%description intl
A PHP replacement layer for the C intl extension [1] that also provides access
to the localization data of the ICU library [2].

[1] http://www.php.net/manual/en/book.intl.php
[2] http://site.icu-project.org/

# ------------------------------------------------------------------------------

%package   locale

Summary:   Symfony Locale Component

# composer.json
Requires:  php-composer(%{composer_vendor}/intl) = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-intl

# Composer
Provides:  php-composer(%{composer_vendor}/locale) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Locale) = %{version}
# Rename
Obsoletes: %{name}2-Locale < %{version}
Provides:  %{name}2-Locale = %{version}

Conflicts: %{name}-locale >= 2.4.0

%description locale
Locale provides fallback code to handle cases when the intl extension is
missing.

The Locale component is deprecated since version 2.3 and will be removed in
Symfony 3.0. You should use the more capable Intl component instead.

# ------------------------------------------------------------------------------

%package   options-resolver

Summary:   Symfony OptionsResolver Component
URL:       http://symfony.com/doc/2.3/components/options_resolver.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/options-resolver) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/OptionsResolver) = %{version}
# Rename
Obsoletes: %{name}2-OptionsResolver < %{version}
Provides:  %{name}2-OptionsResolver = %{version}
Obsoletes: %{name}-optionsresolver  < %{version}
Provides:  %{name}-optionsresolver  = %{version}

Conflicts: %{name}-options-resolver >= 2.4.0

%description options-resolver
The OptionsResolver Component helps you configure objects with option arrays.
It supports default values, option constraints and lazy options.

# ------------------------------------------------------------------------------

%package   process

Summary:   Symfony Process Component
URL:       http://symfony.com/doc/2.3/components/process.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-pcntl
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/process) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Process) = %{version}
# Rename
Obsoletes: %{name}2-Process < %{version}
Provides:  %{name}2-Process = %{version}

Conflicts: %{name}-process >= 2.4.0

%description process
The Process component executes commands in sub-processes.

# ------------------------------------------------------------------------------

%package   property-access

Summary:   Symfony PropertyAccess Component
URL:       http://symfony.com/doc/2.3/components/property_access/introduction.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/property-access) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/PropertyAccess) = %{version}
# Rename
Obsoletes: %{name}2-PropertyAccess < %{version}
Provides:  %{name}2-PropertyAccess = %{version}
Obsoletes: %{name}-propertyaccess  < %{version}
Provides:  %{name}-propertyaccess  = %{version}

Conflicts: %{name}-property-access >= 2.4.0

%description property-access
The PropertyAccess component provides function to read and write from/to an
object or array using a simple string notation.

# ------------------------------------------------------------------------------

%package   routing

Summary:   Symfony Routing Component
URL:       http://symfony.com/doc/2.3/components/routing/index.html

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config) =  %{version}
Requires:  php-composer(%{composer_vendor}/yaml)   =  %{version}
Requires:  php-composer(doctrine/common)           >= %{doctrine_common_min_ver}
Requires:  php-composer(doctrine/common)           <  %{doctrine_common_max_ver}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-dom
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# Composer
Provides:  php-composer(%{composer_vendor}/routing) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Routing) = %{version}
# Rename
Obsoletes: %{name}2-Routing < %{version}
Provides:  %{name}2-Routing = %{version}

Conflicts: %{name}-routing >= 2.4.0

%description routing
The Routing Component maps an HTTP request to a set of configuration variables.

# ------------------------------------------------------------------------------

%package   security

Summary:   Symfony Security Component
URL:       http://symfony.com/doc/2.3/components/security/index.html

# composer.json
Requires:  php-composer(%{composer_vendor}/event-dispatcher)    =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation)     =  %{version}
Requires:  php-composer(%{composer_vendor}/http-kernel)         =  %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/class-loader)        =  %{version}
Requires:  php-composer(%{composer_vendor}/finder)              =  %{version}
Requires:  php-composer(%{composer_vendor}/form)                =  %{version}
Requires:  php-composer(%{composer_vendor}/routing)             =  %{version}
Requires:  php-composer(%{composer_vendor}/validator)           =  %{version}
Requires:  php-composer(doctrine/dbal)                          >= %{doctrine_dbal_min_ver}
Requires:  php-composer(doctrine/dbal)                          <  %{doctrine_dbal_max_ver}
%if 0%{?el6}%{?el7}
Requires:  php-password-compat                                  >= %{password_compat_min_ver}
Requires:  php-password-compat                                  <  %{password_compat_max_ver}
%endif
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-date
Requires:  php-hash
Requires:  php-json
Requires:  php-openssl
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/security) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Security) = %{version}
# Rename
Obsoletes: %{name}2-Security < %{version}
Provides:  %{name}2-Security = %{version}

Conflicts: %{name}-security >= 2.4.0

%description security
The Security Component provides a complete security system for your web
application. It ships with facilities for authenticating using HTTP basic
or digest authentication, interactive form login or X.509 certificate login,
but also allows you to implement your own authentication strategies.
Furthermore, the component provides ways to authorize authenticated users
based on their roles, and it contains an advanced ACL system.

# ------------------------------------------------------------------------------

%package   serializer

Summary:   Symfony Serializer Component
URL:       http://symfony.com/doc/2.3/components/serializer.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
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
# PEAR
Provides:  php-pear(%{pear_channel}/Serializer) = %{version}
# Rename
Obsoletes: %{name}2-Serializer < %{version}
Provides:  %{name}2-Serializer = %{version}

Conflicts: %{name}-serializer >= 2.4.0

%description serializer
The Serializer Component is meant to be used to turn objects into a specific
format (XML, JSON, Yaml, ...) and the other way around.

# ------------------------------------------------------------------------------

%package  stopwatch

Summary:  Symfony Stopwatch Component
URL:      http://symfony.com/doc/2.3/components/stopwatch.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/stopwatch) = %{version}
# PEAR
Provides: php-pear(%{pear_channel}/Stopwatch) = %{version}

Conflicts: %{name}-stopwatch >= 2.4.0

%description stopwatch
Stopwatch component provides a way to profile code.

# ------------------------------------------------------------------------------

%package   templating

Summary:   Symfony Templating Component
URL:       http://symfony.com/doc/2.3/components/templating.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-iconv
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/templating) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Templating) = %{version}
# Rename
Obsoletes: %{name}2-Templating < %{version}
Provides:  %{name}2-Templating = %{version}

Conflicts: %{name}-templating >= 2.4.0

%description templating
Templating provides all the tools needed to build any kind of template system.

It provides an infrastructure to load template files and optionally monitor
them for changes. It also provides a concrete template engine implementation
using PHP with additional tools for escaping and separating templates into
blocks and layouts.

# ------------------------------------------------------------------------------

%package   translation

Summary:   Symfony Translation Component

# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config) = %{version}
Requires:  php-composer(%{composer_vendor}/yaml)   = %{version}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-dom
Requires:  php-iconv
Requires:  php-intl
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/translation) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Translation) = %{version}
# Rename
Obsoletes: %{name}2-Translation < %{version}
Provides:  %{name}2-Translation = %{version}

Conflicts: %{name}-translation >= 2.4.0

%description translation
Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

# ------------------------------------------------------------------------------

%package   validator

Summary:   Symfony Validator Component

# composer.json
Requires:  php-composer(%{composer_vendor}/translation)     =  %{version}
# composer.json: optional
Requires:  php-composer(%{composer_vendor}/config)          =  %{version}
Requires:  php-composer(%{composer_vendor}/http-foundation) =  %{version}
Requires:  php-composer(%{composer_vendor}/intl)            =  %{version}
Requires:  php-composer(%{composer_vendor}/yaml)            =  %{version}
Requires:  php-composer(doctrine/common)                    >= %{doctrine_common_min_ver}
Requires:  php-composer(doctrine/common)                    <  %{doctrine_common_max_ver}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-date
Requires:  php-filter
Requires:  php-intl
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/validator) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Validator) = %{version}
# Rename
Obsoletes: %{name}2-Validator < %{version}
Provides:  %{name}2-Validator = %{version}

Conflicts: %{name}-validator >= 2.4.0

%description validator
This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

Optional:
* APC (php-pecl-apcu)

# ------------------------------------------------------------------------------

%package   yaml

Summary:   Symfony Yaml Component
URL:       http://symfony.com/doc/2.3/components/yaml/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo (computed from version 2.3.25)
Requires:  php-ctype
Requires:  php-date
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/yaml) = %{version}
# PEAR
Provides:  php-pear(%{pear_channel}/Yaml) = %{version}
# Rename
Obsoletes: %{name}2-Yaml < %{version}
Provides:  %{name}2-Yaml = %{version}

Conflicts: %{name}-yaml >= 2.4.0

%description yaml
The YAML Component loads and dumps YAML files.

# ##############################################################################


%prep
%setup -qn %{github_name}-%{github_commit}

# Remove unnecessary files
find src -name '.git*' -delete
rm -rf src/Symfony/Bridge/{Propel1,ProxyManager}

# Add missing files for PEAR compatibility
cd src
tar -xf %{SOURCE3}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{symfony_dir}
cp -rp src/Symfony/* %{buildroot}%{symfony_dir}/

# Symlink main package docs to common sub-package docs
mkdir -p %{buildroot}%{_docdir}
%if 0%{?fedora} >= 20
ln -s %{name}-common %{buildroot}%{_docdir}/%{name}
%else
ln -s %{name}-common-%{version} %{buildroot}%{_docdir}/%{name}-%{version}
%endif


%check
%if %{with_tests}
# Create autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOADER'
<?php

if (!class_exists('Symfony\\Component\\ClassLoader\\UniversalClassLoader', false)) {
    require_once __DIR__.'/../src/Symfony/Component/ClassLoader/UniversalClassLoader.php';
}

use Symfony\Component\ClassLoader\UniversalClassLoader;

$loader = new UniversalClassLoader();
$loader->registerNamespace('Symfony', __DIR__.'/../src');
$loader->useIncludePath(true);
$loader->register();

if (version_compare(PHP_VERSION, '5.4.0', '<')) {
    require __DIR__ . '/../src/Symfony/Component/HttpFoundation/Resources/stubs/SessionHandlerInterface.php';
}

if (file_exists('%{phpdir}/password_compat/password.php')) {
    require '%{phpdir}/password_compat/password.php';
}

return $loader;
AUTOLOADER

# Hack PHPUnit Autoloader (use current symfony instead of system one)
if [ -d %{phpdir}/PHPUnit ]; then
  mkdir PHPUnit
  sed -e '/Symfony/s:\$vendorDir:"./src/":' \
      -e 's:path = dirname(__FILE__):path = "%{phpdir}/PHPUnit":' \
      %{phpdir}/PHPUnit/Autoload.php > PHPUnit/Autoload.php
fi

# Skip tests that rely on external resources
rm -f src/Symfony/Component/HttpFoundation/Tests/Session/Storage/Handler/MongoDbSessionHandlerTest.php
sed 's/function testNonSeekableStream/function SKIP_testNonSeekableStream/' \
    -i src/Symfony/Component/Finder/Tests/FinderTest.php
sed 's/function testCopyForOriginUrlsAndExistingLocalFileDefaultsToNotCopy/function SKIP_testCopyForOriginUrlsAndExistingLocalFileDefaultsToNotCopy/' \
    -i src/Symfony/Component/Filesystem/Tests/FilesystemTest.php

# Skip tests that have intermittent failures
sed 's/function testCheckTimeoutOnStartedProcess/function SKIP_testCheckTimeoutOnStartedProcess/' \
    -i src/Symfony/Component/Process/Tests/AbstractProcessTest.php \
    -i src/Symfony/Component/Process/Tests/SigchildDisabledProcessTest.php

# Temporarily skip tests that are known to fail
sed 's/function testTTYCommand/function SKIP_testTTYCommand/' \
    -i src/Symfony/Component/Process/Tests/AbstractProcessTest.php
sed 's/function testTTYCommandExitCode/function SKIP_testTTYCommandExitCode/' \
    -i src/Symfony/Component/Process/Tests/SigchildDisabledProcessTest.php
sed 's/function testStrict/function SKIP_testStrict/' \
    -i src/Symfony/Component/Validator/Tests/Constraints/EmailValidatorTest.php
%if 0%{?el6}
sed 's/function testForm/function SKIP_testForm/' \
    -i src/Symfony/Component/DomCrawler/Tests/CrawlerTest.php
sed -e 's/function testConstructorHandlesFormAttribute/function SKIP_testConstructorHandlesFormAttribute/' \
    -e 's/function testConstructorHandlesFormValues/function SKIP_testConstructorHandlesFormValues/' \
    -i src/Symfony/Component/DomCrawler/Tests/FormTest.php
rm -f src/Symfony/Component/HttpFoundation/Tests/Session/Storage/Handler/NativeFileSessionHandlerTest.php
%endif

# Run tests
RET=0
for PKG in src/Symfony/*/*; do
    echo -e "\n>>>>>>>>>>>>>>>>>>>>>>> ${PKG}\n"
    %{__phpunit} \
        --include-path ./src \
        --exclude-group tty,benchmark \
        $PKG || RET=1
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

%doc *.md
%doc composer.json
%license LICENSE

%dir %{symfony_dir}
%dir %{symfony_dir}/Bridge
%dir %{symfony_dir}/Bundle
%dir %{symfony_dir}/Component

# ------------------------------------------------------------------------------

%files doctrine-bridge

%license src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/*.md
%doc src/Symfony/Bridge/Doctrine/composer.json

%{symfony_dir}/Bridge/Doctrine
%exclude %{symfony_dir}/Bridge/Doctrine/LICENSE
%exclude %{symfony_dir}/Bridge/Doctrine/*.md
%exclude %{symfony_dir}/Bridge/Doctrine/composer.json
%exclude %{symfony_dir}/Bridge/Doctrine/phpunit.*
%exclude %{symfony_dir}/Bridge/Doctrine/Tests

# ------------------------------------------------------------------------------

%files monolog-bridge

%license src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/*.md
%doc src/Symfony/Bridge/Monolog/composer.json

%{symfony_dir}/Bridge/Monolog
%exclude %{symfony_dir}/Bridge/Monolog/LICENSE
%exclude %{symfony_dir}/Bridge/Monolog/*.md
%exclude %{symfony_dir}/Bridge/Monolog/composer.json
%exclude %{symfony_dir}/Bridge/Monolog/phpunit.*
%exclude %{symfony_dir}/Bridge/Monolog/Tests

# ------------------------------------------------------------------------------

#%%files propel1-bridge

#%%license src/Symfony/Bridge/Propel1/LICENSE
#%%doc src/Symfony/Bridge/Propel1/*.md
#%%doc src/Symfony/Bridge/Propel1/composer.json

# %%{symfony_dir}/Bridge/Propel1
#%%exclude %%{symfony_dir}/Bridge/Propel1/LICENSE
#%%exclude %%{symfony_dir}/Bridge/Propel1/*.md
#%%exclude %%{symfony_dir}/Bridge/Propel1/composer.json
#%%exclude %%{symfony_dir}/Bridge/Propel1/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/Propel1/Tests

# ------------------------------------------------------------------------------

#%%files proxy-manager-bridge

#%%license src/Symfony/Bridge/ProxyManager/LICENSE
#%%doc src/Symfony/Bridge/ProxyManager/*.md
#%%doc src/Symfony/Bridge/ProxyManager/composer.json

# %%{symfony_dir}/Bridge/ProxyManager
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/LICENSE
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/*.md
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/composer.json
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/Tests

# ------------------------------------------------------------------------------

%files swiftmailer-bridge

%license src/Symfony/Bridge/Swiftmailer/LICENSE
%doc src/Symfony/Bridge/Swiftmailer/*.md
%doc src/Symfony/Bridge/Swiftmailer/composer.json

%{symfony_dir}/Bridge/Swiftmailer
%exclude %{symfony_dir}/Bridge/Swiftmailer/LICENSE
%exclude %{symfony_dir}/Bridge/Swiftmailer/*.md
%exclude %{symfony_dir}/Bridge/Swiftmailer/composer.json
#%%exclude %%{symfony_dir}/Bridge/Swiftmailer/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/Swiftmailer/Tests

# ------------------------------------------------------------------------------

%files twig-bridge

%license src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/*.md
%doc src/Symfony/Bridge/Twig/composer.json

%{symfony_dir}/Bridge/Twig
%exclude %{symfony_dir}/Bridge/Twig/LICENSE
%exclude %{symfony_dir}/Bridge/Twig/*.md
%exclude %{symfony_dir}/Bridge/Twig/composer.json
%exclude %{symfony_dir}/Bridge/Twig/phpunit.*
%exclude %{symfony_dir}/Bridge/Twig/Tests

# ------------------------------------------------------------------------------

%files framework-bundle

%doc src/Symfony/Bundle/FrameworkBundle/*.md
%doc src/Symfony/Bundle/FrameworkBundle/composer.json
%license src/Symfony/Bundle/FrameworkBundle/Resources/meta/LICENSE

%{symfony_dir}/Bundle/FrameworkBundle
%exclude %{symfony_dir}/Bundle/FrameworkBundle/*.md
%exclude %{symfony_dir}/Bundle/FrameworkBundle/composer.json
%exclude %{symfony_dir}/Bundle/FrameworkBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/FrameworkBundle/Tests
%exclude %{symfony_dir}/Bundle/FrameworkBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files security-bundle

%doc src/Symfony/Bundle/SecurityBundle/*.md
%doc src/Symfony/Bundle/SecurityBundle/composer.json
%license src/Symfony/Bundle/SecurityBundle/Resources/meta/LICENSE

%{symfony_dir}/Bundle/SecurityBundle
%exclude %{symfony_dir}/Bundle/SecurityBundle/*.md
%exclude %{symfony_dir}/Bundle/SecurityBundle/composer.json
%exclude %{symfony_dir}/Bundle/SecurityBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/SecurityBundle/Tests
%exclude %{symfony_dir}/Bundle/SecurityBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files twig-bundle

%doc src/Symfony/Bundle/TwigBundle/*.md
%doc src/Symfony/Bundle/TwigBundle/composer.json
%license src/Symfony/Bundle/TwigBundle/Resources/meta/LICENSE

%{symfony_dir}/Bundle/TwigBundle
%exclude %{symfony_dir}/Bundle/TwigBundle/*.md
%exclude %{symfony_dir}/Bundle/TwigBundle/composer.json
%exclude %{symfony_dir}/Bundle/TwigBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/TwigBundle/Tests
%exclude %{symfony_dir}/Bundle/TwigBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files web-profiler-bundle

%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%doc src/Symfony/Bundle/WebProfilerBundle/composer.json
%license src/Symfony/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%license src/Symfony/Bundle/WebProfilerBundle/Resources/meta/LICENSE

%{symfony_dir}/Bundle/WebProfilerBundle
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/*.md
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/composer.json
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Tests
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Resources/meta/LICENSE

# ------------------------------------------------------------------------------

%files browser-kit

%license src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/*.md
%doc src/Symfony/Component/BrowserKit/composer.json

%{symfony_dir}/Component/BrowserKit
%exclude %{symfony_dir}/Component/BrowserKit/LICENSE
%exclude %{symfony_dir}/Component/BrowserKit/*.md
%exclude %{symfony_dir}/Component/BrowserKit/composer.json
%exclude %{symfony_dir}/Component/BrowserKit/phpunit.*
%exclude %{symfony_dir}/Component/BrowserKit/Tests

# ------------------------------------------------------------------------------

%files class-loader

%license src/Symfony/Component/ClassLoader/LICENSE
%doc src/Symfony/Component/ClassLoader/*.md
%doc src/Symfony/Component/ClassLoader/composer.json

%{symfony_dir}/Component/ClassLoader
%exclude %{symfony_dir}/Component/ClassLoader/LICENSE
%exclude %{symfony_dir}/Component/ClassLoader/*.md
%exclude %{symfony_dir}/Component/ClassLoader/composer.json
%exclude %{symfony_dir}/Component/ClassLoader/phpunit.*
%exclude %{symfony_dir}/Component/ClassLoader/Tests

# ------------------------------------------------------------------------------

%files config

%license src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/*.md
%doc src/Symfony/Component/Config/composer.json

%{symfony_dir}/Component/Config
%exclude %{symfony_dir}/Component/Config/LICENSE
%exclude %{symfony_dir}/Component/Config/*.md
%exclude %{symfony_dir}/Component/Config/composer.json
%exclude %{symfony_dir}/Component/Config/phpunit.*
%exclude %{symfony_dir}/Component/Config/Tests

# ------------------------------------------------------------------------------

%files console

%license src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/*.md
%doc src/Symfony/Component/Console/composer.json

%{symfony_dir}/Component/Console
%exclude %{symfony_dir}/Component/Console/LICENSE
%exclude %{symfony_dir}/Component/Console/*.md
%exclude %{symfony_dir}/Component/Console/composer.json
%exclude %{symfony_dir}/Component/Console/phpunit.*
%exclude %{symfony_dir}/Component/Console/Tests

# ------------------------------------------------------------------------------

%files css-selector

%license src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/*.md
%doc src/Symfony/Component/CssSelector/composer.json

%{symfony_dir}/Component/CssSelector
%exclude %{symfony_dir}/Component/CssSelector/LICENSE
%exclude %{symfony_dir}/Component/CssSelector/*.md
%exclude %{symfony_dir}/Component/CssSelector/composer.json
%exclude %{symfony_dir}/Component/CssSelector/phpunit.*
%exclude %{symfony_dir}/Component/CssSelector/Tests

# ------------------------------------------------------------------------------

%files debug

%license src/Symfony/Component/Debug/LICENSE
%doc src/Symfony/Component/Debug/*.md
%doc src/Symfony/Component/Debug/composer.json

%{symfony_dir}/Component/Debug
%exclude %{symfony_dir}/Component/Debug/LICENSE
%exclude %{symfony_dir}/Component/Debug/*.md
%exclude %{symfony_dir}/Component/Debug/composer.json
%exclude %{symfony_dir}/Component/Debug/phpunit.*
%exclude %{symfony_dir}/Component/Debug/Tests

# ------------------------------------------------------------------------------

%files dependency-injection

%license src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/*.md
%doc src/Symfony/Component/DependencyInjection/composer.json

%{symfony_dir}/Component/DependencyInjection
%exclude %{symfony_dir}/Component/DependencyInjection/LICENSE
%exclude %{symfony_dir}/Component/DependencyInjection/*.md
%exclude %{symfony_dir}/Component/DependencyInjection/composer.json
%exclude %{symfony_dir}/Component/DependencyInjection/phpunit.*
%exclude %{symfony_dir}/Component/DependencyInjection/Tests

# ------------------------------------------------------------------------------

%files dom-crawler

%license src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/*.md
%doc src/Symfony/Component/DomCrawler/composer.json

%{symfony_dir}/Component/DomCrawler
%exclude %{symfony_dir}/Component/DomCrawler/LICENSE
%exclude %{symfony_dir}/Component/DomCrawler/*.md
%exclude %{symfony_dir}/Component/DomCrawler/composer.json
%exclude %{symfony_dir}/Component/DomCrawler/phpunit.*
%exclude %{symfony_dir}/Component/DomCrawler/Tests

# ------------------------------------------------------------------------------

%files event-dispatcher

%license src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/*.md
%doc src/Symfony/Component/EventDispatcher/composer.json

%{symfony_dir}/Component/EventDispatcher
%exclude %{symfony_dir}/Component/EventDispatcher/LICENSE
%exclude %{symfony_dir}/Component/EventDispatcher/*.md
%exclude %{symfony_dir}/Component/EventDispatcher/composer.json
%exclude %{symfony_dir}/Component/EventDispatcher/phpunit.*
%exclude %{symfony_dir}/Component/EventDispatcher/Tests

# ------------------------------------------------------------------------------

%files filesystem

%license src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/*.md
%doc src/Symfony/Component/Filesystem/composer.json

%{symfony_dir}/Component/Filesystem
%exclude %{symfony_dir}/Component/Filesystem/LICENSE
%exclude %{symfony_dir}/Component/Filesystem/*.md
%exclude %{symfony_dir}/Component/Filesystem/composer.json
%exclude %{symfony_dir}/Component/Filesystem/phpunit.*
%exclude %{symfony_dir}/Component/Filesystem/Tests

# ------------------------------------------------------------------------------

%files finder

%license src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/*.md
%doc src/Symfony/Component/Finder/composer.json

%{symfony_dir}/Component/Finder
%exclude %{symfony_dir}/Component/Finder/LICENSE
%exclude %{symfony_dir}/Component/Finder/*.md
%exclude %{symfony_dir}/Component/Finder/composer.json
%exclude %{symfony_dir}/Component/Finder/phpunit.*
%exclude %{symfony_dir}/Component/Finder/Tests

# ------------------------------------------------------------------------------

%files form

%license src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/*.md
%doc src/Symfony/Component/Form/composer.json

%{symfony_dir}/Component/Form
%exclude %{symfony_dir}/Component/Form/LICENSE
%exclude %{symfony_dir}/Component/Form/*.md
%exclude %{symfony_dir}/Component/Form/composer.json
%exclude %{symfony_dir}/Component/Form/phpunit.*
%exclude %{symfony_dir}/Component/Form/Tests

# ------------------------------------------------------------------------------

%files http-foundation

%license src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/*.md
%doc src/Symfony/Component/HttpFoundation/composer.json

%{symfony_dir}/Component/HttpFoundation
%exclude %{symfony_dir}/Component/HttpFoundation/LICENSE
%exclude %{symfony_dir}/Component/HttpFoundation/*.md
%exclude %{symfony_dir}/Component/HttpFoundation/composer.json
%exclude %{symfony_dir}/Component/HttpFoundation/phpunit.*
%exclude %{symfony_dir}/Component/HttpFoundation/Tests

# ------------------------------------------------------------------------------

%files http-kernel

%license src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/*.md
%doc src/Symfony/Component/HttpKernel/composer.json

%{symfony_dir}/Component/HttpKernel
%exclude %{symfony_dir}/Component/HttpKernel/LICENSE
%exclude %{symfony_dir}/Component/HttpKernel/*.md
%exclude %{symfony_dir}/Component/HttpKernel/composer.json
%exclude %{symfony_dir}/Component/HttpKernel/phpunit.*
%exclude %{symfony_dir}/Component/HttpKernel/Tests

# ------------------------------------------------------------------------------

%files intl

%license src/Symfony/Component/Intl/LICENSE
%doc src/Symfony/Component/Intl/*.md
%doc src/Symfony/Component/Intl/composer.json

%{symfony_dir}/Component/Intl
%exclude %{symfony_dir}/Component/Intl/LICENSE
%exclude %{symfony_dir}/Component/Intl/*.md
%exclude %{symfony_dir}/Component/Intl/composer.json
%exclude %{symfony_dir}/Component/Intl/phpunit.*
%exclude %{symfony_dir}/Component/Intl/Tests

# ------------------------------------------------------------------------------

%files locale

%license src/Symfony/Component/Locale/LICENSE
%doc src/Symfony/Component/Locale/*.md
%doc src/Symfony/Component/Locale/composer.json

%{symfony_dir}/Component/Locale
%exclude %{symfony_dir}/Component/Locale/LICENSE
%exclude %{symfony_dir}/Component/Locale/*.md
%exclude %{symfony_dir}/Component/Locale/composer.json
%exclude %{symfony_dir}/Component/Locale/phpunit.*
%exclude %{symfony_dir}/Component/Locale/Tests

# ------------------------------------------------------------------------------

%files options-resolver

%license src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/*.md
%doc src/Symfony/Component/OptionsResolver/composer.json

%{symfony_dir}/Component/OptionsResolver
%exclude %{symfony_dir}/Component/OptionsResolver/LICENSE
%exclude %{symfony_dir}/Component/OptionsResolver/*.md
%exclude %{symfony_dir}/Component/OptionsResolver/composer.json
%exclude %{symfony_dir}/Component/OptionsResolver/phpunit.*
%exclude %{symfony_dir}/Component/OptionsResolver/Tests

# ------------------------------------------------------------------------------

%files process

%license src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/*.md
%doc src/Symfony/Component/Process/composer.json

%{symfony_dir}/Component/Process
%exclude %{symfony_dir}/Component/Process/LICENSE
%exclude %{symfony_dir}/Component/Process/*.md
%exclude %{symfony_dir}/Component/Process/composer.json
%exclude %{symfony_dir}/Component/Process/phpunit.*
%exclude %{symfony_dir}/Component/Process/Tests

# ------------------------------------------------------------------------------

%files property-access

%license src/Symfony/Component/PropertyAccess/LICENSE
%doc src/Symfony/Component/PropertyAccess/*.md
%doc src/Symfony/Component/PropertyAccess/composer.json

%{symfony_dir}/Component/PropertyAccess
%exclude %{symfony_dir}/Component/PropertyAccess/LICENSE
%exclude %{symfony_dir}/Component/PropertyAccess/*.md
%exclude %{symfony_dir}/Component/PropertyAccess/composer.json
%exclude %{symfony_dir}/Component/PropertyAccess/phpunit.*
%exclude %{symfony_dir}/Component/PropertyAccess/Tests

# ------------------------------------------------------------------------------

%files routing

%license src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/*.md
%doc src/Symfony/Component/Routing/composer.json

%{symfony_dir}/Component/Routing
%exclude %{symfony_dir}/Component/Routing/LICENSE
%exclude %{symfony_dir}/Component/Routing/*.md
%exclude %{symfony_dir}/Component/Routing/composer.json
%exclude %{symfony_dir}/Component/Routing/phpunit.*
%exclude %{symfony_dir}/Component/Routing/Tests

# ------------------------------------------------------------------------------

%files security

%license src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/*.md
%doc src/Symfony/Component/Security/composer.json

%{symfony_dir}/Component/Security
%exclude %{symfony_dir}/Component/Security/LICENSE
%exclude %{symfony_dir}/Component/Security/*.md
%exclude %{symfony_dir}/Component/Security/composer.json
%exclude %{symfony_dir}/Component/Security/phpunit.*
%exclude %{symfony_dir}/Component/Security/Tests

# ------------------------------------------------------------------------------

%files serializer

%license src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/*.md
%doc src/Symfony/Component/Serializer/composer.json

%{symfony_dir}/Component/Serializer
%exclude %{symfony_dir}/Component/Serializer/LICENSE
%exclude %{symfony_dir}/Component/Serializer/*.md
%exclude %{symfony_dir}/Component/Serializer/composer.json
%exclude %{symfony_dir}/Component/Serializer/phpunit.*
%exclude %{symfony_dir}/Component/Serializer/Tests

# ------------------------------------------------------------------------------

%files stopwatch

%license src/Symfony/Component/Stopwatch/LICENSE
%doc src/Symfony/Component/Stopwatch/*.md
%doc src/Symfony/Component/Stopwatch/composer.json

%{symfony_dir}/Component/Stopwatch
%exclude %{symfony_dir}/Component/Stopwatch/LICENSE
%exclude %{symfony_dir}/Component/Stopwatch/*.md
%exclude %{symfony_dir}/Component/Stopwatch/composer.json
%exclude %{symfony_dir}/Component/Stopwatch/phpunit.*
%exclude %{symfony_dir}/Component/Stopwatch/Tests

# ------------------------------------------------------------------------------

%files templating

%license src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/*.md
%doc src/Symfony/Component/Templating/composer.json

%{symfony_dir}/Component/Templating
%exclude %{symfony_dir}/Component/Templating/LICENSE
%exclude %{symfony_dir}/Component/Templating/*.md
%exclude %{symfony_dir}/Component/Templating/composer.json
%exclude %{symfony_dir}/Component/Templating/phpunit.*
%exclude %{symfony_dir}/Component/Templating/Tests

# ------------------------------------------------------------------------------

%files translation

%license src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/*.md
%doc src/Symfony/Component/Translation/composer.json

%{symfony_dir}/Component/Translation
%exclude %{symfony_dir}/Component/Translation/LICENSE
%exclude %{symfony_dir}/Component/Translation/*.md
%exclude %{symfony_dir}/Component/Translation/composer.json
%exclude %{symfony_dir}/Component/Translation/phpunit.*
%exclude %{symfony_dir}/Component/Translation/Tests

# ------------------------------------------------------------------------------

%files validator

%license src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/*.md
%doc src/Symfony/Component/Validator/composer.json

%{symfony_dir}/Component/Validator
%exclude %{symfony_dir}/Component/Validator/LICENSE
%exclude %{symfony_dir}/Component/Validator/*.md
%exclude %{symfony_dir}/Component/Validator/composer.json
%exclude %{symfony_dir}/Component/Validator/phpunit.*
%exclude %{symfony_dir}/Component/Validator/Tests

# ------------------------------------------------------------------------------

%files yaml

%license src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/*.md
%doc src/Symfony/Component/Yaml/composer.json

%{symfony_dir}/Component/Yaml
%exclude %{symfony_dir}/Component/Yaml/LICENSE
%exclude %{symfony_dir}/Component/Yaml/*.md
%exclude %{symfony_dir}/Component/Yaml/composer.json
%exclude %{symfony_dir}/Component/Yaml/phpunit.*
%exclude %{symfony_dir}/Component/Yaml/Tests

# ##############################################################################

%changelog
* Sat Feb 21 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.25-1
- Updated to 2.3.25

* Sun Jan 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.23-1
- Updated to 2.3.23

* Mon Jan 13 2014 Remi Collet <remi@fedoraproject.org> - 2.3.9-0
- EPEL-7 bootstrap build

* Sun Jan 05 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.9-1
- Updated to 2.3.9 (BZ #1038134)
- Conditional %%{?dist}
- Minor bash cosmetic changes
- Skip additional test relying on external resources
- Skip additional el6 test

* Wed Dec 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.8-1
- Updated to 2.3.8 (BZ #1038134)
- Temporarily skip test known to fail on Fedora > 20

* Sat Dec 14 2013 Remi Collet <remi@fedoraproject.org> - 2.3.7-4
- fix PEAR compatibility: add missing "autoloader.php"

* Tue Nov 26 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.7-3
- Fixed several summaries and descriptions ("Symfony2" => "Symfony")

* Fri Nov 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.7-2
- Renamed from "php-symfony2" to "php-symfony"
- Updated main pkg summary
- Removed dependency on common sub-pkg for sub-pkgs that require other sub-pkgs
- Common sub-pkg obsoletes php-channel-symfony2
- Fixed swiftmailerbridge sub-pkg dependency
- Updated %%check to use PHPUnit's "--include-path" option

* Sun Nov 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.7-1
- Updated to 2.3.7
- Separated icu pkg
- Added php-password-compat requires for el6 (PHP < 5.5.0)
- common sub-pkg now owns %%{symfony_dir}/{Bridge,Bundle,Component}
- Fixed classloader URL

* Wed Nov 06 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.6-2
- Updated tests' autoloader
- Individual pkg tests instead of one
- Skip specific tests
- Exclude tty and benchmark test groups
- Fix main package doc symlink

* Mon Oct 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.6-1
- Updated to 2.3.6
- Renamed sub-packages to lowercase

* Sat Jul 13 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3.1-1
- Initial package