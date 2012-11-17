%global libname scssphp

Name:          php-%{libname}
Version:       0.0.4
Release:       1%{?dist}
Summary:       A compiler for SCSS written in PHP

Group:         Development/Libraries
License:       MIT or GPLv3
URL:           http://leafo.net/%{libname}
Source0:       %{url}/src/%{libname}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: help2man
# Test requires
BuildRequires: php-common
# Test requires: phpci
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-pcre

Requires:      php-common
# phpci requires
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
%setup -q -n %{libname}

# AWAITING https://github.com/leafo/scssphp/pull/23
# Create man page for bin
# Required here instead of %%build b/c path to include file is changed
# and files moved
#help2man --no-info pscss > pscss.1

# Update bin require
sed 's#scss.inc.php#%{_datadir}/php/%{libname}/scss.inc.php#' -i pscss

# Update tests' require
find tests -type f -print0 | xargs -0 sed -i \
    's#__DIR__ . "/../scss.inc.php"#"%{_datadir}/php/%{libname}/scss.inc.php"#'


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{libname}
cp -p scss.inc.php %{buildroot}%{_datadir}/php/%{libname}/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
cp -rp tests/* %{buildroot}%{_datadir}/tests/%{name}/

mkdir -p -m 755 %{buildroot}%{_bindir}
cp -p pscss %{buildroot}%{_bindir}

# AWAITING https://github.com/leafo/scssphp/pull/23
#mkdir -p  %{buildroot}%{_mandir}/man1
#cp -p pscss.1  %{buildroot}%{_mandir}/man1/


%check
# Update tests' require to use buildroot
find tests -type f -print0 | xargs -0 sed -i \
    's#%{_datadir}#%{buildroot}%{_datadir}#'

%{_bindir}/phpunit tests


%files
%doc *.md composer.json
%{_datadir}/php/%{libname}
%{_datadir}/tests/%{name}
%{_bindir}/pscss


%changelog
* Sat Nov 17 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.0.4-1
- Initial package
