#
# RPM spec file for php-pimple
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     silexphp
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

%{!?php_inidir:  %global php_inidir  %{_sysconfdir}/php.d}
%{!?phpdir:      %global phpdir      %{_datadir}/php}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       4%{?dist}
Summary:       A simple dependency injection container for PHP (extension)

Group:         Development/Libraries
License:       MIT
URL:           http://pimple.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildRequires: php-devel >= %{php_min_ver}
# For autoload generation
BuildRequires: %{_bindir}/phpab
%if %{with_tests}
# For tests
## composer.json
BuildRequires: %{_bindir}/phpunit
## phpcompatinfo (computed from version 3.0.0)
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api)      = %{php_core_api}

# Extension *or* library
Conflicts:     %{name}-lib

%if 0%{?fedora} < 20 && 0%{?rhel} < 7
# Filter shared private
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}
%endif

%description
%{summary}.

NOTE: This package installs the Pimple EXTENSION. If you would like the LIBRARY,
install "%{name}-lib" instead.  Only one or the other may be installed.

# ------------------------------------------------------------------------------

%package lib

Summary:   A simple dependency injection container for PHP (library)

BuildArch: noarch

# composer.json
Requires:  php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 3.0.0)
Requires:  php-spl

# Library *or* extension
Conflicts: %{name}

# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# Rename
Obsoletes: php-Pimple < %{version}-%{release}
Provides:  php-Pimple = %{version}-%{release}

%description lib
%{summary}.

NOTE: This package installs the Pimple LIBRARY. If you would like the EXTENSION,
install "%{name}" instead. Only one or the other may be installed.

# ------------------------------------------------------------------------------

%prep
%setup -qn %{github_name}-%{github_commit}

# Lib
## Move tests out of src directory
mkdir -p tests/Pimple
mv src/Pimple/Tests tests/Pimple/

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
# Lib
%{_bindir}/phpab --nolower --output src/Pimple/autoload.php src/Pimple

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
mkdir -p %{buildroot}/%{phpdir}/
cp -rp src/* %{buildroot}/%{phpdir}/

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
: Library test suite without extension
%{_bindir}/phpunit --bootstrap %{buildroot}/%{phpdir}/Pimple/autoload.php

: Library test suite with extension
%{_bindir}/php --define extension=ext/NTS/modules/%{ext_name}.so \
    %{_bindir}/phpunit --bootstrap %{buildroot}/%{phpdir}/Pimple/autoload.php

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


%{!?_licensedir:%global license %%doc}

%files
%license LICENSE
%doc CHANGELOG
%doc README.rst
# NTS
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{ext_name}.so
# ZTS
%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{ext_name}.so
%endif

%files lib
%license LICENSE
%doc CHANGELOG
%doc README.rst
%doc composer.json
%{phpdir}/Pimple


%changelog
* Thu May 21 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-4
- Add library autoloader
- Spec cleanup

* Wed Sep 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-3
- Separate extension and library (i.e. sub-package library)

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
