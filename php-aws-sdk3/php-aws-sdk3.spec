#
# Fedora spec file for php-aws-sdk3
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     aws
%global github_name      aws-sdk-php
%global github_version   3.11.4
%global github_commit    2524c78e0fa1ed049719b8b6b0696f0b6dfb1ca2

%global composer_vendor  aws
%global composer_project aws-sdk-php

# "php": ">=5.5"
%global php_min_ver 5.5
# "doctrine/cache": "~1.4"
%global doctrine_cache_min_ver 1.4
%global doctrine_cache_max_ver 2.0
# "guzzlehttp/guzzle": "~5.3|~6.0.1|~6.1"
%global guzzle_min_ver 5.3
%global guzzle_max_ver 7.0
# "guzzlehttp/promises": "~1.0"
%global guzzle_promises_min_ver 1.0
%global guzzle_promises_max_ver 2.0
# "guzzlehttp/psr7": "~1.0"
%global guzzle_psr7_min_ver 1.0
%global guzzle_psr7_max_ver 2.0
# "mtdowling/jmespath.php": "~2.2"
%global jmespath_min_ver 2.2
%global jmespath_max_ver 3.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-aws-sdk3
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Amazon Web Services framework for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://aws.amazon.com/sdkforphp
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli

# composer.json
Requires:      php(language)                        >= %{php_min_ver}
Requires:      php-composer(guzzlehttp/guzzle)      >= %{guzzle_min_ver}
Requires:      php-composer(guzzlehttp/guzzle)      <  %{guzzle_max_ver}
Requires:      php-composer(guzzlehttp/promises)    >= %{guzzle_promises_min_ver}
Requires:      php-composer(guzzlehttp/promises)    <  %{guzzle_promises_max_ver}
Requires:      php-composer(guzzlehttp/psr7)        >= %{guzzle_psr7_min_ver}
Requires:      php-composer(guzzlehttp/psr7)        <  %{guzzle_psr7_max_ver}
Requires:      php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
Requires:      php-composer(mtdowling/jmespath.php) <  %{jmespath_max_ver}
# composer.json: optional
Suggests:      php-curl
Suggests:      php-openssl
Suggests:      php-composer(doctrine/cache)         >= %{doctrine_cache_min_ver}
Suggests:      php-composer(doctrine/cache)         <  %{doctrine_cache_max_ver}
# phpcompatinfo (computed from version 3.11.4)
Requires:      php-date
Requires:      php-filter
Requires:      php-hash
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-session
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xmlwriter
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The AWS SDK for PHP makes it easy for developers to access Amazon Web
Services [1] in their PHP code, and build robust applications and software
using services like Amazon S3, Amazon DynamoDB, Amazon Glacier, etc.

[1] http://aws.amazon.com/


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

if (!isset($fedoraPsr4ClassLoader) || !($fedoraPsr4ClassLoader instanceof \Symfony\Component\ClassLoader\Psr4ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\Psr4ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/Psr4ClassLoader.php';
    }

    $fedoraPsr4ClassLoader = new \Symfony\Component\ClassLoader\Psr4ClassLoader();
    $fedoraPsr4ClassLoader->register();
}

$fedoraPsr4ClassLoader->addPrefix('Aws\\', __DIR__);

// Required dependencies
require_once __DIR__ . '/functions.php';
require_once file_exists('%{phpdir}/GuzzleHttp6/autoload.php')
    ? '%{phpdir}/GuzzleHttp6/autoload.php'
    : '%{phpdir}/GuzzleHttp/autoload.php';
require_once '%{phpdir}/GuzzleHttp/Promise/autoload.php';
require_once '%{phpdir}/GuzzleHttp/Psr7/autoload.php';
require_once '%{phpdir}/JmesPath/autoload.php';

// Optional dependency
if (file_exists('%{phpdir}/Doctrine/Common/Cache/autoload.php')) {
    require_once '%{phpdir}/Doctrine/Common/Cache/autoload.php';
}
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/Aws3
cp -pr src/* %{buildroot}%{phpdir}/Aws3/


%check
: Library version value check
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Aws3/autoload.php";
    exit(version_compare("%{version}", \Aws\Sdk::VERSION, "=") ? 0 : 1);'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc composer.json
%{phpdir}/Aws3


%changelog
* Sun Dec 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.11.4-1
- Initial package
