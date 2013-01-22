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

#-------------------------------------------------------------------------------

%package common

Summary:  Common files for %{name}
Group:    Development/Libraries

Requires: php-common >= %{php_min_ver}

%description common
%{summary}.

%files common
%doc LICENSE *.md
%dir %{_datadir}/php/Symfony
%dir %{_datadir}/php/Symfony/Bridge
%dir %{_datadir}/php/Symfony/Bundle
%dir %{_datadir}/php/Symfony/Component

#-------------------------------------------------------------------------------

%package BrowserKit

Summary:  Symfony2 BrowserKit Component
Group:    Development/Libraries
URL:      http://symfony.com/components

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-DomCrawler = %{version}-%{release}
# phpci requires
Requires: php-date
Requires: php-pcre
Requires: php-reflection
Requires: php-spl
# Optional requires
Requires: %{name}-Process = %{version}-%{release}

Provides: php-pear(%{pear_channel}/BrowserKit)
Provides: php-composer(symfony/browser-kit)

%description BrowserKit
BrowserKit simulates the behavior of a web browser.

The component only provides an abstract client and does not provide any
"default" back-end for the HTTP layer.

%files BrowserKit
%doc src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/composer.json
%doc src/Symfony/Component/BrowserKit/*.md
%{_datadir}/php/Symfony/Component/BrowserKit

#-------------------------------------------------------------------------------

%package ClassLoader

Summary:  Symfony2 ClassLoader Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/class_loader.html

Requires: %{name}-common = %{version}-%{release}
# phpci requires
Requires: php-date
Requires: php-pcre
Requires: php-spl
Requires: php-reflection
Requires: php-tokenizer

Provides: php-pear(%{pear_channel}/ClassLoader)
Provides: php-composer(symfony/class-loader)

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
%{_datadir}/php/Symfony/Component/ClassLoader

#-------------------------------------------------------------------------------

%package Config

Summary:  Symfony2 Config Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/config/index.html

Requires: %{name}-common = %{version}-%{release}
# phpci requires
Requires: php-ctype
Requires: php-date
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

Provides: php-pear(%{pear_channel}/Config)
Provides: php-composer(symfony/config)

%description Config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

%files Config
%doc src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/composer.json
%doc src/Symfony/Component/Config/*.md
%{_datadir}/php/Symfony/Component/Config

#-------------------------------------------------------------------------------

%package Console

Summary:  Symfony2 Console Component
Group:    Development/Libraries
URL:      http://symfony.com/doc/current/components/console.html

Requires: %{name}-common = %{version}-%{release}
# phpci requires
Requires: php-dom
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-readline
Requires: php-reflection
Requires: php-spl

Provides: php-pear(%{pear_channel}/Console)
Provides: php-composer(symfony/console)

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
%{_datadir}/php/Symfony/Component/Console

#-------------------------------------------------------------------------------

%package CssSelector
Summary:  Symfony2 CssSelector Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/CssSelector)

%description CssSelector
%{summary}.

%files CssSelector
%doc src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/composer.json
%doc src/Symfony/Component/CssSelector/*.md
%{_datadir}/php/Symfony/Component/CssSelector

#-------------------------------------------------------------------------------

%package DependencyInjection
Summary:  Symfony2 DependencyInjection Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/DependencyInjection)

%description DependencyInjection
%{summary}.

%files DependencyInjection
%doc src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/composer.json
%doc src/Symfony/Component/DependencyInjection/*.md
%{_datadir}/php/Symfony/Component/DependencyInjection

#-------------------------------------------------------------------------------

%package DomCrawler
Summary:  Symfony2 DomCrawler Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/DomCrawler)

%description DomCrawler
%{summary}.

%files DomCrawler
%doc src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/composer.json
%doc src/Symfony/Component/DomCrawler/*.md
%{_datadir}/php/Symfony/Component/DomCrawler

#-------------------------------------------------------------------------------

%package EventDispatcher
Summary:  Symfony2 EventDispatcher Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/EventDispatcher)

%description EventDispatcher
%{summary}.

%files EventDispatcher
%doc src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/composer.json
%doc src/Symfony/Component/EventDispatcher/*.md
%{_datadir}/php/Symfony/Component/EventDispatcher

#-------------------------------------------------------------------------------

%package Filesystem
Summary:  Symfony2 Filesystem Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Filesystem)

%description Filesystem
%{summary}.

%files Filesystem
%doc src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/composer.json
%doc src/Symfony/Component/Filesystem/*.md
%{_datadir}/php/Symfony/Component/Filesystem

#-------------------------------------------------------------------------------

%package Finder
Summary:  Symfony2 Finder Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Finder)

%description Finder
%{summary}.

%files Finder
%doc src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/composer.json
%doc src/Symfony/Component/Finder/*.md
%{_datadir}/php/Symfony/Component/Finder

#-------------------------------------------------------------------------------

%package Form
Summary:  Symfony2 Form Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Form)

%description Form
%{summary}.

%files Form
%doc src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/composer.json
%doc src/Symfony/Component/Form/*.md
%{_datadir}/php/Symfony/Component/Form

#-------------------------------------------------------------------------------

%package HttpFoundation
Summary:  Symfony2 HttpFoundation Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/HttpFoundation)

%description HttpFoundation
%{summary}.

%files HttpFoundation
%doc src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/composer.json
%doc src/Symfony/Component/HttpFoundation/*.md
%{_datadir}/php/Symfony/Component/HttpFoundation

#-------------------------------------------------------------------------------

%package HttpKernel
Summary:  Symfony2 HttpKernel Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/HttpKernel)

%description HttpKernel
%{summary}.

%files HttpKernel
%doc src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/composer.json
%doc src/Symfony/Component/HttpKernel/*.md
%{_datadir}/php/Symfony/Component/HttpKernel

#-------------------------------------------------------------------------------

%package Locale
Summary:  Symfony2 Locale Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Locale)

%description Locale
%{summary}.

%files Locale
%doc src/Symfony/Component/Locale/LICENSE
%doc src/Symfony/Component/Locale/composer.json
%doc src/Symfony/Component/Locale/*.md
%{_datadir}/php/Symfony/Component/Locale

#-------------------------------------------------------------------------------

%package OptionsResolver
Summary:  Symfony2 OptionsResolver Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/OptionsResolver)

%description OptionsResolver
%{summary}.

%files OptionsResolver
%doc src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/composer.json
%doc src/Symfony/Component/OptionsResolver/*.md
%{_datadir}/php/Symfony/Component/OptionsResolver

#-------------------------------------------------------------------------------

%package Process
Summary:  Symfony2 Process Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Process)

%description Process
%{summary}.

%files Process
%doc src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/composer.json
%doc src/Symfony/Component/Process/*.md
%{_datadir}/php/Symfony/Component/Process

#-------------------------------------------------------------------------------

%package Routing
Summary:  Symfony2 Routing Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Routing)

%description Routing
%{summary}.

%files Routing
%doc src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/composer.json
%doc src/Symfony/Component/Routing/*.md
%{_datadir}/php/Symfony/Component/Routing

#-------------------------------------------------------------------------------

%package Security
Summary:  Symfony2 Security Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Security)

%description Security
%{summary}.

%files Security
%doc src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/composer.json
%doc src/Symfony/Component/Security/*.md
%{_datadir}/php/Symfony/Component/Security

#-------------------------------------------------------------------------------

%package Serializer
Summary:  Symfony2 Serializer Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Serializer)

%description Serializer
%{summary}.

%files Serializer
%doc src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/composer.json
%doc src/Symfony/Component/Serializer/*.md
%{_datadir}/php/Symfony/Component/Serializer

#-------------------------------------------------------------------------------

%package Templating
Summary:  Symfony2 Templating Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Templating)

%description Templating
%{summary}.

%files Templating
%doc src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/composer.json
%doc src/Symfony/Component/Templating/*.md
%{_datadir}/php/Symfony/Component/Templating

#-------------------------------------------------------------------------------

%package Translation
Summary:  Symfony2 Translation Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Translation)

%description Translation
%{summary}.

%files Translation
%doc src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/composer.json
%doc src/Symfony/Component/Translation/*.md
%{_datadir}/php/Symfony/Component/Translation

#-------------------------------------------------------------------------------

%package Validator
Summary:  Symfony2 Validator Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Validator)

%description Validator
%{summary}.

%files Validator
%doc src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/composer.json
%doc src/Symfony/Component/Validator/*.md
%{_datadir}/php/Symfony/Component/Validator

#-------------------------------------------------------------------------------

%package Yaml
Summary:  Symfony2 Yaml Component
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Yaml)

%description Yaml
%{summary}.

%files Yaml
%doc src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/composer.json
%doc src/Symfony/Component/Yaml/*.md
%{_datadir}/php/Symfony/Component/Yaml

#-------------------------------------------------------------------------------

%package DoctrineBridge
Summary:  Symfony2 Doctrine Bridge
Group:    Development/Libraries
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/DoctrineBridge)

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
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/MonologBridge)

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
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/Propel1Bridge)

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
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/SwiftmailerBridge)

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
Requires: %{name}-common = %{version}-%{release}

Provides: php-pear(%{pear_channel}/TwigBridge)

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
Requires: %{name}-common = %{version}-%{release}

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
Requires: %{name}-common = %{version}-%{release}

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
Requires: %{name}-common = %{version}-%{release}

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
Requires: %{name}-common = %{version}-%{release}

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

# Remove doc files
find %{buildroot}%{_datadir}/php -name 'LICENSE' -delete
find %{buildroot}%{_datadir}/php -name 'composer.json' -delete
find %{buildroot}%{_datadir}/php -name '*.md' -delete

#-------------------------------------------------------------------------------

%check

#-------------------------------------------------------------------------------

%changelog
* Tue Jan 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.1.6-1
- Initial package