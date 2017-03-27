# spec file for php-phpdocumentor-reflection-docblock2
#
# Copyright (c) 2014-2015 Remi Collet
#               2017 Remi Collet, Shawn Iwinski
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    d68dbdc53dc358a816f00b300704702b2eaff7b8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpDocumentor
%global gh_project   ReflectionDocBlock
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpdocumentor-reflection-docblock2
Version:        2.0.4
Release:        5%{?dist}
Summary:        DocBlock parser

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-composer(phpunit/phpunit)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, require
#        "php": ">=5.3.3"
# From composer.json, suggest
#        "dflydev/markdown": "1.0.*",
#        "erusev/parsedown": "~0.7"
Requires:       php(language) >= 5.3.3
# From phpcompatinfo report for 2.0.3
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(phpdocumentor/reflection-docblock) = %{version}

# Package rename (php-phpdocumentor-reflection-docblock => php-phpdocumentor-reflection-docblock2)
Obsoletes:      php-phpdocumentor-reflection-docblock < 2.0.4-5
Provides:       php-phpdocumentor-reflection-docblock = %{version}-%{release}


%description
The ReflectionDocBlock component of phpDocumentor provides a DocBlock
parser that is fully compatible with the PHPDoc standard.

With this component, a library can provide support for annotations via
DocBlocks or otherwise retrieve information that is embedded in a DocBlock.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv src/phpDocumentor/Reflection/DocBlock src/phpDocumentor/Reflection/DocBlock2
mv src/phpDocumentor/Reflection/DocBlock.php src/phpDocumentor/Reflection/DocBlock2.php


%build
phpab \
  --template fedora \
  --output   src/phpDocumentor/Reflection/DocBlock2/autoload.php \
  src/phpDocumentor/Reflection


%install
mkdir -p     %{buildroot}%{_datadir}/php
cp -pr src/* %{buildroot}%{_datadir}/php


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
for PHP_EXEC in %{_bindir}/php %{?rhel:php54 php55} php56 php70 php71; do
    if [ "%{_bindir}/php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit --verbose \
            --bootstrap %{buildroot}%{_datadir}/php/phpDocumentor/Reflection/DocBlock2/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/phpDocumentor
%dir %{_datadir}/php/phpDocumentor/Reflection
     %{_datadir}/php/phpDocumentor/Reflection/DocBlock2*


%changelog
* Mon Mar 27 2017 Shawn Iwinski <shawn@iwin.ski> - 2.0.4-5
- Package rename (php-phpdocumentor-reflection-docblock => php-phpdocumentor-reflection-docblock2)
- Switch autoloader to php-composer(fedora/autoloader)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4
- LICENSE is in upstream archive

* Tue Feb  3 2015 Remi Collet <remi@fedoraproject.org> - 2.0.3-2
- add LICENSE from upstream repository

* Fri Dec 19 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- initial package
- open https://github.com/phpDocumentor/ReflectionDocBlock/issues/40
  for missing LICENSE file
