#
# Fedora spec file for php-symfony4
#
# Copyright (c) 2016-2017 Shawn Iwinski <shawn@iwin.ski>
#                         Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      symfony
%global github_version   4.0.0
%global github_prerelease beta1
%global github_commit    88e66db9d83cb81d84fc3c0e9365678c79f17414

%global composer_vendor  symfony
%global composer_project symfony

# "php": "^7.1.3"
%global php_min_ver 7.1.3
# "cache/integration-tests": "dev-master"
#    NOTE: Min and max versions added to restrict to single major version
%global cache_integration_tests_min_ver 0
%global cache_integration_tests_max_ver 1
# "doctrine/annotations": "~1.0"
#     src/Symfony/Bundle/FrameworkBundle/composer.json
#     src/Symfony/Bundle/TwigBundle/composer.json
#     src/Symfony/Component/PropertyInfo/composer.json
#     src/Symfony/Component/Routing/composer.json
#     src/Symfony/Component/Serializer/composer.json
#     src/Symfony/Component/Validator/composer.json
%global doctrine_annotations_min_ver 1.0
%global doctrine_annotations_max_ver 2.0
# "doctrine/cache": "~1.6"
%global doctrine_cache_min_ver 1.6
%global doctrine_cache_max_ver 2.0
# "doctrine/common": "~2.4"
%global doctrine_common_min_ver 2.4
%global doctrine_common_max_ver 3.0
# "doctrine/data-fixtures": "1.0.*"
%global doctrine_datafixtures_min_ver 1.0.0
%global doctrine_datafixtures_max_ver 1.1.0
# "doctrine/dbal": "~2.4"
%global doctrine_dbal_min_ver 2.4
%global doctrine_dbal_max_ver 3.0
# "doctrine/doctrine-bundle": "~1.4"
%global doctrine_bundle_min_ver 1.4
%global doctrine_bundle_max_ver 2.0
# "doctrine/orm": "~2.4,>=2.4.5"
%global doctrine_orm_min_ver 2.4.5
%global doctrine_orm_max_ver 3.0
# "egulias/email-validator": "~1.2,>=1.2.8|~2.0"
%global email_validator_min_ver 1.2.8
%global email_validator_max_ver 3.0
# "fig/link-util": "^1.0"
%global fig_link_util_min_ver 1.0
%global fig_link_util_max_ver 2.0
# "monolog/monolog": "~1.11"
%global monolog_min_ver 1.11
%global monolog_max_ver 2.0
# "ocramius/proxy-manager": "~0.4|~1.0|~2.0"
#     NOTE: Min version not 0.4 to force v1 or v2.
%global proxy_manager_min_ver 1.0
%global proxy_manager_max_ver 3.0
# "phpdocumentor/reflection-docblock": "^3.0|^4.0"
# conflicts: "phpdocumentor/reflection-docblock": "<3.0||>=3.2.0,<3.2.2"
%global phpdocumentor_reflection_docblock_min_ver 3.0
%global phpdocumentor_reflection_docblock_max_ver 5.0
# "psr/cache": "~1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "psr/container": "^1.0"
%global psr_container_min_ver 1.0
%global psr_container_max_ver 2.0
# "psr/link": "^1.0"
%global psr_link_min_ver 1.0
%global psr_link_max_ver 2.0
# "psr/log": "~1.0"
%global psr_log_min_ver 1.0
%global psr_log_max_ver 2.0
# "psr/simple-cache": "^1.0"
%global psr_simple_cache_min_ver 1.0
%global psr_simple_cache_max_ver 2.0
# "symfony/polyfill-intl-icu": "~1.0"
# "symfony/polyfill-mbstring": "~1.0"
# "symfony/polyfill-php72": "~1.0"
%global symfony_polyfill_min_ver 1.0
%global symfony_polyfill_max_ver 2.0
# "symfony/security-acl": "~2.8|~3.0"
#     NOTE: Min version not 4.0 to restrict to single major version
%global symfony_security_acl_min_ver 2.8
%global symfony_security_acl_max_ver 3.0
# "twig/twig": "^1.35|^2.4.4"
%global twig_min_ver 1.35
%global twig_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%global with_sensio_framework_extra_bundle 0

%global php_version_id %(%{_bindir}/php -r "echo PHP_VERSION_ID;")

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global symfony4_dir %{phpdir}/Symfony4

%global symfony4_doc_ver %(echo "%{github_version}" | awk 'BEGIN { FS="." } { print $1"."$2 }')

Name:          php-%{composer_project}4
Version:       %{github_version}
Release:       0.1%{?github_prerelease:.%{github_prerelease}}%{?dist}
Summary:       Symfony PHP framework (version 4)

Group:         Development/Libraries
# MIT and CC-BY-SA:
#     - WebProfiler bundle (web-profiler-bundle sub-package)
# MIT:
#     - All other bridges/bundles/components
License:       MIT and CC-BY-SA
URL:           http://symfony.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-generate-autoloaders.php

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: composer
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(cache/integration-tests) <  %{cache_integration_tests_max_ver}
BuildRequires: php-composer(cache/integration-tests) >= %{cache_integration_tests_min_ver}
BuildRequires: php-composer(doctrine/annotations) <  %{doctrine_annotations_max_ver}
BuildRequires: php-composer(doctrine/annotations) >= %{doctrine_annotations_min_ver}
BuildRequires: php-composer(doctrine/cache) <  %{doctrine_cache_max_ver}
BuildRequires: php-composer(doctrine/cache) >= %{doctrine_cache_min_ver}
BuildRequires: php-composer(doctrine/common) <  %{doctrine_common_max_ver}
BuildRequires: php-composer(doctrine/common) >= %{doctrine_common_min_ver}
BuildRequires: php-composer(doctrine/data-fixtures) <  %{doctrine_datafixtures_max_ver}
BuildRequires: php-composer(doctrine/data-fixtures) >= %{doctrine_datafixtures_min_ver}
BuildRequires: php-composer(doctrine/dbal) <  %{doctrine_dbal_max_ver}
BuildRequires: php-composer(doctrine/dbal) >= %{doctrine_dbal_min_ver}
BuildRequires: php-composer(doctrine/doctrine-bundle) <  %{doctrine_bundle_max_ver}
BuildRequires: php-composer(doctrine/doctrine-bundle) >= %{doctrine_bundle_min_ver}
BuildRequires: php-composer(doctrine/orm) <  %{doctrine_orm_max_ver}
BuildRequires: php-composer(doctrine/orm) >= %{doctrine_orm_min_ver}
BuildRequires: php-composer(egulias/email-validator) <  %{email_validator_max_ver}
BuildRequires: php-composer(egulias/email-validator) >= %{email_validator_min_ver}
BuildRequires: php-composer(fig/link-util) <  %{fig_link_util_max_ver}
BuildRequires: php-composer(fig/link-util) >= %{fig_link_util_min_ver}
BuildRequires: php-composer(monolog/monolog) <  %{monolog_max_ver}
BuildRequires: php-composer(monolog/monolog) >= %{monolog_min_ver}
BuildRequires: php-composer(ocramius/proxy-manager) <  %{proxy_manager_max_ver}
BuildRequires: php-composer(ocramius/proxy-manager) >= %{proxy_manager_min_ver}
BuildRequires: php-composer(phpdocumentor/reflection-docblock) <  %{phpdocumentor_reflection_docblock_max_ver}
BuildRequires: php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver}
BuildConflicts: php-composer(phpdocumentor/reflection-docblock) = 3.2.0
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/container) <  %{psr_container_max_ver}
BuildRequires: php-composer(psr/container) >= %{psr_container_min_ver}
BuildRequires: php-composer(psr/link) <  %{psr_link_max_ver}
BuildRequires: php-composer(psr/link) >= %{psr_link_min_ver}
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
BuildRequires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
BuildRequires: php-composer(symfony/polyfill) <  %{symfony_polyfill_max_ver}
BuildRequires: php-composer(symfony/polyfill) >= %{symfony_polyfill_min_ver}
BuildRequires: php-composer(symfony/security-acl) <  %{symfony_security_acl_max_ver}
BuildRequires: php-composer(symfony/security-acl) >= %{symfony_security_acl_min_ver}
BuildRequires: php-composer(twig/twig) <  %{twig_max_ver}
BuildRequires: php-composer(twig/twig) >= %{twig_min_ver}
# phpcompatinfo for version 4.0.0-beta1
BuildRequires: php-ctype
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-fileinfo
BuildRequires: php-filter
BuildRequires: php-gd
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-json
BuildRequires: php-ldap
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-pdo_sqlite
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-simplexml
BuildRequires: php-sockets
BuildRequires: php-spl
BuildRequires: php-sysvsem
BuildRequires: php-tokenizer
BuildRequires: php-xml
BuildRequires: php-xmlreader
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# Bridges
Requires:      php-composer(%{composer_vendor}/doctrine-bridge) = %{version}
Requires:      php-composer(%{composer_vendor}/monolog-bridge) = %{version}
#Requires:      php-composer(%%{composer_vendor}/phpunit-bridge) = %%{version}
%if 0%{?fedora} >= 26
# this requires ZF and thus PHP 7
Requires:      php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}
%endif
Requires:      php-composer(%{composer_vendor}/twig-bridge) = %{version}
# Bundles
Requires:      php-composer(%{composer_vendor}/debug-bundle) = %{version}
Requires:      php-composer(%{composer_vendor}/framework-bundle) = %{version}
Requires:      php-composer(%{composer_vendor}/security-bundle) = %{version}
Requires:      php-composer(%{composer_vendor}/twig-bundle) = %{version}
Requires:      php-composer(%{composer_vendor}/web-profiler-bundle) = %{version}
Requires:      php-composer(%{composer_vendor}/web-server-bundle) = %{version}
# Components
Requires:      php-composer(%{composer_vendor}/asset) = %{version}
Requires:      php-composer(%{composer_vendor}/browser-kit) = %{version}
Requires:      php-composer(%{composer_vendor}/cache) = %{version}
Requires:      php-composer(%{composer_vendor}/config) = %{version}
Requires:      php-composer(%{composer_vendor}/console) = %{version}
Requires:      php-composer(%{composer_vendor}/css-selector) = %{version}
Requires:      php-composer(%{composer_vendor}/debug) = %{version}
Requires:      php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires:      php-composer(%{composer_vendor}/dom-crawler) = %{version}
Requires:      php-composer(%{composer_vendor}/dotenv) = %{version}
Requires:      php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires:      php-composer(%{composer_vendor}/expression-language) = %{version}
Requires:      php-composer(%{composer_vendor}/filesystem) = %{version}
Requires:      php-composer(%{composer_vendor}/finder) = %{version}
Requires:      php-composer(%{composer_vendor}/form) = %{version}
Requires:      php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires:      php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires:      php-composer(%{composer_vendor}/inflector) = %{version}
Requires:      php-composer(%{composer_vendor}/intl) = %{version}
Requires:      php-composer(%{composer_vendor}/ldap) = %{version}
Requires:      php-composer(%{composer_vendor}/lock) = %{version}
Requires:      php-composer(%{composer_vendor}/options-resolver) = %{version}
Requires:      php-composer(%{composer_vendor}/process) = %{version}
Requires:      php-composer(%{composer_vendor}/property-access) = %{version}
Requires:      php-composer(%{composer_vendor}/property-info) = %{version}
Requires:      php-composer(%{composer_vendor}/routing) = %{version}
Requires:      php-composer(%{composer_vendor}/security) = %{version}
Requires:      php-composer(%{composer_vendor}/serializer) = %{version}
Requires:      php-composer(%{composer_vendor}/stopwatch) = %{version}
Requires:      php-composer(%{composer_vendor}/templating) = %{version}
Requires:      php-composer(%{composer_vendor}/translation) = %{version}
Requires:      php-composer(%{composer_vendor}/validator) = %{version}
Requires:      php-composer(%{composer_vendor}/var-dumper) = %{version}
Requires:      php-composer(%{composer_vendor}/web-link) = %{version}
Requires:      php-composer(%{composer_vendor}/workflow) = %{version}
Requires:      php-composer(%{composer_vendor}/yaml) = %{version}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

NOTE: Does not require PHPUnit bridge.

# ##############################################################################

%package common

Summary:  Symfony common (version 4)
License:  MIT

Requires: php(language) >= %{php_min_ver}
Requires: composer
# Autoloader
Requires: php-composer(fedora/autoloader)

%description common
%{summary}.

# ------------------------------------------------------------------------------

%package doctrine-bridge

Summary:  Symfony Doctrine Bridge (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(doctrine/common) >= %{doctrine_common_min_ver}
Requires: php-composer(doctrine/common) <  %{doctrine_common_max_ver}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/form)
Suggests: php-composer(%{composer_vendor}/property-info)
Suggests: php-composer(%{composer_vendor}/validator)
Suggests: php-composer(doctrine/data-fixtures)
Suggests: php-composer(doctrine/dbal)
Suggests: php-composer(doctrine/orm)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-date
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-pdo_sqlite
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/doctrine-bridge) = %{version}

%description doctrine-bridge
Provides integration for Doctrine (http://www.doctrine-project.org/) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/%{symfony4_doc_ver}/reference/configuration/doctrine.html

Autoloader: %{symfony4_dir}/Bridge/Doctrine/autoload.php

# ------------------------------------------------------------------------------

%package monolog-bridge

Summary:  Symfony Monolog Bridge (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(monolog/monolog) >= %{monolog_min_ver}
Requires: php-composer(monolog/monolog) <  %{monolog_max_ver}
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/console)
Suggests: php-composer(%{composer_vendor}/event-dispatcher)
%endif

# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre

# Composer
Provides: php-composer(%{composer_vendor}/monolog-bridge) = %{version}

%description monolog-bridge
Provides integration for Monolog (https://github.com/Seldaek/monolog) with
various Symfony components.

Configuration reference:
http://symfony.com/doc/%{symfony4_doc_ver}/reference/configuration/monolog.html

Autoloader: %{symfony4_dir}/Bridge/Monolog/autoload.php

# ------------------------------------------------------------------------------

%package phpunit-bridge

Summary:  Symfony PHPUnit Bridge (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/debug)
Suggests: php-pecl(zip)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-pcre
Requires: php-posix
Requires: php-reflection

# Composer
Provides: php-composer(%{composer_vendor}/phpunit-bridge) = %{version}

%description phpunit-bridge
Provides utilities for PHPUnit, especially user deprecation notices management.

It comes with the following features:
* disable the garbage collector
* auto-register class_exists to load Doctrine annotations
* print a user deprecation notices summary at the end of the test suite.

Autoloader: %{symfony4_dir}/Bridge/PhpUnit/autoload.php

# ------------------------------------------------------------------------------

%package proxy-manager-bridge

Summary:  Symfony ProxyManager Bridge (version 4)
License:  MIT

# composer.json
Requires: php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires: php-composer(ocramius/proxy-manager) >= %{proxy_manager_min_ver}
Requires: php-composer(ocramius/proxy-manager) <  %{proxy_manager_max_ver}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-hash
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/proxy-manager-bridge) = %{version}

%description proxy-manager-bridge
Provides integration for ProxyManager [1] with various Symfony components.

Autoloader: %{symfony4_dir}/Bridge/ProxyManager/autoload.php

[1] http://ocramius.github.io/ProxyManager/

# ------------------------------------------------------------------------------

%package twig-bridge

Summary:  Symfony Twig Bridge (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(twig/twig) >= %{twig_min_ver}
Requires: php-composer(twig/twig) <  %{twig_max_ver}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/asset)
Suggests: php-composer(%{composer_vendor}/expression-language)
Suggests: php-composer(%{composer_vendor}/finder)
Suggests: php-composer(%{composer_vendor}/form)
Suggests: php-composer(%{composer_vendor}/http-kernel)
Suggests: php-composer(%{composer_vendor}/routing)
Suggests: php-composer(%{composer_vendor}/security)
Suggests: php-composer(%{composer_vendor}/stopwatch)
Suggests: php-composer(%{composer_vendor}/templating)
Suggests: php-composer(%{composer_vendor}/translation)
Suggests: php-composer(%{composer_vendor}/var-dumper)
Suggests: php-composer(%{composer_vendor}/web-link)
Suggests: php-composer(%{composer_vendor}/yaml)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-hash
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/twig-bridge) = %{version}

%description twig-bridge
Provides integration for Twig (http://twig.sensiolabs.org/) with various
Symfony components.

Autoloader: %{symfony4_dir}/Bridge/Twig/autoload.php

# ------------------------------------------------------------------------------

%package debug-bundle

Summary:  Symfony Debug Bundle (version 4)
License:  MIT

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge) = %{version}
Requires: php-composer(%{composer_vendor}/var-dumper) = %{version}
Requires: php-xml
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/dependency-injection)
%endif
# phpcompatinfo for version 4.0.0-beta1
#     <none>

# Composer
Provides: php-composer(%{composer_vendor}/debug-bundle) = %{version}

%description debug-bundle
%{summary}.

Autoloader: %{symfony4_dir}/Bundle/DebugBundle/autoload.php

# ------------------------------------------------------------------------------

%package framework-bundle

Summary:  Symfony Framework Bundle (version 4)
License:  MIT

# composer.json
Requires: php-composer(%{composer_vendor}/cache) = %{version}
Requires: php-composer(%{composer_vendor}/config) = %{version}
Requires: php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires: php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires: php-composer(%{composer_vendor}/filesystem) = %{version}
Requires: php-composer(%{composer_vendor}/finder) = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/routing) = %{version}
Requires: php-composer(doctrine/cache) >= %{doctrine_cache_min_ver}
Requires: php-composer(doctrine/cache) <  %{doctrine_cache_max_ver}
Requires: php-xml
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/console)
Suggests: php-composer(%{composer_vendor}/form)
Suggests: php-composer(%{composer_vendor}/property-info)
Suggests: php-composer(%{composer_vendor}/serializer)
Suggests: php-composer(%{composer_vendor}/validator)
Suggests: php-composer(%{composer_vendor}/web-link)
Suggests: php-composer(%{composer_vendor}/yaml)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-dom
Requires: php-fileinfo
Requires: php-hash
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-reflection
Requires: php-spl
%if 0%{?fedora}
Suggests: php-pecl(apcu)
%endif

# Composer
Provides: php-composer(%{composer_vendor}/framework-bundle) = %{version}

%description framework-bundle
The FrameworkBundle contains most of the "base" framework functionality and can
be configured under the framework key in your application configuration. This
includes settings related to sessions, translation, forms, validation, routing
and more.

Configuration reference:
http://symfony.com/doc/%{symfony4_doc_ver}/reference/configuration/framework.html

Autoloader: %{symfony4_dir}/Bundle/FrameworkBundle/autoload.php

# ------------------------------------------------------------------------------

%package security-bundle

Summary:  Symfony Security Bundle (version 4)
License:  MIT

# composer.json
Requires: php-composer(%{composer_vendor}/dependency-injection) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/security) = %{version}
Requires: php-xml
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/security-bundle) = %{version}

%description security-bundle
%{summary}.

Autoloader: %{symfony4_dir}/Bundle/SecurityBundle/autoload.php

# ------------------------------------------------------------------------------

%package twig-bundle

Summary:  Symfony Twig Bundle (version 4)
License:  MIT

# composer.json
Requires: php-composer(%{composer_vendor}/config) = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge) = %{version}
Requires: php-composer(twig/twig) <  %{twig_max_ver}
Requires: php-composer(twig/twig) >= %{twig_min_ver}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/twig-bundle) = %{version}

%description twig-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/%{symfony4_doc_ver}/reference/configuration/twig.html

Autoloader: %{symfony4_dir}/Bundle/TwigBundle/autoload.php

# ------------------------------------------------------------------------------

%package web-profiler-bundle

Summary:  Symfony WebProfiler Bundle (version 4)

# composer.json
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/routing) = %{version}
Requires: php-composer(%{composer_vendor}/twig-bridge) = %{version}
Requires: php-composer(%{composer_vendor}/var-dumper) = %{version}
Requires: php-composer(twig/twig) <  %{twig_max_ver}
Requires: php-composer(twig/twig) >= %{twig_min_ver}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/web-profiler-bundle) = %{version}

%description web-profiler-bundle
%{summary}

Configuration reference:
http://symfony.com/doc/%{symfony4_doc_ver}/reference/configuration/web_profiler.html

Autoloader: %{symfony4_dir}/Bundle/WebProfilerBundle/autoload.php

# ------------------------------------------------------------------------------

%package web-server-bundle

Summary:  Symfony WebServer Bundle (version 4)
License:  MIT

# composer.json
Requires: php-composer(%{composer_vendor}/console) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/process) = %{version}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-posix
Requires: php-spl
%if 0%{?fedora}
Suggests: php-pcntl
%endif

# Composer
Provides: php-composer(%{composer_vendor}/web-server-bundle) = %{version}

%description web-server-bundle
%{summary}.

Autoloader: %{symfony4_dir}/Bundle/WebServerBundle/autoload.php

# ------------------------------------------------------------------------------

%package asset

Summary:  Symfony Asset Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/asset.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/http-foundation)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-hash
Requires: php-json
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/asset) = %{version}

%description asset
The Asset component manages asset URLs.

Autoloader: %{symfony4_dir}/Component/Asset/autoload.php

# ------------------------------------------------------------------------------

%package browser-kit

Summary:  Symfony BrowserKit Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/browser_kit.html

# composer.json
Requires: php-composer(%{composer_vendor}/dom-crawler) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/process)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/browser-kit) = %{version}

%description browser-kit
BrowserKit simulates the behavior of a web browser.

The component only provide an abstract client and does not provide any
"default" backend for the HTTP layer.

Autoloader: %{symfony4_dir}/Component/BrowserKit/autoload.php

# ------------------------------------------------------------------------------

%package cache

Summary:  Symfony implementation of PSR-6 (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/cache.html

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(psr/cache) <  %{psr_cache_max_ver}
Requires: php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires: php-composer(psr/log) <  %{psr_log_max_ver}
Requires: php-composer(psr/log) >= %{psr_log_min_ver}
Requires: php-composer(psr/simple-cache) <  %{psr_simple_cache_max_ver}
Requires: php-composer(psr/simple-cache) >= %{psr_simple_cache_min_ver}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-hash
Requires: php-pcre
Requires: php-pdo
Requires: php-reflection
Requires: php-spl
%if 0%{?fedora}
Suggests: php-pecl(apcu)
Suggests: php-pecl(memcached)
Suggests: php-pecl(opcache)
Suggests: php-pecl(redis)
%endif

# Composer
Provides: php-composer(%{composer_vendor}/cache) = %{version}
Provides: php-composer(psr/cache-implementation) = 1.0
Provides: php-composer(psr/simple-cache-implementation) = 1.0

%description cache
The Cache component provides an extended PSR-6 [1] implementation for adding
cache to your applications. It is designed to have a low overhead and it ships
with ready to use adapters for the most common caching backends.

Autoloader: %{symfony4_dir}/Component/Cache/autoload.php

[1] http://www.php-fig.org/psr/psr-6/

# ------------------------------------------------------------------------------

%package config

Summary:  Symfony Config Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/config.html

# composer.json
Requires: php-composer(%{composer_vendor}/filesystem) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/yaml)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-dom
Requires: php-hash
Requires: php-json
Requires: php-libxml
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/config) = %{version}

%description config
The Config Component provides several classes to help you find, load, combine,
autofill and validate configuration values of any kind, whatever their source
may be (Yaml, XML, INI files, or for instance a database).

Autoloader: %{symfony4_dir}/Component/Config/autoload.php

# ------------------------------------------------------------------------------

%package console

Summary:  Symfony Console Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/console.html

# composer.json
Requires: php-composer(%{composer_vendor}/debug) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/event-dispatcher)
Suggests: php-composer(%{composer_vendor}/lock)
Suggests: php-composer(%{composer_vendor}/process)
Suggests: php-composer(psr/log)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-dom
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/console) = %{version}

%description console
The Console component eases the creation of beautiful and testable command line
interfaces.

The Console component allows you to create command-line commands. Your console
commands can be used for any recurring task, such as cronjobs, imports, or
other batch jobs.

Autoloader: %{symfony4_dir}/Component/Console/autoload.php

# ------------------------------------------------------------------------------

%package css-selector

Summary:  Symfony CssSelector Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/css_selector.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre

# Composer
Provides: php-composer(%{composer_vendor}/css-selector) = %{version}

%description css-selector
The CssSelector Component converts CSS selectors to XPath expressions.

Autoloader: %{symfony4_dir}/Component/CssSelector/autoload.php

# ------------------------------------------------------------------------------

%package debug

Summary:  Symfony Debug Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/debug.html

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(psr/log) >= %{psr_log_min_ver}
Requires: php-composer(psr/log) <  %{psr_log_max_ver}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-spl
%if 0%{?fedora}
Suggests: php-pecl(Xdebug)
%endif

# Composer
Provides: php-composer(%{composer_vendor}/debug) = %{version}

%description debug
The Debug Component provides tools to ease debugging PHP code.

Autoloader: %{symfony4_dir}/Component/Debug/autoload.php

# ------------------------------------------------------------------------------

%package dependency-injection

Summary:  Symfony DependencyInjection Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/dependency_injection.html

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(psr/container) >= %{psr_container_min_ver}
Requires: php-composer(psr/container) <  %{psr_container_max_ver}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/expression-language)
Suggests: php-composer(%{composer_vendor}/finder)
Suggests: php-composer(%{composer_vendor}/proxy-manager-bridge)
Suggests: php-composer(%{composer_vendor}/yaml)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-dom
Requires: php-hash
Requires: php-json
Requires: php-libxml
Requires: php-pcre
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/dependency-injection) = %{version}
Provides: php-composer(psr/container-implementation) = 1.0

%description dependency-injection
The Dependency Injection component allows you to standardize and centralize
the way objects are constructed in your application.

Autoloader: %{symfony4_dir}/Component/DependencyInjection/autoload.php

# ------------------------------------------------------------------------------

%package dom-crawler

Summary:  Symfony DomCrawler Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/dom_crawler.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/css-selector)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-dom
Requires: php-hash
Requires: php-libxml
Requires: php-mbstring
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/dom-crawler) = %{version}

%description dom-crawler
The DomCrawler Component eases DOM navigation for HTML and XML documents.

Autoloader: %{symfony4_dir}/Component/DomCrawler/autoload.php

# ------------------------------------------------------------------------------

%package dotenv

Summary:  Registers environment variables from a .env file (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/dotenv.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/dotenv) = %{version}

%description dotenv
The Dotenv Component parses .env files to make environment variables stored in
them accessible via getenv(), $_ENV or $_SERVER.

Autoloader: %{symfony4_dir}/Component/Dotenv/autoload.php

# ------------------------------------------------------------------------------

%package event-dispatcher

Summary:  Symfony EventDispatcher Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/event_dispatcher.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/dependency-injection)
Suggests: php-composer(%{composer_vendor}/http-kernel)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/event-dispatcher) = %{version}

%description event-dispatcher
The Symfony Event Dispatcher component implements the Observer [1] pattern in
a simple and effective way to make all these things possible and to make your
projects truly extensible.

Autoloader: %{symfony4_dir}/Component/EventDispatcher/autoload.php

[1] http://en.wikipedia.org/wiki/Observer_pattern

# ------------------------------------------------------------------------------

%package expression-language

Summary:  Symfony ExpressionLanguage Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/expression_language.html

Requires: php-composer(%{composer_vendor}/cache) = %{version}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/expression-language) = %{version}

%description expression-language
The ExpressionLanguage component provides an engine that can compile and
evaluate expressions. An expression is a one-liner that returns a value
(mostly, but not limited to, Booleans).

Autoloader: %{symfony4_dir}/Component/ExpressionLanguage/autoload.php

# ------------------------------------------------------------------------------

%package filesystem

Summary:  Symfony Filesystem Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/filesystem.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/filesystem) = %{version}

%description filesystem
The Filesystem component provides basic utilities for the filesystem.

Autoloader: %{symfony4_dir}/Component/Filesystem/autoload.php

# ------------------------------------------------------------------------------

%package finder

Summary:  Symfony Finder Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/finder.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/finder) = %{version}

%description finder
The Finder Component finds files and directories via an intuitive fluent
interface.

Autoloader: %{symfony4_dir}/Component/Finder/autoload.php

# ------------------------------------------------------------------------------

%package form

Summary:  Symfony Form Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/form.html

# composer.json
Requires: php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires: php-composer(%{composer_vendor}/intl) = %{version}
Requires: php-composer(%{composer_vendor}/options-resolver) = %{version}
Requires: php-composer(%{composer_vendor}/property-access) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/framework-bundle)
Suggests: php-composer(%{composer_vendor}/security-csrf)
Suggests: php-composer(%{composer_vendor}/twig-bridge)
Suggests: php-composer(%{composer_vendor}/validator)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-reflection
Requires: php-ctype
Requires: php-date
Requires: php-hash
Requires: php-intl
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/form) = %{version}

%description form
Form provides tools for defining forms, rendering and mapping request data
to related models. Furthermore it provides integration with the Validation
component.

Autoloader: %{symfony4_dir}/Component/Form/autoload.php

# ------------------------------------------------------------------------------

%package http-foundation

Summary:  Symfony HttpFoundation Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/http_foundation.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-fileinfo
Requires: php-filter
Requires: php-hash
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-pdo
Requires: php-session
Requires: php-sockets
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/http-foundation) = %{version}

%description http-foundation
The HttpFoundation Component defines an object-oriented layer for the HTTP
specification.

In PHP, the request is represented by some global variables ($_GET, $_POST,
$_FILES, $_COOKIE, $_SESSION, ...) and the response is generated by some
functions (echo, header, setcookie, ...).

The Symfony HttpFoundation component replaces these default PHP global
variables and functions by an Object-Oriented layer.

Autoloader: %{symfony4_dir}/Component/HttpFoundation/autoload.php

# ------------------------------------------------------------------------------

%package http-kernel

Summary:  Symfony HttpKernel Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/http_kernel.html

# composer.json
Requires: php-composer(%{composer_vendor}/debug) = %{version}
Requires: php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(psr/log) >= %{psr_log_min_ver}
Requires: php-composer(psr/log) <  %{psr_log_max_ver}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/browser-kit)
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/console)
Suggests: php-composer(%{composer_vendor}/dependency-injection)
Suggests: php-composer(%{composer_vendor}/var-dumper)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-date
Requires: php-hash
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-session
Requires: php-spl
Requires: php-tokenizer
%if 0%{?fedora}
Suggests: php-pecl(apcu)
Suggests: php-pecl(opcache)
Suggests: php-pecl(Xdebug)
%endif

# Composer
Provides: php-composer(%{composer_vendor}/http-kernel) = %{version}

%description http-kernel
The HttpKernel Component provides a structured process for converting a Request
into a Response by making use of the event dispatcher. It's flexible enough to
create a full-stack framework (Symfony), a micro-framework (Silex) or an
advanced CMS system (Drupal).

Configuration reference:
http://symfony.com/doc/%{symfony4_doc_ver}/reference/configuration/kernel.html

Autoloader: %{symfony4_dir}/Component/HttpKernel/autoload.php

# ------------------------------------------------------------------------------

%package inflector

Summary:  Symfony Inflector Component (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype

# Composer
Provides: php-composer(%{composer_vendor}/inflector) = %{version}

%description inflector
Symfony Inflector Component (version 4).

Autoloader: %{symfony4_dir}/Component/Inflector/autoload.php

# ------------------------------------------------------------------------------

%package intl

Summary:  Symfony Intl Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/intl.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
Requires: php-intl
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-date
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/intl) = %{version}

%description intl
A PHP replacement layer for the C intl extension [1] that also provides access
to the localization data of the ICU library [2].

Autoloader: %{symfony4_dir}/Component/Intl/autoload.php

[1] http://www.php.net/manual/en/book.intl.php
[2] http://site.icu-project.org/

# ------------------------------------------------------------------------------

%package ldap

Summary:  An abstraction in front of PHP's LDAP functions (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/ldap.html

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(%{composer_vendor}/options-resolver) = %{version}
Requires: php-ldap
# phpcompatinfo for version 4.0.0-beta1
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/ldap) = %{version}

%description ldap
%{summary}.

Autoloader: %{symfony4_dir}/Component/Ldap/autoload.php

# ------------------------------------------------------------------------------

%package lock

Summary:  Symfony Lock Component (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(psr/log) <  %{psr_log_max_ver}
Requires: php-composer(psr/log) >= %{psr_log_min_ver}
Requires: php-ldap
# phpcompatinfo for version 4.0.0-beta1
Requires: php-hash
Requires: php-pcre
Requires: php-spl
%if 0%{?fedora}
Suggests: php-pecl(memcached)
Suggests: php-pecl(sysvsem)
%endif

# Composer
Provides: php-composer(%{composer_vendor}/lock) = %{version}

%description lock
%{summary}.

Autoloader: %{symfony4_dir}/Component/Lock/autoload.php

# ------------------------------------------------------------------------------

%package options-resolver

Summary:  Symfony OptionsResolver Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/options_resolver.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-reflection
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/options-resolver) = %{version}

%description options-resolver
The OptionsResolver Component helps you configure objects with option arrays.
It supports default values, option constraints and lazy options.

Autoloader: %{symfony4_dir}/Component/OptionsResolver/autoload.php

# ------------------------------------------------------------------------------

%package process

Summary:  Symfony Process Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/process.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-posix
Requires: php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/process) = %{version}

%description process
The Process component executes commands in sub-processes.

Autoloader: %{symfony4_dir}/Component/Process/autoload.php

# ------------------------------------------------------------------------------

%package property-access

Summary:  Symfony PropertyAccess Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/property_access.html

# composer.json
Requires: php-composer(%{composer_vendor}/inflector) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(psr/cache-implementation)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/property-access) = %{version}

%description property-access
The PropertyAccess component provides function to read and write from/to an
object or array using a simple string notation.

Autoloader: %{symfony4_dir}/Component/PropertyAccess/autoload.php

# ------------------------------------------------------------------------------

%package property-info

Summary:   Symfony PropertyInfo Component (version 4)
License:   MIT
URL:       http://symfony.com/doc/%{symfony4_doc_ver}/components/property_info.html

# composer.json
Requires:  php-composer(%{composer_vendor}/inflector) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests:  php-composer(%{composer_vendor}/doctrine-bridge)
Suggests:  php-composer(%{composer_vendor}/serializer)
Suggests:  php-composer(psr/cache-implementation)
## NOTE: Not php-composer(phpdocumentor/reflection-docblock) to ensure
##       php-phpdocumentor-reflection-docblock2 is not chosen
Suggests:  php-phpdocumentor-reflection-docblock
Conflicts: php-composer(phpdocumentor/reflection-docblock) = 3.2.0
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/property-info) = %{version}

%description property-info
%{summary}.

Autoloader: %{symfony4_dir}/Component/PropertyInfo/autoload.php

# ------------------------------------------------------------------------------

%package routing

Summary:  Symfony Routing Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/routing.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/dependency-injection)
Suggests: php-composer(%{composer_vendor}/expression-language)
Suggests: php-composer(%{composer_vendor}/http-foundation)
Suggests: php-composer(%{composer_vendor}/yaml)
Suggests: php-composer(doctrine/annotations)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-reflection
Requires: php-spl
Requires: php-tokenizer

# Composer
Provides: php-composer(%{composer_vendor}/routing) = %{version}

%description routing
The Routing Component maps an HTTP request to a set of configuration variables.

Autoloader: %{symfony4_dir}/Component/Routing/autoload.php

# ------------------------------------------------------------------------------

%package security

Summary:  Symfony Security Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/security.html

# composer.json
Requires: php-composer(%{composer_vendor}/event-dispatcher) = %{version}
Requires: php-composer(%{composer_vendor}/http-foundation) = %{version}
Requires: php-composer(%{composer_vendor}/http-kernel) = %{version}
Requires: php-composer(%{composer_vendor}/property-access) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/expression-language)
Suggests: php-composer(%{composer_vendor}/form)
Suggests: php-composer(%{composer_vendor}/ldap)
Suggests: php-composer(%{composer_vendor}/routing)
Suggests: php-composer(%{composer_vendor}/validator)
Suggests: php-composer(psr/container)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-date
Requires: php-hash
Requires: php-json
Requires: php-pcre
Requires: php-reflection
Requires: php-session
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/security) = %{version}
Provides: php-composer(%{composer_vendor}/security-core) = %{version}
Provides: php-composer(%{composer_vendor}/security-csrf) = %{version}
Provides: php-composer(%{composer_vendor}/security-guard) = %{version}
Provides: php-composer(%{composer_vendor}/security-http) = %{version}
# Composer sub-packages
Provides: %{name}-security-core = %{version}-%{release}
Provides: %{name}-security-csrf = %{version}-%{release}
Provides: %{name}-security-guard = %{version}-%{release}
Provides: %{name}-security-http = %{version}-%{release}

%description security
The Security Component provides a complete security system for your web
application. It ships with facilities for authenticating using HTTP basic
or digest authentication, interactive form login or X.509 certificate login,
but also allows you to implement your own authentication strategies.
Furthermore, the component provides ways to authorize authenticated users
based on their roles, and it contains an advanced ACL system.

Autoloader: %{symfony4_dir}/Component/Security/autoload.php

# ------------------------------------------------------------------------------

%package serializer

Summary:  Symfony Serializer Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/serializer.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/http-foundation)
Suggests: php-composer(%{composer_vendor}/property-access)
Suggests: php-composer(%{composer_vendor}/property-info)
Suggests: php-composer(%{composer_vendor}/yaml)
Suggests: php-composer(doctrine/annotations)
Suggests: php-composer(doctrine/cache)
Suggests: php-composer(psr/cache-implementation)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-date
Requires: php-dom
Requires: php-filter
Requires: php-json
Requires: php-libxml
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/serializer) = %{version}

%description serializer
The Serializer Component is meant to be used to turn objects into a specific
format (XML, JSON, Yaml, ...) and the other way around.

Autoloader: %{symfony4_dir}/Component/Serializer/autoload.php

# ------------------------------------------------------------------------------

%package stopwatch

Summary:  Symfony Stopwatch Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/stopwatch.html

Requires: %{name}-common = %{version}-%{release}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/stopwatch) = %{version}

%description stopwatch
Stopwatch component provides a way to profile code.

Autoloader: %{symfony4_dir}/Component/Stopwatch/autoload.php

# ------------------------------------------------------------------------------

%package templating

Summary:  Symfony Templating Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/templating.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(psr/log)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-hash
Requires: php-iconv
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/templating) = %{version}

%description templating
Templating provides all the tools needed to build any kind of template system.

It provides an infrastructure to load template files and optionally monitor
them for changes. It also provides a concrete template engine implementation
using PHP with additional tools for escaping and separating templates into
blocks and layouts.

Autoloader: %{symfony4_dir}/Component/Templating/autoload.php

# ------------------------------------------------------------------------------

%package translation

Summary:  Symfony Translation Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/translation.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/yaml)
Suggests: php-composer(psr/log)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-dom
Requires: php-hash
Requires: php-intl
Requires: php-json
Requires: php-libxml
Requires: php-mbstring
Requires: php-pcre
Requires: php-simplexml
Requires: php-spl
Requires: php-tokenizer

# Composer
Provides: php-composer(%{composer_vendor}/translation) = %{version}

%description translation
Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

Autoloader: %{symfony4_dir}/Component/Translation/autoload.php

# ------------------------------------------------------------------------------

%package validator

Summary:  Symfony Validator Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/validator.html

# composer.json
Requires: php-composer(%{composer_vendor}/translation) = %{version}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/config)
Suggests: php-composer(%{composer_vendor}/expression-language)
Suggests: php-composer(%{composer_vendor}/http-foundation)
Suggests: php-composer(%{composer_vendor}/intl)
Suggests: php-composer(%{composer_vendor}/property-access)
Suggests: php-composer(%{composer_vendor}/yaml)
Suggests: php-composer(doctrine/annotations)
Suggests: php-composer(doctrine/cache)
Suggests: php-composer(egulias/email-validator)
Suggests: php-composer(psr/cache-implementation)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-ctype
Requires: php-date
Requires: php-filter
Requires: php-gd
Requires: php-intl
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/validator) = %{version}

%description validator
This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

Autoloader: %{symfony4_dir}/Component/Validator/autoload.php

# ------------------------------------------------------------------------------

%package var-dumper

Summary:  Symfony mechanism for exploring and dumping PHP variables (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/var_dumper.html

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(%{composer_vendor}/polyfill-php72) <  %{symfony_polyfill_max_ver}
Requires: php-composer(%{composer_vendor}/polyfill-php72) >= %{symfony_polyfill_min_ver}
# composer.json: optional
## ext-symfony_debug
# phpcompatinfo for version 4.0.0-beta1
Requires: php-curl
Requires: php-date
Requires: php-dom
Requires: php-gd
Requires: php-iconv
Requires: php-json
Requires: php-mbstring
Requires: php-pcre
Requires: php-posix
Requires: php-reflection
Requires: php-spl
Requires: php-xml
%if 0%{?fedora}
Suggests: php-mysql
Suggests: php-pecl(amqp)
Suggests: php-pgsql
%endif

# Composer
Provides: php-composer(%{composer_vendor}/var-dumper) = %{version}

%description var-dumper
This component provides a mechanism that allows exploring then dumping any PHP
variable.

It handles scalars, objects and resources properly, taking hard and soft
references into account. More than being immune to infinite recursion problems,
it allows dumping where references link to each other. It explores recursive
structures using a breadth-first algorithm.

The component exposes all the parts involved in the different steps of cloning
then dumping a PHP variable, while applying size limits and having specialized
output formats and methods.

Autoloader: %{symfony4_dir}/Component/VarDumper/autoload.php

# ------------------------------------------------------------------------------

%package web-link

Summary:  Symfony WebLink Component (version 4)
License:  MIT

Requires: %{name}-common = %{version}-%{release}
# composer.json
Requires: php-composer(fig/link-util) <  %{fig_link_util_max_ver}
Requires: php-composer(fig/link-util) >= %{fig_link_util_min_ver}
Requires: php-composer(psr/link) <  %{psr_link_max_ver}
Requires: php-composer(psr/link) >= %{psr_link_min_ver}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/http-kernel)
%endif
# phpcompatinfo for version 4.0.0-beta1
#     <none>

# Composer
Provides: php-composer(%{composer_vendor}/web-link) = %{version}

%description web-link
%{summary}.

Autoloader: %{symfony4_dir}/Component/WebLink/autoload.php

# ------------------------------------------------------------------------------

%package workflow

Summary:  Symfony Workflow Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/workflow.html

# composer.json
Requires: php-composer(%{composer_vendor}/property-access) = %{version}
# phpcompatinfo for version 4.0.0-beta1
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/workflow) = %{version}

%description workflow
The Workflow component provides tools for managing a workflow or finite state
machine.

Autoloader: %{symfony4_dir}/Component/Workflow/autoload.php

# ------------------------------------------------------------------------------

%package yaml

Summary:  Symfony Yaml Component (version 4)
License:  MIT
URL:      http://symfony.com/doc/%{symfony4_doc_ver}/components/yaml.html

Requires: %{name}-common = %{version}-%{release}
# composer.json: optional
%if 0%{?fedora}
Suggests: php-composer(%{composer_vendor}/console)
%endif
# phpcompatinfo for version 4.0.0-beta1
Requires: php-json
Requires: php-pcre
Requires: php-spl

# Composer
Provides: php-composer(%{composer_vendor}/yaml) = %{version}

%description yaml
The YAML Component loads and dumps YAML files.

Autoloader: %{symfony4_dir}/Component/Yaml/autoload.php

# ##############################################################################


%prep
%setup -qn %{github_name}-%{github_commit}

cp %{SOURCE1} .
sed 's#__PHPDIR__#%{phpdir}#' -i $(basename %{SOURCE1})

: Remove unnecessary files
find src -name '.git*' -delete


%build
: Create common autoloader
cat <<'AUTOLOAD' | tee src/Symfony/autoload-common.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

if (!defined('FEDORA_SYMFONY4_PHP_DIR')) {
    define('FEDORA_SYMFONY4_PHP_DIR', '%{phpdir}');
}

if (!defined('FEDORA_SYMFONY4_DIR')) {
    define('FEDORA_SYMFONY4_DIR', __DIR__);
}

\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bridge\\', FEDORA_SYMFONY4_DIR.'/Bridge', true);
\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Bundle\\', FEDORA_SYMFONY4_DIR.'/Bundle', true);
\Fedora\Autoloader\Autoload::addPsr4('Symfony\\Component\\', FEDORA_SYMFONY4_DIR.'/Component', true);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Composer/autoload.php',
]);
AUTOLOAD

: Create individual sub-package autoloaders
for AUTOLOADER in $(./%{name}-generate-autoloaders.php)
do
    sed \
        -e 's#__VERSION__#%{version}#' \
        -e 's#__RELEASE__#%{release}#' \
        -e 's#__PHPDIR__#%{phpdir}#' \
        -i $AUTOLOADER
    echo ">>>>>>>>>>>>>>>>>>>> Autoloader: $AUTOLOADER"
    cat $AUTOLOADER
done

: Create whole framework autoloader
cat <<AUTOLOAD | tee src/Symfony/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once __DIR__.'/autoload-common.php';

\Fedora\Autoloader\Dependencies::required(glob('*/*/autoload.php'));
AUTOLOAD

: Create per-type autoloaders
for TYPE in Bridge Bundle Component
do
    cat <<AUTOLOAD | tee src/Symfony/${TYPE}/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once dirname(__DIR__).'/autoload-common.php';

\Fedora\Autoloader\Dependencies::required(glob('*/autoload.php'));
AUTOLOAD
done

: Create dummy Composer autoloader for tests
%if %{with_tests}
pushd src/Symfony
cat <<COMPOSER_JSON | tee composer.json
{
    "autoload": {
        "files": [
            "autoload.php"
        ]
    }
}
COMPOSER_JSON
composer dumpautoload
rm -f composer.json
ln -s ../autoload.php vendor/composer/autoload.php
popd
%endif


%install
mkdir -p %{buildroot}%{symfony4_dir}
cp -rp src/Symfony/* %{buildroot}%{symfony4_dir}/

# Symlink main package docs to common sub-package docs
mkdir -p %{buildroot}%{_docdir}
%if 0%{?fedora} >= 20
ln -s %{name}-common %{buildroot}%{_docdir}/%{name}
%else
ln -s %{name}-common-%{version} %{buildroot}%{_docdir}/%{name}-%{version}
%endif


%check
%if %{with_tests}
: Ensure TZ is set
cp -pf %{_sysconfdir}/php.ini .
echo "date.timezone=UTC" >> php.ini
export PHPRC=$PWD/php.ini

: Set up PSR-0 path for PHPUnit
mkdir psr0
ln -s %{buildroot}%{symfony4_dir} psr0/Symfony
PSR0=$(pwd)/psr0/Symfony

: Modify PHPUnit config
sed -e 's#vendor/autoload\.php#bootstrap.php#' \
    -e 's#\./src/Symfony/#%{buildroot}%{symfony4_dir}/#' \
    phpunit.xml.dist > phpunit.xml

: Skip Intl JSON tests
rm -rf %{buildroot}%{symfony4_dir}/Component/Intl/Tests/Data/Provider/Json

: Run tests
RET=0
for PKG in %{buildroot}%{symfony4_dir}/*/*; do
%if 0%{?rhel} == 6
    if [ "$(basename $PKG)" = "DomCrawler" ]; then
        : Skip as libxml is too old
        continue
    fi
%endif

    if [ "$(basename $PKG)" = "PhpUnit" ]; then
        continue
    elif [ "$(basename $PKG)" = "composer" ]; then
        continue
    elif [ -d $PKG ]; then
        echo -e "\n>>>>>>>>>>>>>>>>>>>> ${PKG}\n"

        : Create tests bootstrap
        cat << BOOTSTRAP | tee bootstrap.php
<?php
require_once '${PKG}/autoload-dev.php';
require_once '%{buildroot}%{symfony4_dir}/Bridge/PhpUnit/bootstrap.php';
require_once '%{buildroot}%{symfony4_dir}/vendor/autoload.php';
BOOTSTRAP

        %{_bindir}/php -d include_path=.:${PSR0}:%{buildroot}%{phpdir}:%{phpdir} \
            %{_bindir}/phpunit --exclude-group benchmark $PKG || RET=1
    fi
done
: Ignore test suite results
%else
: Tests skipped
%endif


%{!?_licensedir:%global license %%doc}

%files
%if 0%{?fedora} >= 20
%doc %{_docdir}/%{name}
%else
%doc %{_docdir}/%{name}-%{version}
%endif
%{symfony4_dir}/Bundle/FullStack.php


# ##############################################################################

%files common

%doc *.md composer.json
%license LICENSE

%dir %{symfony4_dir}
     %{symfony4_dir}/autoload.php
     %{symfony4_dir}/autoload-common.php
%dir %{symfony4_dir}/Bridge
     %{symfony4_dir}/Bridge/autoload.php
%dir %{symfony4_dir}/Bundle
     %{symfony4_dir}/Bundle/autoload.php
%dir %{symfony4_dir}/Component
     %{symfony4_dir}/Component/autoload.php
%exclude %{symfony4_dir}/vendor

# ------------------------------------------------------------------------------

%files doctrine-bridge

%license src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/*.md
%doc src/Symfony/Bridge/Doctrine/composer.json

%{symfony4_dir}/Bridge/Doctrine
%exclude %{symfony4_dir}/Bridge/Doctrine/LICENSE
%exclude %{symfony4_dir}/Bridge/Doctrine/*.md
%exclude %{symfony4_dir}/Bridge/Doctrine/autoload-dev.php
%exclude %{symfony4_dir}/Bridge/Doctrine/composer.json
%exclude %{symfony4_dir}/Bridge/Doctrine/phpunit.*
%exclude %{symfony4_dir}/Bridge/Doctrine/Tests

# ------------------------------------------------------------------------------

%files monolog-bridge

%license src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/*.md
%doc src/Symfony/Bridge/Monolog/composer.json

%{symfony4_dir}/Bridge/Monolog
%exclude %{symfony4_dir}/Bridge/Monolog/LICENSE
%exclude %{symfony4_dir}/Bridge/Monolog/*.md
%exclude %{symfony4_dir}/Bridge/Monolog/autoload-dev.php
%exclude %{symfony4_dir}/Bridge/Monolog/composer.json
%exclude %{symfony4_dir}/Bridge/Monolog/phpunit.*
%exclude %{symfony4_dir}/Bridge/Monolog/Tests

# ------------------------------------------------------------------------------

%files phpunit-bridge

%license src/Symfony/Bridge/PhpUnit/LICENSE
%doc src/Symfony/Bridge/PhpUnit/*.md
%doc src/Symfony/Bridge/PhpUnit/composer.json

%{symfony4_dir}/Bridge/PhpUnit
%exclude %{symfony4_dir}/Bridge/PhpUnit/LICENSE
%exclude %{symfony4_dir}/Bridge/PhpUnit/*.md
%exclude %{symfony4_dir}/Bridge/PhpUnit/autoload-dev.php
%exclude %{symfony4_dir}/Bridge/PhpUnit/composer.json
%exclude %{symfony4_dir}/Bridge/PhpUnit/phpunit.*

# ------------------------------------------------------------------------------

%files proxy-manager-bridge

%license src/Symfony/Bridge/ProxyManager/LICENSE
%doc src/Symfony/Bridge/ProxyManager/*.md
%doc src/Symfony/Bridge/ProxyManager/composer.json

%{symfony4_dir}/Bridge/ProxyManager
%exclude %{symfony4_dir}/Bridge/ProxyManager/LICENSE
%exclude %{symfony4_dir}/Bridge/ProxyManager/*.md
%exclude %{symfony4_dir}/Bridge/ProxyManager/autoload-dev.php
%exclude %{symfony4_dir}/Bridge/ProxyManager/composer.json
%exclude %{symfony4_dir}/Bridge/ProxyManager/phpunit.*
%exclude %{symfony4_dir}/Bridge/ProxyManager/Tests

# ------------------------------------------------------------------------------

%files twig-bridge

%license src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/*.md
%doc src/Symfony/Bridge/Twig/composer.json

%{symfony4_dir}/Bridge/Twig
%exclude %{symfony4_dir}/Bridge/Twig/LICENSE
%exclude %{symfony4_dir}/Bridge/Twig/*.md
%exclude %{symfony4_dir}/Bridge/Twig/autoload-dev.php
%exclude %{symfony4_dir}/Bridge/Twig/composer.json
%exclude %{symfony4_dir}/Bridge/Twig/phpunit.*
%exclude %{symfony4_dir}/Bridge/Twig/Tests

# ------------------------------------------------------------------------------

%files debug-bundle

#%%doc src/Symfony/Bundle/DebugBundle/*.md
%doc src/Symfony/Bundle/DebugBundle/composer.json
%license src/Symfony/Bundle/DebugBundle/LICENSE

%{symfony4_dir}/Bundle/DebugBundle
#%%exclude %%{symfony4_dir}/Bundle/DebugBundle/*.md
%exclude %{symfony4_dir}/Bundle/DebugBundle/autoload-dev.php
%exclude %{symfony4_dir}/Bundle/DebugBundle/composer.json
%exclude %{symfony4_dir}/Bundle/DebugBundle/LICENSE
%exclude %{symfony4_dir}/Bundle/DebugBundle/phpunit.*
%exclude %{symfony4_dir}/Bundle/DebugBundle/Tests

# ------------------------------------------------------------------------------

%files framework-bundle

%doc src/Symfony/Bundle/FrameworkBundle/*.md
%doc src/Symfony/Bundle/FrameworkBundle/composer.json
%license src/Symfony/Bundle/FrameworkBundle/LICENSE

%{symfony4_dir}/Bundle/FrameworkBundle
%exclude %{symfony4_dir}/Bundle/FrameworkBundle/*.md
%exclude %{symfony4_dir}/Bundle/FrameworkBundle/autoload-dev.php
%exclude %{symfony4_dir}/Bundle/FrameworkBundle/composer.json
%exclude %{symfony4_dir}/Bundle/FrameworkBundle/LICENSE
%exclude %{symfony4_dir}/Bundle/FrameworkBundle/phpunit.*
%exclude %{symfony4_dir}/Bundle/FrameworkBundle/Tests

# ------------------------------------------------------------------------------

%files security-bundle

%doc src/Symfony/Bundle/SecurityBundle/*.md
%doc src/Symfony/Bundle/SecurityBundle/composer.json
%license src/Symfony/Bundle/SecurityBundle/LICENSE

%{symfony4_dir}/Bundle/SecurityBundle
%exclude %{symfony4_dir}/Bundle/SecurityBundle/*.md
%exclude %{symfony4_dir}/Bundle/SecurityBundle/autoload-dev.php
%exclude %{symfony4_dir}/Bundle/SecurityBundle/composer.json
%exclude %{symfony4_dir}/Bundle/SecurityBundle/LICENSE
%exclude %{symfony4_dir}/Bundle/SecurityBundle/phpunit.*
%exclude %{symfony4_dir}/Bundle/SecurityBundle/Tests

# ------------------------------------------------------------------------------

%files twig-bundle

%doc src/Symfony/Bundle/TwigBundle/*.md
%doc src/Symfony/Bundle/TwigBundle/composer.json
%license src/Symfony/Bundle/TwigBundle/LICENSE

%{symfony4_dir}/Bundle/TwigBundle
%exclude %{symfony4_dir}/Bundle/TwigBundle/*.md
%exclude %{symfony4_dir}/Bundle/TwigBundle/autoload-dev.php
%exclude %{symfony4_dir}/Bundle/TwigBundle/composer.json
%exclude %{symfony4_dir}/Bundle/TwigBundle/LICENSE
%exclude %{symfony4_dir}/Bundle/TwigBundle/phpunit.*
%exclude %{symfony4_dir}/Bundle/TwigBundle/Tests

# ------------------------------------------------------------------------------

%files web-profiler-bundle

%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%doc src/Symfony/Bundle/WebProfilerBundle/composer.json
%license src/Symfony/Bundle/WebProfilerBundle/LICENSE
%license src/Symfony/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt

%{symfony4_dir}/Bundle/WebProfilerBundle
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/*.md
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/autoload-dev.php
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/composer.json
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/LICENSE
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/phpunit.*
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/Resources/ICONS_LICENSE.txt
%exclude %{symfony4_dir}/Bundle/WebProfilerBundle/Tests

# ------------------------------------------------------------------------------

%files web-server-bundle

%doc src/Symfony/Bundle/WebServerBundle/*.md
%doc src/Symfony/Bundle/WebServerBundle/composer.json
%license src/Symfony/Bundle/WebServerBundle/LICENSE

%{symfony4_dir}/Bundle/WebServerBundle
%exclude %{symfony4_dir}/Bundle/WebServerBundle/*.md
%exclude %{symfony4_dir}/Bundle/WebServerBundle/autoload-dev.php
%exclude %{symfony4_dir}/Bundle/WebServerBundle/composer.json
%exclude %{symfony4_dir}/Bundle/WebServerBundle/LICENSE
%exclude %{symfony4_dir}/Bundle/WebServerBundle/phpunit.*
#%%exclude %%{symfony4_dir}/Bundle/WebServerBundle/Tests

# ------------------------------------------------------------------------------

%files asset

%license src/Symfony/Component/Asset/LICENSE
%doc src/Symfony/Component/Asset/*.md
%doc src/Symfony/Component/Asset/composer.json

%{symfony4_dir}/Component/Asset
%exclude %{symfony4_dir}/Component/Asset/LICENSE
%exclude %{symfony4_dir}/Component/Asset/*.md
%exclude %{symfony4_dir}/Component/Asset/autoload-dev.php
%exclude %{symfony4_dir}/Component/Asset/composer.json
%exclude %{symfony4_dir}/Component/Asset/phpunit.*
%exclude %{symfony4_dir}/Component/Asset/Tests

# ------------------------------------------------------------------------------

%files browser-kit

%license src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/*.md
%doc src/Symfony/Component/BrowserKit/composer.json

%{symfony4_dir}/Component/BrowserKit
%exclude %{symfony4_dir}/Component/BrowserKit/LICENSE
%exclude %{symfony4_dir}/Component/BrowserKit/*.md
%exclude %{symfony4_dir}/Component/BrowserKit/autoload-dev.php
%exclude %{symfony4_dir}/Component/BrowserKit/composer.json
%exclude %{symfony4_dir}/Component/BrowserKit/phpunit.*
%exclude %{symfony4_dir}/Component/BrowserKit/Tests

# ------------------------------------------------------------------------------

%files cache

%license src/Symfony/Component/Cache/LICENSE
%doc src/Symfony/Component/Cache/*.md
%doc src/Symfony/Component/Cache/composer.json

%{symfony4_dir}/Component/Cache
%exclude %{symfony4_dir}/Component/Cache/LICENSE
%exclude %{symfony4_dir}/Component/Cache/*.md
%exclude %{symfony4_dir}/Component/Cache/autoload-dev.php
%exclude %{symfony4_dir}/Component/Cache/composer.json
%exclude %{symfony4_dir}/Component/Cache/phpunit.*
%exclude %{symfony4_dir}/Component/Cache/Tests

# ------------------------------------------------------------------------------

%files config

%license src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/*.md
%doc src/Symfony/Component/Config/composer.json

%{symfony4_dir}/Component/Config
%exclude %{symfony4_dir}/Component/Config/LICENSE
%exclude %{symfony4_dir}/Component/Config/*.md
%exclude %{symfony4_dir}/Component/Config/autoload-dev.php
%exclude %{symfony4_dir}/Component/Config/composer.json
%exclude %{symfony4_dir}/Component/Config/phpunit.*
%exclude %{symfony4_dir}/Component/Config/Tests

# ------------------------------------------------------------------------------

%files console

%license src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/*.md
%doc src/Symfony/Component/Console/composer.json

%{symfony4_dir}/Component/Console
%exclude %{symfony4_dir}/Component/Console/LICENSE
%exclude %{symfony4_dir}/Component/Console/*.md
%exclude %{symfony4_dir}/Component/Console/autoload-dev.php
%exclude %{symfony4_dir}/Component/Console/composer.json
%exclude %{symfony4_dir}/Component/Console/phpunit.*
%exclude %{symfony4_dir}/Component/Console/Tests

# ------------------------------------------------------------------------------

%files css-selector

%license src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/*.md
%doc src/Symfony/Component/CssSelector/composer.json

%{symfony4_dir}/Component/CssSelector
%exclude %{symfony4_dir}/Component/CssSelector/LICENSE
%exclude %{symfony4_dir}/Component/CssSelector/*.md
%exclude %{symfony4_dir}/Component/CssSelector/autoload-dev.php
%exclude %{symfony4_dir}/Component/CssSelector/composer.json
%exclude %{symfony4_dir}/Component/CssSelector/phpunit.*
%exclude %{symfony4_dir}/Component/CssSelector/Tests

# ------------------------------------------------------------------------------

%files debug

%license src/Symfony/Component/Debug/LICENSE
%doc src/Symfony/Component/Debug/*.md
%doc src/Symfony/Component/Debug/composer.json

%{symfony4_dir}/Component/Debug
%exclude %{symfony4_dir}/Component/Debug/LICENSE
%exclude %{symfony4_dir}/Component/Debug/*.md
%exclude %{symfony4_dir}/Component/Debug/autoload-dev.php
%exclude %{symfony4_dir}/Component/Debug/composer.json
%exclude %{symfony4_dir}/Component/Debug/phpunit.*
%exclude %{symfony4_dir}/Component/Debug/Tests
%exclude %{symfony4_dir}/Component/Debug/Resources/ext

# ------------------------------------------------------------------------------

%files dependency-injection

%license src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/*.md
%doc src/Symfony/Component/DependencyInjection/composer.json

%{symfony4_dir}/Component/DependencyInjection
%exclude %{symfony4_dir}/Component/DependencyInjection/LICENSE
%exclude %{symfony4_dir}/Component/DependencyInjection/*.md
%exclude %{symfony4_dir}/Component/DependencyInjection/autoload-dev.php
%exclude %{symfony4_dir}/Component/DependencyInjection/composer.json
%exclude %{symfony4_dir}/Component/DependencyInjection/phpunit.*
%exclude %{symfony4_dir}/Component/DependencyInjection/Tests

# ------------------------------------------------------------------------------

%files dotenv

%license src/Symfony/Component/Dotenv/LICENSE
%doc src/Symfony/Component/Dotenv/*.md
%doc src/Symfony/Component/Dotenv/composer.json

%{symfony4_dir}/Component/Dotenv
%exclude %{symfony4_dir}/Component/Dotenv/LICENSE
%exclude %{symfony4_dir}/Component/Dotenv/*.md
%exclude %{symfony4_dir}/Component/Dotenv/autoload-dev.php
%exclude %{symfony4_dir}/Component/Dotenv/composer.json
%exclude %{symfony4_dir}/Component/Dotenv/phpunit.*
%exclude %{symfony4_dir}/Component/Dotenv/Tests

# ------------------------------------------------------------------------------

%files dom-crawler

%license src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/*.md
%doc src/Symfony/Component/DomCrawler/composer.json

%{symfony4_dir}/Component/DomCrawler
%exclude %{symfony4_dir}/Component/DomCrawler/LICENSE
%exclude %{symfony4_dir}/Component/DomCrawler/*.md
%exclude %{symfony4_dir}/Component/DomCrawler/autoload-dev.php
%exclude %{symfony4_dir}/Component/DomCrawler/composer.json
%exclude %{symfony4_dir}/Component/DomCrawler/phpunit.*
%exclude %{symfony4_dir}/Component/DomCrawler/Tests

# ------------------------------------------------------------------------------

%files event-dispatcher

%license src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/*.md
%doc src/Symfony/Component/EventDispatcher/composer.json

%{symfony4_dir}/Component/EventDispatcher
%exclude %{symfony4_dir}/Component/EventDispatcher/LICENSE
%exclude %{symfony4_dir}/Component/EventDispatcher/*.md
%exclude %{symfony4_dir}/Component/EventDispatcher/autoload-dev.php
%exclude %{symfony4_dir}/Component/EventDispatcher/composer.json
%exclude %{symfony4_dir}/Component/EventDispatcher/phpunit.*
%exclude %{symfony4_dir}/Component/EventDispatcher/Tests

# ------------------------------------------------------------------------------

%files expression-language

%license src/Symfony/Component/ExpressionLanguage/LICENSE
%doc src/Symfony/Component/ExpressionLanguage/*.md
%doc src/Symfony/Component/ExpressionLanguage/composer.json

%{symfony4_dir}/Component/ExpressionLanguage
%exclude %{symfony4_dir}/Component/ExpressionLanguage/LICENSE
%exclude %{symfony4_dir}/Component/ExpressionLanguage/*.md
%exclude %{symfony4_dir}/Component/ExpressionLanguage/autoload-dev.php
%exclude %{symfony4_dir}/Component/ExpressionLanguage/composer.json
%exclude %{symfony4_dir}/Component/ExpressionLanguage/phpunit.*
%exclude %{symfony4_dir}/Component/ExpressionLanguage/Tests

# ------------------------------------------------------------------------------

%files filesystem

%license src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/*.md
%doc src/Symfony/Component/Filesystem/composer.json

%{symfony4_dir}/Component/Filesystem
%exclude %{symfony4_dir}/Component/Filesystem/LICENSE
%exclude %{symfony4_dir}/Component/Filesystem/*.md
%exclude %{symfony4_dir}/Component/Filesystem/autoload-dev.php
%exclude %{symfony4_dir}/Component/Filesystem/composer.json
%exclude %{symfony4_dir}/Component/Filesystem/phpunit.*
%exclude %{symfony4_dir}/Component/Filesystem/Tests

# ------------------------------------------------------------------------------

%files finder

%license src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/*.md
%doc src/Symfony/Component/Finder/composer.json

%{symfony4_dir}/Component/Finder
%exclude %{symfony4_dir}/Component/Finder/LICENSE
%exclude %{symfony4_dir}/Component/Finder/*.md
%exclude %{symfony4_dir}/Component/Finder/autoload-dev.php
%exclude %{symfony4_dir}/Component/Finder/composer.json
%exclude %{symfony4_dir}/Component/Finder/phpunit.*
%exclude %{symfony4_dir}/Component/Finder/Tests

# ------------------------------------------------------------------------------

%files form

%license src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/*.md
%doc src/Symfony/Component/Form/composer.json

%{symfony4_dir}/Component/Form
%exclude %{symfony4_dir}/Component/Form/LICENSE
%exclude %{symfony4_dir}/Component/Form/*.md
%exclude %{symfony4_dir}/Component/Form/autoload-dev.php
%exclude %{symfony4_dir}/Component/Form/composer.json
%exclude %{symfony4_dir}/Component/Form/phpunit.*
%exclude %{symfony4_dir}/Component/Form/Tests

# ------------------------------------------------------------------------------

%files http-foundation

%license src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/*.md
%doc src/Symfony/Component/HttpFoundation/composer.json

%{symfony4_dir}/Component/HttpFoundation
%exclude %{symfony4_dir}/Component/HttpFoundation/LICENSE
%exclude %{symfony4_dir}/Component/HttpFoundation/*.md
%exclude %{symfony4_dir}/Component/HttpFoundation/autoload-dev.php
%exclude %{symfony4_dir}/Component/HttpFoundation/composer.json
%exclude %{symfony4_dir}/Component/HttpFoundation/phpunit.*
%exclude %{symfony4_dir}/Component/HttpFoundation/Tests

# ------------------------------------------------------------------------------

%files http-kernel

%license src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/*.md
%doc src/Symfony/Component/HttpKernel/composer.json

%{symfony4_dir}/Component/HttpKernel
%exclude %{symfony4_dir}/Component/HttpKernel/LICENSE
%exclude %{symfony4_dir}/Component/HttpKernel/*.md
%exclude %{symfony4_dir}/Component/HttpKernel/autoload-dev.php
%exclude %{symfony4_dir}/Component/HttpKernel/composer.json
%exclude %{symfony4_dir}/Component/HttpKernel/phpunit.*
%exclude %{symfony4_dir}/Component/HttpKernel/Tests

# ------------------------------------------------------------------------------

%files inflector

%license src/Symfony/Component/Inflector/LICENSE
%doc src/Symfony/Component/Inflector/*.md
%doc src/Symfony/Component/Inflector/composer.json

%{symfony4_dir}/Component/Inflector
%exclude %{symfony4_dir}/Component/Inflector/LICENSE
%exclude %{symfony4_dir}/Component/Inflector/*.md
%exclude %{symfony4_dir}/Component/Inflector/autoload-dev.php
%exclude %{symfony4_dir}/Component/Inflector/composer.json
%exclude %{symfony4_dir}/Component/Inflector/phpunit.*
%exclude %{symfony4_dir}/Component/Inflector/Tests

# ------------------------------------------------------------------------------

%files intl

%license src/Symfony/Component/Intl/LICENSE
%doc src/Symfony/Component/Intl/*.md
%doc src/Symfony/Component/Intl/composer.json

%{symfony4_dir}/Component/Intl
%exclude %{symfony4_dir}/Component/Intl/LICENSE
%exclude %{symfony4_dir}/Component/Intl/*.md
%exclude %{symfony4_dir}/Component/Intl/autoload-dev.php
%exclude %{symfony4_dir}/Component/Intl/composer.json
%exclude %{symfony4_dir}/Component/Intl/phpunit.*
%exclude %{symfony4_dir}/Component/Intl/Tests

# ------------------------------------------------------------------------------

%files ldap

%license src/Symfony/Component/Ldap/LICENSE
%doc src/Symfony/Component/Ldap/*.md
%doc src/Symfony/Component/Ldap/composer.json

%{symfony4_dir}/Component/Ldap
%exclude %{symfony4_dir}/Component/Ldap/LICENSE
%exclude %{symfony4_dir}/Component/Ldap/*.md
%exclude %{symfony4_dir}/Component/Ldap/autoload-dev.php
%exclude %{symfony4_dir}/Component/Ldap/composer.json
%exclude %{symfony4_dir}/Component/Ldap/phpunit.*
%exclude %{symfony4_dir}/Component/Ldap/Tests

# ------------------------------------------------------------------------------

%files lock

%license src/Symfony/Component/Lock/LICENSE
%doc src/Symfony/Component/Lock/*.md
%doc src/Symfony/Component/Lock/composer.json

%{symfony4_dir}/Component/Lock
%exclude %{symfony4_dir}/Component/Lock/LICENSE
%exclude %{symfony4_dir}/Component/Lock/*.md
%exclude %{symfony4_dir}/Component/Lock/autoload-dev.php
%exclude %{symfony4_dir}/Component/Lock/composer.json
%exclude %{symfony4_dir}/Component/Lock/phpunit.*
%exclude %{symfony4_dir}/Component/Lock/Tests

# ------------------------------------------------------------------------------

%files options-resolver

%license src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/*.md
%doc src/Symfony/Component/OptionsResolver/composer.json

%{symfony4_dir}/Component/OptionsResolver
%exclude %{symfony4_dir}/Component/OptionsResolver/LICENSE
%exclude %{symfony4_dir}/Component/OptionsResolver/*.md
%exclude %{symfony4_dir}/Component/OptionsResolver/autoload-dev.php
%exclude %{symfony4_dir}/Component/OptionsResolver/composer.json
%exclude %{symfony4_dir}/Component/OptionsResolver/phpunit.*
%exclude %{symfony4_dir}/Component/OptionsResolver/Tests

# ------------------------------------------------------------------------------

%files process

%license src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/*.md
%doc src/Symfony/Component/Process/composer.json

%{symfony4_dir}/Component/Process
%exclude %{symfony4_dir}/Component/Process/LICENSE
%exclude %{symfony4_dir}/Component/Process/*.md
%exclude %{symfony4_dir}/Component/Process/autoload-dev.php
%exclude %{symfony4_dir}/Component/Process/composer.json
%exclude %{symfony4_dir}/Component/Process/phpunit.*
%exclude %{symfony4_dir}/Component/Process/Tests

# ------------------------------------------------------------------------------

%files property-access

%license src/Symfony/Component/PropertyAccess/LICENSE
%doc src/Symfony/Component/PropertyAccess/*.md
%doc src/Symfony/Component/PropertyAccess/composer.json

%{symfony4_dir}/Component/PropertyAccess
%exclude %{symfony4_dir}/Component/PropertyAccess/LICENSE
%exclude %{symfony4_dir}/Component/PropertyAccess/*.md
%exclude %{symfony4_dir}/Component/PropertyAccess/autoload-dev.php
%exclude %{symfony4_dir}/Component/PropertyAccess/composer.json
%exclude %{symfony4_dir}/Component/PropertyAccess/phpunit.*
%exclude %{symfony4_dir}/Component/PropertyAccess/Tests

# ------------------------------------------------------------------------------

%files property-info

%license src/Symfony/Component/PropertyInfo/LICENSE
%doc src/Symfony/Component/PropertyInfo/*.md
%doc src/Symfony/Component/PropertyInfo/composer.json

%{symfony4_dir}/Component/PropertyInfo
%exclude %{symfony4_dir}/Component/PropertyInfo/LICENSE
%exclude %{symfony4_dir}/Component/PropertyInfo/*.md
%exclude %{symfony4_dir}/Component/PropertyInfo/autoload-dev.php
%exclude %{symfony4_dir}/Component/PropertyInfo/composer.json
%exclude %{symfony4_dir}/Component/PropertyInfo/phpunit.*
%exclude %{symfony4_dir}/Component/PropertyInfo/Tests

# ------------------------------------------------------------------------------

%files routing

%license src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/*.md
%doc src/Symfony/Component/Routing/composer.json

%{symfony4_dir}/Component/Routing
%exclude %{symfony4_dir}/Component/Routing/LICENSE
%exclude %{symfony4_dir}/Component/Routing/*.md
%exclude %{symfony4_dir}/Component/Routing/autoload-dev.php
%exclude %{symfony4_dir}/Component/Routing/composer.json
%exclude %{symfony4_dir}/Component/Routing/phpunit.*
%exclude %{symfony4_dir}/Component/Routing/Tests

# ------------------------------------------------------------------------------

%files security

%license src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/*.md
%doc src/Symfony/Component/Security/composer.json

%{symfony4_dir}/Component/Security
%exclude %{symfony4_dir}/Component/Security/LICENSE
%exclude %{symfony4_dir}/Component/Security/*.md
%exclude %{symfony4_dir}/Component/Security/autoload-dev.php
%exclude %{symfony4_dir}/Component/Security/composer.json
%exclude %{symfony4_dir}/Component/Security/phpunit.*
%exclude %{symfony4_dir}/Component/Security/*/phpunit.*
%exclude %{symfony4_dir}/Component/Security/*/Tests
%exclude %{symfony4_dir}/Component/Security/*/LICENSE
%exclude %{symfony4_dir}/Component/Security/*/*.md
%exclude %{symfony4_dir}/Component/Security/*/autoload-dev.php
%exclude %{symfony4_dir}/Component/Security/*/composer.json

# ------------------------------------------------------------------------------

%files serializer

%license src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/*.md
%doc src/Symfony/Component/Serializer/composer.json

%{symfony4_dir}/Component/Serializer
%exclude %{symfony4_dir}/Component/Serializer/LICENSE
%exclude %{symfony4_dir}/Component/Serializer/*.md
%exclude %{symfony4_dir}/Component/Serializer/autoload-dev.php
%exclude %{symfony4_dir}/Component/Serializer/composer.json
%exclude %{symfony4_dir}/Component/Serializer/phpunit.*
%exclude %{symfony4_dir}/Component/Serializer/Tests

# ------------------------------------------------------------------------------

%files stopwatch

%license src/Symfony/Component/Stopwatch/LICENSE
%doc src/Symfony/Component/Stopwatch/*.md
%doc src/Symfony/Component/Stopwatch/composer.json

%{symfony4_dir}/Component/Stopwatch
%exclude %{symfony4_dir}/Component/Stopwatch/LICENSE
%exclude %{symfony4_dir}/Component/Stopwatch/*.md
%exclude %{symfony4_dir}/Component/Stopwatch/autoload-dev.php
%exclude %{symfony4_dir}/Component/Stopwatch/composer.json
%exclude %{symfony4_dir}/Component/Stopwatch/phpunit.*
%exclude %{symfony4_dir}/Component/Stopwatch/Tests

# ------------------------------------------------------------------------------

%files templating

%license src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/*.md
%doc src/Symfony/Component/Templating/composer.json

%{symfony4_dir}/Component/Templating
%exclude %{symfony4_dir}/Component/Templating/LICENSE
%exclude %{symfony4_dir}/Component/Templating/*.md
%exclude %{symfony4_dir}/Component/Templating/autoload-dev.php
%exclude %{symfony4_dir}/Component/Templating/composer.json
%exclude %{symfony4_dir}/Component/Templating/phpunit.*
%exclude %{symfony4_dir}/Component/Templating/Tests

# ------------------------------------------------------------------------------

%files translation

%license src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/*.md
%doc src/Symfony/Component/Translation/composer.json

%{symfony4_dir}/Component/Translation
%exclude %{symfony4_dir}/Component/Translation/LICENSE
%exclude %{symfony4_dir}/Component/Translation/*.md
%exclude %{symfony4_dir}/Component/Translation/autoload-dev.php
%exclude %{symfony4_dir}/Component/Translation/composer.json
%exclude %{symfony4_dir}/Component/Translation/phpunit.*
%exclude %{symfony4_dir}/Component/Translation/Tests

# ------------------------------------------------------------------------------

%files validator

%license src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/*.md
%doc src/Symfony/Component/Validator/composer.json

%{symfony4_dir}/Component/Validator
%exclude %{symfony4_dir}/Component/Validator/LICENSE
%exclude %{symfony4_dir}/Component/Validator/*.md
%exclude %{symfony4_dir}/Component/Validator/autoload-dev.php
%exclude %{symfony4_dir}/Component/Validator/composer.json
%exclude %{symfony4_dir}/Component/Validator/phpunit.*
%exclude %{symfony4_dir}/Component/Validator/Tests

# ------------------------------------------------------------------------------

%files var-dumper

%license src/Symfony/Component/VarDumper/LICENSE
%doc src/Symfony/Component/VarDumper/*.md
%doc src/Symfony/Component/VarDumper/composer.json

%{symfony4_dir}/Component/VarDumper
%exclude %{symfony4_dir}/Component/VarDumper/LICENSE
%exclude %{symfony4_dir}/Component/VarDumper/*.md
%exclude %{symfony4_dir}/Component/VarDumper/autoload-dev.php
%exclude %{symfony4_dir}/Component/VarDumper/composer.json
%exclude %{symfony4_dir}/Component/VarDumper/phpunit.*
%exclude %{symfony4_dir}/Component/VarDumper/Tests

# ------------------------------------------------------------------------------

%files web-link

%license src/Symfony/Component/WebLink/LICENSE
%doc src/Symfony/Component/WebLink/*.md
%doc src/Symfony/Component/WebLink/composer.json

%{symfony4_dir}/Component/WebLink
%exclude %{symfony4_dir}/Component/WebLink/LICENSE
%exclude %{symfony4_dir}/Component/WebLink/*.md
%exclude %{symfony4_dir}/Component/WebLink/autoload-dev.php
%exclude %{symfony4_dir}/Component/WebLink/composer.json
%exclude %{symfony4_dir}/Component/WebLink/phpunit.*
%exclude %{symfony4_dir}/Component/WebLink/Tests

# ------------------------------------------------------------------------------

%files workflow

%license src/Symfony/Component/Workflow/LICENSE
%doc src/Symfony/Component/Workflow/*.md
%doc src/Symfony/Component/Workflow/composer.json

%{symfony4_dir}/Component/Workflow
%exclude %{symfony4_dir}/Component/Workflow/LICENSE
%exclude %{symfony4_dir}/Component/Workflow/*.md
%exclude %{symfony4_dir}/Component/Workflow/autoload-dev.php
%exclude %{symfony4_dir}/Component/Workflow/composer.json
%exclude %{symfony4_dir}/Component/Workflow/phpunit.*
%exclude %{symfony4_dir}/Component/Workflow/Tests

# ------------------------------------------------------------------------------

%files yaml

%license src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/*.md
%doc src/Symfony/Component/Yaml/composer.json

%{symfony4_dir}/Component/Yaml
%exclude %{symfony4_dir}/Component/Yaml/LICENSE
%exclude %{symfony4_dir}/Component/Yaml/*.md
%exclude %{symfony4_dir}/Component/Yaml/autoload-dev.php
%exclude %{symfony4_dir}/Component/Yaml/composer.json
%exclude %{symfony4_dir}/Component/Yaml/phpunit.*
%exclude %{symfony4_dir}/Component/Yaml/Tests

# ##############################################################################

%changelog
* Sat Oct 21 2017 Shawn Iwinski <shawn@iwin.ski> - 4.0.0-0.1.beta1
- Update to 4.0.0-beta1
- Add license override for all sub-packages except web-profiler-bundle

* Mon Oct  9 2017 Remi Collet <remi@remirepo.net> - 3.3.10-1
- Update to 3.3.10
- ignore unreliable test suite results

* Wed Sep 13 2017 Remi Collet <remi@remirepo.net> - 3.3.9-1
- Update to 3.3.9

* Tue Aug 29 2017 Remi Collet <remi@remirepo.net> - 3.3.8-1
- Update to 3.3.8
- raise dependency on phpdocumentor/reflection-docblock 3.2.2
- ignore 2 new failed tests

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 3.3.6-5
- fix missing dependency
- fix dev autoloader with patch from
  https://github.com/symfony/symfony/pull/23934

* Sat Aug 19 2017 Shawn Iwinski <shawn@iwin.ski> - 3.3.6-4
- Dynamically generate dev autoloaders
- Add build conditionals to make backporting to remirepo easier

* Fri Aug 18 2017 Shawn Iwinski <shawn@iwin.ski> - 3.3.6-3
- Fix some tests' dev requires (thanks Remi!)

* Mon Aug 14 2017 Shawn Iwinski <shawn@iwin.ski> - 3.3.6-2
- Fix dotenv sub-package Composer provide

* Sun Aug 13 2017 Shawn Iwinski <shawn@iwin.ski> - 3.3.6-1
- Update to 3.3.6 (RHBZ #1460525)
- Remove versions from suggested dependencies

* Wed Aug  2 2017 Remi Collet <remi@remirepo.net> - 3.2.13-1
- Update to 3.2.13
- add dependency on php-xml
- raise dependency on phpdocumentor/reflection-docblock 3.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.11-1
- Update to 3.2.11

* Wed Jul  5 2017 Remi Collet <remi@remirepo.net> - 3.2.10-1
- Update to 3.2.10
- raise dependency on twig 1.34

* Sun Jun 11 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.9-1
- Update to 3.2.9
- Use php-composer(cache/integration-tests)
- Use php-composer(phpdocumentor/reflection-docblock)
- Provide php-composer(symfony/phpunit-bridge)
- Provide whole framework autoloader
- Provide per-type (Bridge, Bundle, Component) autoloaders

* Mon May 15 2017 Remi Collet <remi@remirepo.net> - 3.2.8-3
- add missing dependency on common for cache

* Wed May 10 2017 Remi Collet <remi@remirepo.net> - 3.2.8-2
- add missing dependency on debug for console
- add depdencency on php-symfony-class-loader for class-loader
  to workaround issue with package without version constraint

* Sun May 07 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.8-1
- Update to 3.2.8

* Fri Mar 17 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.6-1
- Modify main package and web-profiler-bundle sub-package licenses
    from "MIT" to "MIT and CC-BY-SA"
- Remove phpunit-bridge dependency from main package
- Fix web-profiler-bundle sub-package's polyfill-php70 dependency versions
- Fix autoloader locations in descriptions

* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.6-2
- Allow Twig v1 and v2

* Fri Mar 10 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.6-1
- Update to 3.2.6

* Tue Feb 21 2017 Shawn Iwinski <shawn@iwin.ski> - 3.2.4-1
- Initial package
