%global github_owner    fabpot
%global github_name     Goutte
%global github_version  1.0.3
%global github_commit   e83f8f9d133dbf9b0254c2874f9c5c6287a3a8e0
# There are commits after the 1.0.3 version tag
%global github_release  .20140118git%(c=%{github_commit}; echo ${c:0:7})

# "php": ">=5.3.0"
%global php_min_ver     5.3.0
# "guzzle/*": ">=3.0.5,<3.9-dev"
%global guzzle_min_ver  3.0.5
%global guzzle_max_ver  3.9
# "symfony/*": "~2.1"
%global symfony_min_ver 2.1
%global symfony_max_ver 3.0

Name:          php-goutte
Version:       %{github_version}
Release:       1%{?github_release}%{dist}
Summary:       A simple PHP web scraper

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
# For tests: phpcompatinfo (computed from v1.0.3 commit e83f8f9d133dbf9b0254c2874f9c5c6287a3a8e0)
BuildRequires: php-curl

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
# phpcompatinfo (computed from v1.0.3 commit e83f8f9d133dbf9b0254c2874f9c5c6287a3a8e0)
Requires:      php-curl

%description
Goutte is a screen scraping and web crawling library for PHP.

Goutte provides a nice API to crawl websites and extract data
from the HTML/XML responses.


%prep
%setup -qn %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php/%{github_name}
cp -p %{github_name}/Client.php %{buildroot}/%{_datadir}/php/%{github_name}/


%check
# Create tests' bootstrap
mkdir vendor
cat > vendor/autoload.php <<'AUTOLOAD'
<?php
spl_autoload_register(function ($class) {
    $src = str_replace(array('\\', '_'), '/', $class).'.php';
    @include_once $src;
});
AUTOLOAD

# Create PHPUnit config w/ colors turned off
sed 's/colors="true"/colors="false"/' phpunit.xml.dist > phpunit.xml

%{_bindir}/phpunit -d date.timezone="UTC"


%files
%doc LICENSE CHANGELOG README.rst composer.json
%{_datadir}/php/%{github_name}/Client.php


%changelog
* Mon Jan 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.3-1.20140118gite83f8f9
- Initial package
