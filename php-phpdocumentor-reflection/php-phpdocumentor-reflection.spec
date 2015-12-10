#
# Fedora spec file for php-phpdocumentor-reflection
#
# Copyright (c) 2015 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      Reflection
%global github_version   1.0.7
%global github_commit    fc40c3f604ac2287eb5c314174d5109b2c699372

%global composer_vendor  phpdocumentor
%global composer_project reflection

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.0-8
%global psr_log_max_ver 2.0
# "nikic/php-parser": "~0.9.4"
%global php_parser_min_ver 0.9.4
%global php_parser_max_ver 1.0
# "phpdocumentor/reflection-docblock": "~2.0"
%global reflection_docblock_min_ver 2.0
%global reflection_docblock_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common reflection classes used by phpdocumentor to reflect the code structure

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language)                                   >= %{php_min_ver}
BuildRequires: php-composer(mockery/mockery)
BuildRequires: php-composer(nikic/php-parser)                  >= %{php_parser_min_ver}
BuildRequires: php-composer(phpdocumentor/reflection-docblock) >= %{reflection_docblock_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
#BuildRequires: php-composer(psr/log)                           >= %%{psr_log_min_ver}
BuildRequires: php-PsrLog                                      >= %{psr_log_min_ver}
## phpcompatinfo (computed from version 1.0.7)
BuildRequires: php-iconv
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(symfony/class-loader)
%endif

# composer.json
Requires:      php(language)                                   >= %{php_min_ver}
Requires:      php-composer(nikic/php-parser)                  >= %{php_parser_min_ver}
Requires:      php-composer(nikic/php-parser)                  <  %{php_parser_max_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) >= %{reflection_docblock_min_ver}
Requires:      php-composer(phpdocumentor/reflection-docblock) <  %{reflection_docblock_max_ver}
Requires:      php-composer(psr/log)                           >= %{psr_log_min_ver}
Requires:      php-composer(psr/log)                           <  %{psr_log_max_ver}
# phpcompatinfo (computed from version 1.0.7)
Requires:      php-iconv
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/phpDocumentor/Reflection/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/phpDocumentor/Reflection/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('phpDocumentor\\Reflection\\', dirname(dirname(__DIR__)));

// Required dependencies
require_once '%{phpdir}/phpDocumentor/Reflection/DocBlock/autoload.php';
require_once '%{phpdir}/PhpParser/autoload.php';
require_once '%{phpdir}/Psr/Log/autoload.php';

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/* %{buildroot}%{phpdir}/


%check
%if %{with_tests}
find %{buildroot}%{phpdir}/ | sed 's#%{buildroot}##' | sort

: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
$fedoraClassLoader =
    require '%{buildroot}%{phpdir}/phpDocumentor/Reflection/autoload.php';
$fedoraClassLoader->addPrefix('phpDocumentor\\Reflection\\', array(
    __DIR__ . '/tests/mocks',
    __DIR__ . '/tests/unit',
));
print_r($fedoraClassLoader);

require_once '%{phpdir}/Mockery/autoload.php';
BOOTSTRAP

: Modify Mockery path
sed 's#vendor/mockery/mockery/library#%{phpdir}#' \
    phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --verbose --bootstrap bootstrap.php
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/phpDocumentor/
     %{phpdir}/phpDocumentor/Reflection/


%changelog
* Wed Dec 09 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.7-1
- Initial package
