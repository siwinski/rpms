<?php
/**
 * Autoloader for simplesamlphp and its' dependencies
 * (created by simplesamlphp-__SPEC_VERSION__-__SPEC_RELEASE__).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '__PHPDIR__/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('SimpleSAML', __DIR__.'/lib/');

// Autoloader for SimpleSAMLphp modules
require_once __DIR__.'/lib/_autoload_modules.php';

// Required dependencies
require_once '__PHPDIR__/robrichards-xmlseclibs/autoload.php';
require_once '__PHPDIR__/SAML2_1/autoload.php';
require_once '__PHPDIR__/WhiteHat101/Crypt/autoload.php';

return $fedoraClassLoader;
