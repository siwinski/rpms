# NOTE: Currently no PEAR install, but there will possibly be one in the
#       future: https://github.com/fabpot/Silex/issues/82

%global libname          Silex

%global git_date         20121130
%global git_hash         5cfa54fce1e2c6c1072def1b79bfb69f4fbdf97e
%global git_shorthash    %(expr substr "%{git_hash}" 1 10)

%global php_min_ver      5.3.3

%global doctrine_min_ver 2.2.0
%global doctrine_max_ver 2.4.0
%global monolog_min_ver  1.0.0
%global monolog_max_ver  1.2.0
%global pimple_min_ver   1.0.0
%global pimple_max_ver   2.0.0
%global swift_min_ver    4.2.0
%global swift_max_ver    4.3.0
%global symfony_min_ver  2.1.0
%global symfony_max_ver  2.3.0
%global twig_min_ver     1.8.0
%global twig_max_ver     2.0.0

Name:          php-%{libname}
Version:       1.0.0
Release:       0.1.%{git_date}git%{git_shorthash}%{?dist}
Summary:       The PHP micro-framework based on the Symfony2 Components

Group:         Development/Libraries
License:       MIT
URL:           http://silex.sensiolabs.org
# NOTE: No tagged version release
Source0:       https://github.com/fabpot/%{libname}/archive/%{git_hash}.tar.gz

BuildArch:     noarch
# Test requires
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires:      php-common >= %{php_min_ver}
#BuildRequires:      php-pear(pear.doctrine-project.org/DoctrineDBAL) >= %{doctrine_min_ver}
#BuildRequires:      php-pear(pear.doctrine-project.org/DoctrineDBAL) <  %{doctrine_max_ver}
BuildRequires: php-pear(pear.swiftmailer.org/Swift) >= %{swift_min_ver}
BuildRequires: php-pear(pear.swiftmailer.org/Swift) <  %{swift_max_ver}
BuildRequires: php-pear(pear.symfony.com/BrowserKit) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/BrowserKit) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Config) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Config) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/CssSelector) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/CssSelector) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/DomCrawler) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/DomCrawler) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/EventDispatcher) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/EventDispatcher) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Finder) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Finder) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Form) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Form) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/HttpFoundation) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/HttpFoundation) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/HttpKernel) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/HttpKernel) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Locale) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Locale) <  %{symfony_max_ver}
#BuildRequires: php-pear(pear.symfony.com/MonologBridge) >= %{symfony_min_ver}
#BuildRequires: php-pear(pear.symfony.com/MonologBridge) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Process) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Process) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Routing) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Routing) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Security) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Security) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Serializer) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Serializer) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Translation) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Translation) <  %{symfony_max_ver}
#BuildRequires: php-pear(pear.symfony.com/TwigBridge) >= %{symfony_min_ver}
#BuildRequires: php-pear(pear.symfony.com/TwigBridge) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.symfony.com/Validator) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Validator) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
BuildRequires: php-Monolog >= %{monolog_min_ver}
#BuildRequires: php-Monolog <  %{monolog_max_ver}
BuildRequires: php-Pimple >= %{pimple_min_ver}
BuildRequires: php-Pimple <  %{pimple_max_ver}
# Test requires: phpci
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-pecl(phar)
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-tokenizer

Requires:      php-common >= %{php_min_ver}
Requires:      php-pear(pear.symfony.com/BrowserKit) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/BrowserKit) <  %{symfony_max_ver}
Requires:      php-pear(pear.symfony.com/CssSelector) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/CssSelector) <  %{symfony_max_ver}
Requires:      php-pear(pear.symfony.com/DomCrawler) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/DomCrawler) <  %{symfony_max_ver}
Requires:      php-pear(pear.symfony.com/EventDispatcher) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/EventDispatcher) <  %{symfony_max_ver}
Requires:      php-pear(pear.symfony.com/HttpFoundation) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/HttpFoundation) <  %{symfony_max_ver}
Requires:      php-pear(pear.symfony.com/HttpKernel) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/HttpKernel) <  %{symfony_max_ver}
Requires:      php-pear(pear.symfony.com/Routing) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/Routing) <  %{symfony_max_ver}
Requires:      php-Pimple >= %{pimple_min_ver}
Requires:      php-Pimple <  %{pimple_max_ver}
# phpci requires
Requires:      php-date
Requires:      php-pcre
Requires:      php-pecl(phar)
Requires:      php-reflection
Requires:      php-session
Requires:      php-tokenizer

%description
Silex is a PHP micro-framework for PHP 5.3. It is built on the shoulders of
Symfony2 and Pimple and also inspired by Sinatra (http://www.sinatrarb.com/).

A micro-framework provides the guts for building simple single-file apps. Silex
aims to be:
* Concise: Silex exposes an intuitive and concise API that is fun to use.
* Extensible: Silex has an extension system based around the Pimple micro
service-container that makes it even easier to tie in third party libraries.
* Testable: Silex uses Symfony2's HttpKernel which abstracts request and
response. This makes it very easy to test apps and the framework itself. It
also respects the HTTP specification and encourages its proper use.


%prep
%setup -q -n %{libname}-%{git_hash}

# Update and move tests' PHPUnit config
sed -e 's#tests/##' \
    -e 's#./src#%{_datadir}/php/%{libname}#' \
    -i phpunit.xml.dist
mv phpunit.xml.dist tests/


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -pr src/%{libname} %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -pr tests/* %{buildroot}%{_datadir}/tests/%{name}/


%files
%doc LICENSE README.md composer.json doc
%{_datadir}/php/%{libname}
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Fri Nov 30 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-0.1.20121130git5cfa54fce1
- Initial package
