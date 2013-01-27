# Tests are only run with rpmbuild --with tests
# "PHP Fatal error: Call to undefined function phpunit_mockobject_autoload()"
%global with_tests %{?_with_tests:1}%{!?_with_tests:0}

# phpci false positive for 5.3.3 because usage of JSON_ERROR_* constants in
# lib/EasyRdf/Parser/Json.php are conditional
%global php_min_ver 5.2.8

Name:          php-EasyRdf
Version:       0.7.2
Release:       1%{?dist}
Summary:       A PHP library designed to make it easy to consume and produce RDF

Group:         Development/Libraries
License:       BSD
URL:           http://www.easyrdf.org
Source0:       %{url}/downloads/easyrdf-%{version}.tar.gz

BuildArch:     noarch
%if %{with_tests}
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# phpci
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-redland
BuildRequires: php-spl
BuildRequires: php-xml
%endif

Requires:      php-common >= %{php_min_ver}
# phpci requires
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-json
Requires:      php-pcre
Requires:      php-redland
Requires:      php-spl
Requires:      php-xml

%description
EasyRdf is a PHP library designed to make it easy to consume and produce RDF
(http://en.wikipedia.org/wiki/Resource_Description_Framework). It was designed
for use in mixed teams of experienced and inexperienced RDF developers. It is
written in Object Oriented PHP and has been tested extensively using PHPUnit.

After parsing EasyRdf builds up a graph of PHP objects that can then be walked
around to get the data to be placed on the page. Dump methods are available to
inspect what data is available during development.

Data is typically loaded into a EasyRdf_Graph object from source RDF documents,
loaded from the web via HTTP. The EasyRdf_GraphStore class simplifies loading
and saving data to a SPARQL 1.1 Graph Store.

SPARQL queries can be made over HTTP to a Triplestore using the
EasyRdf_Sparql_Client class. SELECT and ASK queries will return an
EasyRdf_Sparql_Result object and CONSTRUCT and DESCRIBE queries will
return an EasyRdf_Graph object.


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n easyrdf-%{version}

# Create autoloader for tests
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > test/bootstrap.php

# Update test file
chmod +x test/cli_example_wrapper.php
sed -e 's:/usr/bin/env php:%{_bindir}/php:' \
    -e '/EXAMPLES_DIR = /s|\.\.|../../doc/%{name}-%{version}|' \
    -i test/cli_example_wrapper.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp lib/* %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp test/* %{buildroot}%{_datadir}/tests/%{name}/


%check
%if %{with_tests}
    pwd
    %{_bindir}/phpunit \
        -d include_path="./lib:./test:.:/usr/share/pear" \
        --bootstrap=./test/bootstrap.php \
        test
%else
: Tests skipped, missing '--with tests' option
%endif


%files
%doc *.md composer.json docs examples
%{_datadir}/php/EasyRdf.php
%{_datadir}/php/EasyRdf

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Sun Jan 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.7.2-1
- Initial package
