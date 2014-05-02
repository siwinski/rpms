%global github_owner    PHPOffice
%global github_name     PHPWord
%global github_version  0.9.1
%global github_commit   0f16da9a56d8a7207d845cb3ad3c98ce290fdc76

# "php": ">=5.3.3" (composer.json)
%global php_min_ver     5.3.3

# "phpunit/phpunit": "3.7.*" (composer.json)
%global phpunit_min_ver 3.7.0
%global phpunit_max_ver 3.8.0

# To disable tests use "--without tests"
%global with_tests      %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-phpword
Version:       %{github_version}
Release:       1%{dist}
Summary:       A set of classes to write to and read from different document file formats

Group:         Development/Libraries
# See https://github.com/PHPOffice/PHPWord/issues/211
License:       LGPLv2+
URL:           http://phpoffice.github.io/phpword_features.html
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) >= %{phpunit_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) <  %{phpunit_max_ver}
BuildRequires: php-gd
BuildRequires: php-xml
BuildRequires: php-xmlwriter
BuildRequires: php-xsl
BuildRequires: php-zip
# For tests: phpcompatinfo (computed from version 0.9.1)
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-exif
BuildRequires: php-filter
BuildRequires: php-pcre
BuildRequires: php-simplexml
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-xml
Requires:      php-zip
# composer.json (optional)
Requires:      php-gd
Requires:      php-xmlwriter
Requires:      php-xsl
# phpcompatinfo (computed from version 0.9.1)
Requires:      php-date
Requires:      php-dom
Requires:      php-exif
Requires:      php-filter
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl

%description
PHPWord is a library written in pure PHP that provides a set of classes to
write to and read from different document file formats. The current version
of PHPWord supports Microsoft Office Open XML [1] (OOXML or OpenXML), OASIS
Open Document Format for Office Applications [2] (OpenDocument or ODF), and
Rich Text Format [2] (RTF).

[1] http://en.wikipedia.org/wiki/Office_Open_XML
[2] http://en.wikipedia.org/wiki/OpenDocument
[3] http://en.wikipedia.org/wiki/Rich_Text_Format


%prep
%setup -q -n %{github_name}-%{github_commit}

# Fix script-without-shebang and spurious-executable-perm
# https://github.com/PHPOffice/PHPWord/pull/214
find src -name '*.php' | xargs chmod a-x
chmod a-x *.md

# Fix wrong-file-end-of-line-encoding
# https://github.com/PHPOffice/PHPWord/pull/215
sed -i 's/\r$//' README.md


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp src/* %{buildroot}/%{_datadir}/php/


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

# Skip tests that require external resources
sed 's/function testAddImageByUrl/function SKIP_testAddImageByUrl/' \
    -i tests/PhpWord/Tests/Section/FooterTest.php
sed 's/function testAddImageByUrl/function SKIP_testAddImageByUrl/' \
    -i tests/PhpWord/Tests/Section/HeaderTest.php
sed 's/function testAddSectionImageByUrl/function SKIP_testAddSectionImageByUrl/' \
    -i tests/PhpWord/Tests/Section/Table/CellTest.php
sed 's/function testAddHeaderImageByUrl/function SKIP_testAddHeaderImageByUrl/' \
    -i tests/PhpWord/Tests/Section/Table/CellTest.php
sed 's/function testAddFooterImageByUrl/function SKIP_testAddFooterImageByUrl/' \
    -i tests/PhpWord/Tests/Section/Table/CellTest.php
sed 's/function testAddElements/function SKIP_testAddElements/' \
    -i tests/PhpWord/Tests/SectionTest.php

# Create PHPUnit config w/ colors turned off
sed 's/colors\s*=\s*"true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --include-path="./src:./tests" -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%doc *.md composer.json docs
%{_datadir}/php/PhpWord


%changelog
* Fri May 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 0.9.1-1
- Initial package
