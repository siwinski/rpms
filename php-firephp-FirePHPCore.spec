%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_channel pear.firephp.org
%global pear_name %(echo %{name} | sed -e 's/^php-firephp-//' -e 's/-/_/g')

Name:             php-firephp-FirePHPCore
Version:          0.3.2
Release:          1%{?dist}
Summary:          Firebug Extension for AJAX Development

Group:            Development/Libraries
License:          BSD
URL:              http://www.firephp.org
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-common >= 5.2.0
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-json
Requires:         php-mbstring
Requires:         php-pcre
Requires:         php-reflection
Requires:         php-libxml

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
FirePHP enables you to log to your Firebug Console (http://getfirebug.com)
using a simple PHP method call.

All data is sent via response headers and will not interfere with the content
on your page.

FirePHP is ideally suited for AJAX development where clean JSON and XML
responses are required.


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
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/%{pear_name}


%changelog
* Thu Sep 6 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.2-1
- Initial package
