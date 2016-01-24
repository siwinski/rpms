#!/usr/bin/env php
<?php
/**
 * @copyright Copyright (c) 2016, Shawn Iwinski <shawn@iwin.ski>
 * @license http://opensource.org/licenses/MIT MIT
 */
namespace Drupal8Rpmbuild;

require_once '__PHPDIR__/Symfony/Component/Console/autoload.php';
require_once '__PHPDIR__/Symfony/Component/Yaml/autoload.php';

use Symfony\Component\Console\Application;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Yaml\Yaml;

/**
 * Outputs Drupal 8 virtual provides from files provided via STDIN.
 */
class FindProvides extends Command
{
    /**
     * Configures command.
     */
    protected function configure()
    {
        $this
            ->setName('find-provides')
            ->setDescription('Finds RPM drupal8(*) and php-composer(*) virtual provides')
            // --spec-version
            ->addOption(
                'spec-version',
                null,
                InputOption::VALUE_REQUIRED,
                'RPM spec version'
            );
    }

    /**
     * Outputs Drupal 8 virtual provides from files provided via STDIN.
     *
     * Sorts unique values from {@link executeDrupal8()} and
     * {@link executeComposer()}.  If "--spec-version" option is provided,
     * outputs each virtual provide with its' value.
     */
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
            $output->writeln($specVersion ? ' = '.$specVersion : '');
        }
    }

    /**
     * Returns drupal8(*) virtual provide from a *.info.yml file.
     *
     * @return string|null drupal8(*) virtual provide or null
     */
    private function executeDrupal8($file)
    {
        if (!preg_match('/\.info\.yml$/', $file)) {
            return;
        }

        // Hidden?
        $info = Yaml::parse(file_get_contents($file));
        if (!empty($info['hidden'])) {
            return;
        }

        return sprintf('drupal8(%s)', basename($file, '.info.yml'));
    }

    /**
     * Returns php-composer(*) virtual provides from a composer.json file.
     *
     * Returns values from the following Composer properties:
     * - {@link https://getcomposer.org/doc/04-schema.md#name name}
     * - {@link https://getcomposer.org/doc/04-schema.md#replace replace}
     *     - Values are only returned if their version equals "self.version"
     *
     * @return array|null php-composer(*) virtual provides or null
     */
    private function executeComposer($file)
    {
        if ('composer.json' != basename($file)) {
            return;
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

// Create application, add command, and run
$application = new Application('Drupal 8 RPM Find Provides', '__SPEC_VERSION__-__SPEC_RELEASE__');
$application->add(new FindProvides());
$application->run();
