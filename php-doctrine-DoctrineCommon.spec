%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_channel pear.doctrine-project.org
%global pear_name %(echo %{name} | sed -e 's/^php-doctrine-//' -e 's/-/_/g')

Name:             php-doctrine-DoctrineCommon
Version:          2.2.2
Release:          1%{?dist}
Summary:          Doctrine Common PHP Extensions

Group:            Development/Libraries
License:          LGPLv2
URL:              http://www.doctrine-project.org/projects/common.html
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-common >= 5.3.0
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-ctype
Requires:         php-date
Requires:         php-json
Requires:         php-pcre
Requires:         php-reflection
Requires:         php-spl
Requires:         php-tokenizer

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
The Doctrine Common project is a library that provides extensions to core
PHP functionality.

Optional dependencies:
* APC (for Doctrine\Common\Cache\ApcCache)
* memcache (for Doctrine\Common\Cache\MemcacheCache)
* memcached (for Doctrine\Common\Cache\MemcachedCache)
* XCache (for Doctrine\Common\Cache\XcacheCache)
* Zend Server (for Doctrine\Common\Cache\ZendDataCache)


%prep
%setup -q -c
# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml

# Fix package.xml for LICENSE file to have role="doc" instead of role="data"
# *** NOTE: This needs to be fixed upstream
sed -i \
    's#\(.*\)name="LICENSE" *role="data"\(.*\)#\1 name="LICENSE" role="doc"\2#' \
    %{pear_name}-%{version}/%{name}.xml


%build
# Empty build section, nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_phpdir}/.??*

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
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%dir %{pear_phpdir}/Doctrine
%{pear_phpdir}/Doctrine/Common


%changelog
* Wed Jul 4 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2.2-1
- Initial package
