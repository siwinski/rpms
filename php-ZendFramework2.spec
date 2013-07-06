Name:             php-ZendFramework2
Version:          2.2.1
Release:          1%{?dist}
Summary:          Zend Framework 2

Group:            Development/Libraries
License:          BSD
URL:              http://framework.zend.com
Source0:          https://packages.zendframework.com/releases/ZendFramework-%{version}/ZendFramework-minimal-%{version}.tgz
Source1:          https://packages.zendframework.com/releases/ZendFramework-%{version}/ZendFramework-%{version}-manual-en.tgz
Source2:          https://packages.zendframework.com/releases/ZendFramework-%{version}/ZendFramework-%{version}-apidoc.tgz

BuildArch:        noarch

%description
Zend Framework 2 is an open source framework for developing web applications
and services using PHP 5.3+. Zend Framework 2 uses 100% object-oriented code
and utilises most of the new features of PHP 5.3, namely namespaces, late
static binding, lambda functions and closures.

Zend Framework 2 evolved from Zend Framework 1, a successful PHP framework
with over 15 million downloads.

# ##############################################################################

%package  common

Summary:  Zend Framework 2: Common files

Requires: php(language) >= 5.3.3

%description common
%{summary}.

# ------------------------------------------------------------------------------

%package  Authentication

Summary:  Zend Framework 2: Authentication Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.authentication.html

Requires: %{name}-common  = %{version}-%{release}
Requires: %{name}-Stdlib  = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Crypt   = %{version}-%{release}
Requires: %{name}-Db      = %{version}-%{release}
Requires: %{name}-Session = %{version}-%{release}
Requires: %{name}-Uri     = %{version}-%{release}

%description Authentication
%{summary}.

# ------------------------------------------------------------------------------

%package  Barcode

Summary:  Zend Framework 2: Barcode Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.barcode.html

Requires: %{name}-common   = %{version}-%{release}
Requires: %{name}-Stdlib   = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Validator = %{version}-%{release}
### TODO: ZendPdf

%description Barcode
%{summary}.

# ------------------------------------------------------------------------------

### TODO: SEPARATE OUT!!!

%package  Cache

Summary:  Zend Framework 2: Cache Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.cache.html

Requires: %{name}-common         = %{version}-%{release}
Requires: %{name}-EventManager   = %{version}-%{release}
Requires: %{name}-ServiceManager = %{version}-%{release}
Requires: %{name}-Stdlib         = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Serializer     = %{version}-%{release}
Requires: %{name}-Session        = %{version}-%{release}

%description Cache
%{summary}.

# ------------------------------------------------------------------------------

%package  Captcha

Summary:  Zend Framework 2: Captcha Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.captcha.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Math   = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
### TODO: zendframework/zend-resources
### TODO: zendframework/zendservice-recaptcha

%description Captcha
%{summary}.

# ------------------------------------------------------------------------------

%package  Code

Summary:  Zend Framework 2: Code Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.code.html

Requires: %{name}-common       = %{version}-%{release}
Requires: %{name}-EventManager = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: php-pear(pear.doctrine-project.org/DoctrineCommon) >= 2.1

%description Code
%{summary}.

# ------------------------------------------------------------------------------

%package  Config

Summary:  Zend Framework 2: Config Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.config.html

Requires: %{name}-common        = %{version}-%{release}
Requires: %{name}-Stdlib        = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Json           = %{version}-%{release}
Requires: %{name}-ServiceManager = %{version}-%{release}

%description Config
%{summary}.

# ------------------------------------------------------------------------------

%package  Console

Summary:  Zend Framework 2: Console Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.console.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description Console
%{summary}.

# ------------------------------------------------------------------------------

%package  Crypt

Summary:  Zend Framework 2: Crypt Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.crypt.html

Requires: %{name}-common         = %{version}-%{release}
Requires: %{name}-Math           = %{version}-%{release}
Requires: %{name}-ServiceManager = %{version}-%{release}
Requires: %{name}-Stdlib         = %{version}-%{release}
# phpci
Requires: php-

%description Crypt
%{summary}.

# ------------------------------------------------------------------------------

### TODO: SEPARATE OUT!!!

%package  Db

Summary:  Zend Framework 2: Db Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.db.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description Db
%{summary}.

# ------------------------------------------------------------------------------

%package  Debug

Summary:  Zend Framework 2: Debug Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.debug.html

Requires: %{name}-common  = %{version}-%{release}
Requires: %{name}-Escaper = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Debug
%{summary}.

Optional: XDebug (php-pecl-xdebug)

# ------------------------------------------------------------------------------

%package  Di

Summary:  Zend Framework 2: Di Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.di.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Code   = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description Di
%{summary}.

# ------------------------------------------------------------------------------

%package  Dom

Summary:  Zend Framework 2: Dom Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.dom.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description Dom
%{summary}.

# ------------------------------------------------------------------------------

%package  Escaper

Summary:  Zend Framework 2: Escaper Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.escaper.html

Requires: %{name}-common = %{version}-%{release}
# phpci
Requires: php-

%description Escaper
%{summary}.

# ------------------------------------------------------------------------------

%package  EventManager

Summary:  Zend Framework 2: EventManager Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.eventmanager.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description EventManager
%{summary}.

# ------------------------------------------------------------------------------

%package  Feed

Summary:  Zend Framework 2: Feed Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.feed.html

Requires: %{name}-common         = %{version}-%{release}
Requires: %{name}-Escaper        = %{version}-%{release}
Requires: %{name}-Stdlib         = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Http           = %{version}-%{release}
Requires: %{name}-ServiceManager = %{version}-%{release}
Requires: %{name}-Validator      = %{version}-%{release}

%description Feed
%{summary}.

# ------------------------------------------------------------------------------

%package  File

Summary:  Zend Framework 2: File Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.file.html

Requires: %{name}-common         = %{version}-%{release}
Requires: %{name}-Stdlib         = %{version}-%{release}
# phpci
Requires: php-

%description File
%{summary}.

# ------------------------------------------------------------------------------

%package  Filter

Summary:  Zend Framework 2: Filter Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.filter.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Crypt     = %{version}-%{release}
Requires: %{name}-I18n      = %{version}-%{release}
Requires: %{name}-Uri       = %{version}-%{release}
Requires: %{name}-Validator = %{version}-%{release}

%description Filter
%{summary}.

# ------------------------------------------------------------------------------

%package  Form

Summary:  Zend Framework 2: Form Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.form.html

Requires: %{name}-common      = %{version}-%{release}
Requires: %{name}-InputFilter = %{version}-%{release}
Requires: %{name}-Stdlib      = %{version}-%{release}
# phpci
Requires: php-
# Optional
### TODO: zendframework/zendservice-recaptcha

%description Form
%{summary}.

# ------------------------------------------------------------------------------

%package  Http

Summary:  Zend Framework 2: Http Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.http.html

Requires: %{name}-common    = %{version}-%{release}
Requires: %{name}-Loader    = %{version}-%{release}
Requires: %{name}-Stdlib    = %{version}-%{release}
Requires: %{name}-Uri       = %{version}-%{release}
Requires: %{name}-Validator = %{version}-%{release}
# phpci
Requires: php-

%description Http
%{summary}.

# ------------------------------------------------------------------------------

%package  I18n

Summary:  Zend Framework 2: i18n Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.i18n.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-EventManager = %{version}-%{release}
Requires: %{name}-Filter       = %{version}-%{release}
Requires: %{name}-Validator    = %{version}-%{release}
Requires: %{name}-View         = %{version}-%{release}
### TODO: zendframework/zend-resources

%description I18n
%{summary}.

# ------------------------------------------------------------------------------

%package  InputFilter

Summary:  Zend Framework 2: InputFilter Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.inputfilter.html

Requires: %{name}-common         = %{version}-%{release}
Requires: %{name}-Filter         = %{version}-%{release}
Requires: %{name}-Stdlib         = %{version}-%{release}
Requires: %{name}-Validator      = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-ServiceManager = %{version}-%{release}

%description InputFilter
%{summary}.

# ------------------------------------------------------------------------------

%package  Json

Summary:  Zend Framework 2: Json Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.json.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Server = %{version}-%{release}

%description Json
%{summary}.

# ------------------------------------------------------------------------------

%package  Ldap

Summary:  Zend Framework 2: Ldap Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.ldap.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description Ldap
%{summary}.

# ------------------------------------------------------------------------------

%package  Loader

Summary:  Zend Framework 2: Loader Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.loader.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-

%description Loader
%{summary}.

# ------------------------------------------------------------------------------

%package  Log

Summary:  Zend Framework 2: Log Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.log.html

Requires: %{name}-common         = %{version}-%{release}
Requires: %{name}-ServiceManager = %{version}-%{release}
Requires: %{name}-Stdlib         = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}-Db             = %{version}-%{release}
Requires: %{name}-Escaper        = %{version}-%{release}
Requires: %{name}-Mail           = %{version}-%{release}
Requires: %{name}-Validator      = %{version}-%{release}

%description Log
%{summary}.

# ------------------------------------------------------------------------------

%package  Mail

Summary:  Zend Framework 2: Mail Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.mail.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Mail
%{summary}.

# ------------------------------------------------------------------------------

%package  Math

Summary:  Zend Framework 2: Math Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.math.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Math
%{summary}.

# ------------------------------------------------------------------------------

%package  Memory

Summary:  Zend Framework 2: Memory Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.memory.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Memory
%{summary}.

# ------------------------------------------------------------------------------

%package  Mime

Summary:  Zend Framework 2: Mime Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.mime.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Mime
%{summary}.

# ------------------------------------------------------------------------------

%package  ModuleManager

Summary:  Zend Framework 2: ModuleManager Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.modulemanager.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description ModuleManager
%{summary}.

# ------------------------------------------------------------------------------

%package  Mvc

Summary:  Zend Framework 2: Mvc Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.mvc.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Mvc
%{summary}.

# ------------------------------------------------------------------------------

%package  Navigation

Summary:  Zend Framework 2: Navigation Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.navigation.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Navigation
%{summary}.

# ------------------------------------------------------------------------------

%package  Paginator

Summary:  Zend Framework 2: Paginator Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.paginator.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Paginator
%{summary}.

# ------------------------------------------------------------------------------

%package  Permissions

Summary:  Zend Framework 2: Permissions Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.permissions.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Permissions
%{summary}.

# ------------------------------------------------------------------------------

%package  Permissions

Summary:  Zend Framework 2: Permissions Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.permissions.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Permissions
%{summary}.

# ------------------------------------------------------------------------------

%package  ProgressBar

Summary:  Zend Framework 2: ProgressBar Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.progressbar.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description ProgressBar
%{summary}.

# ------------------------------------------------------------------------------

%package  Serializer

Summary:  Zend Framework 2: Serializer Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.serializer.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Serializer
%{summary}.

# ------------------------------------------------------------------------------

%package  Server

Summary:  Zend Framework 2: Server Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.server.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Server
%{summary}.

# ------------------------------------------------------------------------------

%package  ServiceManager

Summary:  Zend Framework 2: ServiceManager Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.servicemanager.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description ServiceManager
%{summary}.

# ------------------------------------------------------------------------------

%package  Session

Summary:  Zend Framework 2: Session Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.session.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Session
%{summary}.

# ------------------------------------------------------------------------------

%package  Soap

Summary:  Zend Framework 2: Soap Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.soap.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Soap
%{summary}.

# ------------------------------------------------------------------------------

%package  Stdlib

Summary:  Zend Framework 2: Stdlib Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.stdlib.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Stdlib
%{summary}.

# ------------------------------------------------------------------------------

%package  Tag

Summary:  Zend Framework 2: Tag Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.tag.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Tag
%{summary}.

# ------------------------------------------------------------------------------

%package  Test

Summary:  Zend Framework 2: Test Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.test.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Test
%{summary}.

# ------------------------------------------------------------------------------

%package  Text

Summary:  Zend Framework 2: Text Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.text.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Text
%{summary}.

# ------------------------------------------------------------------------------

%package  Uri

Summary:  Zend Framework 2: Uri Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.uri.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Uri
%{summary}.

# ------------------------------------------------------------------------------

%package  Validator

Summary:  Zend Framework 2: Validator Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.validator.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Validator
%{summary}.

# ------------------------------------------------------------------------------

%package  Version

Summary:  Zend Framework 2: Version Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.version.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description Version
%{summary}.

# ------------------------------------------------------------------------------

%package  View

Summary:  Zend Framework 2: View Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.view.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description View
%{summary}.

# ------------------------------------------------------------------------------

%package  XmlRpc

Summary:  Zend Framework 2: XmlRpc Component
URL:      http://framework.zend.com/manual/2.2/en/modules/zend.xmlrpc.html

Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-Stdlib = %{version}-%{release}
# phpci
Requires: php-
# Optional
Requires: %{name}- = %{version}-%{release}

%description XmlRpc
%{summary}.

# ##############################################################################

%prep
%setup -q -n ZendFramework-minimal-%{version}


%build
# Empty build section, nothing required


%install


%check


%files


# ##############################################################################

%files common
%doc *.md composer.json demos
%dir %{_datadir}/php/Zend

# ------------------------------------------------------------------------------

%files Authentication
%doc *.md composer.json
%{_datadir}/php/Zend/Authentication

# ------------------------------------------------------------------------------

%files Barcode
%doc *.md composer.json
%{_datadir}/php/Zend/Barcode

# ------------------------------------------------------------------------------

%files Cache
%doc *.md composer.json
%{_datadir}/php/Zend/Cache

# ------------------------------------------------------------------------------

%files Captcha
%doc *.md composer.json
%{_datadir}/php/Zend/Captcha

# ------------------------------------------------------------------------------

%files Code
%doc *.md composer.json
%{_datadir}/php/Zend/Code

# ------------------------------------------------------------------------------

%files Config
%doc *.md composer.json
%{_datadir}/php/Zend/Config

# ------------------------------------------------------------------------------

%files Console
%doc *.md composer.json
%{_datadir}/php/Zend/Console

# ------------------------------------------------------------------------------

%files Crypt
%doc *.md composer.json
%{_datadir}/php/Zend/Crypt

# ------------------------------------------------------------------------------

%files Db
%doc *.md composer.json
%{_datadir}/php/Zend/Db

# ------------------------------------------------------------------------------

%files Debug
%doc *.md composer.json
%{_datadir}/php/Zend/Debug

# ------------------------------------------------------------------------------

%files Di
%doc *.md composer.json
%{_datadir}/php/Zend/Di

# ------------------------------------------------------------------------------

%files Dom
%doc *.md composer.json
%{_datadir}/php/Zend/Dom

# ------------------------------------------------------------------------------

%files Escaper
%doc *.md composer.json
%{_datadir}/php/Zend/Escaper

# ------------------------------------------------------------------------------

%files EventManager
%doc *.md composer.json
%{_datadir}/php/Zend/EventManager

# ------------------------------------------------------------------------------

%files Feed
%doc *.md composer.json
%{_datadir}/php/Zend/Feed

# ------------------------------------------------------------------------------

%files File
%doc *.md composer.json
%{_datadir}/php/Zend/File

# ------------------------------------------------------------------------------

%files Filter
%doc *.md composer.json
%{_datadir}/php/Zend/Filter

# ------------------------------------------------------------------------------

%files Form
%doc *.md composer.json
%{_datadir}/php/Zend/Form

# ------------------------------------------------------------------------------

%files Http
%doc *.md composer.json
%{_datadir}/php/Zend/Http

# ------------------------------------------------------------------------------

%files I18n
%doc *.md composer.json
%{_datadir}/php/Zend/I18n

# ------------------------------------------------------------------------------

%files InputFilter
%doc *.md composer.json
%{_datadir}/php/Zend/InputFilter

# ------------------------------------------------------------------------------

%files Json
%doc *.md composer.json
%{_datadir}/php/Zend/Json

# ------------------------------------------------------------------------------

%files Ldap
%doc *.md composer.json
%{_datadir}/php/Zend/Ldap

# ------------------------------------------------------------------------------

%files Loader
%doc *.md composer.json
%{_datadir}/php/Zend/Loader

# ------------------------------------------------------------------------------

%files Log
%doc *.md composer.json
%{_datadir}/php/Zend/Log

# ------------------------------------------------------------------------------

%files Mail
%doc *.md composer.json
%{_datadir}/php/Zend/Mail

# ------------------------------------------------------------------------------

%files Math
%doc *.md composer.json
%{_datadir}/php/Zend/Math

# ------------------------------------------------------------------------------

%files Memory
%doc *.md composer.json
%{_datadir}/php/Zend/Memory

# ------------------------------------------------------------------------------

%files Mime
%doc *.md composer.json
%{_datadir}/php/Zend/Mime

# ------------------------------------------------------------------------------

%files ModuleManager
%doc *.md composer.json
%{_datadir}/php/Zend/ModuleManager

# ------------------------------------------------------------------------------

%files Mvc
%doc *.md composer.json
%{_datadir}/php/Zend/Mvc

# ------------------------------------------------------------------------------

%files Navigation
%doc *.md composer.json
%{_datadir}/php/Zend/Navigation

# ------------------------------------------------------------------------------

%files Paginator
%doc *.md composer.json
%{_datadir}/php/Zend/Paginator

# ------------------------------------------------------------------------------

%files Permissions
%doc *.md composer.json
%{_datadir}/php/Zend/Permissions

# ------------------------------------------------------------------------------

%files Permissions
%doc *.md composer.json
%{_datadir}/php/Zend/Permissions

# ------------------------------------------------------------------------------

%files ProgressBar
%doc *.md composer.json
%{_datadir}/php/Zend/ProgressBar

# ------------------------------------------------------------------------------

%files Serializer
%doc *.md composer.json
%{_datadir}/php/Zend/Serializer

# ------------------------------------------------------------------------------

%files Server
%doc *.md composer.json
%{_datadir}/php/Zend/Server

# ------------------------------------------------------------------------------

%files ServiceManager
%doc *.md composer.json
%{_datadir}/php/Zend/ServiceManager

# ------------------------------------------------------------------------------

%files Session
%doc *.md composer.json
%{_datadir}/php/Zend/Session

# ------------------------------------------------------------------------------

%files Soap
%doc *.md composer.json
%{_datadir}/php/Zend/Soap

# ------------------------------------------------------------------------------

%files Stdlib
%doc *.md composer.json
%{_datadir}/php/Zend/Stdlib

# ------------------------------------------------------------------------------

%files Tag
%doc *.md composer.json
%{_datadir}/php/Zend/Tag

# ------------------------------------------------------------------------------

%files Test
%doc *.md composer.json
%{_datadir}/php/Zend/Test

# ------------------------------------------------------------------------------

%files Text
%doc *.md composer.json
%{_datadir}/php/Zend/Text

# ------------------------------------------------------------------------------

%files Uri
%doc *.md composer.json
%{_datadir}/php/Zend/Uri

# ------------------------------------------------------------------------------

%files Validator
%doc *.md composer.json
%{_datadir}/php/Zend/Validator

# ------------------------------------------------------------------------------

%files Version
%doc *.md composer.json
%{_datadir}/php/Zend/Version

# ------------------------------------------------------------------------------

%files View
%doc *.md composer.json
%{_datadir}/php/Zend/View

# ------------------------------------------------------------------------------

%files XmlRpc
%doc *.md composer.json
%{_datadir}/php/Zend/XmlRpc

# ##############################################################################

%changelog
* Fri Jul 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2.1-1
- Initial package
