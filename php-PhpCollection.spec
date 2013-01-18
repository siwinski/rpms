%global github_owner      schmittjoh
%global github_name       php-collection
%global github_version    0.1.0
%global github_commit     360a888f246773e660fce0d175cf62e41f50dd22

%global lib_name          PhpCollection

%global php_min_ver       5.3.0
%global phpoption_min_ver 1.0

Name:          php-%{lib_name}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       General purpose collection library for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://jmsyst.com/libs/%{github_name}
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-PhpOption >= %{phpoption_min_ver}
# Test build requires:phpci
BuildRequires: php-spl

Requires:      php-common >= %{php_min_ver}
Requires:      php-PhpOption >= %{phpoption_min_ver}
# phpci requires
Requires:      php-spl

Conflicts:     php-PhpOption >= 2.0

%description
This library adds basic collections for PHP.

Collections can be seen as more specialized arrays for which certain contracts
are guaranteed.

Supported Collections:
* Sequences
** Keys: numerical, consequentially increasing, no gaps
** Values: anything, duplicates allowed
** Classes: Sequence, SortedSequence
* Maps
** Keys: strings or objects, duplicate keys not allowed
** Values: anything, duplicates allowed
** Classes: Map, ObjectMap (not yet implemented)
* Sets (not yet implemented)
** Keys: not meaningful
** Values: anything, each value must be unique (===)
** Classes: Set

General Characteristics:
* Collections are mutable (new elements may be added, existing elements may be
  modified or removed). Specialized immutable versions may be added in the
  future though.
* Equality comparison between elements are always performed using the shallow
  comparison operator (===).
* Sorting algorithms are unstable, that means the order for equal elements is
  undefined (the default, and only PHP behavior).


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Update and move PHPUnit config
sed 's:tests/::' -i phpunit.xml.dist
mv phpunit.xml.dist tests/

# Overwrite tests/bootstrap.php (which uses Composer autoloader) with simple
# spl autoloader
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD
) > tests/bootstrap.php


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{lib_name} %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/


%check
%{_bindir}/phpunit \
    -d include_path="./src:./tests:.:%{pear_phpdir}:%{_datadir}/php" \
    -c tests/phpunit.xml.dist


%files
%doc LICENSE README.md composer.json
%{_datadir}/php/%{lib_name}

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}


%changelog
* Fri Jan 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.1.0-1
- Initial package
