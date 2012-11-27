# Awaiting the following issue fixes from upstream:
# * PEAR license file (http://drupal.org/node/1643680)
# * PEAR role="doc" (http://drupal.org/node/1643660)
# * PEAR role="test" (http://drupal.org/node/1643676)
# * PEAR extra files (http://drupal.org/node/1772518)
# * drush.bat (http://drupal.org/node/1704986)

%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}

%global pear_channel pear.drush.org
%global pear_name    %(echo %{name} | sed -e 's/^php-drush-//' -e 's/-/_/g')

# Tests are only run with rpmbuild --with tests
# Lot of failures, need investigation
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}

Name:             php-drush-drush
Version:          5.8.0
Release:          1%{?dist}
Summary:          Command line shell and Unix scripting interface for Drupal

Group:            Development/Libraries
License:          GPLv2+
URL:              http://www.drush.org
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:         drupal6-drush = %{version}-%{release}
Obsoletes:        drupal6-drush < 5.7.0-1

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})
%if %{with_tests}
BuildRequires:    php-pear(pear.phpunit.de/PHPUnit) >= 3.5
%endif

Requires:         php-cli >= 5.2
Requires:         php-channel(%{pear_channel})
Requires:         php-pear(PEAR)
Requires:         php-pear(Console_Table)
Requires:         git >= 1.7
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-ctype
Requires:         php-date
Requires:         php-dom
Requires:         php-fileinfo
Requires:         php-hash
Requires:         php-iconv
Requires:         php-json
Requires:         php-mysql
Requires:         php-mysqli
Requires:         php-pcre
Requires:         php-pdo
Requires:         php-pgsql
Requires:         php-posix
Requires:         php-reflection
Requires:         php-simplexml
Requires:         php-spl

%description
Drush is a command line shell and Unix scripting interface for Drupal.  If
you are unfamiliar with shell scripting, reviewing the documentation for your
shell (e.g. man bash) or reading an online tutorial (e.g. search for "bash
tutorial") will help you get the most out of Drush.

Drush core ships with lots of useful commands for interacting with code like
modules/themes/profiles. Similarly, it runs update.php, executes sql queries
and DB migrations, and misc utilities like run cron or clear cache.

Works with Drupal 6, Drupal 7, and usually Drupal 8.


%prep
%setup -q -c

# Update package.xml for files identified with role="php"
# instead of role="test":
# - tests/
# NOTE: Ran before role="doc" update because role="doc" update will
#       overwrite some of these test roles (specifically tests/*.txt)
# *** Upstream issue: http://drupal.org/node/1643676
sed '/name="tests\//s/role="php"/role="test"/' \
    -i package.xml

# Update package.xml for files identified with role="php"
# instead of role="doc":
# - *.txt
# - docs/
# - examples/
# *** Upstream issue: http://drupal.org/node/1643660
sed -e '/name="[^"]*\.txt"/s/role="php"/role="doc"/' \
    -e '/name="docs\//s/role="php"/role="doc"/' \
    -e '/name="examples\//s/role="php"/role="doc"/' \
    -i package.xml

# Remove .travis.yml and .gitignore files from package.xml
# *** Upstream issue: http://drupal.org/node/1772518
sed -e '/.travis.yml/d' \
    -e '/.gitignore/d' \
    -i package.xml

# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml


%build
# Empty build section, nothing required


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Fix some file permissions
chmod a+x %{buildroot}%{pear_phpdir}/%{pear_name}/drush.php
chmod a+x %{buildroot}%{pear_phpdir}/%{pear_name}/drush.complete.sh
chmod a+x %{buildroot}%{pear_testdir}/%{pear_name}/tests/runner.php

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
%if %{with_tests}
    cd %{pear_name}-%{version}/tests
    %{_bindir}/phpunit .
%else
: Tests skipped, missing '--with tests' option
%endif


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
%{pear_phpdir}/%{pear_name}
%{pear_testdir}/%{pear_name}
%{_bindir}/drush*


%changelog
* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 5.8.0-1
- Updated to upstream version 5.8.0

* Thu Nov  8 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 5.7.0-1
- Initial package
