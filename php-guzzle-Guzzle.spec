%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}

%global pear_channel guzzlephp.org/pear
%global pear_name    %(echo %{name} | sed -e 's/^php-guzzle-//' -e 's/-/_/g')

Name:             php-guzzle-Guzzle
Version:          3.0.6
Release:          1%{?dist}
Summary:          PHP HTTP client library and framework for building RESTful web service clients

Group:            Development/Libraries
# License file request: https://github.com/guzzle/guzzle/issues/192
License:          MIT
URL:              http://guzzlephp.org
Source0:          http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)
BuildRequires:    php-channel(%{pear_channel})

Requires:         php-common >= 5.3.2
Requires:         php-pear(PEAR)
Requires:         php-channel(%{pear_channel})
Requires:         php-pear(pear.symfony.com/EventDispatcher) >= 2.1.0
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpci requires
Requires:         php-ctype
Requires:         php-curl
Requires:         php-date
Requires:         php-hash
Requires:         php-intl
Requires:         php-json
Requires:         php-pcre
Requires:         php-reflection
Requires:         php-simplexml
Requires:         php-spl
%{?fedora:Requires: php-filter}

Provides:         php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
Guzzle takes the pain out of sending HTTP requests and the redundancy out
of creating web service clients.

Guzzle is a framework that includes the tools needed to create a robust web
service client, including: Service descriptions for defining the inputs and
outputs of an API, resource iterators for traversing paginated resources,
batching for sending a large number of requests as efficiently as possible.

* All the power of cURL with a simple interface
* Persistent connections and parallel requests
* Streams request and response bodies
* Service descriptions for quickly building clients
* Powered by the Symfony2 EventDispatcher
* Use all of the code or only specific components
* Plugins for caching, logging, OAuth, mocks, and more

Optional dependencies:
* Zend Framework
* Doctrine
* Monolog


%prep
%setup -q -c

# Change role of README file from "data" to "doc"
# https://github.com/guzzle/guzzle/issues/193
sed '/README/s/role="data"/role="doc"/' -i package.xml

# package.xml is version 2.0
mv package.xml %{pear_name}-%{version}/%{name}.xml


%build
# Empty build section, nothing to build


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


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
%{pear_phpdir}/%{pear_name}


%changelog
* Sun Dec 16 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 3.0.6-1
- Updated to upstream version 3.0.6

* Sat Dec  8 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 3.0.5-1
- Initial package
