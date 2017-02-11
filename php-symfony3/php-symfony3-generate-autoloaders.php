#!/usr/bin/env php
<?php

define('SYMFONY_SOURCE_DIR', __DIR__.'/src');

require_once SYMFONY_SOURCE_DIR.'/Symfony/Component/ClassLoader/ClassLoader.php';
$autoloader = new \Symfony\Component\ClassLoader\ClassLoader();
$autoloader->addPrefix('Symfony\\', SYMFONY_SOURCE_DIR);
$autoloader->register();

use Symfony\Component\Finder\Finder;
use Symfony\Component\Finder\SplFileInfo;

$finder = new Finder();
$finder->in(SYMFONY_SOURCE_DIR)->name('composer.json')->sortByName();

foreach ($finder as $composerFile) {
    $autoloadGenerator = new AutoloadGenerator($composerFile);
    echo $autoloadGenerator->getFilename(), "\n";
}


//------------------------------------------------------------------------------


final class AutoloadGenerator {
    private static $pkgMap = [
        'doctrine/annotations'              => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Doctrine/Common/Annotations/autoload.php'       ],
        'doctrine/cache'                    => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Doctrine/Common/Cache/autoload.php'             ],
        'doctrine/common'                   => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Doctrine/Common/autoload.php'                   ],
        'doctrine/data-fixtures'            => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Doctrine/Common/DataFixtures/autoload.php'      ],
        'doctrine/dbal'                     => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Doctrine/DBAL/autoload.php'                     ],
        'doctrine/orm'                      => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Doctrine/ORM/autoload.php'                      ],
        'egulias/email-validator'           => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Egulias/EmailValidator/autoload.php'            ],
        'monolog/monolog'                   => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Monolog/autoload.php'                           ],
        'ocramius/proxy-manager'            => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'ProxyManager/autoload.php'                      ],
        'phpdocumentor/reflection-docblock' => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'phpDocumentor/Reflection/DocBlock3/autoload.php' ],
        'psr/cache-implementation'          => false,
        'psr/cache'                         => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Psr/Cache/autoload.php'                         ],
        'psr/log'                           => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Psr/Log/autoload.php'                           ],
        'symfony/asset'                     => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Asset/autoload.php'                   ],
        'symfony/browser-kit'               => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/BrowserKit/autoload.php'              ],
        'symfony/cache'                     => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Cache/autoload.php'                   ],
        'symfony/class-loader'              => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/ClassLoader/autoload.php'             ],
        'symfony/config'                    => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Config/autoload.php'                  ],
        'symfony/console'                   => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Console/autoload.php'                 ],
        'symfony/css-selector'              => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/CssSelector/autoload.php'             ],
        'symfony/debug-bundle'              => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bundle/DebugBundle/autoload.php'                ],
        'symfony/debug'                     => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Debug/autoload.php'                   ],
        'symfony/dependency-injection'      => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/DependencyInjection/autoload.php'     ],
        'symfony/doctrine-bridge'           => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bridge/Doctrine/autoload.php'                   ],
        'symfony/dom-crawler'               => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/DomCrawler/autoload.php'              ],
        'symfony/event-dispatcher'          => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/EventDispatcher/autoload.php'         ],
        'symfony/expression-language'       => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/ExpressionLanguage/autoload.php'      ],
        'symfony/filesystem'                => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Filesystem/autoload.php'              ],
        'symfony/finder'                    => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Finder/autoload.php'                  ],
        'symfony/form'                      => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Form/autoload.php'                    ],
        'symfony/framework-bundle'          => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bundle/FrameworkBundle/autoload.php'            ],
        'symfony/http-foundation'           => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/HttpFoundation/autoload.php'          ],
        'symfony/http-kernel'               => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/HttpKernel/autoload.php'              ],
        'symfony/inflector'                 => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Inflector/autoload.php'               ],
        'symfony/intl'                      => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Intl/autoload.php'                    ],
        'symfony/ldap'                      => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Ldap/autoload.php'                    ],
        'symfony/monolog-bridge'            => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Monolog/autoload.php'                 ],
        'symfony/options-resolver'          => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/OptionsResolver/autoload.php'         ],
        'symfony/phpunit-bridge'            => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bridge/PhpUnit/autoload.php'                    ],
        'symfony/polyfill-apcu'             => false,
        'symfony/polyfill-iconv'            => false,
        'symfony/polyfill-intl-grapheme'    => false,
        'symfony/polyfill-intl-icu'         => false,
        'symfony/polyfill-intl-normalizer'  => false,
        'symfony/polyfill-mbstring'         => false,
        'symfony/polyfill-php54'            => (PHP_VERSION_ID < 50400) ? [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php55'            => (PHP_VERSION_ID < 50500) ? [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php56'            => (PHP_VERSION_ID < 50600) ? [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php70'            => (PHP_VERSION_ID < 70000) ? [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-util'             => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Symfony/Polyfill/autoload.php'                  ],
        'symfony/polyfill-xml'              => false,
        'symfony/polyfill'                  => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Symfony/Polyfill/autoload.php'                  ],
        'symfony/process'                   => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Process/autoload.php'                 ],
        'symfony/property-access'           => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/PropertyAccess/autoload.php'          ],
        'symfony/property-info'             => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/PropertyInfo/autoload.php'            ],
        'symfony/proxy-manager-bridge'      => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bridge/ProxyManager/autoload.php'               ],
        'symfony/routing'                   => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Routing/autoload.php'                 ],
        'symfony/security-acl'              => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Component/Security/Acl/autoload.php'            ],
        'symfony/security-bundle'           => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bundle/SecurityBundle/autoload.php'             ],
        'symfony/security-core'             => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Security/Core/autoload.php'                ],
        'symfony/security-csrf'             => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Security/Csrf/autoload.php'                ],
        'symfony/security-guard'            => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Security/Guard/autoload.php'                ],
        'symfony/security-http'             => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Security/Http/autoload.php'                ],
        'symfony/security'                  => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Security/autoload.php'                ],
        'symfony/serializer'                => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Serializer/autoload.php'              ],
        'symfony/stopwatch'                 => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Stopwatch/autoload.php'               ],
        'symfony/templating'                => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Templating/autoload.php'              ],
        'symfony/translation'               => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Translation/autoload.php'             ],
        'symfony/twig-bridge'               => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bridge/Twig/autoload.php'                       ],
        'symfony/twig-bundle'               => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bundle/TwigBundle/autoload.php'                 ],
        'symfony/validator'                 => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Validator/autoload.php'               ],
        'symfony/var-dumper'                => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/VarDumper/autoload.php'               ],
        'symfony/web-profiler-bundle'       => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Bundle/WebProfilerBundle/autoload.php'          ],
        'symfony/yaml'                      => [ 'prefix' => 'FEDORA_SYMFONY3_DIR',    'path' => 'Component/Yaml/autoload.php'                    ],
        'twig/twig'                         => [ 'prefix' => 'FEDORA_SYMFONY3_PHP_DIR', 'path' => 'Twig/autoload.php'                              ],
    ];

    private $filename = null;

    public function __construct(SplFileInfo $composerFile) {
        $composerJson = static::composerJson($composerFile);
        $content = static::content(
            $composerJson,
            static::dependencyAutoloaders($composerJson, true),
            static::dependencyAutoloaders($composerJson, false)
        );

        $this->filename = $composerFile->getPath() . '/autoload.php';

        if (FALSE == file_put_contents($this->filename, $content)) {
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

    private static function dependencyAutoloaders($composerJson, $required) {
        $dependencyAutoloaders = [];
        $composerKey = $required ? 'require' : 'suggest';

        if (isset($composerJson[$composerKey])) {
            $dependencies = array_keys(array_filter(
                $composerJson[$composerKey],
                function ($pkg) {
                    return preg_match('#[^/]+/[^/]+#', $pkg);
                },
                ARRAY_FILTER_USE_KEY
            ));

            foreach ($dependencies as $pkg) {
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
        return sprintf("%s.'/%s'", $map['prefix'], $map['path']);
    }

    public function content($composerJson, array $dependencyAutoloadersRequired, array $dependencyAutoloadersOptional) {
        $pkg = explode('/', $composerJson['name'])[1];

        $content = <<<AUTOLOAD
<?php
/**
 * Autoloader for php-symfony3-${pkg} and its' dependencies
 * (created by php-symfony3-__VERSION__-__RELEASE__).
 */

AUTOLOAD;

        // This switch statement handles the "autoload-common" require for sub-sub-modules.
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
}
