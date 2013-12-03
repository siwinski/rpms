%global github_owner   fabpot
%global github_name    Twig-extensions
%global github_version 1.0.1
%global github_commit  f91a82ec225e5bb108e01a0f93c9be04f84dcfa0

%global php_min_ver    5.3.3
# "twig/twig": "~1.0"
%global twig_min_ver   1.0
%global twig_max_ver   2.0

Name:          php-twig-extensions
Version:       %{github_version}
Release:       1%{dist}
Summary:       Twig extensions

Group:         Development/Libraries
License:       MIT
URL:           http://twig.sensiolabs.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
BuildRequires: php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
BuildRequires: php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
# For tests: phpcompatinfo
BuildRequires: php-intl
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl

Requires:      php(language) >= %{php_min_ver}
Requires:      php-pear(pear.twig-project.org/Twig) >= %{twig_min_ver}
Requires:      php-pear(pear.twig-project.org/Twig) <  %{twig_max_ver}
# phpcompatinfo
Requires:      php-intl
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl

%description
Common additional features for Twig that do not directly belong in core Twig.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php
cp -rp lib/* %{buildroot}/%{_datadir}/php/


%check
# Create tests' bootstrap
mkdir vendor
( cat <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace('\\', '/', str_replace('_', '/', $class)).'.php';
    @include_once $src;
});
AUTOLOAD
) > vendor/autoload.php

# Create PHPUnit config w/ colors turned off
cat phpunit.xml.dist \
    | sed 's/colors="true"/colors="false"/' \
    > phpunit.xml

%{_bindir}/phpunit --include-path ./lib:./test -d date.timezone="UTC"


%files
%doc LICENSE README composer.json doc/*
%dir %{_datadir}/php/Twig
     %{_datadir}/php/Twig/Extensions


%changelog
* Mon Dec 02 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.1-1
- Initial package
