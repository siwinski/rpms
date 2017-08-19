#
# Fedora spec file for phpdoc
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      phpDocumentor2
%global github_version   2.9.0
%global github_commit    be607da0eef9b9249c43c5b4820d25d631c73667

%global composer_vendor  phpdocumentor
%global composer_project phpdocumentor

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "cilex/cilex": "~1.0"
%global cilex_min_ver 1.0
%global cilex_max_ver 2.0
# "erusev/parsedown": "~1.0"
%global erusev_parsedown_min_ver 1.0
%global erusev_parsedown_max_ver 2.0
# "jms/serializer": ">=0.12"
#     NOTE: Max version added
%global jms_serializer_min_ver 0.12
%global jms_serializer_max_ver 2.0
# "mikey179/vfsStream": "~1.2"
%global mikey179_vfsstream_min_ver 1.2
%global mikey179_vfsstream_max_ver 2.0
# "mockery/mockery": "~0.9@dev"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0
# "monolog/monolog": "~1.6"
%global monolog_min_ver 1.6
%global monolog_max_ver 2.0
# "phpdocumentor/fileset": "~1.0"
%global phpdocumentor_fileset_min_ver 1.0
%global phpdocumentor_fileset_max_ver 2.0
# "phpdocumentor/graphviz": "~1.0"
%global phpdocumentor_graphviz_min_ver 1.0
%global phpdocumentor_graphviz_max_ver 2.0
# "phpdocumentor/reflection": "^3.0"
%global phpdocumentor_reflection_min_ver 3.0
%global phpdocumentor_reflection_max_ver 4.0
# "phpdocumentor/reflection-docblock": "~2.0"
%global phpdocumentor_reflection_docblock_min_ver 2.0
%global phpdocumentor_reflection_docblock_max_ver 3.0
# "symfony/config": "~2.3"
# "symfony/console": "~2.3"
# "symfony/event-dispatcher": "~2.1"
# "symfony/expression-language": "~2.4"
# "symfony/process": "~2.0"
# "symfony/stopwatch": "~2.3"
# "symfony/validator": "~2.2"
#     NOTE: Min version not 2.4 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 3.0
# "twig/twig": "~1.3"
%global twig_min_ver 1.3
%global twig_max_ver 2.0
# "zendframework/zend-cache": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_cache_min_ver 2.1
%global zendframework_cache_max_ver 4.0
# "zendframework/zend-config": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_config_min_ver 2.1
%global zendframework_config_max_ver 4.0
# "zendframework/zend-filter": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_filter_min_ver 2.1
%global zendframework_filter_max_ver 4.0
# "zendframework/zend-i18n": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_i18n_min_ver 2.1
%global zendframework_i18n_max_ver 4.0
# "zendframework/zend-serializer": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_serializer_min_ver 2.1
%global zendframework_serializer_max_ver 4.0
# "zendframework/zend-servicemanager": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_servicemanager_min_ver 2.1
%global zendframework_servicemanager_max_ver 4.0
# "zendframework/zend-stdlib": "~2.1"
#   NOTE: Max version not 3.0 because tests pass
%global zendframework_stdlib_min_ver 2.1
%global zendframework_stdlib_max_ver 4.0
# "zetacomponents/document": ">=1.3.1"
#     NOTE: Max version to restrict to one major version
%global zetacomponents_document_min_ver 1.3.1
%global zetacomponents_document_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          phpdoc
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Documentation generator for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://www.phpdoc.org

# GitHub export does not include tests.
# Run phpdoc-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

Patch0:        %{name}-adjust-vendor-dir.patch

BuildArch:     noarch
# Composer autoloader generation
Requires:      composer
# Tests
%if %{with_tests}
## composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(cilex/cilex) <  %{cilex_max_ver}
Requires:      php-composer(cilex/cilex) >= %{cilex_min_ver}
Requires:      php-composer(erusev/parsedown) <  %{erusev_parsedown_max_ver}
Requires:      php-composer(erusev/parsedown) >= %{erusev_parsedown_min_ver}
Requires:      php-composer(jms/serializer) <  %{jms_serializer_max_ver}
Requires:      php-composer(jms/serializer) >= %{jms_serializer_min_ver}
Requires:      php-composer(mikey179/vfsStream) <  %{mikey179_vfsstream_max_ver}
Requires:      php-composer(mikey179/vfsStream) >= %{mikey179_vfsstream_min_ver}
Requires:      php-composer(mockery/mockery) <  %{mockery_max_ver}
Requires:      php-composer(mockery/mockery) >= %{mockery_min_ver}
Requires:      php-composer(monolog/monolog) <  %{monolog_max_ver}
Requires:      php-composer(monolog/monolog) >= %{monolog_min_ver}
Requires:      php-composer(phpdocumentor/fileset) <  %{phpdocumentor_fileset_max_ver}
Requires:      php-composer(phpdocumentor/fileset) >= %{phpdocumentor_fileset_min_ver}
Requires:      php-composer(phpdocumentor/graphviz) <  %{phpdocumentor_graphviz_max_ver}
Requires:      php-composer(phpdocumentor/graphviz) >= %{phpdocumentor_graphviz_min_ver}
Requires:      php-composer(phpdocumentor/reflection) <  %{phpdocumentor_reflection_max_ver}
Requires:      php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) <  %{phpdocumentor_reflection_docblock_max_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver}
Requires:      php-composer(phpunit/phpunit)
Requires:      php-composer(symfony/config) <  %{symfony_max_ver}
Requires:      php-composer(symfony/config) >= %{symfony_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/expression-language) <  %{symfony_max_ver}
Requires:      php-composer(symfony/expression-language) >= %{symfony_min_ver}
Requires:      php-composer(symfony/process) <  %{symfony_max_ver}
Requires:      php-composer(symfony/process) >= %{symfony_min_ver}
Requires:      php-composer(symfony/stopwatch) <  %{symfony_max_ver}
Requires:      php-composer(symfony/stopwatch) >= %{symfony_min_ver}
Requires:      php-composer(symfony/validator) <  %{symfony_max_ver}
Requires:      php-composer(symfony/validator) >= %{symfony_min_ver}
Requires:      php-composer(twig/twig) <  %{twig_max_ver}
Requires:      php-composer(twig/twig) >= %{twig_min_ver}
Requires:      php-composer(zendframework/zend-cache) <  %{zendframework_cache_max_ver}
Requires:      php-composer(zendframework/zend-cache) >= %{zendframework_cache_min_ver}
Requires:      php-composer(zendframework/zend-config) <  %{zendframework_config_max_ver}
Requires:      php-composer(zendframework/zend-config) >= %{zendframework_config_min_ver}
Requires:      php-composer(zendframework/zend-filter) <  %{zendframework_filter_max_ver}
Requires:      php-composer(zendframework/zend-filter) >= %{zendframework_filter_min_ver}
Requires:      php-composer(zendframework/zend-i18n) <  %{zendframework_i18n_max_ver}
Requires:      php-composer(zendframework/zend-i18n) >= %{zendframework_i18n_min_ver}
Requires:      php-composer(zendframework/zend-serializer) <  %{zendframework_serializer_max_ver}
Requires:      php-composer(zendframework/zend-serializer) >= %{zendframework_serializer_min_ver}
Requires:      php-composer(zendframework/zend-servicemanager) <  %{zendframework_servicemanager_max_ver}
Requires:      php-composer(zendframework/zend-servicemanager) >= %{zendframework_servicemanager_min_ver}
Requires:      php-composer(zendframework/zend-stdlib) <  %{zendframework_stdlib_max_ver}
Requires:      php-composer(zendframework/zend-stdlib) >= %{zendframework_stdlib_min_ver}
Requires:      php-composer(zetacomponents/document) <  %{zetacomponents_document_max_ver}
Requires:      php-composer(zetacomponents/document) >= %{zetacomponents_document_min_ver}
## phpcompatinfo (computed from version 2.9.0)
Requires:      php-date
Requires:      php-dom
Requires:      php-iconv
Requires:      php-igbinary
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xsl
Requires:      php-zlib
## Autoloader
Requires:      php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(cilex/cilex) <  %{cilex_max_ver}
Requires:      php-composer(cilex/cilex) >= %{cilex_min_ver}
Requires:      php-composer(erusev/parsedown) <  %{erusev_parsedown_max_ver}
Requires:      php-composer(erusev/parsedown) >= %{erusev_parsedown_min_ver}
Requires:      php-composer(jms/serializer) <  %{jms_serializer_max_ver}
Requires:      php-composer(jms/serializer) >= %{jms_serializer_min_ver}
Requires:      php-composer(monolog/monolog) <  %{monolog_max_ver}
Requires:      php-composer(monolog/monolog) >= %{monolog_min_ver}
Requires:      php-composer(phpdocumentor/fileset) <  %{phpdocumentor_fileset_max_ver}
Requires:      php-composer(phpdocumentor/fileset) >= %{phpdocumentor_fileset_min_ver}
Requires:      php-composer(phpdocumentor/graphviz) <  %{phpdocumentor_graphviz_max_ver}
Requires:      php-composer(phpdocumentor/graphviz) >= %{phpdocumentor_graphviz_min_ver}
Requires:      php-composer(phpdocumentor/reflection) <  %{phpdocumentor_reflection_max_ver}
Requires:      php-composer(phpdocumentor/reflection) >= %{phpdocumentor_reflection_min_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) <  %{phpdocumentor_reflection_docblock_max_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) >= %{phpdocumentor_reflection_docblock_min_ver}
Requires:      php-composer(phpunit/phpunit)
Requires:      php-composer(symfony/config) <  %{symfony_max_ver}
Requires:      php-composer(symfony/config) >= %{symfony_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/process) <  %{symfony_max_ver}
Requires:      php-composer(symfony/process) >= %{symfony_min_ver}
Requires:      php-composer(symfony/stopwatch) <  %{symfony_max_ver}
Requires:      php-composer(symfony/stopwatch) >= %{symfony_min_ver}
Requires:      php-composer(symfony/validator) <  %{symfony_max_ver}
Requires:      php-composer(symfony/validator) >= %{symfony_min_ver}
Requires:      php-composer(twig/twig) <  %{twig_max_ver}
Requires:      php-composer(twig/twig) >= %{twig_min_ver}
Requires:      php-composer(zendframework/zend-cache) <  %{zendframework_cache_max_ver}
Requires:      php-composer(zendframework/zend-cache) >= %{zendframework_cache_min_ver}
Requires:      php-composer(zendframework/zend-config) <  %{zendframework_config_max_ver}
Requires:      php-composer(zendframework/zend-config) >= %{zendframework_config_min_ver}
Requires:      php-composer(zendframework/zend-filter) <  %{zendframework_filter_max_ver}
Requires:      php-composer(zendframework/zend-filter) >= %{zendframework_filter_min_ver}
Requires:      php-composer(zendframework/zend-i18n) <  %{zendframework_i18n_max_ver}
Requires:      php-composer(zendframework/zend-i18n) >= %{zendframework_i18n_min_ver}
Requires:      php-composer(zendframework/zend-serializer) <  %{zendframework_serializer_max_ver}
Requires:      php-composer(zendframework/zend-serializer) >= %{zendframework_serializer_min_ver}
Requires:      php-composer(zendframework/zend-servicemanager) <  %{zendframework_servicemanager_max_ver}
Requires:      php-composer(zendframework/zend-servicemanager) >= %{zendframework_servicemanager_min_ver}
Requires:      php-composer(zendframework/zend-stdlib) <  %{zendframework_stdlib_max_ver}
Requires:      php-composer(zendframework/zend-stdlib) >= %{zendframework_stdlib_min_ver}
Requires:      php-composer(zetacomponents/document) <  %{zetacomponents_document_max_ver}
Requires:      php-composer(zetacomponents/document) >= %{zetacomponents_document_min_ver}
# phpcompatinfo (computed from version 2.9.0)
Requires:      php-date
Requires:      php-dom
Requires:      php-iconv
Requires:      php-igbinary
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
Requires:      php-xsl
Requires:      php-zlib
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
phpDocumentor is an application that is capable of analyzing your PHP source
code and DocBlock comments to generate a complete set of API Documentation.

Inspired by phpDocumentor 1 and JavaDoc it continues to innovate and is up to
date with the latest technologies and PHP language features.

Features: phpDocumentor supports the following:
* PHP 5.3 compatible, full support for Namespaces, Closures and more is provided
* Shows any tag, some tags add additional functionality to phpDocumentor
  (such as @link)
* Processing speed, Zend Framework experienced a significant reduction in
  processing time compared to phpDocumentor 1
* Low memory usage, peak memory usage for small projects is less than 20MB,
  medium projects 40MB and large frameworks 100MB
* Incremental parsing, if you kept the Structure file from a previous run you
  get an additional performance boost of up to 80% on top of the mentioned
  processing speed above
* Easy template building, if you want to make a branding you only have to call
  1 task and edit 3 files
* Command-line compatibility with phpDocumentor 1, phpDocumentor 2 is an
  application in its own right but the basic phpDocumentor 1 arguments,
  such as --directory, --file and --target, have been adopted
* Two-step process, phpDocumentor first generates a cache with your application
  structure before creating the output. If you'd like you can use that to power
  your own tools or formatters!

Autoloader: %{phpdir}/phpDocumentor/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

sed -i "s#'@php_dir@#'%{phpdir}#" bin/phpdoc
sed -i 's#@package_version@#%{version}#' src/phpDocumentor/Application.php
echo -n "%{version}" > VERSION

%patch0 -p1
sed -i 's#__PHPDIR__#%{phpdir}#' src/Cilex/Provider/JmsSerializerServiceProvider.php


%build
pushd src/phpDocumentor

: Create Fedora autoloader
cat <<'AUTOLOAD' | tee autoload-fedora.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('Cilex\\Provider\\', __DIR__.'/Cilex/Provider');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Cilex1/autoload.php',
    '%{phpdir}/erusev/parsedown/autoload.php',
    '%{phpdir}/ezc/Document/autoload.php',
    '%{phpdir}/JMS/Serializer/autoload.php',
    '%{phpdir}/Monolog/autoload.php',
    '%{phpdir}/phpDocumentor/Fileset/autoload.php',
    '%{phpdir}/phpDocumentor/GraphViz/autoload.php',
    '%{phpdir}/phpDocumentor/Reflection/autoload.php',
    '%{phpdir}/phpDocumentor/Reflection/DocBlock/autoload.php',
    '%{phpdir}/Symfony/Component/Config/autoload.php',
    '%{phpdir}/Symfony/Component/Console/autoload.php',
    '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    '%{phpdir}/Symfony/Component/Process/autoload.php',
    '%{phpdir}/Symfony/Component/Stopwatch/autoload.php',
    '%{phpdir}/Symfony/Component/Validator/autoload.php',
    '%{phpdir}/Twig/autoload.php',
    '%{phpdir}/Zend/autoload.php',
));
AUTOLOAD

: Create custom composer.json for autoloader dump
cat <<'COMPOSER_JSON' | tee composer.json
{
    "autoload": {
        "files": [
            "autoload-fedora.php"
        ]
    }
}
COMPOSER_JSON

: Generate autoloader
composer dumpautoload --optimize

: Symlink autoloader
ln -s vendor/autoload.php autoload.php

: Cleanup
rm -f composer.json
popd

: Licenses
mkdir -p .rpm/licenses
mv LICENSE .rpm/licenses/
mkdir -p .rpm/licenses/vendor/composer
mv src/phpDocumentor/vendor/composer/LICENSE .rpm/licenses/vendor/composer/
mkdir -p .rpm/licenses/Plugin/Scrybe/
mv src/phpDocumentor/Plugin/Scrybe/docs/license.rst .rpm/licenses/Plugin/Scrybe/

: Docs
mkdir -p .rpm/docs
mv *.md composer.json .rpm/docs/
mkdir -p .rpm/docs/Plugin/LegacyNamespaceConverter
mv src/phpDocumentor/Plugin/LegacyNamespaceConverter/README.md .rpm/docs/Plugin/LegacyNamespaceConverter/
mv src/phpDocumentor/Plugin/Scrybe/docs .rpm/docs/Plugin/Scrybe
mv src/phpDocumentor/Plugin/Scrybe/README.md .rpm/docs/Plugin/Scrybe/


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src/phpDocumentor %{buildroot}%{phpdir}/
cp -rp src/Cilex %{buildroot}%{phpdir}/phpDocumentor/

: Bin
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/phpdoc %{buildroot}%{_bindir}/%{name}


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/phpDocumentor/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\', __DIR__.'/tests/unit/phpDocumentor');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Mockery/autoload.php',
    '%{phpdir}/org/bovigo/vfs/autoload.php',
    '%{phpdir}/Symfony/Component/ExpressionLanguage/autoload.php',
));
BOOTSTRAP

: Update mockery path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' phpunit.xml.dist > phpunit.xml

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        # count(): Parameter must be an array or an object that implements Countable
        if [ $($PHP_EXEC -r 'echo PHP_VERSION_ID;') -ge 70200 ]; then
            sed 's/function testTypeIsInheritedWhenNoneIsPresent/function SKIP_testTypeIsInheritedWhenNoneIsPresent/' \
                -i tests/unit/phpDocumentor/Descriptor/ArgumentDescriptorTest.php
        fi

        $PHP_EXEC -d auto_prepend_file=%{buildroot}%{phpdir}/phpDocumentor/autoload-fedora.php \
            $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
# Library
%{phpdir}/phpDocumentor/Application.php
%{phpdir}/phpDocumentor/Bootstrap.php
%{phpdir}/phpDocumentor/Cilex
%{phpdir}/phpDocumentor/Command
%{phpdir}/phpDocumentor/Compiler
%{phpdir}/phpDocumentor/Configuration
%{phpdir}/phpDocumentor/Configuration.php
%{phpdir}/phpDocumentor/Console
%{phpdir}/phpDocumentor/Descriptor
%{phpdir}/phpDocumentor/Event
%{phpdir}/phpDocumentor/Parser
%{phpdir}/phpDocumentor/Partials
%{phpdir}/phpDocumentor/Plugin
%{phpdir}/phpDocumentor/Transformer
%{phpdir}/phpDocumentor/Translator
%exclude %{phpdir}/phpDocumentor/Plugin/Scrybe/tests
## Autoloaders
%{phpdir}/phpDocumentor/autoload-fedora.php
%{phpdir}/phpDocumentor/autoload.php
%{phpdir}/phpDocumentor/vendor
# Bin
%{_bindir}/%{name}


%changelog
* Sat Aug 19 2017 Shawn Iwinski <shawn@iwin.ski> - 2.9.0-1
- Initial package
