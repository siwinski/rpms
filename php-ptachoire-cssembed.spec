#
# RPM spec file for php-ptachoire-cssembed
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     krichprollsch
%global github_name      phpCssEmbed
%global github_version   1.0.2
%global github_commit    406c6d5b846cafa9186f9944a6210d0e6fed154b

%global composer_vendor  ptachoire
%global composer_project cssembed

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       CSS URL embed library

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
# For tests
BuildRequires: php-phpunit-PHPUnit
# For tests: composer.json
BuildRequires: php(language) >= %{php_min_ver}
# For tests: phpcompatinfo (computed from version 1.0.2)
BuildRequires: php-fileinfo
BuildRequires: php-pcre
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.2)
Requires:      php-fileinfo
Requires:      php-pcre
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -pm 0755 %{buildroot}/%{_datadir}/php
cp -rp src/CssEmbed %{buildroot}/%{_datadir}/php/


%check
%if %{with_tests}
# Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{__phpunit} --include-path %{buildroot}%{_datadir}/php -d date.timezone="UTC"
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc readme.md composer.json
%{_datadir}/php/CssEmbed


%changelog
* Thu Sep 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.2-1
- Initial package
