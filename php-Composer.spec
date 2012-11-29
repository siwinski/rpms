%global lib_name    Composer
%global github_name composer
%global prerelease  alpha6

Name:          php-%{lib_name}
Version:       1.0.0
Release:       0.1.%{prerelease}%{?dist}
Summary:       Dependency Manager for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://getcomposer.org/
Source0:       https://github.com/composer/composer/archive/%{version}-%{prerelease}.tar.gz
#Source1:       http://getcomposer.org/download/1.0.0-alpha6/composer.phar

BuildArch:     noarch

Requires:      php-common >= 5.3.2
Requires:      php-pear(pear.symfony.com/Console) >= 2.1.0
Requires:      php-pear(pear.symfony.com/Finder) >= 2.1.0
Requires:      php-pear(pear.symfony.com/Process) >= 2.1.0
# phpci requires
Requires:      php-curl
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-phar
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-tokenizer
Requires:      php-xsl
Requires:      php-zip
Requires:      php-zlib

%description
Composer is a tool for dependency management in PHP. It allows you to declare
the dependent libraries your project needs and it will install them in your
project for you.


%prep
%setup -q -n %{github_name}-%{version}-%{prerelease}


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/


%files
%doc LICENSE *.md composer.* PORTING_INFO doc
%{_datadir}/php/%{lib_name}


%changelog
* Thu Nov 29 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-0.1.alpha6
- Initial package
