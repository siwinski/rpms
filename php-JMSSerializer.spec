%global github_owner            schmittjoh
%global github_name             serializer
%global github_version          0
%global github_commit           71388cc58d4c146136ff7e32d9691562ddd5ae99
%global github_date             20130129

%global github_release          %{github_date}git%(c=%{github_commit}; echo ${c:0:7})

# NOTE: composer.json lists 5.3.2 min
# JSON_ERROR_UTF8 usage in src/JMS/Serializer/JsonDeserializationVisitor.php
%global php_min_ver             5.3.3

%global doctrine_common_min_ver 2.0
%global doctrine_common_max_ver 3.0

%global metadata_min_ver        1.1.0
%global metadata_max_ver        1.3

%global jmsparser_min_ver       1.0
%global jmsparser_max_ver       2.0

%global phpcollection_min_ver   0.1
%global phpcollection_max_ver   0.3

%global symfony_yaml_min_ver    2.0
%global symfony_yaml_max_ver    3.0

Name:          php-JMSSerializer
Version:       %{github_version}
Release:       0.1.%{github_release}%{?dist}
Summary:       Library for (de-)serializing data of any complexity

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://jmsyst.com/libs/%{github_name}
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-Metadata >= %{metadata_min_ver}
BuildRequires: php-Metadata <  %{metadata_max_ver}
BuildRequires: php-JMSParser >= %{jmsparser_min_ver}
BuildRequires: php-JMSParser <  %{jmsparser_max_ver}
BuildRequires: php-PhpCollection >= %{phpcollection_min_ver}
BuildRequires: php-PhpCollection <  %{phpcollection_max_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineCommon) >= %{doctrine_common_min_ver}
BuildRequires: php-pear(pear.doctrine-project.org/DoctrineCommon) <  %{doctrine_common_max_ver}
#BuildRequires: php-pear(pear.doctrine-project.org/DoctrineORM) >= 2.1
#BuildRequires: php-pear(pear.doctrine-project.org/DoctrineORM) <  2.4
BuildRequires: php-pear(pear.symfony.com/Filesystem) >= 2.0
BuildRequires: php-pear(pear.symfony.com/Filesystem) <  3.0
BuildRequires: php-pear(pear.symfony.com/Form) >= 2.1
BuildRequires: php-pear(pear.symfony.com/Form) <  2.2
BuildRequires: php-pear(pear.symfony.com/Translation) >= 2.0
BuildRequires: php-pear(pear.symfony.com/Translation) <  2.2
BuildRequires: php-pear(pear.symfony.com/Validator) >= 2.0
BuildRequires: php-pear(pear.symfony.com/Validator) <  2.2
BuildRequires: php-pear(pear.symfony.com/Yaml) >= %{symfony_yaml_min_ver}
BuildRequires: php-pear(pear.symfony.com/Yaml) <  %{symfony_yaml_max_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig) >= 1.8
BuildRequires: php-pear(pear.twig-project.org/Twig) <  2.0
# Test build requires: phpci
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl

Requires:      php-common >= %{php_min_ver}
Requires:      php-Metadata >= %{metadata_min_ver}
Requires:      php-Metadata <  %{metadata_max_ver}
Requires:      php-JMSParser >= %{jmsparser_min_ver}
Requires:      php-JMSParser <  %{jmsparser_max_ver}
Requires:      php-PhpCollection >= %{phpcollection_min_ver}
Requires:      php-PhpCollection <  %{phpcollection_max_ver}
Requires:      php-pear(pear.doctrine-project.org/DoctrineCommon) >= %{doctrine_common_min_ver}
Requires:      php-pear(pear.doctrine-project.org/DoctrineCommon) <  %{doctrine_common_max_ver}
# phpci requires
Requires:      php-date
Requires:      php-dom
Requires:      php-json
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
# Optional
Requires:      php-pear(pear.symfony.com/Yaml) >= %{symfony_yaml_min_ver}
Requires:      php-pear(pear.symfony.com/Yaml) <  %{symfony_yaml_max_ver}

%description
This library allows you to (de-)serialize data of any complexity. Currently, it
supports XML, JSON, and YAML.

It also provides you with a rich tool-set to adapt the output to your specific needs.

Built-in features include:
* (De-)serialize data of any complexity; circular references are handled gracefully.
*Supports many built-in PHP types (such as dates)
* Integrates with Doctrine ORM, et. al.
* Supports versioning, e.g. for APIs
* Configurable via PHP, XML, YAML, or Doctrine Annotations


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Update and move PHPUnit config
sed 's:\.\?/\?tests/:./:' -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Overwrite tests/bootstrap.php
mv tests/bootstrap.php tests/bootstrap.php.dist
( cat <<'AUTOLOAD'
<?php
use Doctrine\Common\Annotations\AnnotationRegistry;

call_user_func(function() {
    spl_autoload_register(function ($class) {
        $src = str_replace('\\', '/', $class).'.php';
        @include_once $src;
    });

    AnnotationRegistry::registerLoader('class_exists');
});
AUTOLOAD
) > tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/JMS
cp -rp src/JMS/Serializer %{buildroot}%{_datadir}/php/JMS/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%check
# TODO
#%{_bindir}/phpunit \
#    -d include_path="./src:./tests:.:%{pear_phpdir}:%{_datadir}/php" \
#    -c tests/phpunit.xml.dist


%files
%doc LICENSE README.md composer.json
%dir %{_datadir}/php/JMS
     %{_datadir}/php/JMS/Serializer

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Fri Feb 01 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0-0.1.20130129git71388cc
- Initial package
