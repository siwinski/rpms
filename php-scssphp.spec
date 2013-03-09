%global github_owner   leafo
%global github_name    scssphp
%global github_version 0.0.4
%global github_commit  3463d7dab573b98a45308d6cb8bd29f358ee313a
%global github_date    20130301

%global github_release %{github_date}git%(c=%{github_commit}; echo ${c:0:7})

%global lib_name       scssphp
%global php_min_ver    5.3.0

Name:          php-%{lib_name}
Version:       %{github_version}
Release:       2.%{github_release}%{?dist}
Summary:       A compiler for SCSS written in PHP

Group:         Development/Libraries
License:       MIT or GPLv3
URL:           http://leafo.net/%{lib_name}
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
BuildRequires: help2man
# For tests
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpci
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-pcre

Requires:      php-common >= %{php_min_ver}
# phpci
Requires:      php-ctype
Requires:      php-date
Requires:      php-pcre

%description
SCSS (http://sass-lang.com/) is a CSS preprocessor that adds many features like
variables, mixins, imports, color manipulation, functions, and tons of other
powerful features.

The entire compiler comes in a single class file ready for including in any kind
of project in addition to a command line tool for running the compiler from the
terminal.

scssphp implements SCSS (3.1.20). It does not implement the SASS syntax, only
the SCSS syntax.


%prep
%setup -q -n %{github_name}-%{github_commit}

# Create man page for bin
# Required here b/c path to include file is changed in next command
help2man --no-info ./pscss > pscss.1

# Update bin shebang and require
sed -e 's#/usr/bin/env php#%{__php}#' \
    -e 's#scss.inc.php#%{_datadir}/php/%{lib_name}/scss.inc.php#' \
    -i pscss


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{lib_name}
install -p -m 644 scss.inc.php %{buildroot}%{_datadir}/php/%{lib_name}/

mkdir -p -m 755 %{buildroot}%{_bindir}
install -p -m 755 pscss %{buildroot}%{_bindir}/

mkdir -p -m 755  %{buildroot}%{_mandir}/man1
install -p -m 644 pscss.1 %{buildroot}%{_mandir}/man1/


%check
%{_bindir}/phpunit tests


%files
%doc *.md composer.json
%doc %{_mandir}/man1/pscss.1*
%{_datadir}/php/%{lib_name}
%{_bindir}/pscss


%changelog
* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.0.4-2.20130301git3463d7d
- Updated to latest snapshot
- Added man page
- Removed tests from package

* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.0.4-1
- Initial package
