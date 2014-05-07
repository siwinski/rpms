%global github_owner    nicolas-grekas
%global github_name     Patchwork-UTF8
%global github_version  1.1.21
%global github_commit   f45ba8bc7962b7356847724989a6949b68d975a2

# "php": ">=5.3.0" (composer.json)
%global php_min_ver     5.3.3

# "lib-pcre": ">=7.3" (composer.json)
%global pcre_min_ver    7.3

Name:      php-patchwork-utf8
Version:   %{github_version}
Release:   1%{?github_release}%{dist}
Summary:   Handling of UTF-8 and grapheme clusters for PHP

Group:     Development/Libraries
License:   ASL 2.0 or GPLv2
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch

# composer.json
Requires:  php(language) >= %{php_min_ver}
Requires:  pcre          >= %{pcre_min_ver}
Requires:  php-pcre
# composer.json (optional)
Requires:  php-intl
Requires:  php-iconv
Requires:  php-mbstring
# phpcompatinfo (computed from version 1.1.21)
Requires:  php-filter
Requires:  php-xml

%description
Patchwork UTF-8 gives PHP developers extensive, portable and performant
handling of UTF-8 and grapheme clusters [1].

It provides both :
* a portability layer for mbstring, iconv, and intl Normalizer and grapheme_*
  functions
* an UTF-8 grapheme clusters aware replica of native string functions

It can also serve as a documentation source referencing the practical problems
that arise when handling UTF-8 in PHP: Unicode concepts, related algorithms,
bugs in PHP core, workarounds, etc.

[1] http://unicode.org/reports/tr29/


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -rp class/Patchwork %{buildroot}%{_datadir}/php/


%check
# Upstream tests not provided in export
# See https://github.com/nicolas-grekas/Patchwork-UTF8/blob/master/.gitattributes


%files
%doc *.md composer.json
%{_datadir}/php/Patchwork


%changelog
* Sun May 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.21-1
- Initial package
