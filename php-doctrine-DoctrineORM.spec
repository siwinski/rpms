%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_channel pear.doctrine-project.org
%global pear_name %(echo %{name} | sed -e 's/^php-doctrine-//' -e 's/-/_/g')

Name:             php-doctrine-DoctrineORM
Version:          2.2.2
Release:          1%{?dist}
Summary:          Doctrine Object Relational Mapper

Group:            Development/Libraries
License:          LGPLv2
URL:              http://www.doctrine-project.org/projects/orm.html
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-common >= 5.3.0
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires:         php-pear(%{pear_channel}/DoctrineCommon) >= 2.2.0-0.1.beta1
Requires:         php-pear(%{pear_channel}/DoctrineCommon) <= 2.2.99
Requires:         php-pear(%{pear_channel}/DoctrineDBAL) >= 2.2.0-0.1.beta1
Requires:         php-pear(%{pear_channel}/DoctrineDBAL) <= 2.2.99
Requires:         php-pear(pear.symfony.com/Console) >= 2.0.0
Requires:         php-pear(pear.symfony.com/Yaml) >= 2.0.0
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-ctype
Requires:         php-pcre
Requires:         php-pdo
Requires:         php-reflection
Requires:         php-simplexml
Requires:         php-spl
Requires:         php-tokenizer

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
Object relational mapper (ORM) for PHP that sits on top of a powerful
database abstraction layer (DBAL). One of its key features is the option
to write database queries in a proprietary object oriented SQL dialect
called Doctrine Query Language (DQL), inspired by Hibernate's HQL. This
provides developers with a powerful alternative to SQL that maintains
flexibility without requiring unnecessary code duplication.


%prep
%setup -q -c
# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml

# Fix package.xml for README and LICENSE files to have role="doc" instead of
# role="data"
# *** NOTE: This needs to be fixed upstream
sed -i \
    -e 's#\(.*\)name="Doctrine/ORM/README.markdown" *role="data"\(.*\)#\1 name="Doctrine/ORM/README.markdown" role="doc"\2#' \
    -e 's#\(.*\)name="LICENSE" *role="data"\(.*\)#\1 name="LICENSE" role="doc"\2#' \
    -e 's#\(.*\)name="UPGRADE\([^"]*\)" *role="data"\(.*\)#\1 name="UPGRADE\2" role="doc"\3#' \
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
%{pear_datadir}/%{pear_name}
%{pear_phpdir}/Doctrine/ORM
%{_bindir}/doctrine.bat
%{_bindir}/doctrine.php
%{_bindir}/doctrine


%changelog
* Wed Jul 4 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2.2-1
- Initial package
