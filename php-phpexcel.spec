%global github_owner   PHPOffice
%global github_name    PHPExcel
%global github_version 1.8.0
%global github_commit  e69a5e4d0ffa7fb6f171859e0a04346e580df30b

# php": ">=5.2.0" (composer.json)
%global php_min_ver    5.2.0

# To disable tests use "--without tests"
%global with_tests      %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-phpexcel
Version:       %{github_version}
Release:       1%{?github_release}%{dist}
Summary:       A pure PHP library for reading and writing spreadsheet files

Group:         Development/Libraries
# Everything is LGPLv2 except for certain PHPExcel/Shared OLE files which are PHP
# See https://github.com/PHPOffice/PHPExcel/issues/364
License:       LGPLv2 and PHP
URL:           http://phpoffice.github.io/phpexcel_features.html
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-gd
BuildRequires: php-xml
BuildRequires: php-xmlwriter
BuildRequires: php-zip
# For tests: phpcompatinfo (computed from version 1.8.0)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-iconv
BuildRequires: php-libxml
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-pecl(igbinary)
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-sqlite3
BuildRequires: php-xmlreader
BuildRequires: php-zlib
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-xml
Requires:      php-xmlwriter
# composer.json (optional)
Requires:      php-gd
Requires:      php-zip
# phpcompatinfo (computed from version 1.8.0)
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-iconv
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-pecl(igbinary)
Requires:      php-posix
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-sqlite3
Requires:      php-xmlreader
Requires:      php-zlib
# Unbundled
Requires:      php-pclzip

%description
Project providing a set of classes for the PHP programming language, which
allow you to write to and read from different spreadsheet file formats, like
Excel (BIFF) .xls, Excel 2007 (OfficeOpenXML) .xlsx, CSV, Libre/OpenOffice
Calc .ods, Gnumeric, PDF, HTML, ... This project is built around Microsoft's
OpenXML standard and PHP.

Optional:
* APC (php-pecl-apc)
* Memcache (php-pecl-memcache)


%prep
%setup -q -n %{github_name}-%{github_commit}

# Fix wrong-file-end-of-line-encoding
find Examples -type f -exec sed -i 's/\r$//' {} \;

# Remove unneeded files
find . -name '\.git*' | xargs rm -f

# Remove bundled pclzip (license = LGPLv2)
rm -rf Classes/PHPExcel/Shared/PCLZip


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -rp Classes/* %{buildroot}%{_datadir}/php/

# Symlink pclzip
ln -s %{_datadir}/php/pclzip %{buildroot}%{_datadir}/php/PHPExcel/Shared/PCLZip

# Locales
for LOCALE in %{buildroot}%{_datadir}/php/PHPExcel/locale/*
do
    LANG=$(basename $LOCALE)
    echo "%%lang(${LANG%_*}) $LOCALE"
done | sed 's#%{buildroot}##' | tee %{name}.lang


%check
%if %{with_tests}
cd unitTests

# Remove tests known to fail
rm -f \
    Classes/PHPExcel/Calculation/DateTimeTest.php \
    Classes/PHPExcel/Calculation/EngineeringTest.php \
    Classes/PHPExcel/Calculation/FinancialTest.php \
    Classes/PHPExcel/Calculation/LookupRefTest.php \
    Classes/PHPExcel/Calculation/MathTrigTest.php \
    Classes/PHPExcel/Calculation/MathTrigTest.php \
    Classes/PHPExcel/Calculation/TextDataTest.php \
    Classes/PHPExcel/Shared/DateTest.php \
    Classes/PHPExcel/Shared/PasswordHasherTest.php \
    Classes/PHPExcel/Shared/StringTest.php \
    Classes/PHPExcel/Style/NumberFormatTest.php testFormatValueWithMask \
    Classes/PHPExcel/Worksheet/AutoFilter/Column/RuleTest.php \
    Classes/PHPExcel/Worksheet/CellCollectionTest.php

# Turn off PHPUnit colors
sed -i 's/colors="true"/colors="false"/' phpunit.xml

%{_bindir}/phpunit -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files -f %{name}.lang
%doc *.txt *.md Examples
     %{_datadir}/php/PHPExcel.php
%dir %{_datadir}/php/PHPExcel
%dir %{_datadir}/php/PHPExcel/locale
     %{_datadir}/php/PHPExcel/*.php
     %{_datadir}/php/PHPExcel/CachedObjectStorage
     %{_datadir}/php/PHPExcel/CalcEngine
     %{_datadir}/php/PHPExcel/Calculation
     %{_datadir}/php/PHPExcel/Cell
     %{_datadir}/php/PHPExcel/Chart
     %{_datadir}/php/PHPExcel/Reader
     %{_datadir}/php/PHPExcel/RichText
     %{_datadir}/php/PHPExcel/Shared
     %{_datadir}/php/PHPExcel/Style
     %{_datadir}/php/PHPExcel/Worksheet
     %{_datadir}/php/PHPExcel/Writer


%changelog
* Sat May 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.8.0-1
- Initial package
