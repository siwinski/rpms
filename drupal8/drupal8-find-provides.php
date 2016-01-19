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
class FindProvides extends Command
{
    protected function configure()
    {
        $this
            ->setName('find-provides')
            ->setDescription('Finds RPM provides')
            ->addOption(
                'spec-version',
                null,
                InputOption::VALUE_REQUIRED,
                'Spec/package version'
            );
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $provides = [];

        while ($file = trim(fgets(STDIN))) {
            if (
                !($fileProvides = $this->executeDrupal8($file))
                && !($fileProvides = $this->executeComposer($file))
            ) {
                continue;
            }

            if (is_array($fileProvides)) {
                $provides = array_merge($provides, $fileProvides);
            } else {
                $provides[] = $fileProvides;
            }
        }

        sort($provides);
        $specVersion = $input->getOption('spec-version');

        foreach (array_unique($provides) as $p) {
            $output->write($p);
            $output->writeln($specVersion ? ' = ' . $specVersion : '');
        }
    }

    private function executeDrupal8($file) {
        if (!preg_match('/\.info\.yml$/', $file)) {
            return null;
        }

        // Hidden?
        $info = Yaml::parse(file_get_contents($file));
        if (!empty($info['hidden'])) {
            return null;
        }

        return sprintf('drupal8(%s)', basename($file, '.info.yml'));
    }

    private function executeComposer($file) {
        if ('composer.json' != basename($file)) {
            return null;
        }

        $info = json_decode(file_get_contents($file), true);
        $provides = [$info['name']];

        if (!empty($info['replace'])) {
            foreach ($info['replace'] as $name => $version) {
                if ('self.version' == $version) {
                    $provides[] = $name;
                }
            }
        }

        return array_map(function ($p) {
            return sprintf('php-composer(%s)', $p);
        }, $provides);
    }
}


$application = new Application();
$application->add(new FindProvides());
$application->run();
