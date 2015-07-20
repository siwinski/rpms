#
# Fedora spec file for php-nategood-httpful
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     nategood
%global github_name      httpful
%global github_version   0.2.19
%global github_commit    bd73f89d34d8f879c54ac46eb94b0f7be1d00820

%global composer_vendor  nategood
%global composer_project httpful

# "php": ">=5.3"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A readable, chainable, REST friendly, PHP HTTP client

Group:         Development/Libraries
License:       MIT
URL:           http://phphttpclient.com/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-cli
BuildRequires: php-curl
## phpcompatinfo (computed from version 0.2.19)
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-fileinfo
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-xmlwriter
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-curl
# phpcompatinfo (computed from version 0.2.19)
Requires:      php-dom
Requires:      php-fileinfo
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xmlwriter

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Httpful is a simple Http Client library for PHP 5.3+. There is an emphasis of
readability, simplicity, and flexibility – basically provide the features and
flexibility to get the job done and make those features really easy to use.

Features:
* Readable HTTP Method Support (GET, PUT, POST, DELETE, HEAD, PATCH and OPTIONS)
* Custom Headers
* Automatic "Smart" Parsing
* Automatic Payload Serialization
* Basic Auth
* Client Side Certificate Auth
* Request "Templates"


%prep
%setup -qn %{github_name}-%{github_commit}

: E: script-without-shebang /usr/share/php/Httpful/Request.php
: https://github.com/nategood/httpful/pull/192
chmod a-x src/Httpful/Request.php

: Create autoloader
cat <<'AUTOLOAD' | tee src/Httpful/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 *
 * Created by %{name}-%{version}-%{release}
 */

require_once __DIR__ . '/Bootstrap.php';
\Httpful\Bootstrap::init();
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
%{_bindir}/phpunit --verbose --configuration tests/phpunit.xml
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc *.md
%doc composer.json
%doc examples
%{phpdir}/Httpful


%changelog
* Mon Jul 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2.19-1
- Initial package
