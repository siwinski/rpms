%global github_owner   nicolas-grekas
%global github_name    Patchwork-Dumper
%global github_version 1.1.5
%global github_commit  674e1799838f5ff27b4ca40d9c64752ccc93043d

# "php": ">=5.3.0" (composer.json)
%global php_min_ver    5.3.3

# To disable tests use "--without tests"
%global with_tests     %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-patchwork-dumper
Version:       %{github_version}
Release:       1%{?github_release}%{dist}
Summary:       High accuracy and flexible dumping for PHP variables

Group:         Development/Libraries
License:       ASL 2.0 or GPLv2
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch
%if %{with_tests}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
# For tests: phpcompatinfo (computed from version 1.1.5)
BuildRequires: php-date
BuildRequires: php-gd
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-spl
BuildRequires: php-xml
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.1.5)
Requires:      php-date
Requires:      php-gd
Requires:      php-iconv
Requires:      php-json
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-posix
Requires:      php-reflection
Requires:      php-spl
Requires:      php-xml

%description
This package provides a better debug() function, that you can use instead of
var_dump(), better being for:
* Per object and resource types specialized view: e.g. filter out Doctrine
  noise while dumping a single proxy entity, or get more insight on opened
  files with stream_get_meta_data(). Add your own dedicated Dumper\Caster
  and get the view you need.
* Configurable output format: HTML, command line with colors or a dedicated
  high accuracy JSON format. More to come / add your own.
* Ability to dump internal references, either soft ones (objects or resources)
  or hard ones (=& on arrays or objects properties). Repeated occurrences of
  the same object/array/resource won't appear again and again anymore. Moreover,
  you'll be able to inspected the reference structure of your data.
* Ability to operate in the context of an output buffering handler.
* Full exposure of the internal mechanisms used for walking through an
  arbitrary PHP data structure.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -rp class/Patchwork %{buildroot}%{_datadir}/php/


%check
%if %{with_tests}
# Create autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace(array('\\', '_'), '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD

# Create PHPUnit config w/ colors turned off
sed 's/colors\s*=\s*"true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --include-path="./class:./tests" -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%doc *.md composer.json
%{_datadir}/php/Patchwork


%changelog
* Sun May 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.5-1
- Initial package
