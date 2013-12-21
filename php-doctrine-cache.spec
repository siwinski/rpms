%global github_owner    doctrine
%global github_name     cache
%global github_version  1.3.0
%global github_commit   e16d7adf45664a50fa86f515b6d5e7f670130449

# "php": ">=5.3.2"
%global php_min_ver     5.3.2
# "phpunit/phpunit": ">=3.7"
%global phpunit_min_ver 3.7

%global summary_base    Doctrine Cache

Name:          php-%{github_owner}-%{github_name}
Version:       %{github_version}
Release:       1%{dist}
Summary:       %{summary_base}

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) >= %{phpunit_min_ver}
# For tests: phpcompatinfo (computed from v1.3.0)
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from git commit v1.3.0)
Requires:      php-date
Requires:      php-hash
Requires:      php-pcre
Requires:      php-spl

Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
Cache component extracted from the Doctrine Common project.

Additional handlers:
* APC:       %{name}-apc
* Couchbase: http://pecl.php.net/package/couchbase
* Memcache:  %{name}-memcache
* Memcached: %{name}-memcached
* MongoDB:   %{name}-mongo
* Redis:     %{name}-redis
* Riak:      http://pecl.php.net/package/riak
* XCache:    %{name}-xcache

# ------------------------------------------------------------------------------

%package  apc

Summary:  %{summary_base} - APC handler

Requires: %{name} = %{version}-%{release}
Requires: php-pecl(APC)

%description apc
%{summary_base} - APC handler

# ------------------------------------------------------------------------------

%package  memcache

Summary:  %{summary_base} - Memcache handler

Requires: %{name} = %{version}-%{release}
Requires: php-pecl(memcache)

%description memcache
%{summary_base} - Memcache handle

# ------------------------------------------------------------------------------

%package  memcached

Summary:  %{summary_base} - Memcached handler

Requires: %{name} = %{version}-%{release}
Requires: php-pecl(memcached)

%description memcached
%{summary_base} - Memcached handler

# ------------------------------------------------------------------------------

%package  mongo

Summary:  %{summary_base} - MongoDB handler

Requires: %{name} = %{version}-%{release}
Requires: php-pecl(mongo)

%description mongo
%{summary_base} - MongoDB handler

# ------------------------------------------------------------------------------

%package  redis

Summary:  %{summary_base} - Redis handler

Requires: %{name} = %{version}-%{release}
Requires: php-pecl(redis)

%description redis
%{summary_base} - Redis handler

# ------------------------------------------------------------------------------

%package  xcache

Summary:  %{summary_base} - XCache handler

Requires: %{name} = %{version}-%{release}
Requires: php-xcache

%description xcache
%{summary_base} - XCache handler


# ##############################################################################


%prep
%setup -q -n %{github_name}-%{github_commit}

# Remove files that will never be used
find . -name '*WinCache*' -delete
find . -name '*ZendDataCache*' -delete


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/* %{buildroot}/%{_datadir}/php/


%check
# Create tests' init
( cat <<'AUTOLOAD'
<?php
namespace Doctrine\Tests;

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > tests/Doctrine/Tests/TestInit.php

# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

# Skip tests known to fail
rm -f tests/Doctrine/Tests/Common/Cache/MongoDBCacheTest.php

%{_bindir}/phpunit --include-path ./lib:./tests -d date.timezone="UTC"


# ##############################################################################


%files
%doc LICENSE *.md composer.json
%dir %{_datadir}/php/Doctrine
%dir %{_datadir}/php/Doctrine/Common
     %{_datadir}/php/Doctrine/Common/Cache
%exclude %{_datadir}/php/Doctrine/Common/Cache/ApcCache.php
%exclude %{_datadir}/php/Doctrine/Common/Cache/MemcacheCache.php
%exclude %{_datadir}/php/Doctrine/Common/Cache/MemcachedCache.php
%exclude %{_datadir}/php/Doctrine/Common/Cache/MongoDBCache.php
%exclude %{_datadir}/php/Doctrine/Common/Cache/RedisCache.php
%exclude %{_datadir}/php/Doctrine/Common/Cache/XcacheCache.php

# ------------------------------------------------------------------------------

%files apc
%{_datadir}/php/Doctrine/Common/Cache/ApcCache.php

# ------------------------------------------------------------------------------

%files memcache
%{_datadir}/php/Doctrine/Common/Cache/MemcacheCache.php

# ------------------------------------------------------------------------------

%files memcached
%{_datadir}/php/Doctrine/Common/Cache/MemcachedCache.php

# ------------------------------------------------------------------------------

%files mongo
%{_datadir}/php/Doctrine/Common/Cache/MongoDBCache.php

# ------------------------------------------------------------------------------

%files redis
%{_datadir}/php/Doctrine/Common/Cache/RedisCache.php

# ------------------------------------------------------------------------------

%files xcache
%{_datadir}/php/Doctrine/Common/Cache/XcacheCache.php

# ##############################################################################

%changelog
* Fri Dec 20 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.3.0-1
- Initial package
