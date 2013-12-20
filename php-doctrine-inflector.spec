%global github_owner   doctrine
%global github_name    inflector
%global github_version 1.0
%global github_commit  acd7665c4636cc5c795d4859e0605d95fa86efd4
# Additional commits after v1.0 tag
%global github_release 20131220git%(c=%{github_commit}; echo ${c:0:7})

# "php": ">=5.3.2"
%global php_min_ver    5.3.2

Name:          php-%{github_owner}-%{github_name}
Version:       %{github_version}
Release:       1.%{github_release}%{dist}
Summary:       Common string manipulations with regard to casing and singular/plural rules

Group:         Development/Libraries
License:       MIT
URL:           http://www.doctrine-project.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from git commit acd7665c4636cc5c795d4859e0605d95fa86efd4)
BuildRequires: php-pcre
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from git commit acd7665c4636cc5c795d4859e0605d95fa86efd4)
Requires:      php-pcre

%description
Doctrine Inflector is a small library that can perform string manipulations
with regard to upper-/lowercase and singular/plural forms of words.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/* %{buildroot}/%{_datadir}/php/


%check
# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

%{_bindir}/phpunit --include-path ./lib:./tests -d date.timezone="UTC"


%files
%doc LICENSE *.md composer.json
%dir %{_datadir}/php/Doctrine
%dir %{_datadir}/php/Doctrine/Common
     %{_datadir}/php/Doctrine/Common/Inflector


%changelog
* Fri Dec 20 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1.20131220gitacd7665
- Initial package
