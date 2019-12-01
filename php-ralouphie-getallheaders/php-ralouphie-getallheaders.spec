#
# Fedora spec file for php-ralouphie-getallheaders
#
# Copyright (c) 2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     ralouphie
%global github_name      getallheaders
%global github_version   2.0.5
%global github_commit    5601c8a83fbba7ef674a7369456d12f1e0d0eafa

%global composer_vendor  ralouphie
%global composer_project getallheaders

# "php": ">=5.3"
%global php_min_ver 5.3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A polyfill for getallheaders

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo for version 2.0.5
##     <none>
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo for version 2.0.5
#     <none>

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

https://www.php.net/manual/function.getallheaders.php

Autoloader: %{phpdir}/%{composer_vendor}-%{composer_project}/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Common autoloader
ln -s getallheaders.php src/autoload.php


%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src %{buildroot}%{phpdir}/%{composer_vendor}-%{composer_project}


%check
%if %{with_tests}
: Mock Composer autoloader
mkdir vendor
ln -s %{buildroot}%{phpdir}/%{composer_vendor}-%{composer_project}/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in php php70 php71 php72 php73 php74; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose || RETURN_CODE=1
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
%{phpdir}/%{composer_vendor}-%{composer_project}


%changelog
* Sun Dec 01 2019 Shawn Iwinski <shawn@iwin.ski> - 2.0.5-1
- Initial package
