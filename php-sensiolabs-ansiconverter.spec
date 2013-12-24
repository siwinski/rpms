%global github_owner   sensiolabs
%global github_name    ansi-to-html
%global github_version 1.0.3
%global github_commit  34f153f2d8dd4ec2bb721154f61f0acb61bedaca

# "php": ">=5.3.0"
%global php_min_ver    5.3.0

Name:          php-sensiolabs-ansiconverter
Version:       %{github_version}
Release:       1%{dist}
Summary:       ANSI to HTML5 Converter

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from v1.0.3)
BuildRequires: php-pcre

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from v1.0.3)
Requires:      php-pcre

%description
A library to convert a text with ANSI codes to HTML.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp SensioLabs %{buildroot}/%{_datadir}/php/


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

%{_bindir}/phpunit -d date.timezone="UTC"


%files
%doc LICENSE *.md composer.json
%dir %{_datadir}/php/SensioLabs
     %{_datadir}/php/SensioLabs/AnsiConverter
%exclude %{_datadir}/php/SensioLabs/AnsiConverter/Tests


%changelog
* Tue Dec 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.3-1
- Initial package
