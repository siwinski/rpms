%global lib_name    JsonSchema
%global github_name json-schema

Name:      php-%{lib_name}
Version:   1.2.2
Release:   1%{?dist}
Summary:   PHP implementation of JSON schema

Group:     Development/Libraries
License:   BSD
URL:       https://github.com/justinrainbow/%{github_name}
Source0:   %{url}/archive/%{version}.tar.gz

BuildArch: noarch

Requires:  php-common >= 5.3.0
# phpci requires
Requires:  php-ctype
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

# Create PSR-0 autoloader for tests
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    require_once $src;
});
AUTOLOAD
) > autoload.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/


%check
phpunit --bootstrap=autoload.php -d include_path="src/:tests/:.:/usr/share/pear/" .


%files
%doc LICENSE README.md docs composer.json
%{_datadir}/php/%{lib_name}


%changelog
* Wed Dec  5 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2.2-1
- Updated to upstream version 1.2.2
- Added php-ctype require
- Added PSR-0 autoloader for tests
- Added %%check

* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2.1-1
- Initial package
