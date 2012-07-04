%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_channel pear.doctrine-project.org
%global pear_name %(echo %{name} | sed -e 's/^php-doctrine-//' -e 's/-/_/g')

Name:             php-doctrine-DoctrineDBAL
Version:          2.2.2
Release:          1%{?dist}
Summary:          Doctrine Database Abstraction Layer

Group:            Development/Libraries
License:          LGPLv2
URL:              http://www.doctrine-project.org/projects/dbal.html
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-common >= 5.3.2
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires:         php-pear(%{pear_channel}/DoctrineCommon) >= 2.0.1
Requires:         php-pear(pear.symfony.com/Console) >= 2.0.0
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-date
Requires:         php-mysqli
Requires:         php-pcre
Requires:         php-pdo
Requires:         php-spl

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
Powerful database abstraction layer with many features for database schema
introspection, schema management and PDO abstraction.


%prep
%setup -q -c
# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml

# Fix package.xml for README and LICENSE files to have role="doc" instead of
# role="data"
# *** NOTE: This needs to be fixed upstream
sed -i \
    -e 's#\(.*\)name="Doctrine/DBAL/README.markdown" *role="data"\(.*\)#\1 name="Doctrine/DBAL/README.markdown" role="doc"\2#' \
    -e 's#\(.*\)name="LICENSE" *role="data"\(.*\)#\1 name="LICENSE" role="doc"\2#' \
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
%{pear_phpdir}/Doctrine/DBAL
%{_bindir}/doctrine-dbal.php
%{_bindir}/doctrine-dbal


%changelog
* Wed Jul 4 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2.2-1
- Initial package
