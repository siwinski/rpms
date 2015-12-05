#!/usr/bin/env php
<?php

define('SYMFONY_SOURCE_DIR', __DIR__.'/src');

require_once SYMFONY_SOURCE_DIR.'/Symfony/Component/ClassLoader/ClassLoader.php';
$autoloader = new \Symfony\Component\ClassLoader\ClassLoader();
$autoloader->addPrefix('Symfony\\', SYMFONY_SOURCE_DIR);
$autoloader->register();

use Symfony\Component\Finder\Finder;
use Symfony\Component\Finder\SplFileInfo;
use Symfony\Component\Yaml\Yaml;

$finder = new Finder();
$finder->in(SYMFONY_SOURCE_DIR)->name('composer.json');

foreach ($finder as $composerFile) {
    $autoloadGenerator = new AutoloadGenerator($composerFile);
    $autoloadGenerator->generate();
    echo $autoloadGenerator->getFilename(), "\n";
}


//------------------------------------------------------------------------------


final class AutoloadGenerator {
    private static $pkgMap = [
        'doctrine/annotations'             => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Doctrine/Common/Annotations/autoload.php'   ],
        'doctrine/cache'                   => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Doctrine/Common/autoload.php'               ],
        'doctrine/common'                  => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Doctrine/Common/autoload.php'        ],
        'doctrine/data-fixtures'           => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Doctrine/Common/DataFixtures/autoload.php'  ],
        'doctrine/dbal'                    => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Doctrine/DBAL/autoload.php'                 ],
        'doctrine/orm'                     => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Doctrine/ORM/autoload.php'                  ],
        'egulias/email-validator'          => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Egulias/EmailValidator/autoload.php'        ],
        'monolog/monolog'                  => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Monolog/autoload.php'                       ],
        'ocramius/proxy-manager'           => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'ProxyManager/autoload.php'                  ],
        'phpdocumentor/reflection'         => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'phpDocumentor/Reflection/autoload.php'      ],
        'psr/log'                          => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Psr/Log/autoload.php'                       ],
        'symfony/asset'                    => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Asset/autoload.php'               ],
        'symfony/browser-kit'              => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/BrowserKit/autoload.php'          ],
        'symfony/class-loader'             => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/ClassLoader/autoload.php'         ],
        'symfony/config'                   => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Config/autoload.php'              ],
        'symfony/console'                  => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Console/autoload.php'             ],
        'symfony/css-selector'             => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/CssSelector/autoload.php'         ],
        'symfony/debug-bundle'             => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bundle/DebugBundle/autoload.php'            ],
        'symfony/debug'                    => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Debug/autoload.php'               ],
        'symfony/dependency-injection'     => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/DependencyInjection/autoload.php' ],
        'symfony/doctrine-bridge'          => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bridge/Doctrine/autoload.php'               ],
        'symfony/dom-crawler'              => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/DomCrawler/autoload.php'          ],
        'symfony/event-dispatcher'         => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/EventDispatcher/autoload.php'     ],
        'symfony/expression-language'      => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/ExpressionLanguage/autoload.php'  ],
        'symfony/filesystem'               => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Filesystem/autoload.php'          ],
        'symfony/finder'                   => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Finder/autoload.php'              ],
        'symfony/form'                     => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Form/autoload.php'                ],
        'symfony/framework-bundle'         => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bundle/FrameworkBundle/autoload.php'        ],
        'symfony/http-foundation'          => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/HttpFoundation/autoload.php'      ],
        'symfony/http-kernel'              => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/HttpKernel/autoload.php'          ],
        'symfony/intl'                     => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Intl/autoload.php'                ],
        'symfony/ldap'                     => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Ldap/autoload.php'                ],
        'symfony/monolog-bridge'           => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Monolog/autoload.php'             ],
        'symfony/options-resolver'         => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/OptionsResolver/autoload.php'     ],
        'symfony/phpunit-bridge'           => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bridge/PhpUnit/autoload.php'                ],
        'symfony/polyfill-iconv'           => false,
        'symfony/polyfill-intl-grapheme'   => false,
        'symfony/polyfill-intl-icu'        => false,
        'symfony/polyfill-intl-normalizer' => false,
        'symfony/polyfill-mbstring'        => false,
        'symfony/polyfill-php54'           => (PHP_VERSION_ID < 50400) ? [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php55'           => (PHP_VERSION_ID < 50500) ? [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php56'           => (PHP_VERSION_ID < 50600) ? [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php70'           => (PHP_VERSION_ID < 70000) ? [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Symfony/Polyfill/autoload.php' ] : false,
        'symfony/polyfill-util'            => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Symfony/Polyfill/autoload.php'              ],
        'symfony/polyfill-xml'             => false,
        'symfony/polyfill'                 => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Symfony/Polyfill/autoload.php'              ],
        'symfony/process'                  => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Process/autoload.php'             ],
        'symfony/property-access'          => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/PropertyAccess/autoload.php'      ],
        'symfony/property-info'            => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/PropertyInfo/autoload.php'        ],
        'symfony/proxy-manager-bridge'     => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bridge/ProxyManager/autoload.php'           ],
        'symfony/routing'                  => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Routing/autoload.php'             ],
        'symfony/security-acl'             => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Security/Acl/autoload.php'        ],
        'symfony/security-bundle'          => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bundle/SecurityBundle/autoload.php'         ],
        'symfony/security-core'            => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Security/autoload.php'            ],
        'symfony/security-csrf'            => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Security/autoload.php'            ],
        'symfony/security-guard'           => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Security/autoload.php'            ],
        'symfony/security-http'            => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Security/autoload.php'            ],
        'symfony/security'                 => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Security/autoload.php'            ],
        'symfony/serializer'               => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Serializer/autoload.php'          ],
        'symfony/stopwatch'                => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Stopwatch/autoload.php'           ],
        'symfony/templating'               => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Templating/autoload.php'          ],
        'symfony/translation'              => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Translation/autoload.php'         ],
        'symfony/twig-bridge'              => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bridge/Twig/autoload.php'                   ],
        'symfony/twig-bundle'              => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bundle/TwigBundle/autoload.php'             ],
        'symfony/validator'                => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Validator/autoload.php'           ],
        'symfony/var-dumper'               => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/VarDumper/autoload.php'           ],
        'symfony/web-profiler-bundle'      => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Bundle/WebProfilerBundle/autoload.php'      ],
        'symfony/yaml'                     => [ 'prefix' => '$fedoraSymfony3Dir',    'path' => 'Component/Yaml/autoload.php'                ],
        'twig/twig'                        => [ 'prefix' => '$fedoraSymfony3PhpDir', 'path' => 'Twig/autoload.php'                          ],
    ];

    private $composerFile = null;

    private $composer = null;

    private $dependencies = [];

    private $dependencyAutoloaders = [];

    private $filename = null;

    private $content = null;

    public function __construct(SplFileInfo $composerFile) {
        // Composer
        $this->composerFile = $composerFile;
        $this->composer = json_decode(
            file_get_contents($composerFile->getPathname()),
            true
        );

        // Dependencies
        foreach (['require', 'suggest'] as $composerKey) {
            $this->dependencies[$composerKey] =
                self::getDependenciesByComposerKey($composerKey);
            $this->dependencyAutoloaders[$composerKey] =
                self::getDependencyAutoloadersByComposerKey($composerKey);
        }

        // Filename
        $this->filename = $composerFile->getPath() . '/autoload.php';
    }

    public function __toString() {
        return $this->getContent();
    }

    private function getDependenciesByComposerKey($composerKey) {
        return isset($this->composer[$composerKey])
            ? array_keys(array_filter(
                $this->composer[$composerKey],
                function ($pkg) {
                    return preg_match('#[^/]+/[^/]+#', $pkg);
                },
                ARRAY_FILTER_USE_KEY
            ))
            : [];
    }

    private function getDependencyAutoloadersByComposerKey($composerKey) {
        if (!isset($this->composer[$composerKey])) {
            return [];
        }

        $autoloaders = [];

        foreach ($this->dependencies[$composerKey] as $pkg) {
            if ($autoloader = self::pkg2Autoload($pkg)) {
                $autoloaders[] = $autoloader;
            }
        }

        sort($autoloaders);

        return array_unique($autoloaders);
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

    public function getContent() {
        if (!isset($this->content)) {
            $pkg = explode('/', $this->composer['name'])[1];
            $this->content = <<<AUTOLOAD
<?php
/**
 * Autoloader for php-symfony3-${pkg} and its' dependencies
 * (created by php-symfony3-__VERSION__-__RELEASE__).
 */

require_once dirname(dirname(__DIR__)).'/autoload-common.php';

AUTOLOAD;

            if (!empty($this->dependencyAutoloaders['require'])) {
                $this->content .= "\n// Required dependencies\n";
                $this->content .= array_reduce(
                    $this->dependencyAutoloaders['require'],
                    function ($carry, $item) {
                        return $carry . sprintf("require_once %s;\n", $item);
                    },
                    ''
                );
            }

            if (!empty($this->dependencyAutoloaders['suggest'])) {
                $arrayValuesString = rtrim(array_reduce(
                    $this->dependencyAutoloaders['suggest'],
                    function ($carry, $item) {
                        return $carry . sprintf("    %s,\n", $item);
                    },
                    ''
                ));

                $this->content .= <<<OPTIONAL_DEPENDENCIES

// Optional dependencies
foreach([
${arrayValuesString}
] as \$optionalDependency) {
    if (file_exists(\$optionalDependency)) {
        require_once \$optionalDependency;
    }
}

OPTIONAL_DEPENDENCIES;
            }
        }

        return $this->content;
    }

    public function getFilename() {
        return $this->filename;
    }

    public function generate() {
        if (FALSE == file_put_contents(
            $this->filename,
            $this->getContent()
        )) {
            throw new Exception(sprintf(
                'Failed to generate autoload file "%s"',
                $this->filename
            ));
        }
    }
}
