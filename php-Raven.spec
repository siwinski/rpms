%global github_owner  getsentry
%global github_name   raven-php
%global github_commit 7c13662b139dca970b551387d1f713d809b6d92e

%global lib_name      Raven
# composer.json lists minimum version as 5.2.4, but constants E_DEPRECATED and
# E_USER_DEPRECATED in "lib/Raven/Client.php" make the minimum 5.3.0
%global php_min_ver   5.3.0

Name:      php-Raven
Version:   0.3.1
Release:   1%{?dist}
Summary:   A PHP client for Sentry

Group:     Development/Libraries
License:   ASL 2.0
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz

BuildArch: noarch

Requires:  php-common >= %{php_min_ver}
# phpci requires
Requires:  php-curl
Requires:  php-date
Requires:  php-hash
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-session
Requires:  php-sockets
Requires:  php-spl
Requires:  php-zlib

%description
%{summary} (http://getsentry.com).


%prep
%setup -q -n %{github_name}-%{github_commit}

# TODO: Add comment and pull request
chmod a-x lib/%{lib_name}/Stacktrace.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp lib/%{lib_name} %{buildroot}%{_datadir}/php/


%check
# TODO: Run tests


%files
%doc LICENSE AUTHORS README.rst composer.json
%{_datadir}/php/%{lib_name}


%changelog
* Fri Jan 11 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.1-1
- Initial package
