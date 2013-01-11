%global github_owner  getsentry
%global github_name   raven-php
%global github_commit 7c13662b139dca970b551387d1f713d809b6d92e

%global lib_name      Raven
# composer.json lists minimum version as 5.2.4, but constants E_DEPRECATED and
# E_USER_DEPRECATED in "lib/Raven/Client.php" make the minimum 5.3.0
%global php_min_ver   5.3.0

Name:          php-Raven
Version:       0.3.1
Release:       1%{?dist}
Summary:       A PHP client for Sentry

Group:         Development/Libraries
License:       ASL 2.0
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
# composer.json lists PHPUnit version 3.7, but tests pass with 3.6
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)

Requires:      php-common >= %{php_min_ver}
# phpci requires
Requires:      php-curl
Requires:      php-date
Requires:      php-hash
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-sockets
Requires:      php-spl
Requires:      php-zlib

%description
%{summary} (http://getsentry.com).


%package test
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description test
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Update and move PHPUnit config
sed -e 's:test/::' \
    -e 's:./lib:%{_datadir}/php:' \
    -i phpunit.xml.dist
mv phpunit.xml.dist test/

# Update autoloader require in test bootstrap
sed "/require.*Autoloader/s:.*:require_once 'Raven/Autoloader.php';:" \
    -i test/bootstrap.php

# Remove executable bit
# TODO: GitHub pull request
chmod a-x lib/%{lib_name}/Stacktrace.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp lib/%{lib_name} %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp test/* %{buildroot}%{_datadir}/tests/%{name}/


%check
%{_bindir}/phpunit \
    -d include_path="./lib:./test:.:/usr/share/pear" \
    -c test/phpunit.xml.dist


%files
%doc LICENSE AUTHORS README.rst composer.json
%{_datadir}/php/%{lib_name}

%files test
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Fri Jan 11 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.1-1
- Initial package
