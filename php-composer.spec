%global github_owner   composer
%global github_name    composer
%global github_version 1.0.0
%global github_release alpha6
%global github_commit  0c8158f47d7dda89226d4e816fee1fb9ac6c1204

%global php_min_ver    5.3.2

Name:          php-composer
Version:       1.0.0
Release:       0.1.%{github_release}%{?dist}
Summary:       Dependency Manager for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://getcomposer.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz
#Source1:       http://getcomposer.org/download/1.0.0-alpha6/composer.phar

BuildArch:     noarch

# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# Test build requires: phpci
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-phar
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-tokenizer
BuildRequires: php-xsl
BuildRequires: php-zip
BuildRequires: php-zlib

Requires:      php-common >= %{php_min_ver}
Requires:      php-JsonSchema >= 1.1.0
Requires:      php-jsonlint >= 1.0
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

#Conflicts:     php-JsonSchema >= 1.2.0
Conflicts:     php-jsonlint >= 2.0
Conflicts:     php-pear(pear.symfony.com/Console) >= 3.0.0
Conflicts:     php-pear(pear.symfony.com/Finder) >= 3.0.0
Conflicts:     php-pear(pear.symfony.com/Process) >= 3.0.0

Provides:      php-composer(composer/composer) = %{version}

%description
Composer is a tool for dependency management in PHP. It allows you to declare
the dependent libraries your project needs and it will install them in your
project for you.


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

mv src/bootstrap.php src/Composer/

#
sed -e 's:/usr/bin/env php:%{__php}:' \
    -e "/require.*bootstrap/s:.*:require 'Composer/bootstrap.php';:" \
    -i bin/composer

# Update and move PHPUnit config
sed -e 's:\(\./\)\?tests/:./:' \
    -e 's:./src:%{_datadir}/php:' \
    -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Update complete PHPUnit config
sed -e 's:tests/::' \
    -e 's:../src:%{_datadir}/php:' \
    -i tests/complete.phpunit.xml

#
sed "/require.*bootstrap/s:require.*:require 'Composer/bootstrap.php';:" \
    -i tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/Composer %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_bindir}
install bin/composer %{buildroot}%{_bindir}/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%files
%doc LICENSE *.md composer.json PORTING_INFO doc
%{_datadir}/php/Composer
%{_bindir}/composer

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}

%changelog
* Fri Jan 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-0.1.alpha6
- Initial package
