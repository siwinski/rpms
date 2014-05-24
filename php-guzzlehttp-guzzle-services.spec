%global github_owner     guzzle
%global github_name      guzzle-services
%global github_version   0.2.0
%global github_commit    e079a728689a28e9f4427264bcfc77d0dd6fa98d

%global composer_vendor  guzzlehttp
%global composer_project guzzle-services

# "php": ">=5.4.0"
%global php_min_ver      5.4.0
# "guzzlehttp/command": "~0.2"
%global command_min_ver  0.2
%global command_max_ver  1.0

# Build using "--without tests" to disable tests
%global with_tests       %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Guzzle service descriptions to describe web services

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests: composer.json
BuildRequires: php(language)          >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/command) or php-packagist(guzzlehttp/command) instead
BuildRequires: php-guzzlehttp-command >= %{command_min_ver}
BuildRequires: php-guzzlehttp-command <  %{command_max_ver}
BuildRequires: php-phpunit-PHPUnit
# For tests: phpcompatinfo (computed from version 0.2.0)
BuildRequires: php-date
BuildRequires: php-filter
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-xmlwriter
%endif

# composer.json
Requires:      php(language)          >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/command) or php-packagist(guzzlehttp/command) instead
Requires:      php-guzzlehttp-command >= %{command_min_ver}
Requires:      php-guzzlehttp-command <  %{command_max_ver}
# phpcompatinfo (computed from version 0.2.0)
Requires:      php-date
Requires:      php-filter
Requires:      php-json
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xmlwriter

# TODO: Provide whichever virtual provide that gets approved in Fedora PHP packaging guidelines
#Provides:      php-composer(%%{composer_vendor}/%%{composer_project}) = %%{version}
#Provides:      php-packagist(%%{composer_vendor}/%%{composer_project}) = %%{version}

%description
Provides an implementation of the Guzzle Command library that uses Guzzle
service descriptions to describe web services, serialize requests, and parse
responses into easy to use model structures.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/GuzzleHttp/Command/Guzzle
cp -pr src/* %{buildroot}%{_datadir}/php/GuzzleHttp/Command/Guzzle/


%check
%if %{with_tests}
# Create autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php

require_once '%{_datadir}/php/GuzzleHttp/Stream/functions.php';
require_once '%{_datadir}/php/GuzzleHttp/functions.php';

spl_autoload_register(function ($class) {
    $src = str_replace(array('\\', '_'), '/', $class).'.php';
    if (!@include_once $src) {
        $psr4_class = preg_replace('#^GuzzleHttp\\\Command\\\Guzzle\\\?#', '', $class);
        $psr4_src = str_replace(array('\\', '_'), '/', $psr4_class).'.php';
        @include_once $psr4_src;
    }
});
AUTOLOAD

# Create PHPUnit config w/ colors turned off
sed 's/colors\s*=\s*"true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --include-path="./src:./tests" -d date.timezone="UTC"
%endif


%files
# LICENSE file requested: https://github.com/guzzle/guzzle-services/pull/22
%doc README.rst composer.json
%{_datadir}/php/GuzzleHttp/Command/Guzzle


%changelog
* Sat May 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2.0-1
- Initial package
