# TODO:
# * php-lessphp.noarch: W: spurious-executable-perm /usr/share/doc/php-lessphp-0.3.5/tests/bootstrap.sh
# * php-lessphp.noarch: W: no-manual-page-for-binary plessc
# * Run tests in %%check
# * "tests" sub-package?

%global libname lessphp

Name:      php-%{libname}
Version:   0.3.5
Release:   1%{?dist}
Summary:   A compiler for LESS written in PHP

Group:     Development/Libraries
License:   MIT or GPLv3
URL:       http://leafo.net/lessphp/
Source0:   http://leafo.net/lessphp/src/%{libname}-%{version}.tar.gz

BuildArch: noarch

Requires:  php-common >= 5.1.0
# phpci requires
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl

%description
lessphp is a compiler that generates CSS from a super-set language which
adds a collection of convenient features often seen in other languages.
All CSS is compatible with LESS, so you can start using new features
with your existing CSS.

It is designed to be compatible with less.js (http://lesscss.org/), and
suitable as a drop in replacement for PHP projects.


%prep
%setup -q -c


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
install -p -m 644 %{libname}/lessc.inc.php $RPM_BUILD_ROOT%{_datadir}/php/%{libname}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p %{libname}/plessc $RPM_BUILD_ROOT%{_bindir}


%files
%doc %{libname}/composer.json
%doc %{libname}/docs
%doc %{libname}/LICENSE
%doc %{libname}/README.md
%doc %{libname}/tests
%{_datadir}/php/%{libname}/lessc.inc.php
%{_bindir}/plessc


%changelog
* Sat Jul 7 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.5-1
- Initial package
