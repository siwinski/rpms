#
# Fedora spec file for simplesamlphp
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     simplesamlphp
%global github_name      simplesamlphp
%global github_version   1.14.7
%global github_commit    f5ff7c4643b9b784957f5e1fbf86fc740cd6b78a

%global composer_vendor  simplesamlphp
%global composer_project simplesamlphp

# "php": ">=5.3"
%global php_min_ver 5.3
# "robrichards/xmlseclibs": "~1.4.1"
%global robrichards_xmlseclibs_min_ver 1.4.1
%global robrichards_xmlseclibs_max_ver 1.5.0
# "simplesamlphp/saml2": "~1.7"
%global simplesamlphp_saml2_min_ver 1.7
%global simplesamlphp_saml2_max_ver 2.0
# "whitehat101/apr1-md5": "~1.0"
%global whitehat101_apr1_md5_min_ver 1.0
%global whitehat101_apr1_md5_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%global simplesamlphp     %{_datadir}/%{name}
%global simplesamlphp_etc %{_sysconfdir}/%{name}
%global simplesamlphp_log %{_localstatedir}/log/%{name}
%global simplesamlphp_var %{_localstatedir}/lib/%{name}

%global rpmconfigdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       SAML2 PHP library from SimpleSAMLphp

Group:         Development/Libraries
License:       LGPLv2
URL:           https://simplesamlphp.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz
# Autoloader
Source1:       %{name}-autoload.php
# Apache HTTPD config
Source2:       %{name}.conf
# RPM macros
Source3:       macros.%{name}

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli >= %{php_min_ver}

# composer.json
Requires:      php(language)                        >= %{php_min_ver}
Requires:      php-composer(robrichards/xmlseclibs) <  %{robrichards_xmlseclibs_max_ver}
Requires:      php-composer(robrichards/xmlseclibs) >= %{robrichards_xmlseclibs_min_ver}
Requires:      php-composer(simplesamlphp/saml2)    <  %{simplesamlphp_saml2_max_ver}
Requires:      php-composer(simplesamlphp/saml2)    >= %{simplesamlphp_saml2_min_ver}
Requires:      php-composer(whitehat101/apr1-md5)   <  %{whitehat101_apr1_md5_max_ver}
Requires:      php-composer(whitehat101/apr1-md5)   >= %{whitehat101_apr1_md5_min_ver}
# phpcompatinfo (computed from version 1.14.7)
Requires:      php-curl
Requires:      php-date
Requires:      php-dom
Requires:      php-fileinfo
Requires:      php-hash
Requires:      php-json
Requires:      php-libxml
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-posix
Requires:      php-reflection
Requires:      php-session
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

%if 0%{?fedora} >= 21
# Webserver
Requires:      %{name}-webserver = %{version}-%{release}
## Providers:
## - simplesamlphp-httpd
## - FUTURE PLANNED: simplesamlphp-nginx
Recommends:    %{name}-httpd = %{version}-%{release}
#Suggests:      %%{name}-nginx = %%{version}-%%{release}

# Weak dependencies
Suggests:      php-ldap
Suggests:      php-pecl(krb5)
Suggests:      php-pecl(oauth)
%else
Requires:      %{name}-httpd = %{version}-%{release}
%endif

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
SimpleSAMLphp is an award-winning [1] application written in native PHP that
deals with authentication. The project is led by UNINETT [2], has a large user
base [3], a helpful user community [4] and a large set of external
contributors [5]. The main focus of SimpleSAMLphp is providing support for:

* SAML 2.0 as a Service Provider (SP) [6]
* SAML 2.0 as an Identity Provider (IdP) [7]

However, it also supports some other identity protocols and frameworks, such
as Shibboleth 1.3, A-Select, CAS, OpenID, WS-Federation or OAuth, and is easily
extendable [8], so you can develop your own modules if you like.

With the memcache session handler, SimpleSAMLphp scales pretty well. A
replication layer is built upon memcache, such that an unlimited number
of SimpleSAMLphp web front-ends can work with a back-end matrix of memcache
servers with both replication (fail-over) and load-balancing.

SimpleSAMLphp is tested with several other federation software implementations.
Among others; Shibboleth 1.3, Shibboleth 2.2, PingID, Sun Federation Manager,
Sun Federated Access Manager, Sun Access Manager, mod_mellon, CAS, etc. If
someone discovers incompatibility issues, we try to sort them out as fast as
possible if reported properly through the issue tracker.

Autoloader: %{simplesamlphp}/autoload.php

[1] %{url}/awards
[2] http://uninett.no/
[3] %{url}/users
[4] %{url}/lists
[5] %{url}/developers
[6] %{url}/samlsp
[7] %{url}/samlidp
[8] %{url}/modules
[9] https://github.com/%{github_owner}/%{github_name}/issues

# ------------------------------------------------------------------------------

%package httpd

Summary:    HTTPD integration for %{name}

Requires:   %{name} = %{version}-%{release}
Requires:   httpd
Requires:   httpd-filesystem
%if 0%{?fedora} >= 21
Requires:   php(httpd)
# php(httpd) providers
Recommends: mod_php
Suggests:   php-fpm
%else
Requires:   mod_php
%endif

Provides:   %{name}-webserver = %{version}-%{release}

%description httpd
%{summary}.

#-------------------------------------------------------------------------------

%package doc

Summary: SimpleSAMLphp: Additional documentation

Requires: %{name} = %{version}-%{release}

%description doc
SimpleSAMLphp: Additional documentation.

# ------------------------------------------------------------------------------

%prep
%setup -qn %{github_name}-%{github_commit}

: Remove git files
find . -name '.git*' -print0 | xargs -0 rm

: Update default configs
sed \
    -e '/baseurlpath/s#simplesaml#simplesamlphp#' \
    -e '/certdir/s#cert/#%{simplesamlphp_var}/cert/#' \
    -e '/datadir/s#data/#%{simplesamlphp_var}/data/#' \
    -e '/loggingdir/s#log/#%{simplesamlphp_log}/#' \
    -e 's/na@example.org/root@localhost.localdomain/' \
    -i config-templates/config.php

: Copy other sources into build dir
mkdir .rpm
cp -p %{SOURCE1} .rpm/
cp -p %{SOURCE2} .rpm/
cp -p %{SOURCE3} .rpm/

: Update dynamic values in sources
sed \
    -e 's:__SIMPLESAMLPHP__:%{simplesamlphp}:' \
    -e 's:__SIMPLESAMLPHP_ETC__:%{simplesamlphp_etc}:' \
    -e 's:__SIMPLESAMLPHP_LOG__:%{simplesamlphp_log}:' \
    -e 's:__SIMPLESAMLPHP_VAR__:%{simplesamlphp_var}:' \
    -e 's:__PHPDIR__:%{phpdir}:' \
    -e 's:__SPEC_VERSION__:%{version}:' \
    -e 's:__SPEC_RELEASE__:%{release}:' \
    -i .rpm/*

: Docs
mv docs .rpm/

: Autoloader
cp .rpm/%{name}-autoload.php autoload.php

: Symlink autoloader used by app
mv lib/_autoload.php lib/_autoload.php.dist
ln -s ../autoload.php lib/_autoload.php


%build
# Empty build section, nothing to build


%install
: Main
mkdir -p %{buildroot}%{simplesamlphp}
cp -rp * %{buildroot}%{simplesamlphp}/

# See https://simplesamlphp.org/docs/development/simplesamlphp-install-repo

: Initialize configuration
mkdir -p %{buildroot}%{simplesamlphp_etc}
mv %{buildroot}%{simplesamlphp}/config* %{buildroot}%{simplesamlphp_etc}/
cp -rp %{buildroot}%{simplesamlphp_etc}/config-templates/* \
    %{buildroot}%{simplesamlphp_etc}/config/
ln -s %{simplesamlphp_etc}/config-templates %{buildroot}%{simplesamlphp}/config-templates
ln -s %{simplesamlphp_etc}/config %{buildroot}%{simplesamlphp}/config

: Initialize metadata
mkdir -p %{buildroot}%{simplesamlphp_etc}
mv %{buildroot}%{simplesamlphp}/metadata* %{buildroot}%{simplesamlphp_etc}/
cp -rp %{buildroot}%{simplesamlphp_etc}/metadata-templates/* \
    %{buildroot}%{simplesamlphp_etc}/metadata/
ln -s %{simplesamlphp_etc}/metadata-templates %{buildroot}%{simplesamlphp}/metadata-templates
ln -s %{simplesamlphp_etc}/metadata %{buildroot}%{simplesamlphp}/metadata

: Config certdir and datadir
mkdir -p %{buildroot}%{simplesamlphp_var}/{cert,data}
ln -s %{simplesamlphp_var}/cert %{buildroot}%{simplesamlphp}/cert
ln -s %{simplesamlphp_var}/data %{buildroot}%{simplesamlphp}/data

: Config loggingdir
mkdir -p %{buildroot}%{simplesamlphp_log}
ln -s %{simplesamlphp_log} %{buildroot}%{simplesamlphp}/log

: Apache HTTPD
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -pm 0644 .rpm/%{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

: Docs
%if 0%{?fedora} >= 20
ln -s %{_docdir}/%{name}-doc %{buildroot}%{simplesamlphp}/docs
%else
ln -s %{_docdir}/%{name}-doc-%{version} %{buildroot}%{simplesamlphp}/docs
%endif

: RPM macros
mkdir -p %{buildroot}%{rpmconfigdir}
install -pm 0644 .rpm/macros.%{name} %{buildroot}%{rpmconfigdir}/


%check
: Library version value check
%{_bindir}/php -r '
    require_once "%{buildroot}%{simplesamlphp}/lib/SimpleSAML/Configuration.php";
    $configuration = new \SimpleSAML_Configuration(array(), "");
    $version = $configuration->getVersion();
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%if %{with_tests}
: Tests skipped because upstream requires an old version of PHPUnit and tests fail with current versions
%else
: Tests skipped
%endif

# ------------------------------------------------------------------------------

%{!?_licensedir:%global license %%doc}

%files
%license COPYING
%license LICENSE
%doc *.md
%doc composer.*
# Main
%{simplesamlphp}
%exclude %{simplesamlphp}/*.md
%exclude %{simplesamlphp}/composer.*
%exclude %{simplesamlphp}/COPYING
%exclude %{simplesamlphp}/LICENSE
%exclude %{simplesamlphp}/docs
# Config
%dir                         %{simplesamlphp_etc}
## Managed upstream config templates
%config                      %{simplesamlphp_etc}/config-templates
%config                      %{simplesamlphp_etc}/metadata-templates
# Other
%dir %{simplesamlphp_var}
# RPM macros
%{rpmconfigdir}/macros.%{name}

# ------------------------------------------------------------------------------

%files httpd
                             %config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%dir %attr(0770,root,apache)                    %{simplesamlphp_etc}/config
     %attr(0640,root,apache) %config(noreplace) %{simplesamlphp_etc}/config/*
%dir %attr(0770,root,apache)                    %{simplesamlphp_etc}/metadata
     %attr(0640,root,apache) %config(noreplace) %{simplesamlphp_etc}/metadata/*
%dir %attr(0770,root,apache)                    %{simplesamlphp_log}
%dir %attr(0770,root,apache)                    %{simplesamlphp_var}/cert
%dir %attr(0770,root,apache)                    %{simplesamlphp_var}/data

# ------------------------------------------------------------------------------

%files doc
%doc .rpm/docs/*
%{simplesamlphp}/docs

# ------------------------------------------------------------------------------

%changelog
* Tue Aug 02 2016 Shawn Iwinski <shawn@iwin.ski> - 1.14.7-1
- Update to 1.14.7
- Add library version value check

* Thu Jul 14 2016 Shawn Iwinski <shawn@iwin.ski> - 1.14.5-2
- Fix EPEL 6/7

* Thu Jul 14 2016 Shawn Iwinski <shawn@iwin.ski> - 1.14.5-1
- Initial package
