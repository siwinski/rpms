%global github_owner   sdboyer
%global github_name    gliph
%global github_version 0.1.4
%global github_commit  8da23c6397354e9acc7a7e6f8d2a782fdf21ab54
%global github_date    20131024
%global github_release %{github_date}git%(c=%{github_commit}; echo ${c:0:7})

%global lib_name       Gliph
%global php_min_ver    5.3.0

Name:          php-%{github_name}
Version:       %{github_version}
Release:       1.%{github_release}%{?dist}
Summary:       A graph library for PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) >= 3.7.0
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) <  3.8.0
# For tests: phpcompatinfo
BuildRequires: php-reflection
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo
Requires:      php-spl

%description
Gliph is a graph library for PHP. It provides graph building blocks and
data structures for use by other PHP applications. It is (currently) designed
for use with in-memory graphs, not for interaction with a graph database like
Neo4J (http://neo4j.org/).


%prep
%setup -q -n %{github_name}-%{github_commit}

# Create PHPUnit bootstrap for tests
( cat <<'BOOTSTRAP'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
BOOTSTRAP
) > bootstrap.php

# Create phpunit.xml with updated PHPUnit bootstrap and no colors
cat phpunit.xml.dist | \
    sed -e 's#tests/bootstrap.php#bootstrap.php#' \
        -e 's#colors="true"#colors="false"#' > \
    phpunit.xml


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/


%check
%{_bindir}/phpunit -d include_path="./src:./tests:.:%{pear_phpdir}"


%files
%doc LICENSE README.md composer.json
%{_datadir}/php/%{lib_name}


%changelog
* Thu Oct 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.1.4-1.20131024git8da23c6
- Updated to latest snapshot (commit 8da23c6397354e9acc7a7e6f8d2a782fdf21ab54)
  which includes LICENSE
- "php-common" -> "php(language)"
- Added PHPUnit min/max versions

* Wed Oct 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.1.4-1
- Initial package
