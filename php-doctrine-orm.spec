%global github_owner   doctrine
%global github_name    doctrine2
%global github_version 2.4.1
%global github_commit  84373d05a4198ec380918d535abf83c454c3867f

# "php": ">=5.3.2"
%global php_min_ver         5.3.2
# "doctrine/collections": "~1.1"
%global collections_min_ver 1.1
%global collections_max_ver 2.0
# "doctrine/dbal": "~2.4"
%global dbal_min_ver        2.4
%global dbal_max_ver        3.0
# "symfony/console": "~2.0"
# "symfony/yaml": "~2.1"
%global symfony_min_ver     2.1
%global symfony_max_ver     3.0

Name:      php-%{github_owner}-orm
Version:   %{github_version}
Release:   1%{dist}
Summary:   Doctrine Object-Relational-Mapper (ORM)

Group:     Development/Libraries
License:   MIT
URL:       http://www.doctrine-project.org/projects/orm.html
Source0:   https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch

Requires:  php(language)            >= %{php_min_ver}
Requires:  php-doctrine-collections >= %{collections_min_ver}
Requires:  php-doctrine-collections <  %{collections_max_ver}
Requires:  php-doctrine-dbal        >= %{dbal_min_ver}
Requires:  php-doctrine-dbal        <  %{dbal_max_ver}
Requires:  php-symfony-console      >= %{symfony_min_ver}
Requires:  php-symfony-console      <  %{symfony_max_ver}
Requires:  php-symfony-yaml         >= %{symfony_min_ver}
Requires:  php-symfony-yaml         <  %{symfony_max_ver}
# phpcompatinfo (computed from v2.4.1)
Requires:  php-ctype
Requires:  php-dom
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-reflection
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-tokenizer

# PEAR
Provides:  php-pear(pear.doctrine-project.org/DoctrineORM) = %{version}
# Rename
Obsoletes: php-doctrine-DoctrineORM < %{version}
Provides:  php-doctrine-DoctrineORM = %{version}

%description
Object relational mapper (ORM) for PHP that sits on top of a powerful database
abstraction layer (DBAL). One of its' key features is the option to write
database queries in a proprietary object oriented SQL dialect called Doctrine
Query Language (DQL), inspired by Hibernate's HQL. This provides developers
with a powerful alternative to SQL that maintains flexibility without requiring
unnecessary code duplication.

Optional caches (see Doctrine\ORM\Tools\Setup::createConfiguration()):
* php-doctrine-cache-apc
* php-doctrine-cache-memcache
* php-doctrine-cache-redis
* php-doctrine-cache-xcache


%prep
%setup -q -n %{github_name}-%{github_commit}

# Make a single executable
echo '#!%{_bindir}/php' > bin/doctrine
cat bin/doctrine.php \
    |  sed "/autoload.php/s#.*#spl_autoload_register(function (\$class) {\n    \$src = str_replace('\\\\\\\', '/', \$class).'.php';\n    @include_once \$src;\n});#" \
    >> bin/doctrine
chmod +x bin/doctrine

%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/Doctrine %{buildroot}/%{_datadir}/php/

mkdir -p %{buildroot}/%{_bindir}
cp -p bin/doctrine %{buildroot}/%{_bindir}/


%check
# No upstream tests provided in source


%files
%doc LICENSE *.md *.markdown composer.json
%{_datadir}/php/Doctrine/ORM
%{_bindir}/doctrine


%changelog
* Sat Dec 28 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.1-1
- Initial package
