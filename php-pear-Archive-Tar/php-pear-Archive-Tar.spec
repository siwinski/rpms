#
# Fedora spec file for php-pear-Archive-Tar
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Archive_Tar

# <php>
#   <min>5.2.0</min>
# </php>
%global php_min_ver 5.2.0
# <pearinstaller>
#   <min>1.9.0</min>
# </pearinstaller>
%global pear_min_ver 1.9.0

Name:             php-pear-Archive-Tar
Version:          1.4.2
Release:          1%{?github_release}%{?dist}
Summary:          Tar file management class

Group:            Development/Libraries
License:          BSD
URL:              https://pear.php.net/package/%{pear_name}/
Source0:          http://download.pear.php.net/package/%{pear_name}-%{version}.tgz

BuildArch:        noarch
BuildRequires:    php(language) >= %{php_min_ver}
BuildRequires:    php-pear >= %{pear_min_ver}

Requires:         php(language) >= %{php_min_ver}
Requires:         php-pear >= %{pear_min_ver}
Requires(post):   %{__pear}
Requires(postun): %{__pear}
# phpcompatinfo (computed from version 1.4.2)
Requires:         php-bz2
Requires:         php-date
Requires:         php-pcre
Requires:         php-posix
Requires:         php-zlib

# php-pear-{PEAR_NAME}
Provides:         php-pear-%{pear_name} = %{version}-%{release}
# PEAR
Provides:         php-pear(%{pear_name}) = %{version}
# Composer
Provides:         php-composer(pear/archive_tar) = %{version}

%description
This class provides handling of tar files in PHP.
It supports creating, listing, extracting and adding to tar files.
Gzip support is available if PHP has the zlib extension built-in or
loaded. Bz2 compression is also supported with the bz2 extension loaded.


%prep
%setup -q -c

cd %{pear_name}-%{version}

: package.xml is V2
mv ../package.xml %{name}.xml


%build


%install
cd %{pear_name}-%{version}

: PEAR install
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

: Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

: Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%check
: No upstream tests


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_phpdir}/Archive/Tar.php
%{pear_xmldir}/%{name}.xml


%changelog
* Tue Aug 09 2016 Shawn Iwinski <shawn@iwin.ski> - 1.4.2-1
- Initial package
