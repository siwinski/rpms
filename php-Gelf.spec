%global github_owner  mlehner
%global github_name   gelf-php
%global github_commit 3b327ac0e89057666b09a4ddea515972b766bc9a

%global lib_name      Gelf

Name:      php-%{lib_name}
Version:   1.0
Release:   1%{?dist}
Summary:   A GELF library for Graylog2

Group:     Development/Libraries

# License file request: https://github.com/mlehner/gelf-php/issues/5
License:   *** UNKNOWN ***
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}.tar.gz

BuildArch: noarch

Requires:  php-common >= 5.3.0
# phpci requires
Requires:  php-json
Requires:  php-zlib

%description
%{summary}.

Fork of gelf-php (https://github.com/Graylog2/gelf-php) with PHP namespace
support.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/


%files
%doc composer.json
%{_datadir}/php/%{lib_name}


%changelog
* Fri Jan 11 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
