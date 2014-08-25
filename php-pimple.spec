#
# RPM spec file for php-pimple
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     fabpot
%global github_name      Pimple
%global github_version   3.0.0
%global github_commit    876bf0899d01feacd2a2e83f04641e51350099ef

# Lib
%global composer_vendor  pimple
%global composer_project pimple

# Ext
%global ext_name pimple
%global with_zts 0%{?__ztsphp:1}
%if "%{php_version}" < "5.6"
%global ini_name %{ext_name}.ini
%else
%global ini_name 40-%{ext_name}.ini
%endif

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}
%{!?__php:      %global __php      %{_bindir}/php}
%{!?__phpunit:  %global __phpunit  %{_bindir}/phpunit}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       2%{?dist}
Summary:       A simple dependency injection container for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://pimple.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildRequires: php-devel >= %{php_min_ver}
%if %{with_tests}
# For tests
BuildRequires: php-phpunit-PHPUnit
# For tests: phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# Lib
## composer.json
Requires:      php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 3.0.0)
Requires:      php-spl
# Ext
Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api)      = %{php_core_api}


# Lib
## Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
## Rename
Obsoletes:     php-Pimple < %{version}-%{release}
Provides:      php-Pimple = %{version}-%{release}

%if 0%{?fedora} < 20 && 0%{?rhel} < 7
# Filter shared private
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}
%endif

%description
%{summary}.

WARNING: %{_datadir}/php/Pimple/Pimple.php is only provided for compatibility
with the obsoleted php-Pimple RPM package (i.e. Pimple v1 package) and will be
removed in a future release. Please use the 'Pimple\Container' class instead.


%prep
%setup -qn %{github_name}-%{github_commit}

# Lib
## php-Pimple (i.e. Pimple v1 package) compat
cat > src/Pimple/Pimple.php <<'PHP_PIMPLE_V1_COMPAT'
<?php
/**
 * This file is only provided for compatibility with the obsoleted php-Pimple
 * RPM package (i.e. Pimple v1 package).  Please use the 'Pimple\Container'
 * class instead.
 *
 * WARNING: This file will be removed in a future release.
 */

class_alias('Pimple\Container', 'Pimple');
include __DIR__ . '/Container.php';
PHP_PIMPLE_V1_COMPAT

# Ext
## NTS
mv ext/%{ext_name} ext/NTS
## ZTS
%if %{with_zts}
cp -pr ext/NTS ext/ZTS
%endif

## Create configuration file
cat > %{ini_name} << 'INI'
; Enable %{ext_name} extension
extension=%{ext_name}.so
INI


%build
# Ext
## NTS
pushd ext/NTS
%{_bindir}/phpize
%configure --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}
popd
## ZTS
%if %{with_zts}
pushd ext/ZTS
%{_bindir}/zts-phpize
%configure --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
popd
%endif


%install
# Lib
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp src/* %{buildroot}/%{_datadir}/php/

# Ext
## NTS
make -C ext/NTS install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
## ZTS
%if %{with_zts}
make -C ext/ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif


%check
: Extension NTS minimal load test
%{__php} --no-php-ini \
    --define extension=ext/NTS/modules/%{ext_name}.so \
    --modules | grep %{ext_name}

%if %{with_zts}
: Extension ZTS minimal load test
%{__ztsphp} --no-php-ini \
    --define extension=ext/ZTS/modules/%{ext_name}.so \
    --modules | grep %{ext_name}
%endif

%if %{with_tests}
# Library test suite
## Create autoloader
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php

spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD

## Create PHPUnit config with colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

: Library test suite without extension
%{__phpunit} --include-path %{buildroot}%{_datadir}/php -d date.timezone="UTC"

: Library test suite with extension
%{__php} --define extension=ext/NTS/modules/%{ext_name}.so \
    %{__phpunit} --include-path %{buildroot}%{_datadir}/php -d date.timezone="UTC"

: Extension NTS test suite
pushd ext/NTS
make test NO_INTERACTION=1 REPORT_EXIT_STATUS=1
popd

%if %{with_zts}
: Extension ZTS test suite
pushd ext/ZTS
make test NO_INTERACTION=1 REPORT_EXIT_STATUS=1
popd
%endif
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG README.rst composer.json
# Lib
         %{_datadir}/php/Pimple
%exclude %{_datadir}/php/Pimple/Tests
# Ext
## NTS
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{ext_name}.so
## ZTS
%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{ext_name}.so
%endif


%changelog
* Mon Aug 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-2
- Fixed compat file location in description
- Included real class in compat file
- Always run extension minimal load test
- Fixed test suite with previous installed version
- "make test NO_INTERACTION=1 REPORT_EXIT_STATUS=1" instead of "echo "n" | make test"

* Thu Jul 31 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-1
- Updated to 3.0.0
- Added custom compat file for obsoleted php-Pimple

* Tue Jul 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.1-1
- Initial package
