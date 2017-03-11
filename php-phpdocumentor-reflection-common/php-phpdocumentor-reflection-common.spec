#
# Fedora spec file for php-phpdocumentor-reflection-common
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      ReflectionCommon
%global github_version   1.0
%global github_commit    144c307535e82c8fdcaacbcfc1d6d8eeb896687c

%global composer_vendor  phpdocumentor
%global composer_project reflection-common

# "php": ">=5.5"
%global php_min_ver 5.5

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Common reflection classes used by phpdocumentor

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(phpunit/phpunit)
## phpcompatinfo (computed from version 1.0)
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Common reflection classes used by phpdocumentor to reflect the code structure.

Autoloader: %{phpdir}/phpDocumentor/Reflection/autoload-common.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-common.php src


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor
cp -rp src %{buildroot}%{phpdir}/phpDocumentor/Reflection


%check
%if %{with_tests}
BOOTSTRAP=%{buildroot}%{phpdir}/phpDocumentor/Reflection/autoload-common.php

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php56 php70 php71; do
    if which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose --bootstrap $BOOTSTRAP || RETURN_CODE=1
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
%dir %{phpdir}/phpDocumentor
%dir %{phpdir}/phpDocumentor/Reflection
     %{phpdir}/phpDocumentor/Reflection/autoload-common.php
     %{phpdir}/phpDocumentor/Reflection/Element.php
     %{phpdir}/phpDocumentor/Reflection/File.php
     %{phpdir}/phpDocumentor/Reflection/Fqsen.php
     %{phpdir}/phpDocumentor/Reflection/Location.php
     %{phpdir}/phpDocumentor/Reflection/Project.php
     %{phpdir}/phpDocumentor/Reflection/ProjectFactory.php


%changelog
* Sat Mar 11 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0-1
- Initial package
