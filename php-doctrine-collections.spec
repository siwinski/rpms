%global github_owner   doctrine
%global github_name    collections
%global github_version 1.1
%global github_commit  4d3357cee6ec50c367ab549c0cd01d47d23614e2
# Additional commits after v1.1 tag
%global github_release 20131220git%(c=%{github_commit}; echo ${c:0:7})

# "php": ">=5.3.2"
%global php_min_ver    5.3.2

Name:          php-%{github_owner}-%{github_name}
Version:       %{github_version}
Release:       1.%{github_release}%{dist}
Summary:       Collections abstraction library

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from git commit 4d3357cee6ec50c367ab549c0cd01d47d23614e2)
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from git commit 4d3357cee6ec50c367ab549c0cd01d47d23614e2)
Requires:      php-spl

%description
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/* %{buildroot}/%{_datadir}/php/


%check
# Create tests' autoload
mkdir vendor
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > vendor/autoload.php

# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

%{_bindir}/phpunit --include-path ./lib:./tests -d date.timezone="UTC"


%files
%doc LICENSE *.md composer.json
%dir %{_datadir}/php/Doctrine
%dir %{_datadir}/php/Doctrine/Common
     %{_datadir}/php/Doctrine/Common/Collections


%changelog
* Fri Dec 20 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1-1.20131220git4d3357c
- Initial package
