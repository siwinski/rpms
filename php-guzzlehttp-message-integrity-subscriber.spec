%global github_owner     guzzle
%global github_name      message-integrity-subscriber
%global github_version   0.1.1
%global github_commit    ba578b4bad3ea5668a984835af0c4139a14cb0f3

%global composer_vendor  guzzlehttp
%global composer_project message-integrity-subscriber

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
Summary:       Guzzle message integrity subscriber

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
# For tests: phpcompatinfo (computed from version 0.1.1)
BuildRequires: php-hash
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language)         >= %{php_min_ver}
# TODO: Require php-composer(guzzlehttp/guzzle) or php-packagist(guzzlehttp/guzzle) instead
Requires:      php-guzzlehttp-guzzle >= %{guzzle_min_ver}
Requires:      php-guzzlehttp-guzzle <  %{guzzle_max_ver}
# phpcompatinfo (computed from version 0.1.1)
Requires:      php-hash
Requires:      php-spl

# TODO: Provide whichever virtual provide that gets approved in Fedora PHP packaging guidelines
#Provides:      php-composer(%%{composer_vendor}/%%{composer_project}) = %%{version}
#Provides:      php-packagist(%%{composer_vendor}/%%{composer_project}) = %%{version}

%description
Verifies the integrity of HTTP responses using customizable validators.

This plugin can be used, for example, to validate the message integrity of
responses based on the Content-MD5 header. The plugin offers a convenience
method for validating a Content-MD5 header.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/GuzzleHttp/Subscriber/MessageIntegrity
cp -pr src/* %{buildroot}%{_datadir}/php/GuzzleHttp/Subscriber/MessageIntegrity/


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
        $psr4_class = preg_replace('#^GuzzleHttp\\\Subscriber\\\MessageIntegrity\\\?#', '', $class);
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
%dir %{_datadir}/php/GuzzleHttp/Subscriber/
     %{_datadir}/php/GuzzleHttp/Subscriber/MessageIntegrity


%changelog
* Sat May 24 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.1-1
- Initial package
