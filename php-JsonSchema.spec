%global lib_name    JsonSchema
%global github_name json-schema

Name:      php-%{lib_name}
Version:   1.2.1
Release:   1%{?dist}
Summary:   PHP implementation of JSON schema

Group:     Development/Libraries
License:   BSD
URL:       https://github.com/justinrainbow/%{github_name}
Source0:   %{url}/archive/%{version}.tar.gz

BuildArch: noarch

Requires:  php-common >= 5.3.0
# phpci requires
Requires:  php-curl
Requires:  php-json
Requires:  php-pcre
Requires:  php-spl
%{?fedora:Requires: php-filter}

%description
A PHP implementation for validating JSON structures against a given schema.

See http://json-schema.org for more details.


%prep
%setup -q -n %{github_name}-%{version}

# Clean up unnecessary files
find . -type f -name '.git*' -delete


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/


%files
%doc LICENSE README.md docs composer.json
%{_datadir}/php/%{lib_name}


%changelog
* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2.1-1
- Initial package
