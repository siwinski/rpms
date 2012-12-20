%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}

%global lib_name    PHPParser
%global github_name PHP-Parser

Name:             php-%{lib_name}
Version:          0.9.3
Release:          1%{?dist}
Summary:          A PHP parser written in PHP

Group:            Development/Libraries
License:          BSD
URL:              https://github.com/nikic/%{github_name}
Source0:          %{url}/archive/v%{version}.tar.gz

BuildArch:        noarch
# Test build requires
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# Test build requires: phpci
BuildRequires: php-ctype
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-tokenizer
%if 0%{?fedora}
BuildRequires: php-filter
BuildRequires: php-xmlreader
BuildRequires: php-xmlwriter
%else
BuildRequires: php-libxml
%endif

Requires:         php(language)
# phpci requires
Requires:         php-ctype
Requires:         php-pcre
Requires:         php-spl
Requires:         php-tokenizer
%if 0%{?fedora}
Requires:         php-filter
Requires:         php-xmlreader
Requires:         php-xmlwriter
%else
Requires:         php-libxml
%endif

%description
A PHP parser written in PHP to simplify static analysis and code manipulation.


%package test
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description test
%{summary}.


%prep
%setup -q -n %{github_name}-%{version}

# Update and move bootstrap
sed "s:dirname(__FILE__) . '/PHPParser:'%{lib_name}:" \
    -i lib/bootstrap.php
mv lib/bootstrap.php lib/%{lib_name}/

# Update and move PHPUnit config
sed -e 's:./lib/bootstrap.php:%{_datadir}/php/%{lib_name}/bootstrap.php:' \
    -e 's:./lib/PHPParser/:%{_datadir}/php/%{lib_name}/:' \
    -e 's:./test/:./:' \
    -i phpunit.xml.dist
mv phpunit.xml.dist test/

# Remove executable bit from composer.json
chmod a-x composer.json


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp lib/%{lib_name} %{buildroot}%{_datadir}/php/

mkdir -p -m 755 %{buildroot}%{_datadir}/test/%{name}
cp -rp test/* %{buildroot}%{_datadir}/test/%{name}/


%check
pwd
ls
%{_bindir}/phpunit \
    --bootstrap= lib/%{lib_name}/bootstrap.php \
    -c test/phpunit.xml.dist \
    -d include_path="./lib:./test:.:/usr/share/pear"


%files
%doc LICENSE *.md doc grammar composer.json
%{_datadir}/php/%{lib_name}

%files test
%dir %{_datadir}/test
     %{_datadir}/test/%{name}


%changelog
* Wed Dec 19 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 0.9.3-1
- Initial package
