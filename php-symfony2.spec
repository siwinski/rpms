%global github_owner            symfony
%global github_name             symfony
%global github_version          2.3.1
%global github_commit           0902c606b4df1161f5b786ae89f37b71380b1f23

%global icu_github_owner        symfony
%global icu_github_name         Icu
%global icu_github_version      1.2.0
%global icu_github_commit       7299cd3d8d6602103d1ebff5d0a9917b7bc6de72

%global php_min_ver             5.3.3
%global doctrine_common_min_ver 2.2
%global doctrine_common_max_ver 3.0
%global doctrine_dbal_min_ver   2.2
%global doctrine_dbal_max_ver   3.0
%global doctrine_orm_min_ver    2.2.3
%global doctrine_orm_max_ver    3.0
%global monolog_min_ver         1.3
%global monolog_max_ver         2.0
%global psrlog_min_ver          1.0
%global psrlog_max_ver          2.0
%global swift_min_ver           4.2.0
%global swift_max_ver           5.1.0
%global twig_min_ver            1.11
%global twig_max_ver            2.0

%global symfony_dir             %{_datadir}/php/Symfony
%global pear_channel            pear.symfony.com

Name:          php-symfony2
Version:       %{github_version}
Release:       1%{dist}
Summary:       PHP full-stack web framework

Group:         Development/Libraries
License:       MIT
URL:           http://symfony.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       https://github.com/%{icu_github_owner}/%{icu_github_name}/archive/%{icu_github_commit}/%{name}-Icu-%{icu_github_version}-%{icu_github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-Monolog   >= %{monolog_min_ver}
BuildRequires: php-Monolog   <  %{monolog_max_ver}
BuildRequires: php-PsrLog    >= %{psrlog_min_ver}
BuildRequires: php-PsrLog    <  %{psrlog_max_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineCommon) >= %{doctrine_common_min_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineCommon) <  %{doctrine_common_max_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineDBAL)   >= %{doctrine_dbal_min_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineDBAL)   <  %{doctrine_dbal_max_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineORM)    >= %{doctrine_orm_min_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineORM)    <  %{doctrine_orm_max_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig)               >= %{twig_min_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig)               <  %{twig_max_ver}
## TODO: "doctrine/data-fixtures": "1.0.*"
## TODO: "propel/propel1": "1.6.*"
## TODO: "ircmaxell/password-compat": "1.0.*"
## TODO: "ocramius/proxy-manager": ">=0.3.1,<0.4-dev"
# For tests: phpcompatinfo
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

Requires:      %{name}-common              = %{version}-%{release}
# Bridges
Requires:      %{name}-doctrinebridge      = %{version}-%{release}
Requires:      %{name}-monologbridge       = %{version}-%{release}
#Requires:      %%{name}-propel1bridge       = %%{version}-%%{release}
#Requires:      %%{name}-proxymanagerbridge  = %%{version}-%%{release}
Requires:      %{name}-swiftmailerbridge   = %{version}-%{release}
Requires:      %{name}-twigbridge          = %{version}-%{release}
# Bundles
Requires:      %{name}-frameworkbundle     = %{version}-%{release}
Requires:      %{name}-securitybundle      = %{version}-%{release}
Requires:      %{name}-twigbundle          = %{version}-%{release}
Requires:      %{name}-webprofilerbundle   = %{version}-%{release}
# Components
Requires:      %{name}-browserkit          = %{version}-%{release}
Requires:      %{name}-classloader         = %{version}-%{release}
Requires:      %{name}-config              = %{version}-%{release}
Requires:      %{name}-console             = %{version}-%{release}
Requires:      %{name}-cssselector         = %{version}-%{release}
Requires:      %{name}-debug               = %{version}-%{release}
Requires:      %{name}-dependencyinjection = %{version}-%{release}
Requires:      %{name}-domcrawler          = %{version}-%{release}
Requires:      %{name}-eventdispatcher     = %{version}-%{release}
Requires:      %{name}-filesystem          = %{version}-%{release}
Requires:      %{name}-finder              = %{version}-%{release}
Requires:      %{name}-form                = %{version}-%{release}
Requires:      %{name}-httpfoundation      = %{version}-%{release}
Requires:      %{name}-httpkernel          = %{version}-%{release}
Requires:      %{name}-icu                 = %{icu_github_version}-%{release}
Requires:      %{name}-intl                = %{version}-%{release}
Requires:      %{name}-locale              = %{version}-%{release}
Requires:      %{name}-optionsresolver     = %{version}-%{release}
Requires:      %{name}-process             = %{version}-%{release}
Requires:      %{name}-propertyaccess      = %{version}-%{release}
Requires:      %{name}-routing             = %{version}-%{release}
Requires:      %{name}-security            = %{version}-%{release}
Requires:      %{name}-serializer          = %{version}-%{release}
Requires:      %{name}-stopwatch           = %{version}-%{release}
Requires:      %{name}-templating          = %{version}-%{release}
Requires:      %{name}-translation         = %{version}-%{release}
Requires:      %{name}-validator           = %{version}-%{release}
Requires:      %{name}-yaml                = %{version}-%{release}

%description
%{summary}

# ##############################################################################

%package       common

Summary:       Symfony2 common files

Requires:      php(language) >= %{php_min_ver}

%description common
%{summary}

# ------------------------------------------------------------------------------

%package   doctrinebridge

Summary:   Symfony2 Doctrine Bridge

Requires:  %{name}-common    = %{version}-%{release}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) >= %{doctrine_common_min_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) <  %{doctrine_common_max_ver}
# Optional
Requires:  %{name}-form      = %{version}-%{release}
Requires:  %{name}-validator = %{version}-%{release}
Requires:  php-pear(pear.doctrine-project.org/DoctrineDBAL)   >= %{doctrine_dbal_min_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineDBAL)   <  %{doctrine_dbal_max_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineORM)    >= %{doctrine_orm_min_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineORM)    <  %{doctrine_orm_max_ver}
# phpcompatinfo
Requires:  php-date
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/DoctrineBridge) = %{version}

%description doctrinebridge
Provides integration for Doctrine (http://www.doctrine-project.org/) with
various Symfony2 components.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/doctrine.html

# ------------------------------------------------------------------------------

%package   monologbridge

Summary:   Symfony2 Monolog Bridge

Requires:  %{name}-common     =  %{version}-%{release}
Requires:  %{name}-httpkernel =  %{version}-%{release}
Requires:  php-Monolog        >= %{monolog_min_ver}
Requires:  php-Monolog        <  %{monolog_max_ver}
# phpcompatinfo
Requires:  php-pcre

# PEAR
Provides:  php-pear(%{pear_channel}/MonologBridge) = %{version}

%description monologbridge
Provides integration for Monolog (https://github.com/Seldaek/monolog) with
various Symfony2 components.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/monolog.html

# ------------------------------------------------------------------------------

#%%package   propel1bridge

#Summary:   Symfony2 Propel 1 Bridge

#Requires:  %%{name}-common         = %%{version}-%%{release}
#Requires:  %%{name}-httpfoundation = %%{version}-%%{release}
#Requires:  %%{name}-httpkernel     = %%{version}-%%{release}
#Requires:  %%{name}-form           = %%{version}-%%{release}
## propel/propel1 1.6.*

#%%description propel1bridge
#Provides integration for Propel 1 (http://propelorm.org/) with various
#Symfony2 components.

# ------------------------------------------------------------------------------

#%%package   proxymanagerbridge

#Summary:   Symfony2 ProxyManager Bridge

#Requires:  %%{name}-common              = %%{version}-%%{release}
#Requires:  %%{name}-dependencyinjection = %%{version}-%%{release}
## ocramius/proxy-manager >=0.3.1,<0.4-dev
## phpcompatinfo
#Requires:  php-reflection
#Requires:  php-spl

#%%description proxymanagerbridge
#Provides integration for ProxyManager (https://github.com/Ocramius/ProxyManager)
#with various Symfony2 components.

# ------------------------------------------------------------------------------

%package   swiftmailerbridge

Summary:   Symfony2 Swiftmailer Bridge

Requires:  %{name}-common = %{version}-%{release}
Requires:  php-pear(pear.swiftmailer.org/Swift) >= %{swift_min_ver}
Requires:  php-pear(pear.swiftmailer.org/Swift) >  %{swift_max_ver}
# Optional
Requires:  %{name}-httpkernel = %{version}-%{release}

%description swiftmailerbridge
Provides integration for Swift Mailer (http://swiftmailer.org/) with various
Symfony2 components.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/swiftmailer.html

# ------------------------------------------------------------------------------

%package   twigbridge

Summary:   Symfony2 Twig Bridge

Requires:  %{name}-common = %{version}-%{release}
Requires:  php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
Requires:  php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
# Optional
Requires:  %{name}-form        = %{version}-%{release}
Requires:  %{name}-httpkernel  = %{version}-%{release}
Requires:  %{name}-routing     = %{version}-%{release}
Requires:  %{name}-security    = %{version}-%{release}
Requires:  %{name}-templating  = %{version}-%{release}
Requires:  %{name}-translation = %{version}-%{release}
Requires:  %{name}-yaml        = %{version}-%{release}
# phpcompatinfo
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/TwigBridge) = %{version}

%description twigbridge
Provides integration for Twig (http://twig.sensiolabs.org/) with various
Symfony2 components.

# ------------------------------------------------------------------------------

%package   frameworkbundle

Summary:   Symfony2 Framework Bundle

Requires:  %{name}-common              = %{version}-%{release}
Requires:  %{name}-config              = %{version}-%{release}
Requires:  %{name}-dependencyinjection = %{version}-%{release}
Requires:  %{name}-eventdispatcher     = %{version}-%{release}
Requires:  %{name}-filesystem          = %{version}-%{release}
Requires:  %{name}-httpkernel          = %{version}-%{release}
Requires:  %{name}-routing             = %{version}-%{release}
Requires:  %{name}-stopwatch           = %{version}-%{release}
Requires:  %{name}-templating          = %{version}-%{release}
Requires:  %{name}-translation         = %{version}-%{release}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) >= %{doctrine_common_min_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) <  %{doctrine_common_max_ver}
# Optional
Requires:  %{name}-console             = %{version}-%{release}
Requires:  %{name}-finder              = %{version}-%{release}
Requires:  %{name}-form                = %{version}-%{release}
Requires:  %{name}-validator           = %{version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-fileinfo
Requires:  php-filter
Requires:  php-json
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-spl
Requires:  php-tokenizer

%description frameworkbundle
The FrameworkBundle contains most of the "base" framework functionality and can
be configured under the framework key in your application configuration. This
includes settings related to sessions, translation, forms, validation, routing
and more.

Configuration reference:
http://symfony.com/doc/current/reference/configuration/framework.html

# ------------------------------------------------------------------------------

%package   securitybundle

Summary:   Symfony2 Security Bundle

Requires:  %{name}-common     = %{version}-%{release}
Requires:  %{name}-httpkernel = %{version}-%{release}
Requires:  %{name}-security   = %{version}-%{release}
# phpcompatinfo
Requires:  php-pcre
Requires:  php-spl

%description securitybundle
%{summary}

# ------------------------------------------------------------------------------

%package   twigbundle

Summary:   Symfony2 Twig Bundle

Requires:  %{name}-common     = %{version}-%{release}
Requires:  %{name}-httpkernel = %{version}-%{release}
Requires:  %{name}-twigbridge = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-reflection
Requires:  php-spl

%description twigbundle
%{summary}

Configuration reference:
http://symfony.com/doc/current/reference/configuration/twig.html

# ------------------------------------------------------------------------------

%package   webprofilerbundle

Summary:   Symfony2 WebProfiler Bundle

Requires:  %{name}-common     = %{version}-%{release}
Requires:  %{name}-httpkernel = %{version}-%{release}
Requires:  %{name}-routing    = %{version}-%{release}
Requires:  %{name}-twigbridge = %{version}-%{release}
# phpcompatinfo
Requires:  php-pcre
Requires:  php-spl

%description webprofilerbundle
%{summary}

Configuration reference:
http://symfony.com/doc/current/reference/configuration/web_profiler.html

# ------------------------------------------------------------------------------

%package   browserkit

Summary:   Symfony2 BrowserKit Component

Requires:  %{name}-common     = %{version}-%{release}
Requires:  %{name}-domcrawler = %{version}-%{release}
# Optional
Requires:  %{name}-process    = %{version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/BrowserKit) = %{version}
# Rename
Obsoletes: %{name}-BrowserKit < %{version}
Provides:  %{name}-BrowserKit = %{version}

%description browserkit
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

# ------------------------------------------------------------------------------

%package   classloader

Summary:   Symfony2 ClassLoader Component
URL:       http://symfony.com/doc/current/components/class_loader.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# PEAR
Provides:  php-pear(%{pear_channel}/ClassLoader) = %{version}
# Rename
Obsoletes: %{name}-ClassLoader < %{version}
Provides:  %{name}-ClassLoader = %{version}

%description classloader
The ClassLoader Component loads your project classes automatically if they
follow some standard PHP conventions.

Whenever you use an undefined class, PHP uses the autoloading mechanism
to delegate the loading of a file defining the class. Symfony2 provides
a "universal" autoloader, which is able to load classes from files that
implement one of the following conventions:
* The technical interoperability standards [1] for PHP 5.3 namespaces
  and class names
* The PEAR naming convention [2] for classes

If your classes and the third-party libraries you use for your project follow
these standards, the Symfony2 autoloader is the only autoloader you will ever
need.

Optional: APC, XCache

[1] http://symfony.com/PSR0
[2] http://pear.php.net/manual/en/standards.php

# ------------------------------------------------------------------------------

%package   config

Summary:   Symfony2 Config Component
URL:       http://symfony.com/doc/current/components/config/index.html

Requires:  %{name}-common     = %{version}-%{release}
Requires:  %{name}-filesystem = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Config) = %{version}
# Rename
Obsoletes: %{name}-Config < %{version}
Provides:  %{name}-Config = %{version}

%description config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

# ------------------------------------------------------------------------------

%package   console

Summary:   Symfony2 Console Component
URL:       http://symfony.com/doc/current/components/console/index.html

Requires:  %{name}-common          = %{version}-%{release}
# Optional
Requires:  %{name}-eventdispatcher = %{version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-dom
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-posix
Requires:  php-readline
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Console) = %{version}
# Rename
Obsoletes: %{name}-Console < %{version}
Provides:  %{name}-Console = %{version}

%description console
The Console component eases the creation of beautiful and testable command line
interfaces.

The Console component allows you to create command-line commands. Your console
commands can be used for any recurring task, such as cronjobs, imports, or
other batch jobs.

# ------------------------------------------------------------------------------

%package   cssselector

Summary:   Symfony2 CssSelector Component
URL:       http://symfony.com/doc/current/components/css_selector.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-mbstring
Requires:  php-pcre

# PEAR
Provides:  php-pear(%{pear_channel}/CssSelector) = %{version}
# Rename
Obsoletes: %{name}-CssSelector < %{version}
Provides:  %{name}-CssSelector = %{version}

%description cssselector
The CssSelector Component converts CSS selectors to XPath expressions.

# ------------------------------------------------------------------------------

## TODO: xdebug optional?  NOTE: HttpKernel requires this component

%package   debug

Summary:   Symfony2 Debug Component
URL:       http://symfony.com/doc/current/components/debug.html

Requires:  %{name}-common         = %{version}-%{release}
# Optional
Requires:  %{name}-classloader    = %{version}-%{release}
Requires:  %{name}-httpfoundation = %{version}-%{release}
Requires:  %{name}-httpkernel     = %{version}-%{release}
# phpcompatinfo
#Requires:  php-pecl(xdebug)
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Debug) = %{version}

%description debug
The Debug Component provides tools to ease debugging PHP code.

# ------------------------------------------------------------------------------

%package   dependencyinjection

Summary:   Symfony2 DependencyInjection Component
URL:       http://symfony.com/doc/current/components/dependency_injection/index.html

Requires:  %{name}-common = %{version}-%{release}
# Optional
Requires:  %{name}-config             = %{version}-%{release}
#Requires:  %%{name}-proxymanagerbridge = %%{version}-%%{release}
Requires:  %{name}-yaml               = %{version}-%{release}
# phpcompatinfo
Requires:  php-dom
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/DependencyInjection) = %{version}
# Rename
Obsoletes: %{name}-DependencyInjection < %{version}
Provides:  %{name}-DependencyInjection = %{version}

%description dependencyinjection
The Dependency Injection component allows you to standardize and centralize
the way objects are constructed in your application.

# ------------------------------------------------------------------------------

%package   domcrawler

Summary:   Symfony2 DomCrawler Component
URL:       http://symfony.com/doc/current/components/dom_crawler.html

Requires:  %{name}-common      = %{version}-%{release}
# Optional
Requires:  %{name}-cssselector = %{version}-%{release}
# phpcompatinfo
Requires:  php-dom
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/DomCrawler) = %{version}
# Rename
Obsoletes: %{name}-DomCrawler < %{version}
Provides:  %{name}-DomCrawler = %{version}

%description domcrawler
The DomCrawler Component eases DOM navigation for HTML and XML documents.

# ------------------------------------------------------------------------------

%package   eventdispatcher

Summary:   Symfony2 EventDispatcher Component
URL:       http://symfony.com/doc/current/components/event_dispatcher/index.html

Requires:  %{name}-common              = %{version}-%{release}
# Optional
Requires:  %{name}-dependencyinjection = %{version}-%{release}
Requires:  %{name}-httpkernel          = %{version}-%{release}
# phpcompatinfo
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/EventDispatcher) = %{version}
# Rename
Obsoletes: %{name}-EventDispatcher < %{version}
Provides:  %{name}-EventDispatcher = %{version}

%description eventdispatcher
The Symfony2 Event Dispatcher component implements the Observer [1] pattern in
a simple and effective way to make all these things possible and to make your
projects truly extensible.

[1] http://en.wikipedia.org/wiki/Observer_pattern

# ------------------------------------------------------------------------------

%package   filesystem

Summary:   Symfony2 Filesystem Component
URL:       http://symfony.com/doc/current/components/filesystem.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Filesystem) = %{version}
# Rename
Obsoletes: %{name}-Filesystem < %{version}
Provides:  %{name}-Filesystem = %{version}

%description filesystem
The Filesystem component provides basic utilities for the filesystem.

# ------------------------------------------------------------------------------

%package   finder

Summary:   Symfony2 Finder Component
URL:       http://symfony.com/doc/current/components/finder.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Finder) = %{version}
# Rename
Obsoletes: %{name}-Finder < %{version}
Provides:  %{name}-Finder = %{version}

%description finder
The Finder Component finds files and directories via an intuitive fluent
interface.

# ------------------------------------------------------------------------------

%package   form

Summary:   Symfony2 Form Component

Requires:  %{name}-common          = %{version}-%{release}
Requires:  %{name}-eventdispatcher = %{version}-%{release}
Requires:  %{name}-intl            = %{version}-%{release}
Requires:  %{name}-optionsresolver = %{version}-%{release}
Requires:  %{name}-propertyaccess  = %{version}-%{release}
# Optional
Requires:  %{name}-httpfoundation  = %{version}-%{release}
Requires:  %{name}-validator       = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-date
Requires:  php-intl
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-session
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Form) = %{version}
# Rename
Obsoletes: %{name}-Form < %{version}
Provides:  %{name}-Form = %{version}

%description form
Form provides tools for defining forms, rendering and mapping request data
to related models. Furthermore it provides integration with the Validation
component.

# ------------------------------------------------------------------------------

%package   httpfoundation

Summary:   Symfony2 HttpFoundation Component
URL:       http://symfony.com/doc/current/components/http_foundation/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-fileinfo
Requires:  php-filter
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-session
Requires:  php-sockets
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/HttpFoundation) = %{version}
# Rename
Obsoletes: %{name}-HttpFoundation < %{version}
Provides:  %{name}-HttpFoundation = %{version}

%description httpfoundation
The HttpFoundation Component defines an object-oriented layer for the HTTP
specification.

In PHP, the request is represented by some global variables ($_GET, $_POST,
$_FILES, $_COOKIE, $_SESSION, ...) and the response is generated by some
functions (echo, header, setcookie, ...).

The Symfony2 HttpFoundation component replaces these default PHP global
variables and functions by an Object-Oriented layer.

Optional: memcache, memcached, mongo

# ------------------------------------------------------------------------------

%package   httpkernel

Summary:   Symfony2 HttpKernel Component
URL:       http://symfony.com/doc/current/components/http_kernel/index.html

Requires:  %{name}-common              =  %{version}-%{release}
Requires:  %{name}-debug               =  %{version}-%{release}
Requires:  %{name}-eventdispatcher     =  %{version}-%{release}
Requires:  %{name}-httpfoundation      =  %{version}-%{release}
Requires:  php-PsrLog                  >= %{psrlog_min_ver}
Requires:  php-PsrLog                  <  %{psrlog_max_ver}
# Optional
Requires:  %{name}-browserkit          =  %{version}-%{release}
Requires:  %{name}-classloader         =  %{version}-%{release}
Requires:  %{name}-config              =  %{version}-%{release}
Requires:  %{name}-console             =  %{version}-%{release}
Requires:  %{name}-dependencyinjection =  %{version}-%{release}
Requires:  %{name}-finder              =  %{version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-hash
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-reflection
Requires:  php-spl
Requires:  php-sqlite3
Requires:  php-tokenizer

# PEAR
Provides:  php-pear(%{pear_channel}/HttpKernel) = %{version}
# Rename
Obsoletes: %{name}-HttpKernel < %{version}
Provides:  %{name}-HttpKernel = %{version}

%description httpkernel
The HttpKernel Component provides a structured process for converting a Request
into a Response by making use of the event dispatcher. It's flexible enough to
create a full-stack framework (Symfony), a micro-framework (Silex) or an
advanced CMS system (Drupal).

Configuration reference:
http://symfony.com/doc/current/reference/configuration/kernel.html

Optional: memcache, memcached, redis, Zend OPcache

# ------------------------------------------------------------------------------

%package   icu

Version:   %{icu_github_version}
Summary:   Symfony2 Icu Component
URL:       https://github.com/symfony/Icu

Requires:  %{name}-common = %{github_version}-%{release}
Requires:  %{name}-intl   = %{github_version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-intl
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

%description icu
Contains data of the ICU library.

The bundled resource files have the resource bundle format version 2.* [1],
which can be read using ICU 4.4 and later. Compatibility can be tested with
the test-compat.php script bundled in the Intl component:

%{_bindir}/php %{symfony_dir}/Component/Intl/Resources/bin/test-compat.php

You should not directly use this component. Use it through the API of the Intl
component instead.

[1] http://site.icu-project.org/design/data/res2

# ------------------------------------------------------------------------------

%package   intl

Summary:   Symfony2 Intl Component
URL:       http://symfony.com/doc/current/components/intl.html

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}-icu    = %{icu_github_version}-%{release}
# phpcompatinfo
Requires:  php-date
Requires:  php-intl
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Intl) = %{version}
# Rename
Obsoletes: %{name}-Intl < %{version}
Provides:  %{name}-Intl = %{version}

%description intl
A PHP replacement layer for the C intl extension [1] that also provides access
to the localization data of the ICU library [2].

[1] http://www.php.net/manual/en/book.intl.php
[2] http://site.icu-project.org/

# ------------------------------------------------------------------------------

%package   locale

Summary:   Symfony2 Locale Component

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}-intl   = %{version}-%{release}
# phpcompatinfo
Requires:  php-intl

# PEAR
Provides:  php-pear(%{pear_channel}/Locale) = %{version}
# Rename
Obsoletes: %{name}-Locale < %{version}
Provides:  %{name}-Locale = %{version}

%description locale
Locale provides fallback code to handle cases when the intl extension is
missing.

The Locale component is deprecated since version 2.3 and will be removed in
Symfony 3.0. You should use the more capable Intl component instead.

# ------------------------------------------------------------------------------

%package   optionsresolver

Summary:   Symfony2 OptionsResolver Component
URL:       http://symfony.com/doc/current/components/options_resolver.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-reflection
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/OptionsResolver) = %{version}
# Rename
Obsoletes: %{name}-OptionsResolver < %{version}
Provides:  %{name}-OptionsResolver = %{version}

%description optionsresolver
The OptionsResolver Component helps you configure objects with option arrays.
It supports default values, option constraints and lazy options.

# ------------------------------------------------------------------------------

%package   process

Summary:   Symfony2 Process Component
URL:       http://symfony.com/doc/current/components/process.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-pcntl
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Process) = %{version}
# Rename
Obsoletes: %{name}-Process < %{version}
Provides:  %{name}-Process = %{version}

%description process
The Process Component executes commands in sub-processes.

# ------------------------------------------------------------------------------

%package   propertyaccess

Summary:   Symfony2 PropertyAccess Component
URL:       http://symfony.com/doc/current/components/property_access/introduction.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/PropertyAccess) = %{version}
# Rename
Obsoletes: %{name}-PropertyAccess < %{version}
Provides:  %{name}-PropertyAccess = %{version}

%description propertyaccess
The PropertyAccess component provides function to read and write from/to an
object or array using a simple string notation.

# ------------------------------------------------------------------------------

%package   routing

Summary:   Symfony2 Routing Component
URL:       http://symfony.com/doc/current/components/routing/index.html

Requires:  %{name}-common = %{version}-%{release}
# Optional
Requires:  %{name}-config = %{version}-%{release}
Requires:  %{name}-yaml   = %{version}-%{release}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) >= %{doctrine_common_min_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon) <  %{doctrine_common_max_ver}
# phpcompatinfo
Requires:  php-dom
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl
Requires:  php-tokenizer

# PEAR
Provides:  php-pear(%{pear_channel}/Routing) = %{version}
# Rename
Obsoletes: %{name}-Routing < %{version}
Provides:  %{name}-Routing = %{version}

%description routing
The Routing Component maps an HTTP request to a set of configuration variables.

# ------------------------------------------------------------------------------

%package   security

Summary:   Symfony2 Security Component
URL:       http://symfony.com/doc/current/components/security/index.html

Requires:  %{name}-common          = %{version}-%{release}
Requires:  %{name}-eventdispatcher = %{version}-%{release}
Requires:  %{name}-httpfoundation  = %{version}-%{release}
Requires:  %{name}-httpkernel      = %{version}-%{release}
# Optional
Requires:  %{name}-classloader     = %{version}-%{release}
Requires:  %{name}-finder          = %{version}-%{release}
Requires:  %{name}-form            = %{version}-%{release}
Requires:  %{name}-routing         = %{version}-%{release}
Requires:  %{name}-validator       = %{version}-%{release}
Requires:  php-pear(pear.doctrine-project.org/DoctrineDBAL) >= %{doctrine_dbal_min_ver}
Requires:  php-pear(pear.doctrine-project.org/DoctrineDBAL) <  %{doctrine_dbal_max_ver}
# TODO: "ircmaxell/password-compat": "1.0.*"
# phpcompatinfo
Requires:  php-date
Requires:  php-hash
Requires:  php-json
Requires:  php-openssl
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Security) = %{version}
# Rename
Obsoletes: %{name}-Security < %{version}
Provides:  %{name}-Security = %{version}

%description security
The Security Component provides a complete security system for your web
application. It ships with facilities for authenticating using HTTP basic
or digest authentication, interactive form login or X.509 certificate login,
but also allows you to implement your own authentication strategies.
Furthermore, the component provides ways to authorize authenticated users
based on their roles, and it contains an advanced ACL system.

# ------------------------------------------------------------------------------

%package   serializer

Summary:   Symfony2 Serializer Component
URL:       http://symfony.com/doc/current/components/serializer.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-dom
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Serializer) = %{version}
# Rename
Obsoletes: %{name}-Serializer < %{version}
Provides:  %{name}-Serializer = %{version}

%description serializer
The Serializer Component is meant to be used to turn objects into a specific
format (XML, JSON, Yaml, ...) and the other way around.

# ------------------------------------------------------------------------------

%package   stopwatch

Summary:   Symfony2 Stopwatch Component
URL:       http://symfony.com/doc/current/components/stopwatch.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Stopwatch) = %{version}

%description stopwatch
Stopwatch component provides a way to profile code.

# ------------------------------------------------------------------------------

%package   templating

Summary:   Symfony2 Templating Component
URL:       http://symfony.com/doc/current/components/templating.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-iconv
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Templating) = %{version}
# Rename
Obsoletes: %{name}-Templating < %{version}
Provides:  %{name}-Templating = %{version}

%description templating
Templating provides all the tools needed to build any kind of template system.

It provides an infrastructure to load template files and optionally monitor
them for changes. It also provides a concrete template engine implementation
using PHP with additional tools for escaping and separating templates into
blocks and layouts.

# ------------------------------------------------------------------------------

%package   translation

Summary:   Symfony2 Translation Component

Requires:  %{name}-common = %{version}-%{release}
# Optional
Requires:  %{name}-config = %{version}-%{release}
Requires:  %{name}-yaml   = %{version}-%{release}
# phpcompatinfo
Requires:  php-dom
Requires:  php-iconv
Requires:  php-intl
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-simplexml
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Translation) = %{version}
# Rename
Obsoletes: %{name}-Translation < %{version}
Provides:  %{name}-Translation = %{version}

%description translation
Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

# ------------------------------------------------------------------------------

%package   validator

Summary:   Symfony2 Validator Component

Requires:  %{name}-common         = %{version}-%{release}
Requires:  %{name}-translation    = %{version}-%{release}
# Optional
Requires:  %{name}-config         = %{version}-%{release}
Requires:  %{name}-httpfoundation = %{version}-%{release}
Requires:  %{name}-intl           = %{version}-%{release}
Requires:  %{name}-yaml           = %{version}-%{release}
Requires:  php-pear(pear.doctrine-project.org/DoctrineCommon)
# phpcompatinfo
Requires:  php-ctype
Requires:  php-date
Requires:  php-filter
Requires:  php-intl
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Validator) = %{version}
# Rename
Obsoletes: %{name}-Validator < %{version}
Provides:  %{name}-Validator = %{version}

%description validator
This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

Optional: APC

# ------------------------------------------------------------------------------

%package   yaml

Summary:   Symfony2 Yaml Component
URL:       http://symfony.com/doc/current/components/yaml/index.html

Requires:  %{name}-common = %{version}-%{release}
# phpcompatinfo
Requires:  php-ctype
Requires:  php-date
Requires:  php-iconv
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-spl

# PEAR
Provides:  php-pear(%{pear_channel}/Yaml) = %{version}
# Rename
Obsoletes: %{name}-Yaml < %{version}
Provides:  %{name}-Yaml = %{version}

%description yaml
The YAML Component loads and dumps YAML files.

# ##############################################################################


%prep
%setup -q -n %{github_name}-%{github_commit}

# Setup Icu component
mkdir -p -m 755 src/Symfony/Component/Icu
pushd src/Symfony/Component/Icu
  tar xzf %{SOURCE1} --strip-components 1 || tar xzf %{SOURCE1} --strip-path 1
popd

# Remove unnecessary files
find src -name '.git*' -delete
rm -rf src/Symfony/Bridge/{Propel1,ProxyManager}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{symfony_dir}
cp -rp src/Symfony/* %{buildroot}%{symfony_dir}/

# Symlink package docs to common sub-package docs
mkdir -p %{buildroot}%{_docdir}
ln -s %{name}-common-%{version} %{buildroot}%{_docdir}/%{name}-%{version}

# Lang files
for res_file in \
    %{buildroot}%{symfony_dir}/Component/Icu/Resources/data/*/*.res
do
    res_file_lang=$(basename $res_file | sed 's#\(_.*\)*\.res##')
    if [ "root" != "$res_file_lang" ] && \
       [ "supplementaldata" != "$res_file_lang" ]
    then
        echo "%lang($res_file_lang) $res_file"
    else
        echo "$res_file"
    fi
done > %{name}-icu.lang
sed -i "s#%{buildroot}##" %{name}-icu.lang


%check
# Create autoloader
mkdir vendor
( cat <<'AUTOLOADER'
<?php

require_once __DIR__.'/../src/Symfony/Component/ClassLoader/UniversalClassLoader.php';

use Symfony\Component\ClassLoader\UniversalClassLoader;

$loader = new UniversalClassLoader();
$loader->useIncludePath(true);
$loader->register();

return $loader;
AUTOLOADER
) > vendor/autoload.php

# Turn off colors
sed 's/colors="true"/colors="false"/' -i phpunit.xml.dist

# Run tests
%{_bindir}/phpunit \
    -d include_path="./src:%{_datadir}/php:%{pear_phpdir}" \
    -d date.timezone="UTC" \
    || : Temporarily ignore failed tests


%files
# Empty files section, included in sub-package "common"


# ##############################################################################

%files common

%doc LICENSE *.md composer.*
%doc %{_docdir}/%{name}-%{version}

%dir %{symfony_dir}

# ------------------------------------------------------------------------------

%files doctrinebridge

%doc src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/*.md
%doc src/Symfony/Bridge/Doctrine/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Doctrine
%exclude %{symfony_dir}/Bridge/Doctrine/LICENSE
%exclude %{symfony_dir}/Bridge/Doctrine/*.md
%exclude %{symfony_dir}/Bridge/Doctrine/composer.*
%exclude %{symfony_dir}/Bridge/Doctrine/phpunit.*
%exclude %{symfony_dir}/Bridge/Doctrine/Tests

# ------------------------------------------------------------------------------

%files monologbridge

%doc src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/*.md
%doc src/Symfony/Bridge/Monolog/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Monolog
%exclude %{symfony_dir}/Bridge/Monolog/LICENSE
%exclude %{symfony_dir}/Bridge/Monolog/*.md
%exclude %{symfony_dir}/Bridge/Monolog/composer.*
%exclude %{symfony_dir}/Bridge/Monolog/phpunit.*
%exclude %{symfony_dir}/Bridge/Monolog/Tests

# ------------------------------------------------------------------------------

#%%files propel1bridge

#%%doc src/Symfony/Bridge/Propel1/LICENSE
#%%doc src/Symfony/Bridge/Propel1/*.md
#%%doc src/Symfony/Bridge/Propel1/composer.*

#%%dir     %%{symfony_dir}/Bridge
#         %%{symfony_dir}/Bridge/Propel1
#%%exclude %%{symfony_dir}/Bridge/Propel1/LICENSE
#%%exclude %%{symfony_dir}/Bridge/Propel1/*.md
#%%exclude %%{symfony_dir}/Bridge/Propel1/composer.*
#%%exclude %%{symfony_dir}/Bridge/Propel1/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/Propel1/Tests

# ------------------------------------------------------------------------------

#%%files proxymanagerbridge

#%%doc src/Symfony/Bridge/ProxyManager/LICENSE
#%%doc src/Symfony/Bridge/ProxyManager/*.md
#%%doc src/Symfony/Bridge/ProxyManager/composer.*

#%%dir     %%{symfony_dir}/Bridge
#         %%{symfony_dir}/Bridge/ProxyManager
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/LICENSE
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/*.md
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/composer.*
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/ProxyManager/Tests

# ------------------------------------------------------------------------------

%files swiftmailerbridge

%doc src/Symfony/Bridge/Swiftmailer/LICENSE
%doc src/Symfony/Bridge/Swiftmailer/*.md
%doc src/Symfony/Bridge/Swiftmailer/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Swiftmailer
%exclude %{symfony_dir}/Bridge/Swiftmailer/LICENSE
%exclude %{symfony_dir}/Bridge/Swiftmailer/*.md
%exclude %{symfony_dir}/Bridge/Swiftmailer/composer.*
#%%exclude %%{symfony_dir}/Bridge/Swiftmailer/phpunit.*
#%%exclude %%{symfony_dir}/Bridge/Swiftmailer/Tests

# ------------------------------------------------------------------------------

%files twigbridge

%doc src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/*.md
%doc src/Symfony/Bridge/Twig/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Twig
%exclude %{symfony_dir}/Bridge/Twig/LICENSE
%exclude %{symfony_dir}/Bridge/Twig/*.md
%exclude %{symfony_dir}/Bridge/Twig/composer.*
%exclude %{symfony_dir}/Bridge/Twig/phpunit.*
%exclude %{symfony_dir}/Bridge/Twig/Tests

# ------------------------------------------------------------------------------

%files frameworkbundle

%doc src/Symfony/Bundle/FrameworkBundle/LICENSE
%doc src/Symfony/Bundle/FrameworkBundle/*.md
%doc src/Symfony/Bundle/FrameworkBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/FrameworkBundle
%exclude %{symfony_dir}/Bundle/FrameworkBundle/LICENSE
%exclude %{symfony_dir}/Bundle/FrameworkBundle/*.md
%exclude %{symfony_dir}/Bundle/FrameworkBundle/composer.*
%exclude %{symfony_dir}/Bundle/FrameworkBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/FrameworkBundle/Tests

# ------------------------------------------------------------------------------

%files securitybundle

%doc src/Symfony/Bundle/SecurityBundle/LICENSE
%doc src/Symfony/Bundle/SecurityBundle/*.md
%doc src/Symfony/Bundle/SecurityBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/SecurityBundle
%exclude %{symfony_dir}/Bundle/SecurityBundle/LICENSE
%exclude %{symfony_dir}/Bundle/SecurityBundle/*.md
%exclude %{symfony_dir}/Bundle/SecurityBundle/composer.*
%exclude %{symfony_dir}/Bundle/SecurityBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/SecurityBundle/Tests

# ------------------------------------------------------------------------------

%files twigbundle

%doc src/Symfony/Bundle/TwigBundle/LICENSE
%doc src/Symfony/Bundle/TwigBundle/*.md
%doc src/Symfony/Bundle/TwigBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/TwigBundle
%exclude %{symfony_dir}/Bundle/TwigBundle/LICENSE
%exclude %{symfony_dir}/Bundle/TwigBundle/*.md
%exclude %{symfony_dir}/Bundle/TwigBundle/composer.*
%exclude %{symfony_dir}/Bundle/TwigBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/TwigBundle/Tests

# ------------------------------------------------------------------------------

%files webprofilerbundle

%doc src/Symfony/Bundle/WebProfilerBundle/LICENSE
%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%doc src/Symfony/Bundle/WebProfilerBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/WebProfilerBundle
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/LICENSE
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/*.md
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/composer.*
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Tests

# ------------------------------------------------------------------------------

%files browserkit

%doc src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/*.md
%doc src/Symfony/Component/BrowserKit/composer.*

         %{symfony_dir}/Component/BrowserKit
%exclude %{symfony_dir}/Component/BrowserKit/LICENSE
%exclude %{symfony_dir}/Component/BrowserKit/*.md
%exclude %{symfony_dir}/Component/BrowserKit/composer.*
%exclude %{symfony_dir}/Component/BrowserKit/phpunit.*
%exclude %{symfony_dir}/Component/BrowserKit/Tests

# ------------------------------------------------------------------------------

%files classloader

%doc src/Symfony/Component/ClassLoader/LICENSE
%doc src/Symfony/Component/ClassLoader/*.md
%doc src/Symfony/Component/ClassLoader/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/ClassLoader
%exclude %{symfony_dir}/Component/ClassLoader/LICENSE
%exclude %{symfony_dir}/Component/ClassLoader/*.md
%exclude %{symfony_dir}/Component/ClassLoader/composer.*
%exclude %{symfony_dir}/Component/ClassLoader/phpunit.*
%exclude %{symfony_dir}/Component/ClassLoader/Tests

# ------------------------------------------------------------------------------

%files config

%doc src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/*.md
%doc src/Symfony/Component/Config/composer.*

         %{symfony_dir}/Component/Config
%exclude %{symfony_dir}/Component/Config/LICENSE
%exclude %{symfony_dir}/Component/Config/*.md
%exclude %{symfony_dir}/Component/Config/composer.*
%exclude %{symfony_dir}/Component/Config/phpunit.*
%exclude %{symfony_dir}/Component/Config/Tests

# ------------------------------------------------------------------------------

%files console

%doc src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/*.md
%doc src/Symfony/Component/Console/composer.*

         %{symfony_dir}/Component/Console
%exclude %{symfony_dir}/Component/Console/LICENSE
%exclude %{symfony_dir}/Component/Console/*.md
%exclude %{symfony_dir}/Component/Console/composer.*
%exclude %{symfony_dir}/Component/Console/phpunit.*
%exclude %{symfony_dir}/Component/Console/Tests

# ------------------------------------------------------------------------------

%files cssselector

%doc src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/*.md
%doc src/Symfony/Component/CssSelector/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/CssSelector
%exclude %{symfony_dir}/Component/CssSelector/LICENSE
%exclude %{symfony_dir}/Component/CssSelector/*.md
%exclude %{symfony_dir}/Component/CssSelector/composer.*
%exclude %{symfony_dir}/Component/CssSelector/phpunit.*
%exclude %{symfony_dir}/Component/CssSelector/Tests

# ------------------------------------------------------------------------------

%files debug

%doc src/Symfony/Component/Debug/LICENSE
%doc src/Symfony/Component/Debug/*.md
%doc src/Symfony/Component/Debug/composer.*

         %{symfony_dir}/Component/Debug
%exclude %{symfony_dir}/Component/Debug/LICENSE
%exclude %{symfony_dir}/Component/Debug/*.md
%exclude %{symfony_dir}/Component/Debug/composer.*
%exclude %{symfony_dir}/Component/Debug/phpunit.*
%exclude %{symfony_dir}/Component/Debug/Tests

# ------------------------------------------------------------------------------

%files dependencyinjection

%doc src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/*.md
%doc src/Symfony/Component/DependencyInjection/composer.*

         %{symfony_dir}/Component/DependencyInjection
%exclude %{symfony_dir}/Component/DependencyInjection/LICENSE
%exclude %{symfony_dir}/Component/DependencyInjection/*.md
%exclude %{symfony_dir}/Component/DependencyInjection/composer.*
%exclude %{symfony_dir}/Component/DependencyInjection/phpunit.*
%exclude %{symfony_dir}/Component/DependencyInjection/Tests

# ------------------------------------------------------------------------------

%files domcrawler

%doc src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/*.md
%doc src/Symfony/Component/DomCrawler/composer.*

         %{symfony_dir}/Component/DomCrawler
%exclude %{symfony_dir}/Component/DomCrawler/LICENSE
%exclude %{symfony_dir}/Component/DomCrawler/*.md
%exclude %{symfony_dir}/Component/DomCrawler/composer.*
%exclude %{symfony_dir}/Component/DomCrawler/phpunit.*
%exclude %{symfony_dir}/Component/DomCrawler/Tests

# ------------------------------------------------------------------------------

%files eventdispatcher

%doc src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/*.md
%doc src/Symfony/Component/EventDispatcher/composer.*

         %{symfony_dir}/Component/EventDispatcher
%exclude %{symfony_dir}/Component/EventDispatcher/LICENSE
%exclude %{symfony_dir}/Component/EventDispatcher/*.md
%exclude %{symfony_dir}/Component/EventDispatcher/composer.*
%exclude %{symfony_dir}/Component/EventDispatcher/phpunit.*
%exclude %{symfony_dir}/Component/EventDispatcher/Tests

# ------------------------------------------------------------------------------

%files filesystem

%doc src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/*.md
%doc src/Symfony/Component/Filesystem/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Filesystem
%exclude %{symfony_dir}/Component/Filesystem/LICENSE
%exclude %{symfony_dir}/Component/Filesystem/*.md
%exclude %{symfony_dir}/Component/Filesystem/composer.*
%exclude %{symfony_dir}/Component/Filesystem/phpunit.*
%exclude %{symfony_dir}/Component/Filesystem/Tests

# ------------------------------------------------------------------------------

%files finder

%doc src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/*.md
%doc src/Symfony/Component/Finder/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Finder
%exclude %{symfony_dir}/Component/Finder/LICENSE
%exclude %{symfony_dir}/Component/Finder/*.md
%exclude %{symfony_dir}/Component/Finder/composer.*
%exclude %{symfony_dir}/Component/Finder/phpunit.*
%exclude %{symfony_dir}/Component/Finder/Tests

# ------------------------------------------------------------------------------

%files form

%doc src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/*.md
%doc src/Symfony/Component/Form/composer.*

         %{symfony_dir}/Component/Form
%exclude %{symfony_dir}/Component/Form/LICENSE
%exclude %{symfony_dir}/Component/Form/*.md
%exclude %{symfony_dir}/Component/Form/composer.*
%exclude %{symfony_dir}/Component/Form/phpunit.*
%exclude %{symfony_dir}/Component/Form/Tests

# ------------------------------------------------------------------------------

%files httpfoundation

%doc src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/*.md
%doc src/Symfony/Component/HttpFoundation/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/HttpFoundation
%exclude %{symfony_dir}/Component/HttpFoundation/LICENSE
%exclude %{symfony_dir}/Component/HttpFoundation/*.md
%exclude %{symfony_dir}/Component/HttpFoundation/composer.*
%exclude %{symfony_dir}/Component/HttpFoundation/phpunit.*
%exclude %{symfony_dir}/Component/HttpFoundation/Tests

# ------------------------------------------------------------------------------

%files httpkernel

%doc src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/*.md
%doc src/Symfony/Component/HttpKernel/composer.*

         %{symfony_dir}/Component/HttpKernel
%exclude %{symfony_dir}/Component/HttpKernel/LICENSE
%exclude %{symfony_dir}/Component/HttpKernel/*.md
%exclude %{symfony_dir}/Component/HttpKernel/composer.*
%exclude %{symfony_dir}/Component/HttpKernel/phpunit.*
%exclude %{symfony_dir}/Component/HttpKernel/Tests

# ------------------------------------------------------------------------------

%files icu -f %{name}-icu.lang

%doc src/Symfony/Component/Icu/LICENSE
%doc src/Symfony/Component/Icu/*.md
%doc src/Symfony/Component/Icu/composer.*
%doc src/Symfony/Component/Icu/Resources/data/*.txt

%dir     %{symfony_dir}/Component/Icu
         %{symfony_dir}/Component/Icu/*.php
%dir     %{symfony_dir}/Component/Icu/Resources
%dir     %{symfony_dir}/Component/Icu/Resources/data
%dir     %{symfony_dir}/Component/Icu/Resources/data/curr
%dir     %{symfony_dir}/Component/Icu/Resources/data/lang
%dir     %{symfony_dir}/Component/Icu/Resources/data/locales
%dir     %{symfony_dir}/Component/Icu/Resources/data/region
%exclude %{symfony_dir}/Component/Icu/LICENSE
%exclude %{symfony_dir}/Component/Icu/*.md
%exclude %{symfony_dir}/Component/Icu/composer.*
%exclude %{symfony_dir}/Component/Icu/phpunit.*
%exclude %{symfony_dir}/Component/Icu/Resources/data/*.txt
%exclude %{symfony_dir}/Component/Icu/Tests

# ------------------------------------------------------------------------------

%files intl

%doc src/Symfony/Component/Intl/LICENSE
%doc src/Symfony/Component/Intl/*.md
%doc src/Symfony/Component/Intl/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Intl
%exclude %{symfony_dir}/Component/Intl/LICENSE
%exclude %{symfony_dir}/Component/Intl/*.md
%exclude %{symfony_dir}/Component/Intl/composer.*
%exclude %{symfony_dir}/Component/Intl/phpunit.*
%exclude %{symfony_dir}/Component/Intl/Tests

# ------------------------------------------------------------------------------

%files locale

%doc src/Symfony/Component/Locale/LICENSE
%doc src/Symfony/Component/Locale/*.md
%doc src/Symfony/Component/Locale/composer.*

         %{symfony_dir}/Component/Locale
%exclude %{symfony_dir}/Component/Locale/LICENSE
%exclude %{symfony_dir}/Component/Locale/*.md
%exclude %{symfony_dir}/Component/Locale/composer.*
%exclude %{symfony_dir}/Component/Locale/phpunit.*
%exclude %{symfony_dir}/Component/Locale/Tests

# ------------------------------------------------------------------------------

%files optionsresolver

%doc src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/*.md
%doc src/Symfony/Component/OptionsResolver/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/OptionsResolver
%exclude %{symfony_dir}/Component/OptionsResolver/LICENSE
%exclude %{symfony_dir}/Component/OptionsResolver/*.md
%exclude %{symfony_dir}/Component/OptionsResolver/composer.*
%exclude %{symfony_dir}/Component/OptionsResolver/phpunit.*
%exclude %{symfony_dir}/Component/OptionsResolver/Tests

# ------------------------------------------------------------------------------

%files process

%doc src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/*.md
%doc src/Symfony/Component/Process/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Process
%exclude %{symfony_dir}/Component/Process/LICENSE
%exclude %{symfony_dir}/Component/Process/*.md
%exclude %{symfony_dir}/Component/Process/composer.*
%exclude %{symfony_dir}/Component/Process/phpunit.*
%exclude %{symfony_dir}/Component/Process/Tests

# ------------------------------------------------------------------------------

%files propertyaccess

%doc src/Symfony/Component/PropertyAccess/LICENSE
%doc src/Symfony/Component/PropertyAccess/*.md
%doc src/Symfony/Component/PropertyAccess/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/PropertyAccess
%exclude %{symfony_dir}/Component/PropertyAccess/LICENSE
%exclude %{symfony_dir}/Component/PropertyAccess/*.md
%exclude %{symfony_dir}/Component/PropertyAccess/composer.*
#%%exclude %%{symfony_dir}/Component/PropertyAccess/phpunit.*
#%%exclude %%{symfony_dir}/Component/PropertyAccess/Tests

# ------------------------------------------------------------------------------

%files routing

%doc src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/*.md
%doc src/Symfony/Component/Routing/composer.*

         %{symfony_dir}/Component/Routing
%exclude %{symfony_dir}/Component/Routing/LICENSE
%exclude %{symfony_dir}/Component/Routing/*.md
%exclude %{symfony_dir}/Component/Routing/composer.*
%exclude %{symfony_dir}/Component/Routing/phpunit.*
%exclude %{symfony_dir}/Component/Routing/Tests

# ------------------------------------------------------------------------------

%files security

%doc src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/*.md
%doc src/Symfony/Component/Security/composer.*

         %{symfony_dir}/Component/Security
%exclude %{symfony_dir}/Component/Security/LICENSE
%exclude %{symfony_dir}/Component/Security/*.md
%exclude %{symfony_dir}/Component/Security/composer.*
%exclude %{symfony_dir}/Component/Security/phpunit.*
%exclude %{symfony_dir}/Component/Security/Tests

# ------------------------------------------------------------------------------

%files serializer

%doc src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/*.md
%doc src/Symfony/Component/Serializer/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Serializer
%exclude %{symfony_dir}/Component/Serializer/LICENSE
%exclude %{symfony_dir}/Component/Serializer/*.md
%exclude %{symfony_dir}/Component/Serializer/composer.*
%exclude %{symfony_dir}/Component/Serializer/phpunit.*
%exclude %{symfony_dir}/Component/Serializer/Tests

# ------------------------------------------------------------------------------

%files stopwatch

%doc src/Symfony/Component/Stopwatch/LICENSE
%doc src/Symfony/Component/Stopwatch/*.md
%doc src/Symfony/Component/Stopwatch/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Stopwatch
%exclude %{symfony_dir}/Component/Stopwatch/LICENSE
%exclude %{symfony_dir}/Component/Stopwatch/*.md
%exclude %{symfony_dir}/Component/Stopwatch/composer.*
#%%exclude %%{symfony_dir}/Component/Stopwatch/phpunit.*
#%%exclude %%{symfony_dir}/Component/Stopwatch/Tests

# ------------------------------------------------------------------------------

%files templating

%doc src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/*.md
%doc src/Symfony/Component/Templating/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Templating
%exclude %{symfony_dir}/Component/Templating/LICENSE
%exclude %{symfony_dir}/Component/Templating/*.md
%exclude %{symfony_dir}/Component/Templating/composer.*
%exclude %{symfony_dir}/Component/Templating/phpunit.*
%exclude %{symfony_dir}/Component/Templating/Tests

# ------------------------------------------------------------------------------

%files translation

%doc src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/*.md
%doc src/Symfony/Component/Translation/composer.*

         %{symfony_dir}/Component/Translation
%exclude %{symfony_dir}/Component/Translation/LICENSE
%exclude %{symfony_dir}/Component/Translation/*.md
%exclude %{symfony_dir}/Component/Translation/composer.*
%exclude %{symfony_dir}/Component/Translation/phpunit.*
%exclude %{symfony_dir}/Component/Translation/Tests

# ------------------------------------------------------------------------------

%files validator

%doc src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/*.md
%doc src/Symfony/Component/Validator/composer.*

         %{symfony_dir}/Component/Validator
%exclude %{symfony_dir}/Component/Validator/LICENSE
%exclude %{symfony_dir}/Component/Validator/*.md
%exclude %{symfony_dir}/Component/Validator/composer.*
%exclude %{symfony_dir}/Component/Validator/phpunit.*
%exclude %{symfony_dir}/Component/Validator/Tests

# ------------------------------------------------------------------------------

%files yaml

%doc src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/*.md
%doc src/Symfony/Component/Yaml/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Yaml
%exclude %{symfony_dir}/Component/Yaml/LICENSE
%exclude %{symfony_dir}/Component/Yaml/*.md
%exclude %{symfony_dir}/Component/Yaml/composer.*
%exclude %{symfony_dir}/Component/Yaml/phpunit.*
%exclude %{symfony_dir}/Component/Yaml/Tests

# ##############################################################################

%changelog
* Sat Jul 13 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.3.1-2
- Renamed to lowercase

* Sat Jul 13 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.3.1-1
- Initial package
