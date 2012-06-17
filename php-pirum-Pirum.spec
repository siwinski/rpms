%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_channel pear.pirum-project.org
%global pear_name %(echo %{name} | sed -e 's/^php-pirum-//' -e 's/-/_/g')

Name:             php-pirum-Pirum
Version:          1.1.4
Release:          1%{?dist}
Summary:          A simple PEAR channel server manager

Group:            Development/Libraries
License:          MIT
URL:              http://pirum.sensiolabs.org
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-common >= 5.2.1
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-date
Requires:         php-json
Requires:         php-pcre
Requires:         php-posix
Requires:         php-simplexml
Requires:         php-spl
Requires:         php-zlib

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
Pirum is a simple and nice looking PEAR channel server manager that lets you
setup PEAR channel servers in a matter of minutes. Pirum is best suited when
you want to create small PEAR channels for a few packages written by a few
developers.

Pirum consists of just one file: a command line tool written in PHP. There are
no external dependencies, no need for a database, and nothing needs to be
installed or configured.

As of Pirum 1.1, a composer repository is generated as well.


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
%{_bindir}/pirum


%changelog
* Sun Jun 17 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.4-1
- Initial package
