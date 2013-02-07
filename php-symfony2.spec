%global github_owner   symfony
%global github_name    symfony
%global github_version 2.1.6
%global github_commit  9270c41d91433a9af09ed2ae9d2756358b8b245b

%global pear_channel   pear.symfony.com

%global php_min_ver    5.3.3

Name:          php-symfony2
Version:       %{github_version}
Release:       1%{dist}
Summary:       PHP framework

Group:         Development/Libraries
License:       MIT
URL:           http://symfony.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)

# Components
Requires: %{name}-BrowserKit = %{version}-%{release}
Requires: %{name}-ClassLoader = %{version}-%{release}
Requires: %{name}-Config = %{version}-%{release}
Requires: %{name}-Console = %{version}-%{release}
Requires: %{name}-CssSelector = %{version}-%{release}
Requires: %{name}-DependencyInjection = %{version}-%{release}
Requires: %{name}-DomCrawler = %{version}-%{release}
Requires: %{name}-EventDispatcher = %{version}-%{release}
Requires: %{name}-Filesystem = %{version}-%{release}
Requires: %{name}-Finder = %{version}-%{release}
Requires: %{name}-Form = %{version}-%{release}
Requires: %{name}-HttpFoundation = %{version}-%{release}
Requires: %{name}-HttpKernel = %{version}-%{release}
Requires: %{name}-Locale = %{version}-%{release}
Requires: %{name}-OptionsResolver = %{version}-%{release}
Requires: %{name}-Process = %{version}-%{release}
Requires: %{name}-Routing = %{version}-%{release}
Requires: %{name}-Security = %{version}-%{release}
Requires: %{name}-Serializer = %{version}-%{release}
Requires: %{name}-Templating = %{version}-%{release}
Requires: %{name}-Translation = %{version}-%{release}
Requires: %{name}-Validator = %{version}-%{release}
Requires: %{name}-Yaml = %{version}-%{release}

# Bridges
Requires: %{name}-DoctrineBridge = %{version}-%{release}
Requires: %{name}-MonologBridge = %{version}-%{release}
Requires: %{name}-Propel1Bridge = %{version}-%{release}
Requires: %{name}-SwiftmailerBridge = %{version}-%{release}
Requires: %{name}-TwigBridge = %{version}-%{release}

# Bundles
Requires: %{name}-FrameworkBundle = %{version}-%{release}
Requires: %{name}-SecurityBundle = %{version}-%{release}
Requires: %{name}-TwigBundle = %{version}-%{release}
Requires: %{name}-WebProfilerBundle = %{version}-%{release}

%description
TODO

%files
%doc LICENSE *.md

#-------------------------------------------------------------------------------

%package BrowserKit

Summary:  Symfony2 BrowserKit Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
Requires: %{name}-DomCrawler = %{version}-%{release}
# phpci
Requires: php-date
Requires: php-pcre
Requires: php-reflection
Requires: php-spl
# Optional
Requires: %{name}-Process = %{version}-%{release}

Provides: php-pear(%{pear_channel}/BrowserKit) = %{version}

%description BrowserKit
BrowserKit simulates the behavior of a web browser.

The component only provides an abstract client and does not provide any
"default" back-end for the HTTP layer.

%files BrowserKit
%doc src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/composer.json
%doc src/Symfony/Component/BrowserKit/*.md
%{_datadir}/php/Symfony/Component/BrowserKit
%exclude %{_datadir}/php/Symfony/Component/BrowserKit/Tests

#-------------------------------------------------------------------------------

%package BrowserKit-tests

Summary: Test suite for %{name}-BrowserKit
Group:   Development/Libraries

Requires: %{name}-BrowserKit = %{version}-%{release}

%description BrowserKit-tests
%{summary}.

%files BrowserKit-tests
%{_datadir}/php/Symfony/Component/BrowserKit/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-BrowserKit-tests

#-------------------------------------------------------------------------------

%package ClassLoader

Summary:  Symfony2 ClassLoader Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/class_loader.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-date
Requires: php-pcre
Requires: php-spl
Requires: php-reflection
Requires: php-tokenizer

Provides: php-pear(%{pear_channel}/ClassLoader) = %{version}

%description ClassLoader
The ClassLoader Component loads your project classes automatically if they
follow some standard PHP conventions.

Whenever you use an undefined class, PHP uses the auto-loading mechanism to
delegate the loading of a file defining the class. Symfony2 provides a
"universal" auto-loader, which is able to load classes from files that
implement one of the following conventions:

* The technical interoperability standards (http://symfony.com/PSR0) for
  PHP 5.3 name-spaces and class names.

* The PEAR (http://pear.php.net/manual/en/standards.php) naming convention for
  classes.

If your classes and the third-party libraries you use for your project follow
these standards, the Symfony2 auto-loader is the only auto-loader you will
ever need.

Optional dependencies: APC, XCache

%files ClassLoader
%doc src/Symfony/Component/ClassLoader/LICENSE
%doc src/Symfony/Component/ClassLoader/composer.json
%doc src/Symfony/Component/ClassLoader/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/ClassLoader
%exclude %{_datadir}/php/Symfony/Component/ClassLoader/Tests

#-------------------------------------------------------------------------------

%package ClassLoader-tests

Summary: Test suite for %{name}-ClassLoader
Group:   Development/Libraries

Requires: %{name}-ClassLoader = %{version}-%{release}

%description ClassLoader-tests
%{summary}.

%files ClassLoader-tests
%{_datadir}/php/Symfony/Component/ClassLoader/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-ClassLoader-tests

#-------------------------------------------------------------------------------

%package Config

Summary:  Symfony2 Config Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/config/index.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

Provides: php-pear(%{pear_channel}/Config) = %{version}

%description Config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

%files Config
%doc src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/composer.json
%doc src/Symfony/Component/Config/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Config
%exclude %{_datadir}/php/Symfony/Component/Config/Tests

#-------------------------------------------------------------------------------

%package Config-tests

Summary: Test suite for %{name}-Config
Group:   Development/Libraries

Requires: %{name}-Config = %{version}-%{release}

%description Config-tests
%{summary}.

%files Config-tests
%{_datadir}/php/Symfony/Component/Config/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Config-tests

#-------------------------------------------------------------------------------

%package Console

Summary:  Symfony2 Console Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/console.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-dom
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-readline
Requires: php-reflection
Requires: php-spl

Provides: php-pear(%{pear_channel}/Console) = %{version}

%description Console
The Console component eases the creation of beautiful and testable command line
interfaces.

The Console component allows you to create command-line commands. Your console
commands can be used for any recurring task, such as cron jobs, imports, or
other batch jobs.

%files Console
%doc src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/composer.json
%doc src/Symfony/Component/Console/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Console
%exclude %{_datadir}/php/Symfony/Component/Console/Tests

#-------------------------------------------------------------------------------

%package Console-tests

Summary: Test suite for %{name}-Console
Group:   Development/Libraries

Requires: %{name}-Console = %{version}-%{release}

%description Console-tests
%{summary}.

%files Console-tests
%{_datadir}/php/Symfony/Component/Console/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Console-tests

#-------------------------------------------------------------------------------

%package CssSelector

Summary:  Symfony2 CssSelector Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/css_selector.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-mbstring
Requires: php-pcre
Requires: php-spl

Provides: php-pear(%{pear_channel}/CssSelector) = %{version}

%description CssSelector
The CssSelector Component converts CSS selectors to XPath expressions.

%files CssSelector
%doc src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/composer.json
%doc src/Symfony/Component/CssSelector/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/CssSelector
%exclude %{_datadir}/php/Symfony/Component/CssSelector/Tests

#-------------------------------------------------------------------------------

%package CssSelector-tests

Summary: Test suite for %{name}-CssSelector
Group:   Development/Libraries

Requires: %{name}-CssSelector = %{version}-%{release}

%description CssSelector-tests
%{summary}.

%files CssSelector-tests
%{_datadir}/php/Symfony/Component/CssSelector/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-CssSelector-tests

#-------------------------------------------------------------------------------

%package DependencyInjection

Summary:  Symfony2 DependencyInjection Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/dependency_injection/index.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-dom
Requires: php-libxml
Requires: php-pcre
Requires: php-pecl(phar)
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl
# Optional
Requires: %{name}-Config = %{version}-%{release}
Requires: %{name}-Yaml = %{version}-%{release}

Provides: php-pear(%{pear_channel}/DependencyInjection) = %{version}

%description DependencyInjection
The Dependency Injection component allows you to standardize and centralize the
way objects are constructed in your application.

For an introduction to Dependency Injection and service containers see
Service Container (http://symfony.com/doc/current/book/service_container.html).

%files DependencyInjection
%doc src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/composer.json
%doc src/Symfony/Component/DependencyInjection/*.md
%{_datadir}/php/Symfony/Component/DependencyInjection
%exclude %{_datadir}/php/Symfony/Component/DependencyInjection/Tests

#-------------------------------------------------------------------------------

%package DependencyInjection-tests

Summary: Test suite for %{name}-DependencyInjection
Group:   Development/Libraries

Requires: %{name}-DependencyInjection = %{version}-%{release}

%description DependencyInjection-tests
%{summary}.

%files DependencyInjection-tests
%{_datadir}/php/Symfony/Component/DependencyInjection/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-DependencyInjection-tests

#-------------------------------------------------------------------------------

%package DomCrawler

Summary:  Symfony2 DomCrawler Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/dom_crawler.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-dom
Requires: php-libxml
Requires: php-mbstring
Requires: php-pcre
Requires: php-spl
# Optional
Requires: %{name}-CssSelector = %{version}-%{release}

Provides: php-pear(%{pear_channel}/DomCrawler) = %{version}

%description DomCrawler
The DomCrawler Component eases DOM navigation for HTML and XML documents.

%files DomCrawler
%doc src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/composer.json
%doc src/Symfony/Component/DomCrawler/*.md
%{_datadir}/php/Symfony/Component/DomCrawler
%exclude %{_datadir}/php/Symfony/Component/DomCrawler/Tests

#-------------------------------------------------------------------------------

%package DomCrawler-tests

Summary: Test suite for %{name}-DomCrawler
Group:   Development/Libraries

Requires: %{name}-DomCrawler = %{version}-%{release}

%description DomCrawler-tests
%{summary}.

%files DomCrawler-tests
%{_datadir}/php/Symfony/Component/DomCrawler/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-DomCrawler-tests

#-------------------------------------------------------------------------------

%package EventDispatcher

Summary:  Symfony2 EventDispatcher Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/event_dispatcher/index.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-spl
# Optional
Requires: %{name}-DependencyInjection = %{version}-%{release}
Requires: %{name}-HttpKernel = %{version}-%{release}

Provides: php-pear(%{pear_channel}/EventDispatcher) = %{version}

%description EventDispatcher
The Symfony2 Event Dispatcher component implements the Observer
(http://en.wikipedia.org/wiki/Observer_pattern) pattern in a simple and
effective way to make all these things possible and to make your projects
truly extensible.

Take a simple example from the Symfony2 HttpKernel component. Once a Response
object has been created, it may be useful to allow other elements in the system
to modify it (e.g. add some cache headers) before it's actually used. To make
this possible, the Symfony2 kernel throws an event - kernel.response. Here's
how it works:

* A listener (PHP object) tells a central dispatcher object that it wants to
  listen to the kernel.response event;
* At some point, the Symfony2 kernel tells the dispatcher object to dispatch
  the kernel.response event, passing with it an Event object that has access to
  the Response object;
* The dispatcher notifies (i.e. calls a method on) all listeners of the
  kernel.response event, allowing each of them to make modifications to the
  Response object.

%files EventDispatcher
%doc src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/composer.json
%doc src/Symfony/Component/EventDispatcher/*.md
%{_datadir}/php/Symfony/Component/EventDispatcher
%exclude %{_datadir}/php/Symfony/Component/EventDispatcher/Tests

#-------------------------------------------------------------------------------

%package EventDispatcher-tests

Summary: Test suite for %{name}-EventDispatcher
Group:   Development/Libraries

Requires: %{name}-EventDispatcher = %{version}-%{release}

%description EventDispatcher-tests
%{summary}.

%files EventDispatcher-tests
%{_datadir}/php/Symfony/Component/EventDispatcher/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-EventDispatcher-tests

#-------------------------------------------------------------------------------

%package Filesystem

Summary:  Symfony2 Filesystem Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/filesystem.html

Requires: %{name}-common = %{version}-%{release}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-posix
Requires: php-spl

Provides: php-pear(%{pear_channel}/Filesystem) = %{version}

%description Filesystem
The Filesystem component provides basic utilities for the filesystem.

%files Filesystem
%doc src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/composer.json
%doc src/Symfony/Component/Filesystem/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Filesystem
%exclude %{_datadir}/php/Symfony/Component/Filesystem/Tests

#-------------------------------------------------------------------------------

%package Filesystem-tests

Summary: Test suite for %{name}-Filesystem
Group:   Development/Libraries

Requires: %{name}-Filesystem = %{version}-%{release}

%description Filesystem-tests
%{summary}.

%files Filesystem-tests
%{_datadir}/php/Symfony/Component/Filesystem/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Filesystem-tests

#-------------------------------------------------------------------------------

%package Finder

Summary:  Symfony2 Finder Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/finder.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-date
Requires: php-pcre
Requires: php-spl

Provides: php-pear(%{pear_channel}/Finder) = %{version}

%description Finder
The Finder Component finds files and directories via an intuitive fluent
interface.

%files Finder
%doc src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/composer.json
%doc src/Symfony/Component/Finder/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Finder
%exclude %{_datadir}/php/Symfony/Component/Finder/Tests

#-------------------------------------------------------------------------------

%package Finder-tests

Summary: Test suite for %{name}-Finder
Group:   Development/Libraries

Requires: %{name}-Finder = %{version}-%{release}

%description Finder-tests
%{summary}.

%files Finder-tests
%{_datadir}/php/Symfony/Component/Finder/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Finder-tests

#-------------------------------------------------------------------------------

%package Form

Summary:  Symfony2 Form Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
Requires: %{name}-EventDispatcher = %{version}-%{release}
Requires: %{name}-Locale = %{version}-%{release}
Requires: %{name}-OptionsResolver = %{version}-%{release}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-dom
Requires: php-intl
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-session
Requires: php-spl
# Optional
Requires: %{name}-HttpFoundation = %{version}-%{release}
Requires: %{name}-Validator = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Form) = %{version}

%description Form
Form provides tools for defining forms, rendering and binding request data
to related models. Furthermore it provides integration with the Validation
component.

%files Form
%doc src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/composer.json
%doc src/Symfony/Component/Form/*.md
%{_datadir}/php/Symfony/Component/Form
%exclude %{_datadir}/php/Symfony/Component/Form/Tests

#-------------------------------------------------------------------------------

%package Form-tests

Summary: Test suite for %{name}-Form
Group:   Development/Libraries

Requires: %{name}-Form = %{version}-%{release}

%description Form-tests
%{summary}.

%files Form-tests
%{_datadir}/php/Symfony/Component/Form/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Form-tests

#-------------------------------------------------------------------------------

%package HttpFoundation

Summary:  Symfony2 HttpFoundation Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/http_foundation/index.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-date
Requires: php-fileinfo
Requires: php-json
Requires: php-pcre
Requires: php-pdo
Requires: php-reflection
Requires: php-session
Requires: php-sockets
Requires: php-spl
%{?fedora:Requires: php-filter}

Provides: php-pear(%{pear_channel}/HttpFoundation) = %{version}

%description HttpFoundation
The HttpFoundation Component defines an object-oriented layer for the HTTP
specification.

In PHP, the request is represented by some global variables ($_GET, $_POST,
$_FILE, $_COOKIE, $_SESSION...) and the response is generated by some functions
(echo, header, setcookie, ...).

The Symfony2 HttpFoundation component replaces these default PHP global
variables and functions by an Object-Oriented layer.

Optional dependencies: memcache, memcached, mongo

%files HttpFoundation
%doc src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/composer.json
%doc src/Symfony/Component/HttpFoundation/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/HttpFoundation
%exclude %{_datadir}/php/Symfony/Component/HttpFoundation/Tests

#-------------------------------------------------------------------------------

%package HttpFoundation-tests

Summary: Test suite for %{name}-HttpFoundation
Group:   Development/Libraries

Requires: %{name}-HttpFoundation = %{version}-%{release}

%description HttpFoundation-tests
%{summary}.

%files HttpFoundation-tests
%{_datadir}/php/Symfony/Component/HttpFoundation/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-HttpFoundation-tests

#-------------------------------------------------------------------------------

%package HttpKernel

Summary:  Symfony2 HttpKernel Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
Requires: %{name}-EventDispatcher = %{version}-%{release}
Requires: %{name}-HttpFoundation = %{version}-%{release}
# phpci
Requires: php-date
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-pdo
Requires: php-pdo_mysql
Requires: php-pdo_sqlite
Requires: php-reflection
Requires: php-session
Requires: php-spl
Requires: php-tokenizer
# Optional
Requires: %{name}-BrowserKit = %{version}-%{release}
Requires: %{name}-ClassLoader = %{version}-%{release}
Requires: %{name}-Config = %{version}-%{release}
Requires: %{name}-Console = %{version}-%{release}
Requires: %{name}-DependencyInjection = %{version}-%{release}
Requires: %{name}-Finder = %{version}-%{release}

Provides: php-pear(%{pear_channel}/HttpKernel) = %{version}

%description HttpKernel
HttpKernel provides the building blocks to create flexible and fast
HTTP-based frameworks.

It takes a Request as an input and should return a Response as an output.
Using this interface makes your code compatible with all frameworks using
the Symfony2 components. And this will give you many cool features for free.

Optional dependencies: memcache, memcached, mongo

%files HttpKernel
%doc src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/composer.json
%doc src/Symfony/Component/HttpKernel/*.md
%{_datadir}/php/Symfony/Component/HttpKernel
%exclude %{_datadir}/php/Symfony/Component/HttpKernel/Tests

#-------------------------------------------------------------------------------

%package HttpKernel-tests

Summary: Test suite for %{name}-HttpKernel
Group:   Development/Libraries

Requires: %{name}-HttpKernel = %{version}-%{release}

%description HttpKernel-tests
%{summary}.

%files HttpKernel-tests
%{_datadir}/php/Symfony/Component/HttpKernel/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-HttpKernel-tests

#-------------------------------------------------------------------------------

%package Locale

Summary:  Symfony2 Locale Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/locale.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-intl
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl

Provides: php-pear(%{pear_channel}/Locale) = %{version}

%description Locale
Locale component provides fallback code to handle cases when the intl extension
is missing. Additionally it extends the implementation of a native Locale
(http://php.net/manual/en/class.locale.php) class with several handy methods.

Replacement for the following functions and classes is provided:

* intl_is_failure
* intl_get_error_code
* intl_get_error_message
* Collator
* IntlDateFormatter
* Locale
* NumberFormatter

Stub implementation only supports the en locale.

%files Locale
%doc src/Symfony/Component/Locale/LICENSE
%doc src/Symfony/Component/Locale/composer.json
%doc src/Symfony/Component/Locale/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Locale
# TODO: LANG FILES!!! -- http://pkgs.fedoraproject.org/cgit/php-symfony2-Locale.git/tree/php-symfony2-Locale.spec
%exclude %{_datadir}/php/Symfony/Component/Locale/Tests

#-------------------------------------------------------------------------------

%package Locale-tests

Summary: Test suite for %{name}-Locale
Group:   Development/Libraries

Requires: %{name}-Locale = %{version}-%{release}

%description Locale-tests
%{summary}.

%files Locale-tests
%{_datadir}/php/Symfony/Component/Locale/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Locale-tests

#-------------------------------------------------------------------------------

%package OptionsResolver

Summary:  Symfony2 OptionsResolver Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-reflection
Requires: php-spl

Provides: php-pear(%{pear_channel}/OptionsResolver) = %{version}

%description OptionsResolver
OptionsResolver helps at configuring objects with option arrays.

It supports default values on different levels of your class hierarchy, option
constraints (required vs. optional, allowed values) and lazy options whose
default value depends on the value of another option.

%files OptionsResolver
%doc src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/composer.json
%doc src/Symfony/Component/OptionsResolver/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/OptionsResolver
%exclude %{_datadir}/php/Symfony/Component/OptionsResolver/Tests

#-------------------------------------------------------------------------------

%package OptionsResolver-tests

Summary: Test suite for %{name}-OptionsResolver
Group:   Development/Libraries

Requires: %{name}-OptionsResolver = %{version}-%{release}

%description OptionsResolver-tests
%{summary}.

%files OptionsResolver-tests
%{_datadir}/php/Symfony/Component/OptionsResolver/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-OptionsResolver-tests

#-------------------------------------------------------------------------------

%package Process

Summary:  Symfony2 Process Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/process.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-pcntl
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

Provides: php-pear(%{pear_channel}/Process) = %{version}

%description Process
%{summary}.

%files Process
%doc src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/composer.json
%doc src/Symfony/Component/Process/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Process
%exclude %{_datadir}/php/Symfony/Component/Process/Tests

#-------------------------------------------------------------------------------

%package Process-tests

Summary: Test suite for %{name}-Process
Group:   Development/Libraries

Requires: %{name}-Process = %{version}-%{release}

%description Process-tests
%{summary}.

%files Process-tests
%{_datadir}/php/Symfony/Component/Process/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Process-tests

#-------------------------------------------------------------------------------

%package Routing

Summary:  Symfony2 Routing Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/routing.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-dom
Requires: php-libxml
Requires: php-pcre
Requires: php-reflection
Requires: php-spl
Requires: php-tokenizer
# Optional
Requires: %{name}-Config = %{version}-%{release}
Requires: %{name}-Yaml = %{version}-%{release}
Requires: php-pear(pear.doctrine-project.org/DoctrineCommon) >= 2.2
Requires: php-pear(pear.doctrine-project.org/DoctrineCommon) <  2.4

Provides: php-pear(%{pear_channel}/Routing) = %{version}

%description Routing
The Routing Component maps an HTTP request to a set of configuration variables.

%files Routing
%doc src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/composer.json
%doc src/Symfony/Component/Routing/*.md
%{_datadir}/php/Symfony/Component/Routing
%exclude %{_datadir}/php/Symfony/Component/Routing/Tests

#-------------------------------------------------------------------------------

%package Routing-tests

Summary: Test suite for %{name}-Routing
Group:   Development/Libraries

Requires: %{name}-Routing = %{version}-%{release}

%description Routing-tests
%{summary}.

%files Routing-tests
%{_datadir}/php/Symfony/Component/Routing/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Routing-tests

#-------------------------------------------------------------------------------

%package Security

Summary:  Symfony2 Security Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
Requires: %{name}-EventDispatcher = %{version}-%{release}
Requires: %{name}-HttpFoundation = %{version}-%{release}
Requires: %{name}-HttpKernel = %{version}-%{release}
# phpci
Requires: php-date
Requires: php-hash
Requires: php-json
Requires: php-openssl
Requires: php-pcre
Requires: php-pdo
Requires: php-reflection
Requires: php-spl
# Optional
Requires: %{name}-ClassLoader = %{version}-%{release}
Requires: %{name}-Finder = %{version}-%{release}
Requires: %{name}-Form = %{version}-%{release}
Requires: %{name}-Routing = %{version}-%{release}
Requires: %{name}-Validator = %{version}-%{release}
# TODO: Add DoctrineDBAL (>=2.2,<2.4-dev) when available

Provides: php-pear(%{pear_channel}/Security) = %{version}

%description Security
Security provides an infrastructure for sophisticated authorization systems,
which makes it possible to easily separate the actual authorization logic from
so called user providers that hold the users credentials. It is inspired by
the Java Spring framework.

Optional dependencies: DoctrineCommon and DoctrineDBAL

%files Security
%doc src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/composer.json
%doc src/Symfony/Component/Security/*.md
%{_datadir}/php/Symfony/Component/Security
%exclude %{_datadir}/php/Symfony/Component/Security/Tests

#-------------------------------------------------------------------------------

%package Security-tests

Summary: Test suite for %{name}-Security
Group:   Development/Libraries

Requires: %{name}-Security = %{version}-%{release}

%description Security-tests
%{summary}.

%files Security-tests
%{_datadir}/php/Symfony/Component/Security/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Security-tests

#-------------------------------------------------------------------------------

%package Serializer

Summary:  Symfony2 Serializer Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-dom
Requires: php-json
Requires: php-libxml
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl

Provides: php-pear(%{pear_channel}/Serializer) = %{version}

%description Serializer
With the Serializer component it's possible to handle serializing data
structures, including object graphs, into array structures or other
formats like XML and JSON.  It can also handle deserializing XML and
JSON back to object graphs.

%files Serializer
%doc src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/composer.json
%doc src/Symfony/Component/Serializer/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Serializer
%exclude %{_datadir}/php/Symfony/Component/Serializer/Tests

#-------------------------------------------------------------------------------

%package Serializer-tests

Summary: Test suite for %{name}-Serializer
Group:   Development/Libraries

Requires: %{name}-Serializer = %{version}-%{release}

%description Serializer-tests
%{summary}.

%files Serializer-tests
%{_datadir}/php/Symfony/Component/Serializer/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Serializer-tests

#-------------------------------------------------------------------------------

%package Templating

Summary:  Symfony2 Templating Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/templating.html

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-iconv
Requires: php-mbstring
Requires: php-pcre
Requires: php-spl

Provides: php-pear(%{pear_channel}/Templating) = %{version}

%description Templating
Templating provides all the tools needed to build any kind of template system.

It provides an infrastructure to load template files and optionally monitor
them for changes. It also provides a concrete template engine implementation
using PHP with additional tools for escaping and separating templates into
blocks and layouts.

%files Templating
%doc src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/composer.json
%doc src/Symfony/Component/Templating/*.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Component
     %{_datadir}/php/Symfony/Component/Templating
%exclude %{_datadir}/php/Symfony/Component/Templating/Tests

#-------------------------------------------------------------------------------

%package Templating-tests

Summary: Test suite for %{name}-Templating
Group:   Development/Libraries

Requires: %{name}-Templating = %{version}-%{release}

%description Templating-tests
%{summary}.

%files Templating-tests
%{_datadir}/php/Symfony/Component/Templating/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Templating-tests

#-------------------------------------------------------------------------------

%package Translation

Summary:  Symfony2 Translation Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-dom
Requires: php-intl
Requires: php-libxml
Requires: php-mbstring
Requires: php-pcre
Requires: php-simplexml
Requires: php-spl
# Optional
Requires: %{name}-Config = %{version}-%{release}
Requires: %{name}-Yaml = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Translation) = %{version}

%description Translation
Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

%files Translation
%doc src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/composer.json
%doc src/Symfony/Component/Translation/*.md
%{_datadir}/php/Symfony/Component/Translation
%exclude %{_datadir}/php/Symfony/Component/Translation/Tests

#-------------------------------------------------------------------------------

%package Translation-tests

Summary: Test suite for %{name}-Translation
Group:   Development/Libraries

Requires: %{name}-Translation = %{version}-%{release}

%description Translation-tests
%{summary}.

%files Translation-tests
%{_datadir}/php/Symfony/Component/Translation/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Translation-tests

#-------------------------------------------------------------------------------

%package Validator

Summary:  Symfony2 Validator Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-dom
Requires: php-intl
Requires: php-libxml
Requires: php-mbstring
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl
%{?fedora:Requires: php-filter}
# Optional
Requires: %{name}-HttpFoundation = %{version}-%{release}
Requires: %{name}-Yaml = %{version}-%{release}
Requires: php-pear(pear.doctrine-project.org/DoctrineCommon) >= 2.1
Requires: php-pear(pear.doctrine-project.org/DoctrineCommon) <  2.4

Provides: php-pear(%{pear_channel}/Validator) = %{version}

%description Validator
This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

%files Validator
%doc src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/composer.json
%doc src/Symfony/Component/Validator/*.md
%{_datadir}/php/Symfony/Component/Validator
%exclude %{_datadir}/php/Symfony/Component/Validator/Tests

#-------------------------------------------------------------------------------

%package Validator-tests

Summary: Test suite for %{name}-Validator
Group:   Development/Libraries

Requires: %{name}-Validator = %{version}-%{release}

%description Validator-tests
%{summary}.

%files Validator-tests
%{_datadir}/php/Symfony/Component/Validator/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Validator-tests

#-------------------------------------------------------------------------------

%package Yaml
Summary:  Symfony2 Yaml Component
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}
# phpci
Requires: php-ctype
Requires: php-date
Requires: php-iconv
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-spl

Provides: php-pear(%{pear_channel}/Yaml) = %{version}

%description Yaml
The Symfony2 YAML Component parses YAML strings to convert them to PHP arrays.
It is also able to convert PHP arrays to YAML strings.

YAML, YAML Ain't Markup Language, is a human friendly data serialization
standard for all programming languages. YAML is a great format for your
configuration files. YAML files are as expressive as XML files and as readable
as INI files.

The Symfony2 YAML Component implements the YAML 1.2 version of the
specification.

%files Yaml
%doc src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/composer.json
%doc src/Symfony/Component/Yaml/*.md
%{_datadir}/php/Symfony/Component/Yaml
%exclude %{_datadir}/php/Symfony/Component/Yaml/Tests

#-------------------------------------------------------------------------------

%package Yaml-tests

Summary: Test suite for %{name}-Yaml
Group:   Development/Libraries

Requires: %{name}-Yaml = %{version}-%{release}

%description Yaml-tests
%{summary}.

%files Yaml-tests
%{_datadir}/php/Symfony/Component/Yaml/Tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}-Yaml-tests

#-------------------------------------------------------------------------------

%package DoctrineBridge
Summary:  Symfony2 Doctrine Bridge
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

Provides: php-pear(%{pear_channel}/DoctrineBridge) = %{version}

%description DoctrineBridge
%{summary}.

%files DoctrineBridge
%doc src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/composer.json
%doc src/Symfony/Bridge/Doctrine/*.md
%{_datadir}/php/Symfony/Bridge/Doctrine

#-------------------------------------------------------------------------------

%package MonologBridge
Summary:  Symfony2 Monolog Bridge
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

Provides: php-pear(%{pear_channel}/MonologBridge) = %{version}

%description MonologBridge
%{summary}.

%files MonologBridge
%doc src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/composer.json
%doc src/Symfony/Bridge/Monolog/*.md
%{_datadir}/php/Symfony/Bridge/Monolog

#-------------------------------------------------------------------------------

%package Propel1Bridge
Summary:  Symfony2 Propel1 Bridge
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

Provides: php-pear(%{pear_channel}/Propel1Bridge) = %{version}

%description Propel1Bridge
%{summary}.

%files Propel1Bridge
%doc src/Symfony/Bridge/Propel1/LICENSE
%doc src/Symfony/Bridge/Propel1/composer.json
%doc src/Symfony/Bridge/Propel1/*.md
%{_datadir}/php/Symfony/Bridge/Propel1

#-------------------------------------------------------------------------------

%package SwiftmailerBridge
Summary:  Symfony2 Swiftmailer Bridge
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

Provides: php-pear(%{pear_channel}/SwiftmailerBridge) = %{version}

%description SwiftmailerBridge
%{summary}.

%files SwiftmailerBridge
%doc src/Symfony/Bridge/Swiftmailer/LICENSE
%doc src/Symfony/Bridge/Swiftmailer/composer.json
%doc src/Symfony/Bridge/Swiftmailer/*.md
%{_datadir}/php/Symfony/Bridge/Swiftmailer

#-------------------------------------------------------------------------------

%package TwigBridge
Summary:  Symfony2 Twig Bridge
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

Provides: php-pear(%{pear_channel}/TwigBridge) = %{version}

%description TwigBridge
%{summary}.

%files TwigBridge
%doc src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/composer.json
%doc src/Symfony/Bridge/Twig/*.md
%{_datadir}/php/Symfony/Bridge/Twig

#-------------------------------------------------------------------------------

%package FrameworkBundle
Summary:  Symfony2 Framework Bundle
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

%description FrameworkBundle
%{summary}.

%files FrameworkBundle
%doc src/Symfony/Bundle/FrameworkBundle/LICENSE
%doc src/Symfony/Bundle/FrameworkBundle/composer.json
%doc src/Symfony/Bundle/FrameworkBundle/*.md
%{_datadir}/php/Symfony/Bundle/FrameworkBundle

#-------------------------------------------------------------------------------

%package SecurityBundle
Summary:  Symfony2 Security Bundle
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

%description SecurityBundle
%{summary}.

%files SecurityBundle
%doc src/Symfony/Bundle/SecurityBundle/LICENSE
%doc src/Symfony/Bundle/SecurityBundle/composer.json
%doc src/Symfony/Bundle/SecurityBundle/*.md
%{_datadir}/php/Symfony/Bundle/SecurityBundle

#-------------------------------------------------------------------------------

%package TwigBundle
Summary:  Symfony2 Twig Bundle
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

%description TwigBundle
%{summary}.

%files TwigBundle
%doc src/Symfony/Bundle/TwigBundle/LICENSE
%doc src/Symfony/Bundle/TwigBundle/composer.json
%doc src/Symfony/Bundle/TwigBundle/*.md
%{_datadir}/php/Symfony/Bundle/TwigBundle

#-------------------------------------------------------------------------------

%package WebProfilerBundle
Summary:  Symfony2 WebProfiler Bundle
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

%description WebProfilerBundle
%{summary}.

%files WebProfilerBundle
%doc src/Symfony/Bundle/WebProfilerBundle/LICENSE
%doc src/Symfony/Bundle/WebProfilerBundle/composer.json
%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%{_datadir}/php/Symfony/Bundle/WebProfilerBundle

#-------------------------------------------------------------------------------

%prep
%setup -q -n %{github_name}-%{github_commit}

# Remove unnecessary files
find src -name '.git*' -delete

#-------------------------------------------------------------------------------

%build
# Empty build section, nothing to build

#-------------------------------------------------------------------------------

%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/Symfony %{buildroot}%{_datadir}/php

# Remove doc files (already marked as %%doc in %%files)
find %{buildroot}%{_datadir}/php -name 'LICENSE' -delete
find %{buildroot}%{_datadir}/php -name 'composer.json' -delete
find %{buildroot}%{_datadir}/php -name '*.md' -delete

#-------------------------------------------------------------------------------

%check

#-------------------------------------------------------------------------------

%changelog
* Tue Jan 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.1.6-1
- Initial package