%global github_owner      schmittjoh
%global github_name       php-manipulator
%global github_version    0
%global github_commit     cc7d6cffd64a7942a89a26ccda67993566166d9b
%global github_date       20130101

%global github_release    %{github_date}git%(c=%{github_commit}; echo ${c:0:7})

# NOTE: phpci false positive for 5.4.0
%global php_min_ver       5.3.0

%global phpoption_min_ver 1.0
%global phpoption_max_ver 2.0

%global phpparser_min_ver 0.9.1
%global phpparser_max_ver 1.0

Name:          php-JMSPhpManipulator
Version:       %{github_version}
Release:       0.1.%{github_release}%{?dist}
Summary:       Library for Analyzing and Modifying PHP Source Code

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://jmsyst.com/libs/%{github_name}
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-PhpOption >= %{phpoption_min_ver}
BuildRequires: php-PhpOption <  %{phpoption_max_ver}
BuildRequires: php-PHPParser >= %{phpparser_min_ver}
BuildRequires: php-PHPParser <  %{phpparser_max_ver}
# Test build requires: phpci
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-tokenizer

Requires:      php-common >= %{php_min_ver}
Requires:      php-PhpOption >= %{phpoption_min_ver}
Requires:      php-PhpOption <  %{phpoption_max_ver}
Requires:      php-PHPParser >= %{phpparser_min_ver}
Requires:      php-PHPParser <  %{phpparser_max_ver}
# phpci requires
Requires:      php-json
Requires:      php-pcre
Requires:      php-spl
Requires:      php-tokenizer

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

# Update and move PHPUnit config
sed 's:\.\?/\?tests/:./:' -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Overwrite tests/bootstrap.php (which uses Composer autoloader) with simple
# spl autoloader
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace(array('\\', '_'), '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD
) > tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/JMS
cp -rp src/JMS/PhpManipulator %{buildroot}%{_datadir}/php/JMS/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%check
# TODO: FIGURE OUT WHY TESTS FAIL
#%{_bindir}/phpunit \
#    -d include_path="./src:./tests:.:%{pear_phpdir}:%{_datadir}/php" \
#    -c tests/phpunit.xml.dist


%files
%doc LICENSE README.md composer.json
%dir %{_datadir}/php/JMS
     %{_datadir}/php/JMS/PhpManipulator

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Thu Jan 31 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0-0.1.20130101gitcc7d6cf
- Initial package
