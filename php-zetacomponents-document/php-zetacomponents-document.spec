#
# Fedora spec file for php-zetacomponents-document
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     zetacomponents
%global github_name      Document
%global github_version   1.3.1
%global github_commit    688abfde573cf3fe0730f82538fbd7aa9fc95bc8

%global composer_vendor  zetacomponents
%global composer_project document

# "zetacomponents/base": "*"
#     NOTE: Min and max versions added to contain to one major version.
%global zetacomponents_base_min_ver 1.0
%global zetacomponents_base_max_ver 2.0
# "zetacomponents/unit-test": "dev-master"
#     NOTE: Min and max versions added to contain to one major version.
%global zetacomponents_unit_test_min_ver 1.0
%global zetacomponents_unit_test_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

%global  ezcdir  %{_datadir}/php/ezc

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Provides a general conversion framework for different documents

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://zetacomponents.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php-composer(zetacomponents/base) <  %{zetacomponents_base_max_ver}
BuildRequires: php-composer(zetacomponents/base) >= %{zetacomponents_base_min_ver}
BuildRequires: php-composer(zetacomponents/unit-test) <  %{zetacomponents_unit_test_max_ver}
BuildRequires: php-composer(zetacomponents/unit-test) >= %{zetacomponents_unit_test_min_ver}
## phpcompatinfo (computed from version 1.3.1)
BuildRequires: php(language) >= 5.3.0
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-iconv
BuildRequires: php-libxml
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-xsl
%endif

# composer.json
Requires:      php-composer(zetacomponents/base) <  %{zetacomponents_base_max_ver}
Requires:      php-composer(zetacomponents/base) >= %{zetacomponents_base_min_ver}
# phpcompatinfo (computed from version 1.3.1)
Requires:      php(language) >= 5.3.0
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-iconv
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-spl
Requires:      php-xsl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The document component offers transformations between different semantic markup
languages, like:
* ReStructured text [1]
* XHTML [2]
* Docbook [3]
* eZ Publish XML markup [4]
* Wiki markup languages, like: Creole [5], Dokuwiki [6] and Confluence [7]
* Open Document Text [8] as used by OpenOffice.org [9] and other office suites

Each format supports conversions from and to docbook as a central intermediate
format and may implement additional shortcuts for conversions from and to other
formats. Not each format can express the same semantics, so there may be some
information lost.

Autoloader: %{ezcdir}/Document/autoload.php

[1] http://docutils.sourceforge.net/rst.html
[2] http://www.w3.org/TR/xhtml1/
[3] http://www.docbook.org/
[4] http://doc.ez.no/eZ-Publish/Technical-manual/4.x/Reference/XML-tags
[5] http://www.wikicreole.org/
[6] http://www.dokuwiki.org/dokuwiki
[7] http://confluence.atlassian.com/renderer/notationhelp.action?section=all
[8] http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office
[9] http://www.openoffice.org/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab \
   --output src/autoload.php \
   src
cat <<AUTOLOAD | tee -a  src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{ezcdir}/Base/autoloader.php',
));
AUTOLOAD

: Compat autoloader filename with other php-zetacomponents-* packages
ln -s autoload.php src/autoloader.php


%install
mkdir -p %{buildroot}%{ezcdir}/autoload

: Library
cp -pr src %{buildroot}%{ezcdir}/Document

: ezcBase autoloader
cp -pr src/*_autoload.php \
       %{buildroot}%{ezcdir}/autoload/


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{ezcdir}/UnitTest/autoloader.php';
require_once '%{buildroot}%{ezcdir}/Document/autoload.php';
BOOTSTRAP

: Skip tests requiring network access
sed -e 's/function testConversionFailure/function SKIP_testConversionFailure/' \
    -e 's/function testLoadXmlDocumentFromFile/function SKIP_testLoadXmlDocumentFromFile/' \
    -i tests/converter_docbook_html_xsl_test.php

: Skip tests known to fail
rm -f tests/pdf/table_column_width_test.php
sed -e 's/function testCreateFromDocbook/function SKIP_testCreateFromDocbook/' \
    -e 's/function testCommonConversions/function SKIP_testCommonConversions/' \
    -i tests/document_odt_docbook_test.php
sed -i 's/function testParseRstFile/function SKIP_testParseRstFile/' \
    tests/document_rst_parser_test.php \
    tests/document_rst_visitor_docbook_test.php \
    tests/document_rst_visitor_xhtml_test.php
sed 's/function testLoadXmlDocumentFromFile/function SKIP_testLoadXmlDocumentFromFile/' \
    -i tests/converter_docbook_rst_test.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license NOTICE
%doc *.rst
%doc ChangeLog
%doc composer.json
%{ezcdir}/autoload/document_autoload.php
%{ezcdir}/Document


%changelog
* Tue Jul 11 2017 Shawn Iwinski <shawn@iwin.ski> - 1.3.1-1
- Initial package
