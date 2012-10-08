%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}

%global pear_channel pear.symfony.com
%global pear_name    %(echo %{name} | sed -e 's/^php-symfony2-//' -e 's/-/_/g')
%global php_min_ver  5.3.3

Name:             php-symfony2-OptionsResolver
Version:          2.1.2
Release:          1%{?dist}
Summary:          Symfony2 %{pear_name} Component

Group:            Development/Libraries
License:          MIT
URL:              http://symfony.com/components
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz
Patch0:           php-symfony2-OptionsResolver.tests.bootstrap.patch

BuildArch:        noarch

BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})
# Test requires
BuildRequires:    php-common >= %{php_min_ver}
BuildRequires:    php-pear(pear.phpunit.de/PHPUnit)
# Test requires: phpci
Requires:         php-reflection
Requires:         php-spl

Requires:         php-common >= %{php_min_ver}
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-reflection
Requires:         php-spl

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
OptionsResolver helps at configuring objects with option arrays.

It supports default values on different levels of your class hierarchy, option
constraints (required vs. optional, allowed values) and lazy options whose
default value depends on the value of another option.


%prep
%setup -q -c

# Patches
cd %{pear_name}-%{version}
%patch0 -p0
cd ..

# Modify PEAR package.xml file:
# - Change role from "php" to "test" for all test files
# - Remove md5sum from bootsrap.php file since it was patched
sed -e '/phpunit.xml.dist/s/role="php"/role="test"/' \
    -e '/Tests/s/role="php"/role="test"/' \
    -e '/bootstrap.php/s/md5sum="[^"]*"\s*//' \
    -i package.xml

# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml


%build
# Empty build section, nothing required


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_phpdir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}


%check
cd %{pear_name}-%{version}/Symfony/Component/%{pear_name}
%{_bindir}/phpunit


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%dir %{pear_phpdir}/Symfony
%dir %{pear_phpdir}/Symfony/Component
     %{pear_phpdir}/Symfony/Component/%{pear_name}
%{pear_testdir}/%{pear_name}


%changelog
* Mon Oct  8 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 2.1.2-2
- Added PEAR package.xml modificaions
- Added patch for tests' bootstrap.php
- Added tests (%%check)

* Thu Sep 20 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 2.1.2-1
- Initial package
