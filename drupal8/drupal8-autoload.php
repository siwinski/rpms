<?php
/**
 * Autoloader for drupal8 and its' dependencies
 * (created by drupal8-__SPEC_VERSION__-__SPEC_RELEASE__).
 *
 * NOTE: This is an RPM-managed autoload file and is not the default
 * Drupal-provided one.  The original Drupal-provided autoload file
 * has been moved to autoload.php.dist.
 *
 * @see index.php
 * @see core/install.php
 * @see core/rebuild.php
 * @see core/modules/statistics/statistics.php
 *
 * @return \Composer\Autoload\ClassLoader
 */

$drupal8ComposerAutoloadClassLoader = require __DIR__.'/core/vendor/autoload.php';

// Required dependencies
require_once '__PHPDIR__/Composer/Semver/autoload.php';
require_once '__PHPDIR__/Doctrine/Common/Annotations/autoload.php';
require_once '__PHPDIR__/Doctrine/Common/autoload.php';
require_once '__PHPDIR__/EasyRdf/autoload.php';
require_once '__PHPDIR__/Egulias/EmailValidator/autoload.php';
require_once '__PHPDIR__/GuzzleHttp6/autoload.php';
require_once '__PHPDIR__/Masterminds/HTML5/autoload.php';
require_once '__PHPDIR__/random_compat/autoload.php';
require_once '__PHPDIR__/Stack/autoload-builder.php';
require_once '__PHPDIR__/Symfony/Bridge/PsrHttpMessage/autoload.php';
require_once '__PHPDIR__/Symfony/Cmf/Component/Routing/autoload.php';
require_once '__PHPDIR__/Symfony/Component/ClassLoader/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Console/autoload.php';
require_once '__PHPDIR__/Symfony/Component/DependencyInjection/autoload.php';
require_once '__PHPDIR__/Symfony/Component/EventDispatcher/autoload.php';
require_once '__PHPDIR__/Symfony/Component/HttpFoundation/autoload.php';
require_once '__PHPDIR__/Symfony/Component/HttpKernel/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Process/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Routing/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Serializer/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Translation/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Validator/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Yaml/autoload.php';
require_once '__PHPDIR__/Twig/autoload.php';
require_once '__PHPDIR__/Zend/autoload.php';
require_once '__PHPDIR__/Zend/Diactoros/autoload.php';

// Modules', profiles', and themes' autoloaders
foreach(['modules', 'profiles', 'themes'] as $projectType) {
    if ($projectTypeAutoloadFiles = glob("$projectType/*/autoload.php")) {
        foreach ($projectTypeAutoloadFiles as $projectTypeAutoloader) {
            require_once $projectTypeAutoloader;
        }
    }
}

return $drupal8ComposerAutoloadClassLoader;
