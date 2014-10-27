#
# RPM spec file for php-ocramius-generated-hydrator
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Ocramius
%global github_name      GeneratedHydrator
%global github_version   1.1.0
%global github_commit    6842b76141dc3a57f822f2e287d699135e7b3c57

%global composer_vendor  ocramius
%global composer_project generated-hydrator

# "php": "~5.4"
#     NOTE: Max version ignored on purpose
%global php_min_ver 5.4
# "nikic/php-parser": "1.0.*"
%global php_parser_min_ver 1.0.0
%global php_parser_max_ver 1.1.0
# "ocramius/code-generator-utils": "0.3.*"
%global ocramius_cgu_min_ver 0.3.0
%global ocramius_cgu_max_ver 0.4.0
# "zendframework/zend-stdlib": "~2.3"
%global zf_stdlib_min_ver 2.3
%global zf_stdlib_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:     %global phpdir     %{_datadir}/php}
%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       An object hydrator

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(nikic/php-parser) >= %{php_parser_min_ver}
BuildRequires: php-composer(nikic/php-parser) <  %{php_parser_max_ver}
BuildRequires: php-composer(ocramius/code-generator-utils) >= %{ocramius_cgu_min_ver}
BuildRequires: php-composer(ocramius/code-generator-utils) <  %{ocramius_cgu_max_ver}
BuildRequires: php-composer(zendframework/zend-stdlib) >= %{zf_stdlib_min_ver}
BuildRequires: php-composer(zendframework/zend-stdlib) <  %{zf_stdlib_max_ver}
BuildRequires: php-phpunit-PHPUnit
# phpcompatinfo (computed from version 1.1.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(nikic/php-parser) >= %{php_parser_min_ver}
Requires:      php-composer(nikic/php-parser) <  %{php_parser_max_ver}
Requires:      php-composer(ocramius/code-generator-utils) >= %{ocramius_cgu_min_ver}
Requires:      php-composer(ocramius/code-generator-utils) <  %{ocramius_cgu_max_ver}
Requires:      php-composer(zendframework/zend-stdlib) >= %{zf_stdlib_min_ver}
Requires:      php-composer(zendframework/zend-stdlib) <  %{zf_stdlib_max_ver}
# phpcompatinfo (computed from version 1.1.0)
Requires:      php-reflection
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
GeneratedHydrator is a library about high performance transition of data from
arrays to objects and from objects to arrays.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
# Create autoloader
cat > autoload.php <<'AUTOLOAD'
<?php

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD

# Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{__phpunit} \
    --bootstrap autoload.php \
    --include-path %{buildroot}%{phpdir}:./tests \
    -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%{phpdir}/GeneratedHydrator


%changelog
* Mon Oct 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.0-1
- Initial package
