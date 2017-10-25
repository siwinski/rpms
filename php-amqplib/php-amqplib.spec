#
# Fedora spec file for php-php-amqplib-php-amqplib
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-amqplib
%global github_name      php-amqplib
%global github_version   2.7.0
%global github_commit    f48748546e398d846134c594dfca9070c4c3b356

%global composer_vendor  php-amqplib
%global composer_project php-amqplib

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Pure PHP implementation of the AMQP protocol

Group:         Development/Libraries
License:       LGPLv2
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-php-amqplib-php-amqplib-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-bcmath
BuildRequires: php-mbstring
BuildRequires: php-sockets
## phpcompatinfo for version 2.7.0
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-bcmath
Requires:      php-mbstring
# composer.json: suggest
Requires:      php-sockets
# phpcompatinfo for version 2.7.0
Requires:      php-date
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
%if 0%{?fedora} >= 21
Suggests:      php-pcntl
%endif

# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      %{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library is a pure PHP implementation of the AMQP 0-9-1 protocol [1]. It's
been tested against RabbitMQ [2].

Autoloader: %{phpdir}/PhpAmqpLib/autoload.php

[1] http://www.rabbitmq.com/tutorials/amqp-concepts.html
[2] http://www.rabbitmq.com/

%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee PhpAmqpLib/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PhpAmqpLib\\', __DIR__);
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp PhpAmqpLib %{buildroot}%{phpdir}/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/PhpAmqpLib/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PhpAmqpLib\\Tests\\Unit\\', __DIR__.'/tests/Unit');
BOOTSTRAP

: Remove tests requiring a running AMQP service
rm -f tests/Unit/Wire/IO/SocketIOTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            --testsuite="Unit Tests"|| RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/PhpAmqpLib


%changelog
* Wed Oct 25 2017 Shawn Iwinski <shawn@iwin.ski> - 2.7.0-1
- Initial package
