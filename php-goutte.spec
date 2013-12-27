%global github_owner    fabpot
%global github_name     Goutte
%global github_version  1.0.3
%global github_commit   75c9f23c4122caf4ea3e87a42a00b471366e707f

# "php": ">=5.3.0"
%global php_min_ver     5.3.0
# "guzzle/*": ">=3.0.5,<3.8-dev"
%global guzzle_min_ver  3.0.5
%global guzzle_max_ver  3.8
# "symfony/*": "~2.1"
%global symfony_min_ver 2.1
%global symfony_max_ver 3.0

Name:          php-goutte
Version:       %{github_version}
Release:       1%{dist}
Summary:       A simple PHP Web Scraper

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# For tests
BuildRequires: php(language)           >= %{php_min_ver}
BuildRequires: php-symfony-browserkit  >= %{symfony_min_ver}
BuildRequires: php-symfony-browserkit  <  %{symfony_max_ver}
BuildRequires: php-symfony-cssselector >= %{symfony_min_ver}
BuildRequires: php-symfony-cssselector <  %{symfony_max_ver}
BuildRequires: php-symfony-domcrawler  >= %{symfony_min_ver}
BuildRequires: php-symfony-domcrawler  <  %{symfony_max_ver}
BuildRequires: php-symfony-finder      >= %{symfony_min_ver}
BuildRequires: php-symfony-finder      <  %{symfony_max_ver}
BuildRequires: php-symfony-process     >= %{symfony_min_ver}
BuildRequires: php-symfony-process     <  %{symfony_max_ver}
BuildRequires: php-pear(guzzlephp.org/pear/Guzzle) >= %{guzzle_min_ver}
BuildRequires: php-pear(guzzlephp.org/pear/Guzzle) <  %{guzzle_max_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# For tests: phpcompatinfo (computed from v1.0.3)
BuildRequires: php-curl
BuildRequires: php-spl

Requires:      php(language)           >= %{php_min_ver}
Requires:      php-symfony-browserkit  >= %{symfony_min_ver}
Requires:      php-symfony-browserkit  <  %{symfony_max_ver}
Requires:      php-symfony-cssselector >= %{symfony_min_ver}
Requires:      php-symfony-cssselector <  %{symfony_max_ver}
Requires:      php-symfony-domcrawler  >= %{symfony_min_ver}
Requires:      php-symfony-domcrawler  <  %{symfony_max_ver}
Requires:      php-symfony-finder      >= %{symfony_min_ver}
Requires:      php-symfony-finder      <  %{symfony_max_ver}
Requires:      php-symfony-process     >= %{symfony_min_ver}
Requires:      php-symfony-process     <  %{symfony_max_ver}
Requires:      php-pear(guzzlephp.org/pear/Guzzle) >= %{guzzle_min_ver}
Requires:      php-pear(guzzlephp.org/pear/Guzzle) <  %{guzzle_max_ver}
# phpcompatinfo (computed from v1.0.3)
Requires:      php-curl

%description
Goutte is a screen scraping and web crawling library for PHP.

Goutte provides a nice API to crawl websites and extract data
from the HTML/XML responses.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php/%{github_name}
cp -p %{github_name}/Client.php %{buildroot}/%{_datadir}/php/%{github_name}/


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

%{_bindir}/phpunit -d date.timezone="UTC"


%files
%doc LICENSE *.md CHANGELOG composer.json
%{_datadir}/php/%{github_name}/Client.php


%changelog
* Fri Dec 27 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.3-1
- Initial package
