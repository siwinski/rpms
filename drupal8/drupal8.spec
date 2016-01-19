#
# Copyright (c) 2013-2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Disable automatic requires/provides processing
AutoReqProv: no

# core/composer.json
## "php": ">=5.5.9"
%global php_min_ver 5.5.9
## "behat/mink": "~1.6"
%global behat_mink_min_ver 1.6
%global behat_mink_max_ver 2.0
## "behat/mink-goutte-driver": "~1.2"
%global behat_mink_goutte_driver_min_ver 1.2
%global behat_mink_goutte_driver_max_ver 2.0
## "composer/semver": "~1.0"
%global composer_semver_min_ver 1.0
%global composer_semver_max_ver 2.0
## "doctrine/annotations": "1.2.*"
%global doctrine_annotations_min_ver 1.2.0
%global doctrine_annotations_max_ver 1.3.0
## "doctrine/common": "2.5.*"
%global doctrine_common_min_ver 2.5.0
%global doctrine_common_max_ver 2.6.0
## "easyrdf/easyrdf": "0.9.*"
%global easyrdf_min_ver 0.9.0
%global easyrdf_max_ver 1.0.0
## "egulias/email-validator": "1.2.*"
%global email_validator_min_ver 1.2.0
%global email_validator_max_ver 1.3.0
## "guzzlehttp/guzzle": "~6.1"
%global guzzle_min_ver 6.1
%global guzzle_max_ver 7.0
## "jcalderonzumba/gastonjs": "^1.1@dev"
%global gastonjs_min_ver 1.1
%global gastonjs_max_ver 2.0
## "jcalderonzumba/mink-phantomjs-driver": "~0.3.1"
%global mink_phantomjs_driver_min_ver 0.3.1
%global mink_phantomjs_driver_max_ver 0.4.0
## "masterminds/html5": "~2.1"
%global masterminds_html5_min_ver 2.1
%global masterminds_html5_max_ver 3.0
## "mikey179/vfsStream": "~1.2"
%global vfsstream_min_ver 1.2
%global vfsstream_max_ver 2.0
## "phpunit/phpunit": "~4.8"
%global phpunit_min_ver 4.8
## "stack/builder": "1.0.*"
%global stack_builder_min_ver 1.0.0
%global stack_builder_max_ver 1.1.0
## "symfony/class-loader": "2.7.*"
## "symfony/css-selector": "2.7.*"
## "symfony/console": "2.7.*"
## "symfony/dependency-injection": "2.7.*"
## "symfony/event-dispatcher": "2.7.*"
## "symfony/http-foundation": "~2.7.2"
## "symfony/http-kernel": "2.7.*"
## "symfony/routing": "2.7.*"
## "symfony/serializer": "2.7.*"
## "symfony/translation": "2.7.*"
## "symfony/validator": "2.7.*"
## "symfony/process": "2.7.*"
## "symfony/yaml": "2.7.*"
### NOTE: Min version not 2.7.0 because autoloader required
%global symfony_min_ver 2.7.1
%global symfony_max_ver 2.8.0
## "symfony-cmf/routing": "1.3.*"
%global symfony_cmf_routing_min_ver 1.3.0
%global symfony_cmf_routing_max_ver 1.4.0
## "symfony/psr-http-message-bridge": "v0.2"
%global symfony_psr_http_message_bridge_min_ver 0.2
%global symfony_psr_http_message_bridge_max_ver 0.3
## "twig/twig": "^1.23.1"
%global twig_min_ver 1.23.1
%global twig_max_ver 2.0
## "zendframework/zend-feed": "~2.4"
%global zend_feed_min_ver 2.4
%global zend_feed_max_ver 3.0
## "zendframework/zend-diactoros": "~1.1"
%global zend_diactoros_min_ver 1.1
%global zend_diactoros_max_ver 2.0

# composer.json
## "composer/installers": "^1.0.21"
%global composer_installers_min_ver 1.0.21
%global composer_installers_max_ver 2.0.0
## "wikimedia/composer-merge-plugin": "~1.3"
### Note: No requirement because needs Composer hooks to work
### See: https://bugzilla.redhat.com/show_bug.cgi?id=1291081

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

# Drupal 8 directories
%global drupal8      %{_datadir}/drupal8
%global drupal8_var  %{_localstatedir}/lib/%{name}
%global drupal8_conf %{_sysconfdir}/%{name}

%{!?phpdir:  %global phpdir  %{_datadir}/php}


Name:      drupal8
Version:   8.0.2
Release:   1%{?dist}
Summary:   An open source content management platform

Group:     Applications/Publishing
License:   GPLv2+
URL:       https://www.drupal.org/8
Source0:   http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
# Modify core/composer.json
Source1:   %{name}-modify-core-composer-json.php
# RPM AutoReqProv
Source2:   macros.%{name}
Source3:   %{name}.attr
Source4:   %{name}-find-provides.php
Source5:   %{name}-find-requires.php
# Apache HTTPD conf
Source6:   %{name}.conf

BuildArch: noarch

Requires:  httpd
Requires:  mod_php

# composer.json
Requires:  php(language)                                 >= %{php_min_ver}
Requires:  php-composer(phpunit/phpunit)                 >= %{phpunit_min_ver}
Requires:  php-composer(composer/semver)                 >= %{composer_semver_min_ver}
Requires:  php-composer(composer/semver)                 <  %{composer_semver_max_ver}
Requires:  php-composer(doctrine/annotations)            >= %{doctrine_annotations_min_ver}
Requires:  php-composer(doctrine/annotations)            <  %{doctrine_annotations_max_ver}
Requires:  php-composer(doctrine/common)                 >= %{doctrine_common_min_ver}
Requires:  php-composer(doctrine/common)                 <  %{doctrine_common_max_ver}
Requires:  php-composer(easyrdf/easyrdf)                 >= %{easyrdf_min_ver}
Requires:  php-composer(easyrdf/easyrdf)                 <  %{easyrdf_max_ver}
Requires:  php-composer(egulias/email-validator)         >= %{email_validator_min_ver}
Requires:  php-composer(egulias/email-validator)         <  %{email_validator_max_ver}
Requires:  php-composer(guzzlehttp/guzzle)               >= %{guzzle_min_ver}
Requires:  php-composer(guzzlehttp/guzzle)               <  %{guzzle_max_ver}
Requires:  php-composer(masterminds/html5)               >= %{masterminds_html5_min_ver}
Requires:  php-composer(masterminds/html5)               <  %{masterminds_html5_max_ver}
Requires:  php-composer(stack/builder)                   >= %{stack_builder_min_ver}
Requires:  php-composer(stack/builder)                   <  %{stack_builder_max_ver}
Requires:  php-composer(symfony/class-loader)            >= %{symfony_min_ver}
Requires:  php-composer(symfony/class-loader)            <  %{symfony_max_ver}
Requires:  php-composer(symfony/console)                 >= %{symfony_min_ver}
Requires:  php-composer(symfony/console)                 <  %{symfony_max_ver}
Requires:  php-composer(symfony/dependency-injection)    >= %{symfony_min_ver}
Requires:  php-composer(symfony/dependency-injection)    <  %{symfony_max_ver}
Requires:  php-composer(symfony/event-dispatcher)        >= %{symfony_min_ver}
Requires:  php-composer(symfony/event-dispatcher)        <  %{symfony_max_ver}
Requires:  php-composer(symfony/http-foundation)         >= %{symfony_min_ver}
Requires:  php-composer(symfony/http-foundation)         <  %{symfony_max_ver}
Requires:  php-composer(symfony/http-kernel)             >= %{symfony_min_ver}
Requires:  php-composer(symfony/http-kernel)             <  %{symfony_max_ver}
Requires:  php-composer(symfony/process)                 >= %{symfony_min_ver}
Requires:  php-composer(symfony/process)                 <  %{symfony_max_ver}
Requires:  php-composer(symfony/psr-http-message-bridge) >= %{symfony_psr_http_message_bridge_min_ver}
Requires:  php-composer(symfony/psr-http-message-bridge) <  %{symfony_psr_http_message_bridge_max_ver}
Requires:  php-composer(symfony/routing)                 >= %{symfony_min_ver}
Requires:  php-composer(symfony/routing)                 <  %{symfony_max_ver}
Requires:  php-composer(symfony/serializer)              >= %{symfony_min_ver}
Requires:  php-composer(symfony/serializer)              <  %{symfony_max_ver}
Requires:  php-composer(symfony/translation)             >= %{symfony_min_ver}
Requires:  php-composer(symfony/translation)             <  %{symfony_max_ver}
Requires:  php-composer(symfony/validator)               >= %{symfony_min_ver}
Requires:  php-composer(symfony/validator)               <  %{symfony_max_ver}
Requires:  php-composer(symfony/yaml)                    >= %{symfony_min_ver}
Requires:  php-composer(symfony/yaml)                    <  %{symfony_max_ver}
Requires:  php-composer(symfony-cmf/routing)             >= %{symfony_cmf_routing_min_ver}
Requires:  php-composer(symfony-cmf/routing)             <  %{symfony_cmf_routing_max_ver}
Requires:  php-composer(twig/twig)                       >= %{twig_min_ver}
Requires:  php-composer(twig/twig)                       <  %{twig_max_ver}
Requires:  php-composer(zendframework/zend-diactoros)    >= %{zend_diactoros_min_ver}
Requires:  php-composer(zendframework/zend-diactoros)    <  %{zend_diactoros_max_ver}
Requires:  php-composer(zendframework/zend-feed)         >= %{zend_feed_min_ver}
Requires:  php-composer(zendframework/zend-feed)         <  %{zend_feed_max_ver}
# phpcompatinfo (computed from version 8.0.2)
Requires:  php-bz2
Requires:  php-ctype
Requires:  php-curl
Requires:  php-date
Requires:  php-dom
Requires:  php-filter
Requires:  php-ftp
Requires:  php-gd
Requires:  php-hash
Requires:  php-iconv
Requires:  php-intl
Requires:  php-json
Requires:  php-libxml
Requires:  php-mbstring
Requires:  php-openssl
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-recode
Requires:  php-reflection
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-tokenizer
Requires:  php-xml
Requires:  php-zip
Requires:  php-zlib
# Weak dependencies
Suggests:  php-pecl(apcu)

# drupal8(*) virtual provides
## Core
Provides:  drupal8(core)                         = %{version}
## Other
Provides:  drupal8(action)                       = %{version}
Provides:  drupal8(aggregator)                   = %{version}
Provides:  drupal8(automated_cron)               = %{version}
Provides:  drupal8(ban)                          = %{version}
Provides:  drupal8(bartik)                       = %{version}
Provides:  drupal8(basic_auth)                   = %{version}
Provides:  drupal8(block)                        = %{version}
Provides:  drupal8(block_content)                = %{version}
Provides:  drupal8(book)                         = %{version}
Provides:  drupal8(breakpoint)                   = %{version}
Provides:  drupal8(ckeditor)                     = %{version}
Provides:  drupal8(color)                        = %{version}
Provides:  drupal8(comment)                      = %{version}
Provides:  drupal8(config)                       = %{version}
Provides:  drupal8(config_translation)           = %{version}
Provides:  drupal8(contact)                      = %{version}
Provides:  drupal8(content_translation)          = %{version}
Provides:  drupal8(contextual)                   = %{version}
Provides:  drupal8(datetime)                     = %{version}
Provides:  drupal8(dblog)                        = %{version}
Provides:  drupal8(dynamic_page_cache)           = %{version}
Provides:  drupal8(editor)                       = %{version}
Provides:  drupal8(field)                        = %{version}
Provides:  drupal8(field_ui)                     = %{version}
Provides:  drupal8(file)                         = %{version}
Provides:  drupal8(filter)                       = %{version}
Provides:  drupal8(forum)                        = %{version}
Provides:  drupal8(hal)                          = %{version}
Provides:  drupal8(help)                         = %{version}
Provides:  drupal8(history)                      = %{version}
Provides:  drupal8(image)                        = %{version}
Provides:  drupal8(inline_form_errors)           = %{version}
Provides:  drupal8(language)                     = %{version}
Provides:  drupal8(link)                         = %{version}
Provides:  drupal8(locale)                       = %{version}
Provides:  drupal8(menu_link_content)            = %{version}
Provides:  drupal8(menu_ui)                      = %{version}
Provides:  drupal8(migrate)                      = %{version}
Provides:  drupal8(migrate_drupal)               = %{version}
Provides:  drupal8(minimal)                      = %{version}
Provides:  drupal8(node)                         = %{version}
Provides:  drupal8(nyan_cat)                     = %{version}
Provides:  drupal8(options)                      = %{version}
Provides:  drupal8(page_cache)                   = %{version}
Provides:  drupal8(path)                         = %{version}
Provides:  drupal8(quickedit)                    = %{version}
Provides:  drupal8(rdf)                          = %{version}
Provides:  drupal8(responsive_image)             = %{version}
Provides:  drupal8(rest)                         = %{version}
Provides:  drupal8(search)                       = %{version}
Provides:  drupal8(search_embedded_form)         = %{version}
Provides:  drupal8(search_extra_type)            = %{version}
Provides:  drupal8(search_query_alter)           = %{version}
Provides:  drupal8(serialization)                = %{version}
Provides:  drupal8(seven)                        = %{version}
Provides:  drupal8(shortcut)                     = %{version}
Provides:  drupal8(simpletest)                   = %{version}
Provides:  drupal8(standard)                     = %{version}
Provides:  drupal8(stark)                        = %{version}
Provides:  drupal8(statistics)                   = %{version}
Provides:  drupal8(syslog)                       = %{version}
Provides:  drupal8(system)                       = %{version}
Provides:  drupal8(taxonomy)                     = %{version}
Provides:  drupal8(taxonomy_crud)                = %{version}
Provides:  drupal8(telephone)                    = %{version}
Provides:  drupal8(text)                         = %{version}
Provides:  drupal8(toolbar)                      = %{version}
Provides:  drupal8(toolbar_disable_user_toolbar) = %{version}
Provides:  drupal8(tour)                         = %{version}
Provides:  drupal8(tracker)                      = %{version}
Provides:  drupal8(twig)                         = %{version}
Provides:  drupal8(update)                       = %{version}
Provides:  drupal8(user)                         = %{version}
Provides:  drupal8(views)                        = %{version}
Provides:  drupal8(views_ui)                     = %{version}

# php-composer(*) virtual provides
## composer.json
Provides:  php-composer(drupal/drupal)                = %{version}
## core/composer.json
### name
Provides:  php-composer(drupal/core)                  = %{version}
### replace
Provides:  php-composer(drupal/action)                = %{version}
Provides:  php-composer(drupal/aggregator)            = %{version}
Provides:  php-composer(drupal/automated_cron)        = %{version}
Provides:  php-composer(drupal/ban)                   = %{version}
Provides:  php-composer(drupal/bartik)                = %{version}
Provides:  php-composer(drupal/basic_auth)            = %{version}
Provides:  php-composer(drupal/block)                 = %{version}
Provides:  php-composer(drupal/block_content)         = %{version}
Provides:  php-composer(drupal/book)                  = %{version}
Provides:  php-composer(drupal/breakpoint)            = %{version}
Provides:  php-composer(drupal/ckeditor)              = %{version}
Provides:  php-composer(drupal/classy)                = %{version}
Provides:  php-composer(drupal/color)                 = %{version}
Provides:  php-composer(drupal/comment)               = %{version}
Provides:  php-composer(drupal/config)                = %{version}
Provides:  php-composer(drupal/config_translation)    = %{version}
Provides:  php-composer(drupal/contact)               = %{version}
Provides:  php-composer(drupal/content_translation)   = %{version}
Provides:  php-composer(drupal/contextual)            = %{version}
Provides:  php-composer(drupal/core-annotation)       = %{version}
Provides:  php-composer(drupal/core-bridge)           = %{version}
Provides:  php-composer(drupal/core-datetime)         = %{version}
Provides:  php-composer(drupal/core-diff)             = %{version}
Provides:  php-composer(drupal/core-discovery)        = %{version}
Provides:  php-composer(drupal/core-event-dispatcher) = %{version}
Provides:  php-composer(drupal/core-file-cache)       = %{version}
Provides:  php-composer(drupal/core-gettext)          = %{version}
Provides:  php-composer(drupal/core-graph)            = %{version}
Provides:  php-composer(drupal/core-php-storage)      = %{version}
Provides:  php-composer(drupal/core-plugin)           = %{version}
Provides:  php-composer(drupal/core-proxy-builder)    = %{version}
Provides:  php-composer(drupal/core-serialization)    = %{version}
Provides:  php-composer(drupal/core-transliteration)  = %{version}
Provides:  php-composer(drupal/core-utility)          = %{version}
Provides:  php-composer(drupal/core-uuid)             = %{version}
Provides:  php-composer(drupal/datetime)              = %{version}
Provides:  php-composer(drupal/dblog)                 = %{version}
Provides:  php-composer(drupal/dynamic_page_cache)    = %{version}
Provides:  php-composer(drupal/editor)                = %{version}
Provides:  php-composer(drupal/entity_reference)      = %{version}
Provides:  php-composer(drupal/field)                 = %{version}
Provides:  php-composer(drupal/field_ui)              = %{version}
Provides:  php-composer(drupal/file)                  = %{version}
Provides:  php-composer(drupal/filter)                = %{version}
Provides:  php-composer(drupal/forum)                 = %{version}
Provides:  php-composer(drupal/hal)                   = %{version}
Provides:  php-composer(drupal/help)                  = %{version}
Provides:  php-composer(drupal/history)               = %{version}
Provides:  php-composer(drupal/image)                 = %{version}
Provides:  php-composer(drupal/inline_form_errors)    = %{version}
Provides:  php-composer(drupal/language)              = %{version}
Provides:  php-composer(drupal/link)                  = %{version}
Provides:  php-composer(drupal/locale)                = %{version}
Provides:  php-composer(drupal/menu_link_content)     = %{version}
Provides:  php-composer(drupal/menu_ui)               = %{version}
Provides:  php-composer(drupal/migrate)               = %{version}
Provides:  php-composer(drupal/migrate_drupal)        = %{version}
Provides:  php-composer(drupal/minimal)               = %{version}
Provides:  php-composer(drupal/node)                  = %{version}
Provides:  php-composer(drupal/options)               = %{version}
Provides:  php-composer(drupal/page_cache)            = %{version}
Provides:  php-composer(drupal/path)                  = %{version}
Provides:  php-composer(drupal/quickedit)             = %{version}
Provides:  php-composer(drupal/rdf)                   = %{version}
Provides:  php-composer(drupal/responsive_image)      = %{version}
Provides:  php-composer(drupal/rest)                  = %{version}
Provides:  php-composer(drupal/search)                = %{version}
Provides:  php-composer(drupal/serialization)         = %{version}
Provides:  php-composer(drupal/seven)                 = %{version}
Provides:  php-composer(drupal/shortcut)              = %{version}
Provides:  php-composer(drupal/simpletest)            = %{version}
Provides:  php-composer(drupal/standard)              = %{version}
Provides:  php-composer(drupal/stark)                 = %{version}
Provides:  php-composer(drupal/statistics)            = %{version}
Provides:  php-composer(drupal/syslog)                = %{version}
Provides:  php-composer(drupal/system)                = %{version}
Provides:  php-composer(drupal/taxonomy)              = %{version}
Provides:  php-composer(drupal/telephone)             = %{version}
Provides:  php-composer(drupal/text)                  = %{version}
Provides:  php-composer(drupal/toolbar)               = %{version}
Provides:  php-composer(drupal/tour)                  = %{version}
Provides:  php-composer(drupal/tracker)               = %{version}
Provides:  php-composer(drupal/update)                = %{version}
Provides:  php-composer(drupal/user)                  = %{version}
Provides:  php-composer(drupal/views)                 = %{version}
Provides:  php-composer(drupal/views_ui)              = %{version}

# Bundled
## core/core.libraries.yml
### core/assets/vendor/backbone
###     License:  MIT
###     Upstream: https://github.com/jashkenas/backbone
Provides:  bundled(js-backbone) = 1.2.3
### core/assets/vendor/ckeditor
###     License:  GPLv2+
###     Upstream: https://github.com/ckeditor/ckeditor-dev
Provides:  bundled(ckeditor) = 4.5.5
### core/assets/vendor/classList
###     License:  Public Domain
###     Upstream: https://github.com/eligrey/classList.js
Provides:  bundled(js-classList) = 2014_12_13
### core/assets/vendor/domready
###     License:  MIT
###     Upstream: https://github.com/ded/domready
Provides:  bundled(js-domready) = 1.0.8
### core/assets/vendor/farbtastic
###     License:  GPLv2+
###     Upstream: https://github.com/mattfarina/farbtastic
Provides:  bundled(js-farbtastic) = 1.2
### core/assets/vendor/html5shiv
###     License:  GPLv2+
###     Upstream: https://github.com/aFarkas/html5shiv
Provides:  bundled(js-html5shiv) = 3.7.3
### core/assets/vendor/jquery
###     License:  MIT
###     Upstream: https://github.com/jquery/jquery
Provides:  bundled(js-jquery) = 2.1.4
### core/assets/vendor/jquery.cookie
###     License:  MIT
###     Upstream: https://github.com/carhartl/jquery-cookie
Provides:  bundled(js-jquery-cookie) = 1.4.1
### core/assets/vendor/jquery-form
###     License:  GPLv2+
###     Upstream: https://github.com/malsup/form
Provides:  bundled(js-jquery-form) = 3.51
### core/assets/vendor/jquery-joyride
###     License:  MIT
###     Upstream: https://github.com/zurb/joyride
Provides:  bundled(js-jquery-joyride) = 2.1.0
### core/assets/vendor/jquery-once
###     License:  GPLv2+
###     Upstream: https://github.com/RobLoach/jquery-once
Provides:  bundled(js-jquery-once) = 2.1.1
### core/assets/vendor/jquery.ui
###     License:  Public Domain
###     Upstream: https://github.com/jquery/jquery-ui
Provides:  bundled(js-jquery-ui) = 1.11.4
### core/assets/vendor/jquery-ui-touch-punch
###     License:  GPLv2+
###     Upstream: https://github.com/furf/jquery-ui-touch-punch
Provides:  bundled(js-jquery-ui-touch-punch) = 0.2.3
### core/assets/vendor/matchMedia
###     License:  MIT
###     Upstream: https://github.com/paulirish/matchMedia.js
Provides:  bundled(js-matchMedia) = 0.2.0
### core/assets/vendor/modernizr
###     License:  MIT
###     Upstream: https://github.com/Modernizr/Modernizr
Provides:  bundled(js-modernizr) = 3.1.0
### core/assets/vendor/normalize-css
###     License:  MIT
###     Upstream: https://github.com/necolas/normalize.css
Provides:  bundled(css-normalize) = 3.0.3
### core/assets/vendor/picturefill
###     License:  MIT
###     Upstream: https://github.com/scottjehl/picturefill
Provides:  bundled(js-picturefill) = 3.0.1
### core/assets/vendor/underscore
###     License:  MIT
###     Upstream: https://github.com/jashkenas/underscore
Provides:  bundled(js-underscore) = 1.8.3

## core/composer.json (see composer.lock for versions)
### vendor/behat/mink
###     License:  MIT
###     Upstream: https://github.com/minkphp/Mink
Provides:  bundled(php-behat-mink) = 1.7.0
### vendor/behat/mink-browserkit-driver
###     License:  MIT
###     Upstream: https://github.com/minkphp/MinkBrowserKitDriver
Provides:  bundled(php-behat-mink-browserkit-driver) = 1.3.0
### vendor/behat/mink-goutte-driver
###     License:  MIT
###     Upstream: https://github.com/minkphp/MinkGoutteDriver
Provides:  bundled(php-behat-mink-goutte-driver) = 1.2.0
### vendor/jcalderonzumba/gastonjs
###     License:  MIT
###     Upstream: https://github.com/jcalderonzumba/gastonjs
Provides:  bundled(php-jcalderonzumba-gastonjs) = 1.0.1
### vendor/jcalderonzumba/mink-phantomjs-driver
###     License:  MIT
###     Upstream: https://github.com/jcalderonzumba/MinkPhantomJSDriver
Provides:  bundled(php-jcalderonzumba-mink-phantomjs-driver) = 0.3.0


%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.


%package rpmbuild
Summary:  Rpmbuild files for %{name}
Group:    Development/Tools
Requires: php-composer(symfony/console)
Requires: php-composer(symfony/yaml)

%description rpmbuild
%{summary}.


%prep
%setup -q -c

pushd drupal-%{version}

: Remove unneeded files
find . -name '*~' -delete
find . -name '.git*' -delete
find . -name 'web.config' -delete
rm -rf vendor

: Apache .htaccess
sed 's!# RewriteBase /$!# RewriteBase /\n  RewriteBase /drupal8!' \
    -i .htaccess

: Update php bin
sed 's#/bin/php#%{_bindir}/php#' \
    -i core/scripts/update-countries.sh

# TODO: Update phpunit bin
# core/modules/simpletest/simpletest.module:simpletest_phpunit_command()

: Fix "non-executable-script" rpmlint errors
chmod +x \
    core/scripts/cron-curl.sh \
    core/scripts/cron-lynx.sh \
    core/scripts/db-tools.php \
    core/scripts/dump-database-d6.sh \
    core/scripts/dump-database-d7.sh \
    core/scripts/generate-d6-content.sh \
    core/scripts/generate-d7-content.sh \
    core/scripts/generate-proxy-class.php

: Fix "script-without-shebang" rpmlint errors
chmod -x \
    core/assets/vendor/jquery-once/jquery.once.min.js.map \
    core/modules/block_content/migration_templates/d7_custom_block.yml \
    core/modules/block_content/src/Plugin/migrate/source/d7/BlockCustom.php \
    core/modules/block/migration_templates/d7_block.yml \
    core/modules/comment/migration_templates/d7_comment_entity_display.yml \
    core/modules/comment/migration_templates/d7_comment_entity_form_display_subject.yml \
    core/modules/comment/migration_templates/d7_comment_entity_form_display.yml \
    core/modules/comment/migration_templates/d7_comment_field_instance.yml \
    core/modules/comment/migration_templates/d7_comment_field.yml \
    core/modules/comment/migration_templates/d7_comment_type.yml \
    core/modules/comment/migration_templates/d7_comment.yml \
    core/modules/comment/src/Plugin/migrate/source/d7/Comment.php \
    core/modules/field/migration_templates/d7_field_instance_widget_settings.yml \
    core/modules/field/migration_templates/d7_field_instance.yml \
    core/modules/field/migration_templates/d7_field.yml \
    core/modules/field/src/Plugin/migrate/process/d7/FieldInstanceDefaults.php \
    core/modules/field/src/Plugin/migrate/process/d7/FieldInstanceSettings.php \
    core/modules/field/src/Plugin/migrate/process/d7/FieldSettings.php \
    core/modules/field/src/Plugin/migrate/source/d7/FieldInstance.php \
    core/modules/field/src/Plugin/migrate/source/d7/Field.php \
    core/modules/filter/src/Plugin/migrate/source/d7/FilterFormat.php \
    core/modules/image/migration_templates/d7_image_settings.yml \
    core/modules/user/migration_templates/d7_user_flood.yml \
    core/modules/user/migration_templates/d7_user_role.yml \
    core/modules/user/migration_templates/d7_user.yml \
    core/modules/user/src/Plugin/migrate/source/d7/Role.php \
    core/modules/user/src/Plugin/migrate/source/d7/User.php \
    core/modules/views_ui/src/ParamConverter/ViewUIConverter.php \
    core/scripts/run-tests.sh

: Modify core/composer.json
%{SOURCE1} modify-core-composer-json --builddir=$(pwd) --phpdir=%{phpdir}

popd

: RPM AutoReqProv
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .
cp -p %{SOURCE5} .

: Apache HTTPD conf
cp -p %{SOURCE6} .

: Update macros version and base path
sed -e 's:__DRUPAL8_VERSION__:%{version}:' \
    -e 's:__DRUPAL8_PHP_MIN_VER__:%{php_min_ver}:' \
    -e 's:__DRUPAL8__:%{drupal8}:' \
    -e 's:__DRUPAL8_VAR__:%{drupal8_var}:' \
    -e 's:__DRUPAL8_CONF__:%{drupal8_conf}:' \
    -i macros.%{name}


%build
pushd drupal-%{version}
    pushd core
        : Create Composer autoloader
        %{_bindir}/composer dump-autoload --optimize
    popd

    ln -s core/vendor vendor
popd


%install
pushd drupal-%{version}

: Main
mkdir -p %{buildroot}%{drupal8}
cp -pr * %{buildroot}%{drupal8}/

: Sites
mkdir -p %{buildroot}%{drupal8_conf}/sites
mv %{buildroot}%{drupal8}/sites/* %{buildroot}%{drupal8_conf}/sites/
rmdir %{buildroot}%{drupal8}/sites
ln -s %{drupal8_conf}/sites %{buildroot}%{drupal8}/sites

: Files
mkdir -p %{buildroot}%{drupal8_var}/files/{public,private}/default
ln -s %{drupal8_var}/files/public/default \
    %{buildroot}%{drupal8_conf}/sites/default/files

# Apache .htaccess
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 .htaccess %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.htaccess
ln -s %{_sysconfdir}/httpd/conf.d/%{name}.htaccess %{buildroot}%{drupal8}/.htaccess

popd

# RPM AutoReqProv
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -pm 0644 macros.%{name} %{buildroot}%{_rpmconfigdir}/macros.d/
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
install -pm 0644 %{name}.attr %{buildroot}%{_rpmconfigdir}/fileattrs/
install -pm 0755 %{name}-find-provides.php %{buildroot}%{_rpmconfigdir}/
install -pm 0755 %{name}-find-requires.php %{buildroot}%{_rpmconfigdir}/

# Apache HTTPD conf
install -pm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/


%check
# Ensure RewriteBase
grep \
'RewriteBase /drupal8' \
        %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.htaccess \
        --quiet \
    || exit 1

pushd drupal-%{version}

# Ensure php bin updated
grep -r '#!/bin/php' . && exit 1

%if %{with_tests}
# Unit tests
pushd core

# Skip certain tests that require the "willReturn" function in PHPUnit MockObject > 2
#   Note: This is because of PHPUnit < 4.1
#%if 0%{?fedora} < 21 && 0%{?rhel} < 7
#sed 's/function testSetError/function SKIP_testSetError/' \
#    -i tests/Drupal/Tests/Core/Form/FormStateTest.php
#sed -e 's/function testRedirectWithResult/function SKIP_testRedirectWithResult/' \
#    -e 's/function testRedirectWithRouteWithResult/function SKIP_testRedirectWithRouteWithResult/' \
#    -e 's/function testRedirectWithResponseObject/function SKIP_testRedirectWithResponseObject/' \
#    -e 's/function testRedirectWithoutResult/function SKIP_testRedirectWithoutResult/' \
#    -i tests/Drupal/Tests/Core/Form/FormSubmitterTest.php
#%endif

# Skip tests with PHPUnit 4.2+ deprecated functions
#   Note: This is because of PHPUnit > 4.1
#   See:  https://www.drupal.org/node/2331685
%if 0%{?fedora} >= 21 && 0%{?rhel} >= 7
# assertTag
rm -f tests/Drupal/Tests/Core/Utility/LinkGeneratorTest.php
# assertSelectEquals
sed 's/function testPrint/function SKIP_testPrint/' \
    -i tests/Drupal/Tests/Core/Template/AttributeTest.php
%endif

# Symfony DependencyInjection pkg does not include test files so skip this test
rm -f tests/Drupal/Tests/Core/DependencyInjection/ContainerBuilderTest.php

%{_bindir}/phpunit

popd
%else
: Test suite skipped
%endif

popd


%files
# Core
%doc drupal-%{version}/README.txt
%doc drupal-%{version}/composer.*
%doc drupal-%{version}/core/*.txt
%doc drupal-%{version}/example.*
%dir %{drupal8}
     %{drupal8}/.htaccess
     %{drupal8}/*.*
     %{drupal8}/core
%dir %{drupal8}/modules
     %{drupal8}/modules/README.txt
%dir %{drupal8}/profiles
     %{drupal8}/profiles/README.txt
     %{drupal8}/sites
%dir %{drupal8}/themes
     %{drupal8}/themes/README.txt
     %{drupal8}/vendor
# Sites
%dir  %{drupal8_conf}
%dir  %{drupal8_conf}/sites
      %{drupal8_conf}/sites/example.*
      %{drupal8_conf}/sites/README.txt
%config(noreplace) %{drupal8_conf}/sites/development.services.yml
%dir  %{drupal8_conf}/sites/default
      %{drupal8_conf}/sites/default/default.*
# Files
%{drupal8_conf}/sites/default/files
%dir                         %{drupal8_var}
%dir                         %{drupal8_var}/files
%dir                         %{drupal8_var}/files/private
%dir %attr(0775,root,apache) %{drupal8_var}/files/private/default
%dir                         %{drupal8_var}/files/public
%dir %attr(0775,root,apache) %{drupal8_var}/files/public/default
# Apache
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.htaccess

%files rpmbuild
%{_rpmconfigdir}/macros.d/macros.%{name}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}-find-provides.php
%{_rpmconfigdir}/%{name}-find-requires.php


%changelog
* Tue Jan 19 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0.2-1
- Updated to 8.0.2
- Modified drupal8(*) virtual provides
- Added php-composer(*) virtual provides
- Added custom autoloader (and removed Composer autoload modifications)
- Added "drupal8_var" and "drupal8_conf" macros
- "%%{_sysconfdir}/%%{name}/*" => "%%{_sysconfdir}/%%{name}/sites/*"
- "%%{_localstatedir}/lib/%%{name}/*" => "%%{_localstatedir}/lib/%%{name}/files/*"

* Sat Oct 10 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0.0-0.14.rc1
- Updated to 8.0.0-rc1

* Sat Nov 22 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0.0-0.13.beta3
- Updated to 8.0.0-beta3

* Wed Jul 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.12.alpha13
- Updated to 8.0-alpha13

* Sun Jun 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.11.alpha12
- Updated to 8.0-alpha12

* Fri May 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.10.alpha11
- Updated to 8.0-alpha11
- Many more changes...

* Sun Jan 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.9.alpha7
- Updated to release tag 8.0-alpha7
- Updated URL
- Moved .htaccess file to Apache conf dir
- Fixed Apache conf file
- Removed PSR Log dependency (dependencies pull this in)
- Unbundle EasyRDF, Gliph, Symfony, Zend Framework 2 Feed
- Added specific file requires to make sure broken dependency if providing
  pkg moves file
- Keep modules, profiles, and themes README files in directories
- Unbundling now uses autoloader instead of symlinks

* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.8.alpha4
- Updated to release tag 8.0-alpha4
- Require correct min PHP version 5.3.10 instead of 5.3.3
- Require correct min/max pkg versions
- Use bundled Doctrine, EasyRdf, Symfony, Symfony CMF Routing, and Twig
  because required versions are not available in Fedora
- Updated phpcompatinfo requires:
  Added: openssl, tokenizer
  Removed: bcmath, gmp

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.7.20130616git1648a47
- Updated to 2013-06-16 snapshot
- No auto-provide hidden projects
- Static virtual provides instead of dynamic

* Wed Jun 12 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.6.20130612gite952a21
- Updated to 2013-06-12 snapshot

* Sun May 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.5.20130504git5838ea9
- Updated to 2013-05-04 snapshot

* Thu Apr 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.4.20130403giteebd063
- Updated to 2013-04-03 snapshot
- Updated note about PHP minimum version
- Added php-Assetic and php-SymfonyCmfRouting requires
- Removed vendors (bundled libraries) phpci requires
- Updated composer file locations

* Thu Mar 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.3.20130309git3210003
- %%{drupal8}/sites => %%{_sysconfdir}/%%{name}
- Marked Apache config as %%config
- Marked modules/profiles/themes README.txt as %%doc
- Specific dir and file ownership
- Removed example.gitignore
- Added files dir and symlink

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.2.20130309git3210003
- Updated to latest 2013-03-09 snapshot
- *.info => *.info.yml
- Added PyYAML require for rpmbuild sub-package
- Un-bundled PHPUnit

* Mon Feb 25 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 8.0-0.1.20130224git8afbc08
- Initial package
