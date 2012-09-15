%global libname monolog

Name:      php-%{libname}
Version:   1.2.1
Release:   1%{?dist}
Summary:   Logging for PHP 5.3

Group:     Development/Libraries
License:   MIT
URL:       https://github.com/Seldaek/%{libname}/
# To create source tarball:
# 1) Clone git repo and checkout version tag:
#    git clone -b VERSION https://github.com/Seldaek/monolog.git
# 2) Create tarball:
#    tar --exclude-vcs -czf monolog-VERSION.tar.gz monolog
Source0:   %{libname}-%{version}.tar.gz

BuildArch: noarch

Requires:  php-common >= 5.3.0
# phpci requires
Requires:  php-curl
Requires:  php-date
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-sockets
Requires:  php-spl
# phpci dist specific requires
%{?fedora:Requires: php-filter}

%description
%{summary}.

Optional packages:
* php-pecl-amqp
      Allow sending log messages to an AMQP server (1.0+ required)
* php-pecl-mongo
      Allow sending log messages to a MongoDB server
* php-swift-Swift
      Sends emails using a Swift_Mailer instance
* https://github.com/mlehner/gelf-php
      Allow sending log messages to a GrayLog2 server


%prep
%setup -q -c

# Move docs
mkdir %{libname}-docs
mv -f \
    %{libname}/*.mdown \
    %{libname}/LICENSE \
    %{libname}/composer.json \
    %{libname}/doc \
    %{libname}-docs

# Clean up unnecessary files
rm -f %{libname}/.travis.yml

# Remove tests -- they require composer installs and autoloader to run
rm -rf \
    %{libname}/phpunit.xml.dist \
    %{libname}/tests


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
cp -pr %{libname}/* $RPM_BUILD_ROOT%{_datadir}/php/%{libname}/


%files
%doc %{libname}-docs/*
%{_datadir}/php/%{libname}


%changelog
* Fri Sep 7 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.2.1-1
- Updated to upstream version 1.2.1
- Fixed license
- Added optional packages to description
- Added additional requires

* Sun Jul 22 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.0-1
- Initial package
