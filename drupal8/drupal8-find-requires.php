#!/usr/bin/env php
<?php
/**
 * Fedora Drupal 8 RPM find requires
 *
 * Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
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
 * Outputs Drupal 8 requires from files provided via STDIN.
 */
class FindRequires extends Command
{
    const PHP_MIN_VER = '__DRUPAL8_PHP_MIN_VER__';

    /**
     * Configures command.
     */
    protected function configure()
    {
        $this
            ->setName('find-requires')
            ->setDescription('Finds RPM requires')
            // --drupal-project
            ->addOption(
                'drupal8-project',
                null,
                InputOption::VALUE_REQUIRED,
                'Drupal 8 project name (i.e. https://www.drupal.org/project/<info>DRUPAL8-PROJECT</info>)'
            )
            // --spec-name
            ->addOption(
                'spec-name',
                null,
                InputOption::VALUE_REQUIRED,
                'RPM spec name (used as "--drupal-project" failover, without "drupal8-" prefix if "--drupal-project" was not provided)'
            );
    }

    /**
     * Outputs Drupal 8 requires from files provided via STDIN.
     *
     * Starts with "drupal8(core)".
     *
     * Sorts unique values from main project's *.info.yml file's "dependencies"
     * property.
     */
    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $requires = ['drupal8(core)'];

        $drupalProject = $input->getOption('drupal8-project');
        if (empty($drupalProject)) {
            $specName = $input->getOption('spec-name');
            $drupalProject = preg_replace('/^drupal8-/', '', $specName);
        }

        if (!empty($drupalProject)) {
            $drupalProjectFilename = sprintf(
                '/%s/%s.info.yml',
                $drupalProject,
                $drupalProject
            );

            while ($file = trim(fgets(STDIN))) {
                if (!preg_match('/'.preg_quote($drupalProjectFilename, '/').'$/', $file)) {
                    continue;
                }

                $info = Yaml::parse(file_get_contents($file));

                if (empty($info['hidden']) && !empty($info['dependencies'])) {
                    foreach ($info['dependencies'] as $dependency) {
                        // See https://www.drupal.org/node/2299747
                        $matches = [];
                        if (preg_match('/^([^:]+:)?(\S+)\s*(\(([<>]?=?)\s*([^\)]+)\))?/', $dependency, $matches)) {
                            // Matches example "project:module (>=version)":
                            //     [0] => project:module (>=version)
                            //     [1] => project:
                            //     [2] => module
                            //     [3] => (>=version)
                            //     [4] => >=
                            //     [5] => version

                            // Dependency with version constraint
                            if (!empty($matches[4]) && !empty($matches[5])) {
                                // PHP language dependency?
                                if ('php' == $matches[2]) {
                                    // Greater version dependency than Drupal 8's min?
                                    if (version_compare($matches[5], static::PHP_MIN_VER, '>')) {
                                        $requires[] = sprintf('php(language) %s %s', $matches[4], $matches[5]);
                                    }
                                // Non-PHP language dependency
                                } else {
                                    $requires[] = sprintf('drupal8(%s) %s %s', $matches[2], $matches[4], $matches[5]);
                                }
                            // Dependency without version constraint
                            } elseif ('php' != $matches[2]) {
                                $requires[] = sprintf('drupal8(%s)', $matches[2]);
                            }
                        }
                    }
                }

                break;
            }

            sort($requires);
        }

        foreach (array_unique($requires) as $req) {
            $output->writeln($req);
        }
    }
}

// Create application, add command, and run
$application = new Application('Fedora Drupal 8 RPM find requires', '__SPEC_VERSION__-__SPEC_RELEASE__');
$application->add(new FindRequires());
$application->run();