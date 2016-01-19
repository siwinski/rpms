#!/usr/bin/env php
<?php
/**
 * @license MIT
 * @author Shawn Iwinski <shawn@iwin.ski>
 */
namespace Drupal8Rpmbuild;

require_once '/usr/share/php/Symfony/Component/Console/autoload.php';

use Symfony\Component\Console\Application;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;

/**
 *
 */
class ModifyCoreComposerJson extends Command
{
    protected function configure()
    {
        $this
            ->setName('modify-core-composer-json')
            ->setDescription('Modifies core/composer.json')
            ->addOption(
                'builddir',
                null,
                InputOption::VALUE_REQUIRED,
                'RPM build dir (RPM macro "%{_builddir}")'
            )
            ->addOption(
                'phpdir',
                null,
                InputOption::VALUE_REQUIRED,
                'System PHP library directory'
            );
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $composerJsonFile = $input->getOption('builddir').'/core/composer.json';
        $this->executeDistCopy($input, $output, $composerJsonFile);
        $composerJsonDecoded = $this->executeDecode($input, $output, $composerJsonFile);

        // Empty "require", "require-dev", and "scripts"
        unset($composerJsonDecoded['require']);
        unset($composerJsonDecoded['require-dev']);
        unset($composerJsonDecoded['scripts']);

        // Modify "autoload" "files" to include de-coupled libraries' autoloaders
        $phpDir = $input->getOption('phpdir');
        $composerJsonDecoded['autoload']['files'] = array_merge(
            $composerJsonDecoded['autoload']['files'],
            array(
                $phpDir.'/Composer/Semver/autoload.php',
                $phpDir.'/Doctrine/Common/Annotations/autoload.php',
                $phpDir.'/Doctrine/Common/autoload.php',
                $phpDir.'/EasyRdf/autoload.php',
                $phpDir.'/Egulias/EmailValidator/autoload.php',
                $phpDir.'/GuzzleHttp6/autoload.php',
                $phpDir.'/Masterminds/HTML5/autoload.php',
                $phpDir.'/Stack/autoload-builder.php',
                $phpDir.'/Symfony/Bridge/PsrHttpMessage/autoload.php',
                $phpDir.'/Symfony/Cmf/Component/Routing/autoload.php',
                $phpDir.'/Symfony/Component/ClassLoader/autoload.php',
                $phpDir.'/Symfony/Component/Console/autoload.php',
                $phpDir.'/Symfony/Component/DependencyInjection/autoload.php',
                $phpDir.'/Symfony/Component/EventDispatcher/autoload.php',
                $phpDir.'/Symfony/Component/HttpFoundation/autoload.php',
                $phpDir.'/Symfony/Component/HttpKernel/autoload.php',
                $phpDir.'/Symfony/Component/Process/autoload.php',
                $phpDir.'/Symfony/Component/Routing/autoload.php',
                $phpDir.'/Symfony/Component/Serializer/autoload.php',
                $phpDir.'/Symfony/Component/Translation/autoload.php',
                $phpDir.'/Symfony/Component/Validator/autoload.php',
                $phpDir.'/Symfony/Component/Yaml/autoload.php',
                $phpDir.'/Twig/autoload.php',
                $phpDir.'/Zend/autoload.php',
                $phpDir.'/Zend/Diactoros/autoload.php',
            )
        );

        $this->executeEncode($input, $output, $composerJsonFile, $composerJsonDecoded);
    }

    protected function executeDistCopy(InputInterface $input, OutputInterface $output, $composerJsonFile)
    {
        // Copy composer.json to composer.json.dist
        $composerJsonFileDist = $composerJsonFile.'.dist';
        $output->writeln(sprintf(
          'Copying "%s" to "%s"...',
          $composerJsonFile,
          $composerJsonFileDist
        ));
        if (!copy(
            $composerJsonFile,
            $composerJsonFileDist
        )) {
            throw new \Exception(sprintf(
              'Failed to copy "%s" to "%s"',
              $composerJsonFile,
              $composerJsonFileDist
            ));
        }
    }

    protected function executeDecode(InputInterface $input, OutputInterface $output, $composerJsonFile)
    {
        // Read composer.json
        $output->writeln(sprintf('Reading "%s"...', $composerJsonFile));
        $composerJsonContents = file_get_contents($composerJsonFile);
        if (false === $composerJsonContents) {
            throw new \Exception(sprintf('Failed to read "%s"', $composerJsonFile));
        }

        // Decode composer.json
        $output->writeln(sprintf('Decoding "%s"...', $composerJsonFile));
        $composerJsonDecoded = json_decode($composerJsonContents, true);
        if (null === $composerJsonDecoded) {
            throw new \Exception(sprintf('Failed to parse "%s"', $composerJsonFile));
        }

        return $composerJsonDecoded;
    }

    protected function executeEncode(InputInterface $input, OutputInterface $output, $composerJsonFile, array $composerJsonDecoded)
    {
        // Encode composer.json contents
        $output->writeln(sprintf('Encoding "%s"...', $composerJsonFile));
        $composerJsonEncoded = json_encode($composerJsonDecoded, JSON_PRETTY_PRINT);
        if (false === $composerJsonEncoded) {
            throw new \Exception(sprintf('Failed to encode "%s"', $composerJsonFile));
        }

        // Re-write composer.json
        $output->writeln(sprintf('Writing "%s"...', $composerJsonFile));
        if (false === file_put_contents($composerJsonFile, $composerJsonEncoded)) {
            throw new \Exception(sprintf('Failed to write "%s"', $composerJsonFile));
        }
    }
}

$application = new Application();
$application->add(new ModifyCoreComposerJson());
$application->run();
