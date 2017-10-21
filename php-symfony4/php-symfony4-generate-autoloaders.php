#!/usr/bin/env php
<?php

define('SYMFONY_SOURCE_DIR', __DIR__.'/src/Symfony');

require_once '__PHPDIR__/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Symfony\\', SYMFONY_SOURCE_DIR);

use Symfony\Component\Finder\Finder;
use Symfony\Component\Finder\SplFileInfo;

$finder = new Finder();
$finder->in(SYMFONY_SOURCE_DIR)->name('composer.json')->sortByName();

foreach ($finder as $composerFile) {
    $autoloadGenerator = new AutoloadGenerator($composerFile);
    echo $autoloadGenerator->getFilename().PHP_EOL;
    echo $autoloadGenerator->getDevFilename().PHP_EOL;
}


//------------------------------------------------------------------------------


final class AutoloadGenerator {
    private static $pkgMap = [
        'cache/integration-tests' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Cache/IntegrationTests/autoload.php',
        ],
        'doctrine/annotations' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/Common/Annotations/autoload.php',
        ],
        'doctrine/cache' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/Common/Cache/autoload.php',
        ],
        'doctrine/collections' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/Common/Collections/autoload.php',
        ],
        'doctrine/common' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/Common/autoload.php',
        ],
        'doctrine/data-fixtures' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/Common/DataFixtures/autoload.php',
        ],
        'doctrine/dbal' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/DBAL/autoload.php',
        ],
        'doctrine/doctrine-bundle' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/Bundle/DoctrineBundle/autoload.php',
        ],
        'doctrine/orm' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Doctrine/ORM/autoload.php',
        ],
        'egulias/email-validator' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => [
                'Egulias/EmailValidator2/autoload.php',
                'Egulias/EmailValidator/autoload.php',
            ],
        ],
        'fig/link-util' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Fig/Link/autoload.php',
        ],
        'monolog/monolog' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Monolog/autoload.php',
        ],
        'ocramius/proxy-manager' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'ProxyManager/autoload.php',
        ],
        'phpdocumentor/reflection-docblock' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => [
                'phpDocumentor/Reflection/DocBlock4/autoload.php',
                'phpDocumentor/Reflection/DocBlock/autoload.php',
            ],
        ],
        'predis/predis' => false,
        'psr/cache-implementation' => false,
        'psr/cache' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Psr/Cache/autoload.php',
        ],
        'psr/container' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Psr/Container/autoload.php',
        ],
        'psr/link' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Psr/Link/autoload.php',
        ],
        'psr/log' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Psr/Log/autoload.php',
        ],
        'psr/simple-cache' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Psr/SimpleCache/autoload.php',
        ],
        'symfony/asset' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Asset/autoload.php',
        ],
        'symfony/browser-kit' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/BrowserKit/autoload.php',
        ],
        'symfony/cache' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Cache/autoload.php',
        ],
        'symfony/class-loader' => false,
        'symfony/config' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Config/autoload.php',
        ],
        'symfony/console' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Console/autoload.php',
        ],
        'symfony/css-selector' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/CssSelector/autoload.php',
        ],
        'symfony/debug-bundle' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bundle/DebugBundle/autoload.php',
        ],
        'symfony/debug' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Debug/autoload.php',
        ],
        'symfony/dependency-injection' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/DependencyInjection/autoload.php',
        ],
        'symfony/doctrine-bridge' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bridge/Doctrine/autoload.php',
        ],
        'symfony/dom-crawler' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/DomCrawler/autoload.php',
        ],
        'symfony/event-dispatcher' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/EventDispatcher/autoload.php',
        ],
        'symfony/expression-language' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/ExpressionLanguage/autoload.php',
        ],
        'symfony/filesystem' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Filesystem/autoload.php',
        ],
        'symfony/finder' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Finder/autoload.php',
        ],
        'symfony/form' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Form/autoload.php',
        ],
        'symfony/framework-bundle' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bundle/FrameworkBundle/autoload.php',
        ],
        'symfony/http-foundation' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/HttpFoundation/autoload.php',
        ],
        'symfony/http-kernel' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/HttpKernel/autoload.php',
        ],
        'symfony/inflector' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Inflector/autoload.php',
        ],
        'symfony/intl' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Intl/autoload.php',
        ],
        'symfony/ldap' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Ldap/autoload.php',
        ],
        'symfony/lock' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Lock/autoload.php',
        ],
        'symfony/monolog-bridge' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Monolog/autoload.php',
        ],
        'symfony/options-resolver' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/OptionsResolver/autoload.php',
        ],
        'symfony/phpunit-bridge' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bridge/PhpUnit/autoload.php',
        ],
        'symfony/polyfill-intl-icu' => false,
        'symfony/polyfill-mbstring' => false,
        'symfony/polyfill-php72' => (PHP_VERSION_ID < 70200)
            ? [
                'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
                'path' => 'Symfony/Polyfill/autoload.php',
            ]
            : false,
        'symfony/process' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Process/autoload.php',
        ],
        'symfony/property-access' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/PropertyAccess/autoload.php',
        ],
        'symfony/property-info' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/PropertyInfo/autoload.php',
        ],
        'symfony/proxy-manager-bridge' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bridge/ProxyManager/autoload.php',
        ],
        'symfony/routing' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Routing/autoload.php',
        ],
        'symfony/security-acl' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => 'Symfony/Component/Security/Acl/autoload.php',
        ],
        'symfony/security-bundle' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bundle/SecurityBundle/autoload.php',
        ],
        'symfony/security-core' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Security/Core/autoload.php',
        ],
        'symfony/security-csrf' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Security/Csrf/autoload.php',
        ],
        'symfony/security-guard' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Security/Guard/autoload.php',
        ],
        'symfony/security-http' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Security/Http/autoload.php',
        ],
        'symfony/security' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Security/autoload.php',
        ],
        'symfony/serializer' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Serializer/autoload.php',
        ],
        'symfony/stopwatch' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Stopwatch/autoload.php',
        ],
        'symfony/templating' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Templating/autoload.php',
        ],
        'symfony/translation' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Translation/autoload.php',
        ],
        'symfony/twig-bridge' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bridge/Twig/autoload.php',
        ],
        'symfony/twig-bundle' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bundle/TwigBundle/autoload.php',
        ],
        'symfony/validator' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Validator/autoload.php',
        ],
        'symfony/var-dumper' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/VarDumper/autoload.php',
        ],
        'symfony/web-link' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/WebLink/autoload.php',
        ],
        'symfony/web-profiler-bundle' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Bundle/WebProfilerBundle/autoload.php',
        ],
        'symfony/workflow' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Workflow/autoload.php',
        ],
        'symfony/yaml' => [
            'prefix' => 'FEDORA_SYMFONY4_DIR',
            'path' => 'Component/Yaml/autoload.php',
        ],
        'twig/twig' => [
            'prefix' => 'FEDORA_SYMFONY4_PHP_DIR',
            'path' => [
                'Twig2/autoload.php',
                'Twig/autoload.php',
            ],
        ],
    ];

    private $filename = null;

    private $devFilename = null;

    public function __construct(SplFileInfo $composerFile) {
        $composerJson = static::composerJson($composerFile);

        // autoload.php
        $content = static::content(
            $composerJson,
            static::dependencyAutoloaders($composerJson, 'require'),
            static::dependencyAutoloaders($composerJson, 'suggest')
        );
        $this->filename = $composerFile->getPath() . '/autoload.php';
        if (FALSE == file_put_contents($this->filename, $content)) {
            throw new Exception(sprintf(
                'Failed to generate autoload file "%s"',
                $this->filename
            ));
        }

        // autoload-dev.php
        $content = static::content(
            $composerJson,
            static::dependencyAutoloaders($composerJson, 'require-dev'),
            [],
            true
        );
        $this->devFilename = $composerFile->getPath() . '/autoload-dev.php';
        if (FALSE == file_put_contents($this->devFilename, $content)) {
            throw new Exception(sprintf(
                'Failed to generate autoload file "%s"',
                $this->filename
            ));
        }
    }

    private static function composerJson(SplFileInfo $composerFile) {
      $composerJson = json_decode(
          file_get_contents($composerFile->getPathname()),
          true
      );

      if (!isset($composerJson)) {
          throw new \Exception(sprintf(
              'Failed to JSON decode "%s"',
              $composerFile->getPathname()
          ));
      }

      return $composerJson;
    }

    private static function dependencyAutoloaders($composerJson, $composerKey) {
        $dependencyAutoloaders = [];

        if (isset($composerJson[$composerKey])) {
            $dependencies = array_keys(array_filter(
                $composerJson[$composerKey],
                function ($pkg) {
                    return preg_match('#[^/]+/[^/]+#', $pkg);
                },
                ARRAY_FILTER_USE_KEY
            ));

            foreach ($dependencies as $pkg) {
                // Use Symfony cache component as PSR cache implementation
                // for "require-dev" dependency.
                if (
                    ('require-dev' == $composerKey)
                    && ('psr/cache-implementation' == $pkg)
                ) {
                    $pkg = 'symfony/cache';
                }

                if ($autoloader = self::pkg2Autoload($pkg)) {
                    $dependencyAutoloaders[] = $autoloader;
                }
            }

            ksort($dependencyAutoloaders);
        }

        return $dependencyAutoloaders;
    }

    private static function pkg2Autoload ($pkg) {
        if (!isset(self::$pkgMap[$pkg])) {
            throw new Exception(sprintf('No autoload map found for pkg "%s"', $pkg));
        } elseif (empty(self::$pkgMap[$pkg])) {
            return null;
        }

        $map = self::$pkgMap[$pkg];
        $prefix = $map['prefix'];
        $path = $map['path'];

        return is_array($path)
            ? sprintf('[%s]', implode(', ', array_map(function ($map_path) use ($prefix) {
                return sprintf("%s.'/%s'", $prefix, $map_path);
            }, $path)))
            : sprintf("%s.'/%s'", $prefix, $path);
    }

    public function content($composerJson, array $dependencyAutoloadersRequired, array $dependencyAutoloadersOptional = [], $dev = false) {
        $pkg = explode('/', $composerJson['name'])[1];

        $content = <<<AUTOLOAD
<?php
/**
 * Autoloader for php-symfony4-${pkg} and its' dependencies
 * (created by php-symfony4-__VERSION__-__RELEASE__).
 */

AUTOLOAD;

        // This switch statement handles the "autoload-common" require for sub-sub-modules.
        if (!$dev) {
            switch ($pkg) {
                case 'security-core':
                case 'security-csrf':
                case 'security-guard':
                case 'security-http':
                    $content .= "require_once dirname(dirname(dirname(__DIR__))).'/autoload-common.php';".PHP_EOL;
                    break;
                default:
                    $content .= "require_once dirname(dirname(__DIR__)).'/autoload-common.php';".PHP_EOL;
            }
        } else {
            switch ($pkg) {
                case 'security-core':
                case 'security-csrf':
                case 'security-guard':
                case 'security-http':
                    $content .= "require_once dirname(__DIR__).'/autoload.php';".PHP_EOL;
                    break;
                default:
                    $content .= "require_once __DIR__.'/autoload.php';".PHP_EOL;
            }
        }

        if (!empty($dependencyAutoloadersRequired)) {
            $dependencyAutoloadersRequiredString = implode(",\n    ", $dependencyAutoloadersRequired);
            $content .= <<<DEPENDENCY_AUTOLOADERS_REQUIRED


\Fedora\Autoloader\Dependencies::required([
    $dependencyAutoloadersRequiredString
]);
DEPENDENCY_AUTOLOADERS_REQUIRED;
        }

        if (!empty($dependencyAutoloadersOptional)) {
            $dependencyAutoloadersOptionalString = implode(",\n    ", $dependencyAutoloadersOptional);
            $content .= <<<DEPENDENCY_AUTOLOADERS_REQUIRED


\Fedora\Autoloader\Dependencies::optional([
    $dependencyAutoloadersOptionalString
]);
DEPENDENCY_AUTOLOADERS_REQUIRED;
        }

        return $content.PHP_EOL;
    }

    public function getFilename() {
        return $this->filename;
    }

    public function getDevFilename() {
        return $this->devFilename;
    }
}
