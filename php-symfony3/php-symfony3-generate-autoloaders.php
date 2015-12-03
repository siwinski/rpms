#!/usr/bin/env php
<?php

define('SYMFONY_SOURCE_DIR', __DIR__.'/src');

$phpDir = '/usr/share/php';

require_once SYMFONY_SOURCE_DIR.'/Symfony/Component/ClassLoader/ClassLoader.php';
//echo "REQUIRE = '" . SYMFONY_SOURCE_DIR.'/Symfony/Component/ClassLoader/ClassLoader.php' . "'\n";
$autoloader = new \Symfony\Component\ClassLoader\ClassLoader();
$autoloader->addPrefix('Symfony\\', SYMFONY_SOURCE_DIR);
$autoloader->register();

use Symfony\Component\Finder\Finder;
use Symfony\Component\Yaml\Yaml;

$finder = new Finder();
$finder->in(SYMFONY_SOURCE_DIR)->name('composer.json');

foreach ($finder as $composerFile) {
    $path = $composerFile->getPath();
    $relativePath = $composerFile->getRelativePath();
    $relativePathParts = explode('/', $relativePath);

    $symfonyType = $relativePathParts[1];
    $symfonyTypeName = $relativePathParts[2];

    $namespace = str_replace('/', '\\\\', $relativePath) . '\\\\';

    $composer = json_decode(file_get_contents($composerFile->getPathname()), true);
    $composerRequire = isset($composer['require'])
        ? pkgFilter($composer['require'])
        : [];
    $composerSuggest = isset($composer['suggest'])
        ? pkgFilter($composer['suggest'])
        : [];

    $requiredAutoloaders = [];
    foreach ($composerRequire as $pkg => $version) {
        $requiredAutoloaders[] = pkg2Autoload($pkg, $symfonyType);
    }

    list($composerVendor, $composerProject) = explode('/', $composer['name']);

    $autoloadFile = $path . '/autoload.php';
    $autoload = <<<AUTOLOAD
<?php
/**
 * Autoloader for php-symfony3-${composerProject} and its' dependencies
 * (created by php-symfony3-%{release}).
 */

require_once dirname(dirname(__DIR__)).'/autoload-common.php';

AUTOLOAD;
    if (!empty($requiredAutoloaders)) {
        $autoload .= "\n// Required dependencies\n";

        sort($requiredAutoloaders);
        foreach (array_unique($requiredAutoloaders) as $required) {
            if ($required) {
                $autoload .= "require_once $required;\n";
            }
        }
    }

    $r = print_r($composerRequire, true);
    $s = print_r($composerSuggest, true);
    echo <<<DEBUG






>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
path = $path
relativePath = $relativePath
type = $symfonyType
type name = $symfonyTypeName
namespace = $namespace
require = $r
suggest = $s
autoloadFile = $autoloadFile
autoload = $autoload

DEBUG;
flush();
}



function pkgFilter ($pkg) {
    return array_filter(
        $pkg,
        function ($p) {
            return preg_match('#[^/]+/[^/]+#', $p);
        },
        ARRAY_FILTER_USE_KEY
    );
}

function pkg2Autoload ($pkg) {
    static $pkgMap = [
        'doctrine/annotations'             => [ 'prefix' => '$fedoraPhpDir',              'path' => 'Doctrine/Common/Annotations/autoload.php' ],
        'doctrine/cache'                   => [ 'prefix' => '$fedoraPhpDir',              'path' => 'Doctrine/Common/autoload.php' ],
        'doctrine/common'                  => [ 'prefix' => '$fedoraPhpDir',              'path' => 'Doctrine/Common/Common/autoload.php' ],
        'monolog/monolog'                  => [ 'prefix' => '$fedoraPhpDir',              'path' => 'Monolog/autoload.php' ],
        'ocramius/proxy-manager'           => [ 'prefix' => '$fedoraPhpDir',              'path' => 'ProxyManager/autoload.php' ],
        'psr/log'                          => [ 'prefix' => '$fedoraPhpDir',              'path' => 'Psr/Log/autoload.php' ],
        'symfony/asset'                    => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Asset/autoload.php' ],
        'symfony/browser-kit'              => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'BrowserKit/autoload.php' ],
        'symfony/class-loader'             => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'ClassLoader/autoload.php' ],
        'symfony/config'                   => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Config/autoload.php' ],
        'symfony/console'                  => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Console/autoload.php' ],
        'symfony/css-selector'             => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'CssSelector/autoload.php'         ],
        'symfony/debug-bundle'             => [ 'prefix' => '$fedoraSymfonyBundleDir',    'path' => 'DebugBundle/autoload.php'         ],
        'symfony/debug'                    => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Debug/autoload.php'               ],
        'symfony/dependency-injection'     => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'DependencyInjection/autoload.php' ],
        'symfony/doctrine-bridge'          => [ 'prefix' => '$fedoraSymfonyBridgeDir',    'path' => 'Doctrine/autoload.php' ],
        'symfony/dom-crawler'              => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'DomCrawler/autoload.php' ],
        'symfony/event-dispatcher'         => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'EventDispatcher/autoload.php' ],
        'symfony/expression-language'      => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'ExpressionLanguage/autoload.php' ],
        'symfony/filesystem'               => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Filesystem/autoload.php' ],
        'symfony/finder'                   => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Finder/autoload.php' ],
        'symfony/form'                     => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Form/autoload.php' ],
        'symfony/framework-bundle'         => [ 'prefix' => '$fedoraSymfonyBundleDir',    'path' => 'FrameworkBundle/autoload.php' ],
        'symfony/http-foundation'          => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'HttpFoundation/autoload.php' ],
        'symfony/http-kernel'              => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'HttpKernel/autoload.php' ],
        'symfony/intl'                     => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Intl/autoload.php' ],
        'symfony/ldap'                     => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Ldap/autoload.php' ],
        'symfony/monolog-bridge'           => [ 'prefix' => '$fedoraSymfonyBridgeDir',    'path' => 'Monolog/autoload.php' ],
        'symfony/options-resolver'         => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'OptionsResolver/autoload.php' ],
        'symfony/phpunit-bridge'           => [ 'prefix' => '$fedoraSymfonyBridgeDir',    'path' => 'PhpUnit/autoload.php' ],
        'symfony/polyfill-iconv'           => false,
        'symfony/polyfill-intl-grapheme'   => false,
        'symfony/polyfill-intl-icu'        => false,
        'symfony/polyfill-intl-normalizer' => false,
        'symfony/polyfill-mbstring'        => false,
        'symfony/polyfill-php54'           => (PHP_VERSION_ID < 50400) ? [ 'prefix' => '$fedoraSymfonyDir', 'path' => 'Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php55'           => (PHP_VERSION_ID < 50500) ? [ 'prefix' => '$fedoraSymfonyDir', 'path' => 'Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php56'           => (PHP_VERSION_ID < 50600) ? [ 'prefix' => '$fedoraSymfonyDir', 'path' => 'Polyfill/autoload.php' ] : false,
        'symfony/polyfill-php70'           => (PHP_VERSION_ID < 70000) ? [ 'prefix' => '$fedoraSymfonyDir', 'path' => 'Polyfill/autoload.php' ] : false,
        'symfony/polyfill-util'            => [ 'prefix' => '$fedoraSymfonyDir',          'path' => 'Polyfill/autoload.php' ],
        'symfony/polyfill-xml'             => false,
        'symfony/polyfill'                 => [ 'prefix' => '$fedoraSymfonyDir',          'path' => 'Polyfill/autoload.php' ],
        'symfony/process'                  => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Process/autoload.php' ],
        'symfony/property-access'          => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'PropertyAccess/autoload.php' ],
        'symfony/property-info'            => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'PropertyInfo/autoload.php' ],
        'symfony/proxy-manager-bridge'     => [ 'prefix' => '$fedoraSymfonyBridgeDir',    'path' => 'ProxyManager/autoload.php' ],
        'symfony/routing'                  => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Routing/autoload.php' ],
        'symfony/security-bundle'          => [ 'prefix' => '$fedoraSymfonyBundleDir',    'path' => 'SecurityBundle/autoload.php' ],
        'symfony/security-core'            => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Security/Core/autoload.php' ],
        'symfony/security-csrf'            => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Security/Csrf/autoload.php' ],
        'symfony/security-guard'           => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Security/Guard/autoload.php' ],
        'symfony/security-http'            => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Security/Http/autoload.php' ],
        'symfony/security'                 => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Security/autoload.php' ],
        'symfony/serializer'               => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Serializer/autoload.php' ],
        'symfony/stopwatch'                => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Stopwatch/autoload.php' ],
        'symfony/templating'               => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Templating/autoload.php' ],
        'symfony/translation'              => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Translation/autoload.php' ],
        'symfony/twig-bridge'              => [ 'prefix' => '$fedoraSymfonyBridgeDir',    'path' => 'Twig/autoload.php' ],
        'symfony/twig-bundle'              => [ 'prefix' => '$fedoraSymfonyBundleDir',    'path' => 'TwigBundle/autoload.php' ],
        'symfony/validator'                => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Validator/autoload.php' ],
        'symfony/var-dumper'               => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'VarDumper/autoload.php' ],
        'symfony/web-profiler-bundle'      => [ 'prefix' => '$fedoraSymfonyBundleDir',    'path' => 'WebProfilerBundle/autoload.php' ],
        'symfony/yaml'                     => [ 'prefix' => '$fedoraSymfonyComponentDir', 'path' => 'Yaml/autoload.php' ],
        'twig/twig'                        => [ 'prefix' => '$fedoraPhpDir',              'path' => 'Twig/autoload.php' ],
    ];

    if (!isset($pkgMap[$pkg])) {
        fwrite(STDERR, "ERROR: No autoload map found for pkg '$pkg'\n");
        exit(1);
    } elseif (empty($pkgMap[$pkg])) {
        return null;
    }

    $map = $pkgMap[$pkg];

    return $map['prefix'] . ".'/" . $map['path'] . "'";
}
