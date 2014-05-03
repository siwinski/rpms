%global github_owner    PHPOffice
%global github_name     PHPPowerPoint
# See CHANGELOG.md for version
%global github_version  0.2.0
%global github_commit   50fd978df41f031c1ceadfcc18b947231cefe1a1
%global github_release  .20140426git%(c=%{github_commit}; echo ${c:0:7})

# "php": ">=5.2.0" (composer.json)
%global php_min_ver     5.2.0

# "phpunit/phpunit": "3.7.*" (composer.json)
%global phpunit_min_ver 3.7.0
%global phpunit_max_ver 3.8.0

# To disable tests use "--without tests"
%global with_tests      %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-phppowerpoint
Version:       %{github_version}
Release:       0.1%{?github_release}%{dist}
Summary:       A pure PHP library for writing presentations files

Group:         Development/Libraries
License:       LGPLv2
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) >= %{phpunit_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit) <  %{phpunit_max_ver}
BuildRequires: php-gd
BuildRequires: php-xml
BuildRequires: php-zip
# For tests: phpcompatinfo (computed from pre-release version 0.2.0 commit 50fd978df41f031c1ceadfcc18b947231cefe1a1)
BuildRequires: php-date
BuildRequires: php-ereg
BuildRequires: php-iconv
BuildRequires: php-mbstring
BuildRequires: php-simplexml
BuildRequires: php-spl
BuildRequires: php-xmlwriter
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-xml
# composer.json (optional)
Requires:      php-gd
Requires:      php-zip
# phpcompatinfo (computed from pre-release version 0.2.0 commit 50fd978df41f031c1ceadfcc18b947231cefe1a1)
Requires:      php-date
Requires:      php-ereg
Requires:      php-iconv
Requires:      php-mbstring
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xmlwriter

%description
PHPPowerPoint is a library written in pure PHP that provides a set of classes
to write to different presentation file formats, i.e. OpenXML (.pptx) and
OpenDocument (.odp).


%prep
%setup -q -n %{github_name}-%{github_commit}

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' README.md


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp Classes/* %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
# Create PHPUnit config w/ colors turned off
sed 's/colors\s*=\s*"true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit
%else
: Tests skipped
%endif


%files
%doc *.md composer.json Documentation/*.md
%{_datadir}/php/PHPPowerPoint.php
%{_datadir}/php/PHPPowerPoint


%changelog
* Sat May 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.2.0-0.1.20140426git50fd978
- Initial package
