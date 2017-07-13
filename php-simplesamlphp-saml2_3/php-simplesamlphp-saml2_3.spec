#
# Fedora spec file for php-simplesamlphp-saml2_3
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     simplesamlphp
%global github_name      saml2
%global github_version   3.0.0
%global github_commit    cea679a3113d1f8198ab7d0a734de740412d0d0d

%global composer_vendor  simplesamlphp
%global composer_project saml2

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "mockery/mockery": "~0.9"
%global mockery_min_ver 0.9
%global mockery_max_ver 1.0
# "psr/log": "~1.0"
#     NOTE: Min version not 1.0 because autoloader required
%global psr_log_min_ver 1.0.1
%global psr_log_max_ver 2.0
# "robrichards/xmlseclibs": "^2.0|^3.0"
#     NOTE: Max version not 4.0 because it is unknown at this time how 3.0 will be packaged
%global robrichards_xmlseclibs_min_ver 2.0
%global robrichards_xmlseclibs_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}_3
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       SAML2 PHP library from SimpleSAMLphp (version 3)

Group:         Development/Libraries
License:       LGPLv2
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
BuildRequires: php-composer(psr/log) <  %{psr_log_max_ver}
BuildRequires: php-composer(psr/log) >= %{psr_log_min_ver}
BuildRequires: php-composer(robrichards/xmlseclibs) <  %{robrichards_xmlseclibs_max_ver}
BuildRequires: php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver}
BuildRequires: php-dom
BuildRequires: php-openssl
BuildRequires: php-zlib
%if 0%{!?el6:1}
BuildRequires: php-composer(mockery/mockery) <  %{mockery_max_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
%endif
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-date
BuildRequires: php-libxml
BuildRequires: php-mcrypt
BuildRequires: php-pcre
BuildRequires: php-soap
BuildRequires: php-spl
%endif
## Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/log) <  %{psr_log_max_ver}
Requires:      php-composer(psr/log) >= %{psr_log_min_ver}
Requires:      php-composer(robrichards/xmlseclibs) <  %{robrichards_xmlseclibs_max_ver}
Requires:      php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver}
Requires:      php-dom
Requires:      php-openssl
Requires:      php-zlib
# phpcompatinfo (computed from version 3.0.0)
Requires:      php-date
Requires:      php-libxml
Requires:      php-pcre
Requires:      php-soap
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
A PHP library for SAML2 related functionality. Extracted from SimpleSAMLphp [1],
used by OpenConext [2]. This library started as a collaboration between
UNINETT [3] and SURFnet [4] but everyone is invited to contribute.

Autoloader: %{phpdir}/SAML2_3/autoload.php

[1] https://www.simplesamlphp.org/
[2] https://www.openconext.org/
[3] https://www.uninett.no/
[4] https://www.surfnet.nl/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/SAML2/autoload.php src/SAML2
cat <<'AUTOLOAD' >> src/SAML2/autoload.php

class_alias('\\SAML2\\Constants', 'SAML2_Const');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Psr/Log/autoload.php',
    '%{phpdir}/RobRichards/XMLSecLibs/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/SAML2 %{buildroot}%{phpdir}/SAML2_3


%check
%if %{with_tests}
: Create pseudo Composer autoloader
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests
cat <<'AUTOLOAD' | tee -a vendor/autoload.php
require_once '%{buildroot}%{phpdir}/SAML2_3/autoload.php';
%if 0%{!?el6:1}
require_once '%{phpdir}/Mockery/autoload.php';
%endif
AUTOLOAD

%if 0%{?el6}
: Remove tests requiring Mockery
grep -r --files-with-matches Mockery tests | xargs rm -f
%endif

: Skip test known to fail
sed 's/function testToString/function SKIP_testToString/' \
    -i tests/SAML2/XML/saml/NameIDTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --configuration=tools/phpunit --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/SAML2_3


%changelog
* Wed Jul 12 2017 Shawn Iwinski <shawn@iwin.ski> - 3.0.0-1
- Initial package
