%global github_owner    doctrine
%global github_name     dbal
%global github_version  2.4.1
%global github_commit   328357bd9eea9d671fe5fff0737f01953bfe66a0

# "php": ">=5.3.2"
%global php_min_ver             5.3.2
# "doctrine/common": "~2.4"
%global doctrine_common_min_ver 2.4
%global doctrine_common_max_ver 3.0
# "symfony/console": "~2.0"
%global symfony_console_min_ver 2.0
%global symfony_console_max_ver 3.0

Name:      php-%{github_owner}-%{github_name}
Version:   %{github_version}
Release:   1%{dist}
Summary:   Doctrine Database Abstraction Layer (DBAL)

Group:     Development/Libraries
License:   MIT
URL:       http://www.doctrine-project.org/projects/dbal.html
Source0:   https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Patches required for OwnCloud 6.0.0a.
#
# Changes to test files have been removed because they are not provided in source.
#
# "Don't add 'NOT NULL' to the 'ALTER TABLE' when that hasn't changed"
# https://github.com/doctrine/dbal/commit/eee502c9ef34322c12607dafb4e1ef1ee8ea8daa
Patch0:    %{name}-eee502c9ef34322c12607dafb4e1ef1ee8ea8daa.patch
# "Add primary key to 'ALTER TABLE' in MySql"
# https://github.com/doctrine/dbal/commit/69b377bbbf61ec97163579e7c28ea47521fc1fad
Patch1:    %{name}-69b377bbbf61ec97163579e7c28ea47521fc1fad.patch
# "When changing from a non-primary index to a primary index, the droppe..."
# https://github.com/doctrine/dbal/commit/075c68b7518e27d46d7f700a1d42ebf43f6ebdfd
Patch2:    %{name}-075c68b7518e27d46d7f700a1d42ebf43f6ebdfd.patch

BuildArch: noarch

Requires:  php(language)       >= %{php_min_ver}
Requires:  php-doctrine-common >= %{doctrine_common_min_ver}
Requires:  php-doctrine-common <  %{doctrine_common_max_ver}
Requires:  php-symfony-console >= %{symfony_console_min_ver}
Requires:  php-symfony-console <  %{symfony_console_max_ver}
# phpcompatinfo (computed from v2.4.1)
Requires:  php-date
Requires:  php-json
Requires:  php-pcre
Requires:  php-pdo
Requires:  php-spl

# PEAR
Provides:  php-pear(pear.doctrine-project.org/DoctrineDBAL) = %{version}
# Rename
Obsoletes: php-doctrine-DoctrineDBAL < %{version}
Provides:  php-doctrine-DoctrineDBAL = %{version}

%description
The Doctrine database abstraction & access layer (DBAL) offers a lightweight
and thin runtime layer around a PDO-like API and a lot of additional, horizontal
features like database schema introspection and manipulation through an OO API.

The fact that the Doctrine DBAL abstracts the concrete PDO API away through the
use of interfaces that closely resemble the existing PDO API makes it possible
to implement custom drivers that may use existing native or self-made APIs. For
example, the DBAL ships with a driver for Oracle databases that uses the oci8
extension under the hood.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Apply patches
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Make a single executable
echo '#!%{_bindir}/php' > bin/doctrine-dbal
cat bin/doctrine-dbal.php \
    |  sed 's#Doctrine/Common/ClassLoader.php#%{_datadir}/php/Doctrine/Common/ClassLoader.php#' \
    >> bin/doctrine-dbal
chmod +x bin/doctrine-dbal

# Remove empty file
rm -f lib/Doctrine/DBAL/README.markdown

# Remove executable bits
chmod a-x \
    lib/Doctrine/DBAL/Types/JsonArrayType.php \
    lib/Doctrine/DBAL/Types/SimpleArrayType.php


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/Doctrine %{buildroot}/%{_datadir}/php/

mkdir -p %{buildroot}/%{_bindir}
cp -p bin/doctrine-dbal %{buildroot}/%{_bindir}/


%check
# No upstream tests provided in source


%files
%doc LICENSE *.md UPGRADE composer.json
%{_datadir}/php/Doctrine/DBAL
%{_bindir}/doctrine-dbal


%changelog
* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4.1-1
- Initial package
