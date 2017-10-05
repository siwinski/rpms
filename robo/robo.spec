#
# Fedora spec file for robo
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     consolidation
%global github_name      Robo
%global github_version   1.1.3
%global github_commit    21370cc6fea83729ab6d903f8f382389b14ae90c

%global composer_vendor  consolidation
%global composer_project robo

# "php": ">=5.5.0"
%global php_min_ver 5.5.0
# "codeception/aspect-mock": "~1"
%global codeception_aspect_mock_min_ver 1.0
%global codeception_aspect_mock_max_ver 2.0
# "codeception/base": "^2.2.6"
%global codeception_base_min_ver 2.2.6
%global codeception_base_max_ver 3.0
# "codeception/verify": "^0.3.2"
%global codeception_verify_min_ver 0.3.2
%global codeception_verify_max_ver 1.0
# "consolidation/annotated-command": "^2.2"
%global consolidation_annotated_command_min_ver 2.2
%global consolidation_annotated_command_max_ver 3.0
# "consolidation/config": "^1.0.1"
%global consolidation_config_min_ver 1.0.1
%global consolidation_config_max_ver 2.0
# "consolidation/log": "~1"
%global consolidation_log_min_ver 1.0
%global consolidation_log_max_ver 2.0
# "consolidation/output-formatters": "^3.1.5"
%global consolidation_output_formatters_min_ver 3.1.5
%global consolidation_output_formatters_max_ver 4.0
# "henrikbjorn/lurker": "~1"
%global henrikbjorn_lurker_min_ver 1.0
%global henrikbjorn_lurker_max_ver 2.0
# "league/container": "^2.2"
%global league_container_min_ver 2.2
%global league_container_max_ver 3.0
# "natxet/CssMin": "~3"
%global natxet_cssmin_min_ver 3.0
%global natxet_cssmin_max_ver 4.0
# "patchwork/jsqueeze": "~2"
%global patchwork_jsqueeze_min_ver 2.0
%global patchwork_jsqueeze_max_ver 3.0
# "pear/archive_tar": "^1.4.2"
%global pear_archive_tar_min_ver 1.4.2
%global pear_archive_tar_max_ver 2.0
# "phpunit/php-code-coverage": "~2|~4"
%global phpunit_php_code_coverage_min_ver 2
%global phpunit_php_code_coverage_max_ver 5
# "symfony/console": "~2.8|~3.0"
# "symfony/event-dispatcher": "~2.5|~3.0
# "symfony/filesystem": "~2.5|~3.0"
# "symfony/finder": "~2.5|~3.0"
# "symfony/process": "~2.5|~3.0"
%global symfony_min_ver 2.8
%global symfony_max_ver 4.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          robo
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Modern task runner

Group:         Development/Libraries
License:       MIT
URL:           http://robo.li
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
#BuildRequires: php-composer(codeception/aspect-mock) <  %{codeception_aspect_mock_max_ver}
#BuildRequires: php-composer(codeception/aspect-mock) >= %{codeception_aspect_mock_min_ver}
#BuildRequires: php-composer(codeception/base) <  %{codeception_base_max_ver}
#BuildRequires: php-composer(codeception/base) >= %{codeception_base_min_ver}
#BuildRequires: php-composer(codeception/verify) <  %{codeception_verify_max_ver}
#BuildRequires: php-composer(codeception/verify) >= %{codeception_verify_min_ver}
BuildRequires: php-composer(consolidation/annotated-command) <  %{consolidation_annotated_command_max_ver}
BuildRequires: php-composer(consolidation/annotated-command) >= %{consolidation_annotated_command_min_ver}
BuildRequires: php-composer(consolidation/config) <  %{consolidation_config_max_ver}
BuildRequires: php-composer(consolidation/config) >= %{consolidation_config_min_ver}
BuildRequires: php-composer(consolidation/log) <  %{consolidation_log_max_ver}
BuildRequires: php-composer(consolidation/log) >= %{consolidation_log_min_ver}
BuildRequires: php-composer(consolidation/output-formatters) <  %{consolidation_output_formatters_max_ver}
BuildRequires: php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver}
BuildRequires: php-composer(henrikbjorn/lurker) <  %{henrikbjorn_lurker_max_ver}
BuildRequires: php-composer(henrikbjorn/lurker) >= %{henrikbjorn_lurker_min_ver}
BuildRequires: php-composer(league/container) <  %{league_container_max_ver}
BuildRequires: php-composer(league/container) >= %{league_container_min_ver}
BuildRequires: php-composer(natxet/CssMin) <  %{natxet_cssmin_max_ver}
BuildRequires: php-composer(natxet/CssMin) >= %{natxet_cssmin_min_ver}
BuildRequires: php-composer(patchwork/jsqueeze) <  %{patchwork_jsqueeze_max_ver}
BuildRequires: php-composer(patchwork/jsqueeze) >= %{patchwork_jsqueeze_min_ver}
BuildRequires: php-composer(pear/archive_tar) <  %{pear_archive_tar_max_ver}
BuildRequires: php-composer(pear/archive_tar) >= %{pear_archive_tar_min_ver}
BuildRequires: php-composer(phpunit/php-code-coverage) <  %{phpunit_php_code_coverage_max_ver}
BuildRequires: php-composer(phpunit/php-code-coverage) >= %{phpunit_php_code_coverage_min_ver}
BuildRequires: php-composer(symfony/console) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/console) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/filesystem) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/filesystem) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/finder) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder) >= %{symfony_min_ver}
BuildRequires: php-composer(symfony/process) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/process) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.1.3)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-fileinfo
BuildRequires: php-json
BuildRequires: php-pcntl
BuildRequires: php-pcre
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer
BuildRequires: php-zip
BuildRequires: php-zlib
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(consolidation/annotated-command) <  %{consolidation_annotated_command_max_ver}
Requires:      php-composer(consolidation/annotated-command) >= %{consolidation_annotated_command_min_ver}
Requires:      php-composer(consolidation/config) <  %{consolidation_config_max_ver}
Requires:      php-composer(consolidation/config) >= %{consolidation_config_min_ver}
Requires:      php-composer(consolidation/log) <  %{consolidation_log_max_ver}
Requires:      php-composer(consolidation/log) >= %{consolidation_log_min_ver}
Requires:      php-composer(consolidation/output-formatters) <  %{consolidation_output_formatters_max_ver}
Requires:      php-composer(consolidation/output-formatters) >= %{consolidation_output_formatters_min_ver}
Requires:      php-composer(league/container) <  %{league_container_max_ver}
Requires:      php-composer(league/container) >= %{league_container_min_ver}
Requires:      php-composer(symfony/console) <  %{symfony_max_ver}
Requires:      php-composer(symfony/console) >= %{symfony_min_ver}
Requires:      php-composer(symfony/event-dispatcher) <  %{symfony_max_ver}
Requires:      php-composer(symfony/event-dispatcher) >= %{symfony_min_ver}
Requires:      php-composer(symfony/filesystem) <  %{symfony_max_ver}
Requires:      php-composer(symfony/filesystem) >= %{symfony_min_ver}
Requires:      php-composer(symfony/finder) <  %{symfony_max_ver}
Requires:      php-composer(symfony/finder) >= %{symfony_min_ver}
Requires:      php-composer(symfony/process) <  %{symfony_max_ver}
Requires:      php-composer(symfony/process) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 1.1.3)
Requires:      php-curl
Requires:      php-date
Requires:      php-fileinfo
Requires:      php-json
Requires:      php-pcntl
Requires:      php-pcre
Requires:      php-posix
Requires:      php-reflection
Requires:      php-spl
Requires:      php-tokenizer
Requires:      php-zip
Requires:      php-zlib
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Weak dependencies
## composer.json: suggest
Suggests:      php-composer(henrikbjorn/lurker) <  %{henrikbjorn_lurker_max_ver}
Suggests:      php-composer(henrikbjorn/lurker) >= %{henrikbjorn_lurker_min_ver}
Suggests:      php-composer(natxet/CssMin) <  %{natxet_cssmin_max_ver}
Suggests:      php-composer(natxet/CssMin) >= %{natxet_cssmin_min_ver}
Suggests:      php-composer(patchwork/jsqueeze) <  %{patchwork_jsqueeze_max_ver}
Suggests:      php-composer(patchwork/jsqueeze) >= %{patchwork_jsqueeze_min_ver}
Suggests:      php-composer(pear/archive_tar) <  %{pear_archive_tar_max_ver}
Suggests:      php-composer(pear/archive_tar) >= %{pear_archive_tar_min_ver}

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# Standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}

%description
Robo is a task runner you always have been looking for. It allows you to write
fully customizable tasks in common OOP PHP style. Robo has comprehensive list
of built-in common tasks for development, testing, and deployment.

Use Robo to:
* automate your common tasks
* start workers
* run parallel tasks
* execute commands
* run tests
* watch filesystem changes


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Robo\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/League/Container/autoload.php',
    '%{phpdir}/Consolidation/AnnotatedCommand/autoload.php',
    '%{phpdir}/Consolidation/OutputFormatters/autoload.php',
    '%{phpdir}/Consolidation/Log/autoload.php',
    '%{phpdir}/Consolidation/Config/autoload.php',
    [
        '%{phpdir}/Symfony3/Component/Finder/autoload.php',
        '%{phpdir}/Symfony/Component/Finder/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Console/autoload.php',
        '%{phpdir}/Symfony/Component/Console/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Process/autoload.php',
        '%{phpdir}/Symfony/Component/Process/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/Filesystem/autoload.php',
        '%{phpdir}/Symfony/Component/Filesystem/autoload.php',
    ],
    [
        '%{phpdir}/Symfony3/Component/EventDispatcher/autoload.php',
        '%{phpdir}/Symfony/Component/EventDispatcher/autoload.php',
    ],
]);

// @todo Archive Tar

\Fedora\Autoloader\Dependencies::optional([
    '%{phpdir}/Lurker/autoload.php',
    '%{phpdir}/Patchwork/autoload-jsqueeze.php',
    '%{phpdir}/natxet/CssMin/autoload.php',
]);
AUTOLOAD


%install
: Library
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/Robo

: Bin
mkdir -p %{buildroot}%{_bindir}
install -m 0755 robo %{buildroot}%{_bindir}/%{name}


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/consolidation/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Robo\\', __DIR__.'/tests/src');

\Fedora\Autoloader\Dependencies::required([
    // codeception/base
    // codeception/verify
    // codeception/aspect-mock
]);
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        echo "***** SKIP TESTS FOR NOW *****"
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%doc docs
# Library
%{phpdir}/Robo
# Bin
%{_bindir}/%{name}


%changelog
* Thu Oct 05 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.3-1
- Initial package
