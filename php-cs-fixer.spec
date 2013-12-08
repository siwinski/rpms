%global github_owner    fabpot
%global github_name     PHP-CS-Fixer
%global github_version  0.3.0
%global github_commit   2910b9664f64d8f01341049e58615e86723fd42e
# There are commits after the 0.3.0 version tag
%global github_release  20131207git%(c=%{github_commit}; echo ${c:0:7})

# NOTE: composer.json not updated after https://github.com/fabpot/PHP-CS-Fixer/pull/258
%global php_min_ver     5.3.3
# "sebastian/diff": "1.1.*"
%global diff_min_ver    1.1.0
%global diff_max_ver    1.2.0
# "symfony/*": "~2.1"
%global symfony_min_ver 2.1.0
%global symfony_max_ver 3.0.0

%global symfony_dir     %{_datadir}/php/Symfony

Name:          php-cs-fixer
Version:       %{github_version}
Release:       1.%{github_release}%{dist}
Summary:       PHP Coding Standards Fixer

Group:         Development/Libraries
License:       MIT
URL:           http://cs.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language)                  >= %{php_min_ver}
BuildRequires: php-symfony-console            >= %{symfony_min_ver}
BuildRequires: php-symfony-console            <  %{symfony_max_ver}
BuildRequires: php-symfony-filesystem         >= %{symfony_min_ver}
BuildRequires: php-symfony-filesystem         <  %{symfony_max_ver}
BuildRequires: php-symfony-finder             >= %{symfony_min_ver}
BuildRequires: php-symfony-finder             <  %{symfony_max_ver}
BuildRequires: php-pear(pear.phpunit.de/Diff) >= %{diff_min_ver}
BuildRequires: php-pear(pear.phpunit.de/Diff) <  %{diff_max_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo
BuildRequires: php-dom
BuildRequires: php-pcre
BuildRequires: php-spl

Requires:      php(language)                  >= %{php_min_ver}
Requires:      php-symfony-console            >= %{symfony_min_ver}
Requires:      php-symfony-console            <  %{symfony_max_ver}
Requires:      php-symfony-filesystem         >= %{symfony_min_ver}
Requires:      php-symfony-filesystem         <  %{symfony_max_ver}
Requires:      php-symfony-finder             >= %{symfony_min_ver}
Requires:      php-symfony-finder             <  %{symfony_max_ver}
Requires:      php-pear(pear.phpunit.de/Diff) >= %{diff_min_ver}
Requires:      php-pear(pear.phpunit.de/Diff) <  %{diff_max_ver}
# phpcompatinfo
Requires:      php-dom
Requires:      php-pcre
Requires:      php-spl

%description
The PHP Coding Standards Fixer tool fixes most issues in your code when you want
to follow the PHP coding standards as defined in the PSR-1 and PSR-2 documents.

If you are already using PHP_CodeSniffer to identify coding standards problems
in your code, you know that fixing them by hand is tedious, especially on large
projects. This tool does the job for you.

NOTE: The "compile" and "self-update" commands have been removed.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Remove compile command
rm -f Symfony/CS/Console/Command/CompileCommand.php
sed -i '/CompileCommand/d' Symfony/CS/Console/Application.php

# Remove self-update command
rm -f Symfony/CS/Console/Command/SelfUpdateCommand.php
sed -i '/SelfUpdateCommand/d' Symfony/CS/Console/Application.php

# Rewrite bin
( cat <<'BIN'
#!%{_bindir}/php
<?php

/*
 * This file is part of the Symfony CS utility.
 *
 * (c) Fabien Potencier <fabien@symfony.com>
 *
 * This source file is subject to the MIT license that is bundled
 * with this source code in the file LICENSE.
 */

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});

use Symfony\CS\Console\Application;

$application = new Application();
$application->run();
BIN
) > php-cs-fixer


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{symfony_dir}
cp -rp Symfony/CS %{buildroot}/%{symfony_dir}/

mkdir -p %{buildroot}/%{_bindir}
cp php-cs-fixer %{buildroot}/%{_bindir}/


%check
# Create tests' bootstrap
mkdir vendor
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > vendor/autoload.php

# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

%{_bindir}/phpunit \
    -d date.timezone="UTC"


%files
%doc LICENSE README* composer.json
%{symfony_dir}/CS
%exclude %{symfony_dir}/CS/Tests
%{_bindir}/php-cs-fixer


%changelog
* Sun Dec 08 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.0-1.20131207git2910b96
- Initial package
