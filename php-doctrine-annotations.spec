%global github_owner   doctrine
%global github_name    annotations
%global github_version 1.1.2
%global github_commit  a11349d39d85bef75a71bd69bd604ac4fb993f03
# Additional commits after v1.1.2 tag
%global github_release 20131220git%(c=%{github_commit}; echo ${c:0:7})

# "php": ">=5.3.2"
%global php_min_ver    5.3.2
# "doctrine/cache": "1.*"
%global cache_min_ver  1.0
%global cache_max_ver  2.0
# "doctrine/lexer": "1.*"
%global lexer_min_ver  1.0
%global lexer_max_ver  2.0

Name:          php-%{github_owner}-%{github_name}
Version:       %{github_version}
Release:       1.%{github_release}%{dist}
Summary:       PHP docblock annotations parser library

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language)      >= %{php_min_ver}
BuildRequires: php-doctrine-cache >= %{cache_min_ver}
BuildRequires: php-doctrine-cache <  %{cache_max_ver}
BuildRequires: php-doctrine-lexer >= %{lexer_min_ver}
BuildRequires: php-doctrine-lexer <  %{lexer_max_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from v1.1.2 git commit a11349d39d85bef75a71bd69bd604ac4fb993f03)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-tokenizer

Requires:      php(language)      >= %{php_min_ver}
Requires:      php-doctrine-lexer >= %{lexer_min_ver}
Requires:      php-doctrine-lexer <  %{lexer_max_ver}
# phpcompatinfo (computed from v1.1.2 git commit a11349d39d85bef75a71bd69bd604ac4fb993f03)
Requires:      php-ctype
Requires:      php-date
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
Requires:      php-tokenizer

%description
%{summary} (extracted from Doctrine Common).


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/* %{buildroot}/%{_datadir}/php/


%check
# Create tests' init
( cat <<'TESTINIT'
<?php
namespace Doctrine\Tests;

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});

\Doctrine\Common\Annotations\AnnotationRegistry::registerAutoloadNamespace(
    'Doctrine\Tests\Common\Annotations\Fixtures', __DIR__ . '/../../'
);
TESTINIT
) > tests/Doctrine/Tests/TestInit.php

# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

%{_bindir}/phpunit --include-path ./lib:./tests -d date.timezone="UTC"


%files
%doc LICENSE *.md composer.json
%{_datadir}/php/Doctrine/Common/Annotations


%changelog
* Mon Dec 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.2-1.20131220gita11349d
- Initial package
