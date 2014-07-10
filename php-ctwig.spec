#
# RPM spec file for php-ctwig and php-twig
#
# Copyright (c) 2014 Shawn Iwinski <shawn.iwinski@gmail.com>
#                    Remi Collet <remi@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     fabpot
%global github_name      Twig
%global github_version   1.16.0
%global github_commit    8ce37115802e257a984a82d38254884085060024

# Lib
%global composer_vendor  twig
%global composer_project twig

# Ext
%global with_zts 0%{?__ztsphp:1}
%global ext_name twig
%if "%{php_version}" < "5.6"
%global ini_name %{ext_name}.ini
%else
%global ini_name 40-%{ext_name}.ini
%endif

# "php": ">=5.2.4"
%global php_min_ver 5.2.4

# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}
%{!?__php:      %global __php      %{_bindir}/php}

Name:          php-ctwig
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Extension to improve performance of Twig

Group:         Development/Libraries
License:       BSD
URL:           http://twig.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildRequires: php-devel >= %{php_min_ver}
%if %{with_tests}
# For tests
BuildRequires: php-phpunit-PHPUnit
# For tests: phpcompatinfo (computed from version 1.16.0)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api)      = %{php_core_api}

# Rename
Obsoletes:     php-twig-ctwig         < %{version}
Provides:      php-twig-ctwig         = %{version}-%{release}
Provides:      php-twig-ctwig%{?_isa} = %{version}
Obsoletes:     php-twig-CTwig         < %{version}
Provides:      php-twig-CTwig         = %{version}-%{release}
# Noarch sub-package now uses this name
Obsoletes:     php-twig%{?_isa}       < %{version}
# PECL
Provides:      php-pecl(pear.twig-project.org/CTwig)         = %{version}
Provides:      php-pecl(pear.twig-project.org/CTwig)%{?_isa} = %{version}

%if 0%{?fedora} < 20
# Filter shared private
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}
%endif

%description
Twig is a PHP template engine.

This package provides the Twig C extension (CTwig) to improve performance
of the Twig template language, used by Twig PHP extension (php-twig-Twig).


%package -n php-%{composer_vendor}

Summary:   The flexible, fast, and secure template engine for PHP

BuildArch: noarch

Requires:  php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.16.0)
Requires:  php-ctype
Requires:  php-date
Requires:  php-dom
Requires:  php-hash
Requires:  php-iconv
Requires:  php-json
Requires:  php-mbstring
Requires:  php-pcre
Requires:  php-reflection
Requires:  php-spl

# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# Rename
Obsoletes: php-twig-Twig < %{version}
Provides:  php-twig-Twig = %{version}-%{release}
# PEAR
Provides:  php-pear(pear.twig-project.org/Twig) = %{version}

%description -n php-%{composer_vendor}
%{summary}.

* Fast: Twig compiles templates down to plain optimized PHP code. The
  overhead compared to regular PHP code was reduced to the very minimum.

* Secure: Twig has a sandbox mode to evaluate untrusted template code. This
  allows Twig to be used as a template language for applications where users
  may modify the template design.

* Flexible: Twig is powered by a flexible lexer and parser. This allows the
  developer to define its own custom tags and filters, and create its own
  DSL.

Optional dependency: Xdebug (php-pecl-xdebug)


%prep
%setup -qn %{github_name}-%{github_commit}

# Ext
cd ext

## NTS
mv %{ext_name} NTS

## ZTS
%if %{with_zts}
cp -pr NTS ZTS
%endif

## Create configuration file
cat > %{ini_name} << 'INI'
; Enable %{ext_name} extension module
extension=%{ext_name}.so
INI


%build
# Ext
cd ext

## NTS
cd NTS
%{_bindir}/phpize
%configure --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

## ZTS
%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
# Lib
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/* %{buildroot}/%{_datadir}/php/

# Ext
cd ext

## NTS
make -C NTS install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

## ZTS
%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 0644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif


%check
%if %{with_tests}
# Lib
# Create PHPUnit config w/ colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit --include-path ./lib -d date.timezone="UTC"

# Ext
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=ext/NTS/modules/%{ext_name}.so \
    --modules | grep %{ext_name}

%if %{with_zts}
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=ext/ZTS/modules/%{ext_name}.so \
    --modules | grep %{ext_name}
%endif
%else
: Tests skipped
%endif


%files
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{ext_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{ext_name}.so
%endif

%files -n php-%{composer_vendor}
%doc LICENSE CHANGELOG README.rst composer.json
%{_datadir}/php/Twig


%changelog
* Thu Jul 10 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-1
- Initial package
