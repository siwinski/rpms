%global github_owner   schmittjoh
%global github_name    parser-lib
%global github_version 1.0.0
%global github_commit  c509473bc1b4866415627af0e1c6cc8ac97fa51d

%global php_min_ver    5.3.0

Name:          php-JMSParser
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Library for writing recursive-descent parsers

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://jmsyst.com/libs/%{github_name}
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# Test build requires: phpci
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl

Requires:      php-common >= %{php_min_ver}
Requires:      php-PhpOption >= 0.9
# phpci requires
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

Conflicts:     php-PhpOption >= 2.0

%description
%{summary}.


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

# PHPUnit config
sed 's:\(\./\)\?tests/:./:' -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Rewrite tests' bootstrap (which uses Composer autoloader) with simple
# autoloader that uses include path
mv tests/bootstrap.php tests/bootstrap.php.dist
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/JMS
cp -rp src/JMS/Parser %{buildroot}%{_datadir}/php/JMS/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%check
%{_bindir}/phpunit \
    -d include_path="./src:./tests:.:%{pear_phpdir}:%{_datadir}/php" \
    -c tests/phpunit.xml.dist


%files
%doc LICENSE README.md composer.json
%dir %{_datadir}/php/JMS
     %{_datadir}/php/JMS/Parser

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Thu Jan 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-1
- Initial package
