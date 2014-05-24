%global github_owner     guzzle
%global github_name      command
%global github_version   0.4.0
%global github_commit    a06e799bca01ebddf46757e678ede6cf17147f9e

%global composer_vendor  guzzlehttp
%global composer_project command

# "php": ">=5.4.0"
%global php_min_ver      5.4.0
# "guzzlehttp/guzzle": "~4.0"
%global guzzle_min_ver   4.0
%global guzzle_max_ver   5.0

# Build using "--without tests" to disable tests
%global with_tests       %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Provides the foundation for building command based web service clients

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests: composer.json
BuildRequires: php(language)         >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/guzzle) or php-packagist(guzzlehttp/guzzle) instead
BuildRequires: php-guzzlehttp-guzzle >= %{guzzle_min_ver}
BuildRequires: php-guzzlehttp-guzzle <  %{guzzle_max_ver}
BuildRequires: php-phpunit-PHPUnit
# For tests: phpcompatinfo (computed from version 0.4.0)
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language)         >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/guzzle) or php-packagist(guzzlehttp/guzzle) instead
Requires:      php-guzzlehttp-guzzle >= %{guzzle_min_ver}
Requires:      php-guzzlehttp-guzzle <  %{guzzle_max_ver}
# phpcompatinfo (computed from version 0.4.0)
Requires:      php-spl

# TODO: Provide whichever virtual provide that gets approved in Fedora PHP packaging guidelines
#Provides:      php-composer(%%{composer_vendor}/%%{composer_project}) = %%{version}
#Provides:      php-packagist(%%{composer_vendor}/%%{composer_project}) = %%{version}

%description
This library provides an event-based abstraction over Guzzle HTTP requests and
responses using commands and models. Events are emitted for preparing commands,
processing commands, and handling errors encountered while executing a command.

Commands: Key value pair objects representing an action to take on a web
    service. Commands have a name and a set of parameters.

Models: Models are key value pair objects representing the result of an
    API operation.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/GuzzleHttp/Command
cp -pr src/* %{buildroot}%{_datadir}/php/GuzzleHttp/Command/


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
        $psr4_class = preg_replace('#^GuzzleHttp\\\Command\\\?#', '', $class);
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
%doc LICENSE README.rst composer.json
%{_datadir}/php/GuzzleHttp/Command


%changelog
* Sat May 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Initial package
