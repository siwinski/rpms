#!/usr/bin/env php
<?php
/**
 * @license MIT
 * @author Shawn Iwinski <shawn@iwin.ski>
 */
namespace Drupal8Rpmbuild;

require_once '/usr/share/php/Symfony/Component/Console/autoload.php';
require_once '/usr/share/php/Symfony/Component/Yaml/autoload.php';

use Symfony\Component\Console\Application;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Yaml\Yaml;

/**
 *
 */
class FindRequires extends Command
{
    const BASE_PATH = '__DRUPAL8__';
    const PHP_MIN_VER = '__DRUPAL8_PHP_MIN_VER__';

    protected function configure()
    {
        $this
            ->setName('find-requires')
            ->setDescription('Finds RPM requires');
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $requires = [];

        while ($file = trim(fgets(STDIN))) {
            if (
                !($fileRequires = $this->executeDrupal8($file))
                && !($fileRequires = $this->executeComposer($file))
            ) {
                continue;
            }

            if (is_array($fileRequires)) {
                $requires = array_merge($requires, $fileRequires);
            } else {
                $requires[] = $fileRequires;
            }
        }

        sort($requires);

        foreach (array_unique($requires) as $req) {
            $output->writeln($req);
        }
    }

    private function executeDrupal8($file) {
        return null;
        if (!preg_match('/\.info\.yml$/', $file)) {
            return null;
        }

        $info = Yaml::parse(file_get_contents($file));

        // Hidden?
        if (!empty($info['hidden'])) {
            return null;
        }

        if (empty($info['dependencies'])) {
            return null;
        }

        return array_map(function ($dependency) {
            return sprintf('drupal8(%s)', $dependency);
        }, $info['dependencies']);
    }

    private function executeComposer($file) {
        if ('composer.json' != basename($file)) {
            return null;
        }

        $info = json_decode(file_get_contents($file), true);

        if (empty($info['require'])) {
            return null;
        }

        print_r($info['require']);

        $requires = [];

        foreach ($info['require'] as $key => $value) {
            $requires[] = sprintf('php-composer(%s)', $key);
        }

        return $requires;
    }
}

$application = new Application();
$application->add(new FindRequires());
$application->run();
