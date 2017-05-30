#
# Fedora spec file for php-phpdocumentor-fileset
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     phpDocumentor
%global github_name      Fileset
%global github_version   1.0.0
%global github_commit    bfa78d8fa9763dfce6d0e5d3730c1d8ab25d34b0

%global composer_vendor  phpdocumentor
%global composer_project fileset

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "symfony/finder": "~2.1"
#     NOTE: Min version not 2.1 because autoloader required
%global symfony_min_ver %{?el6:2.3.31}%{!?el6:2.7.1}
%global symfony_max_ver 3.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Component for collecting a set of files given dirs and file paths

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
BuildRequires: php-composer(symfony/finder) <  %{symfony_max_ver}
BuildRequires: php-composer(symfony/finder) >= %{symfony_min_ver}
## phpcompatinfo (computed from version 1.0.0)
BuildRequires: php-fileinfo
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(symfony/finder) <  %{symfony_max_ver}
Requires:      php-composer(symfony/finder) >= %{symfony_min_ver}
# phpcompatinfo (computed from version 1.0.0)
Requires:      php-fileinfo
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A fileset component that manages the collection of files using directories and
filenames.

Autoloader: %{phpdir}/phpDocumentor/Fileset/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/phpDocumentor/Fileset/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('phpDocumentor\\Fileset\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Symfony/Component/Finder/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor/
cp -rp src/phpDocumentor/Fileset %{buildroot}%{phpdir}/phpDocumentor/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55} php56 php70 php71 php72; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/phpDocumentor/Fileset/autoload.php \
            || RETURN_CODE=1
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
     %{phpdir}/phpDocumentor/Fileset


%changelog
* Tue May 30 2017 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
