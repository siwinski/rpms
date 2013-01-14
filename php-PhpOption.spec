%global github_owner  schmittjoh
%global github_name   php-option
%global github_commit b9c60ebf8242cf409d8734b6a757ba0ce1691493

%global lib_name      PhpOption
%global php_min_ver   5.3.0

Name:          php-%{lib_name}
Version:       1.0.0
Release:       1%{?dist}
Summary:       Option Type for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)

Requires:      php-common >= %{php_min_ver}
# No phpci requires

%description
This package adds an Option type for PHP.

The Option type is intended for cases where you sometimes might return a value
(typically an object), and sometimes you might return no value (typically null)
depending on arguments, or other runtime factors.

Often times, you forget to handle the case where no value is returned. Not
intentionally of course, but maybe you did not account for all possible states
of the sytem; or maybe you indeed covered all cases, then time goes on, code is
refactored, some of these your checks might become invalid, or incomplete.
Suddenly, without noticing, the no value case is not handled anymore. As a
result, you might sometimes get fatal PHP errors telling you that you called a
method on a non-object; users might see blank pages, or worse.

On one hand, the Option type forces a developer to consciously think about both
cases (returning a value, or returning no value). That in itself will already
make your code more robust. On the other hand, the Option type also allows the
API developer to provide more concise API methods, and empowers the API user in
how he consumes these methods.


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Update and move PHPUnit config
sed 's:tests/::' -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Overwrite tests/bootstrap.php (which uses Composer autoloader) with simple
# spl autoloader
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD
) > tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%check
%{_bindir}/phpunit \
    -d include_path="./src:./tests:.:%{pear_phpdir}" \
    -c tests/phpunit.xml.dist


%files
%doc LICENSE README.md composer.json
%{_datadir}/php/%{lib_name}

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Mon Jan 14 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-1
- Initial package
