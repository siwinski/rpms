#
# Fedora spec file for php-aws-sdk3
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     aws
%global github_name      aws-sdk-php
%global github_version   3.17.6
%global github_commit    d5a5145263da88c9ba870b579c3d4f648b82d2a9

%global composer_vendor  aws
%global composer_project aws-sdk-php

# "php": ">=5.5"
%global php_min_ver 5.5
# "andrewsville/php-token-reflection": "^1.4"
%global tokenreflection_min_ver 1.4
%global tokenreflection_max_ver 2.0
# "aws/aws-php-sns-message-validator": "~1.0"
%global aws_sns_message_validator_min_ver 1.0
%global aws_sns_message_validator_max_ver 2.0
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
# "nette/neon": "^2.3"
%global nette_neon_min_ver 2.3
%global nette_neon_max_ver 3.0
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-aws-sdk3
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Amazon Web Services framework for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://aws.amazon.com/sdkforphp

# GitHub export does not include tests.
# Run php-aws-sdk3-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Library version value and autoloader check
BuildRequires: php-cli                              >= %{php_min_ver}
BuildRequires: php-composer(guzzlehttp/guzzle)      >= %{guzzle_min_ver}
BuildRequires: php-composer(guzzlehttp/promises)    >= %{guzzle_promises_min_ver}
BuildRequires: php-composer(guzzlehttp/psr7)        >= %{guzzle_psr7_min_ver}
BuildRequires: php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
BuildRequires: php-composer(symfony/class-loader)
# Tests
%if %{with_tests}
## Classmap
BuildRequires: php-composer(theseer/autoload)
## composer.json
BuildRequires: php-composer(andrewsville/php-token-reflection) >= %{tokenreflection_min_ver}
BuildRequires: php-composer(aws/aws-php-sns-message-validator) >= %{aws_sns_message_validator_min_ver}
BuildRequires: php-composer(doctrine/cache)                    >= %{doctrine_cache_min_ver}
BuildRequires: php-composer(nette/neon)                        >= %{nette_neon_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/cache)                         >= %{psr_cache_min_ver}
## phpcompatinfo (computed from version 3.17.6)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-xml
BuildRequires: php-xmlwriter
%endif

# composer.json
Requires:      php(language)                        >= %{php_min_ver}
Requires:      php-composer(guzzlehttp/guzzle)      <  %{guzzle_max_ver}
Requires:      php-composer(guzzlehttp/guzzle)      >= %{guzzle_min_ver}
Requires:      php-composer(guzzlehttp/promises)    <  %{guzzle_promises_max_ver}
Requires:      php-composer(guzzlehttp/promises)    >= %{guzzle_promises_min_ver}
Requires:      php-composer(guzzlehttp/psr7)        <  %{guzzle_psr7_max_ver}
Requires:      php-composer(guzzlehttp/psr7)        >= %{guzzle_psr7_min_ver}
Requires:      php-composer(mtdowling/jmespath.php) <  %{jmespath_max_ver}
Requires:      php-composer(mtdowling/jmespath.php) >= %{jmespath_min_ver}
# phpcompatinfo (computed from version 3.17.6)
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

# Weak dependencies
## composer.json: optional
Suggests:      php-curl
Suggests:      php-openssl
Suggests:      php-composer(doctrine/cache)
Conflicts:     php-doctrine-cache <  %{doctrine_cache_min_ver}
Conflicts:     php-doctrine-cache >= %{doctrine_cache_max_ver}
Suggests:      php-composer(aws/aws-php-sns-message-validator)
Conflicts:     php-aws-php-sns-message-validator <  %{aws_sns_message_validator_min_ver}
Conflicts:     php-aws-php-sns-message-validator >= %{aws_sns_message_validator_max_ver}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The AWS SDK for PHP makes it easy for developers to access Amazon Web
Services [1] in their PHP code, and build robust applications and software
using services like Amazon S3, Amazon DynamoDB, Amazon Glacier, etc.

Autoloader: %{phpdir}/Aws3/autoload.php

[1] http://aws.amazon.com/


%prep
%setup -qn %{github_name}-%{github_commit}

: Remove executable bits
chmod a-x composer.json


%build
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
    $fedoraPsr4ClassLoader->register(true);
}

$fedoraPsr4ClassLoader->addPrefix('Aws\\', __DIR__);

// Required dependencies
require_once __DIR__.'/functions.php';
require_once file_exists('%{phpdir}/GuzzleHttp6/autoload.php')
    ? '%{phpdir}/GuzzleHttp6/autoload.php'
    : '%{phpdir}/GuzzleHttp/autoload.php';
require_once '%{phpdir}/GuzzleHttp/Promise/autoload.php';
require_once '%{phpdir}/GuzzleHttp/Psr7/autoload.php';
require_once '%{phpdir}/JmesPath/autoload.php';

// Optional dependencies
@include_once '%{phpdir}/Aws/Sns/autoload.php';
@include_once '%{phpdir}/Doctrine/Common/Cache/autoload.php';
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Aws3
cp -pr src/* %{buildroot}%{phpdir}/Aws3/


%check
: Library version value and autoloader check
%{_bindir}/php -r '
    require_once "%{buildroot}%{phpdir}/Aws3/autoload.php";
    $version = \Aws\Sdk::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with_tests}
: Make PSR-0 tests
mkdir -p tests-psr0/Aws
ln -s ../../tests tests-psr0/Aws/Test

: Create tests classmap
%{_bindir}/phpab --nolower --output bootstrap.classmap.php build/

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
error_reporting(-1);
date_default_timezone_set('UTC');

require_once '%{buildroot}%{phpdir}/Aws3/autoload.php';

$fedoraClassLoader->addPrefix('Aws\\Test\\', __DIR__.'/tests-psr0');
$fedoraClassLoader->addPrefix('TokenReflection\\', '%{phpdir}');

require_once __DIR__.'/bootstrap.classmap.php';
require_once '%{phpdir}/Nette/Neon/autoload.php';
require_once '%{phpdir}/Psr/Cache/autoload.php';
BOOTSTRAP

: Skip tests known to fail
rm -f \
    tests/Integ/GuzzleV5HandlerTest.php \
    tests/Integ/GuzzleV6StreamHandlerTest.php

export AWS_ACCESS_KEY_ID=foo
export AWS_SECRET_ACCESS_KEY=bar
%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc README.md
%doc UPGRADING.md
%{phpdir}/Aws3


%changelog
* Tue Apr 12 2016 Shawn Iwinski <shawn@iwin.ski> - 3.17.6-1
- Initial package
