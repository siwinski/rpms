%global github_owner        kriswallsmith
%global github_name         assetic
%global github_version      1.1.0
%global github_prerelease   alpha1
%global github_commit       7edb812fa2ac6c5a455af2066bc21637977ef945
%global github_date         20120828

%global php_min_ver         5.3.1

%global symfony_min_ver     2.1.0
%global symfony_max_ver     2.2
%global twig_min_ver        1.6.0
%global twig_max_ver        2.0

Name:          php-Assetic
Version:       %{github_version}
Release:       0.1.%{github_prerelease}%{?dist}
Summary:       Asset Management for PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-pear(pear.symfony.com/Process) >= %{symfony_min_ver}
BuildRequires: php-pear(pear.symfony.com/Process) <  %{symfony_max_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
BuildRequires: php-lessphp
# TODO:        leafo/scssphp
# TODO:        ptachoire/cssembed
# phpci
BuildRequires: php-ctype
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-fileinfo
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-openssl
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-tokenizer

Requires:      php-common >= %{php_min_ver}
Requires:      php-pear(pear.symfony.com/Process) >= %{symfony_min_ver}
Requires:      php-pear(pear.symfony.com/Process) <  %{symfony_max_ver}
# phpci requires
Requires:      php-ctype
Requires:      php-curl
Requires:      php-date
Requires:      php-json
Requires:      php-pcre
Requires:      php-spl
Requires:      php-tokenizer
# Optional requires
Requires:      php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
Requires:      php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
Requires:      php-lessphp
# TODO:        leafo/scssphp
# TODO:        ptachoire/cssembed

%description
Assetic is an asset management framework for PHP.

Optional dependency: APC


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

mv phpunit.xml.dist tests/
mv src/functions.php src/Assetic/


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/* %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%files
%doc LICENSE *.md composer.json
%{_datadir}/php/Assetic

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Thu Jan 31 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.0-0.1.alpha1
- Initial package
