# TODO:
# * Fix rpmlint errors
# * Awaiting the following issue fixes from upstream:
# ** PEAR role="doc" (http://drupal.org/node/1643660)
# ** PEAR role="test" (http://drupal.org/node/1643676)
# ** PEAR license file (http://drupal.org/node/1643680)

# NOTE: Update upstream issue http://drupal.org/node/508086 when this RPM
# is complete

%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_channel pear.drush.org
%global pear_name %(echo %{name} | sed -e 's/^php-drush-//' -e 's/-/_/g')

Name:             php-drush-drush
Version:          5.4.0
Release:          1%{?dist}
Summary:          Command line shell and Unix scripting interface for Drupal

Group:            Development/Libraries
License:          GPLv2+
URL:              http://www.drush.org
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-cli >= 5.2
Requires:         php-channel(%{pear_channel})
Requires:         php-pear(PEAR)
Requires:         php-pear(pear.phpunit.de/PHPUnit) >= 3.5
Requires:         git >= 1.7
Requires(post):   %{__pear}
Requires(postun): %{__pear}

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
Drush is a command line shell and Unix scripting interface for Drupal.  If
you are unfamiliar with shell scripting, reviewing the documentation for your
shell (e.g. man bash) or reading an online tutorial (e.g. search for "bash
tutorial") will help you get the most out of Drush.

Drush core ships with lots of useful commands for interacting with code like
modules/themes/profiles. Similarly, it runs update.php, executes sql queries
and DB migrations, and misc utilities like run cron or clear cache.


%prep
%setup -q -c
# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml


%build
# Empty build section, nothing to build


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_phpdir}/.??* \
    $RPM_BUILD_ROOT%{pear_phpdir}/%{pear_name}/.travis.yml \
    $RPM_BUILD_ROOT%{_bindir}/drush.bat
find $RPM_BUILD_ROOT%{pear_phpdir}/%{pear_name} -name .gitignore -delete

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/%{pear_name}
%{_bindir}/drush


%changelog
* Sun Jun 17 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 5.4.0-1
- Initial package
