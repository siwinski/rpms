%global libname monolog

Name:      php-%{libname}
Version:   1.1.0
Release:   1%{?dist}
Summary:   Logging for PHP 5.3

Group:     Development/Libraries
License:   Public Domain
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
Requires:  php-date
Requires:  php-json
Requires:  php-libxml
Requires:  php-pcre
Requires:  php-spl
# phpci dist specific requires
%{?fedora:Requires: php-filter}

%description
%{summary}.


%prep
%setup -q -c

# Move docs
mkdir -p %{libname}-docs
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
* Sun Jul 22 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.0-1
- Initial package
