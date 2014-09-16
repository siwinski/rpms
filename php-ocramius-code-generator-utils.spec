#
# RPM spec file for php-ocramius-code-generator-utils
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Ocramius
%global github_name      CodeGenerationUtils
%global github_version   0.3.0
%global github_commit    5d9c4e3ae36010fef22b3393b3734c84106d1d5c

%global composer_vendor  ocramius
%global composer_project code-generator-utils

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "phpunit/phpunit": ">=3.7"
#     NOTE: Max version ignored on purpose
%global phpunit_min_ver 3.7
# "nikic/php-parser": "1.0.*"
%global php_parser_min_ver 1.0.0
%global php_parser_max_ver 1.1.0

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A set of code generator utilities built on top of PHP-Parsers

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-phpunit-PHPUnit >= %{phpunit_min_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{php_parser_min_ver}
BuildRequires: php-composer(nikic/php-parser) <  %{php_parser_max_ver}
# For tests: phpcompatinfo (computed from version 0.3.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(nikic/php-parser) >= %{php_parser_min_ver}
Requires:      php-composer(nikic/php-parser) <  %{php_parser_max_ver}
# phpcompatinfo (computed from version 0.3.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A set of code generator utilities built on top of PHP-Parsers that ease its use
when combined with Reflection.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}/%{_datadir}/php
cp -rp src/* %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
# Create autoloader
cat > autoload.php <<'AUTOLOAD'
<?php

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', rtrim($class, '_')).'.php';
    @include_once $src;
});
AUTOLOAD

# Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{__phpunit} \
    --bootstrap autoload.php \
    --include-path %{buildroot}%{_datadir}/php:./tests \
    -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%{_datadir}/php/CodeGenerationUtils


%changelog
* Tue Sep 16 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.0-1
- Initial package
