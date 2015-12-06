#
# RPM spec file for php-aws-sdk2
#
# Copyright (c) 2013-2015 Joseph Marrero <jmarrero@fedoraproject.org>
#                         Gregor Tätzner <brummbq@fedoraproject.org>
#                         Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     aws
%global github_name      aws-sdk-php
%global github_version   2.8.21
%global github_commit    92642ca4906e6681a1301971cf41500d7c68581c

%global composer_vendor  aws
%global composer_project aws-sdk-php

%global pear_channel     pear.amazonwebservices.com
%global pear_name        sdk

# "php": ">=5.3.3"
%global php_min_ver      5.3.3
# "guzzle/guzzle": "~3.7"
%global guzzle_min_ver   3.7
%global guzzle_max_ver   4.0
# "doctrine/cache": "~1.0"
%global cache_min_ver    1.0
%global cache_max_ver    2.0
# "monolog/monolog": "~1.4"
%global monolog_min_ver  1.4
%global monolog_max_ver  2.0
# "symfony/yaml": "~2.1"
%global yaml_min_ver     2.1
%global yaml_max_ver     3.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-aws-sdk2
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Amazon Web Services framework for PHP

Group:         Development/Libraries
License:       ASL 2.0
URL:           http://aws.amazon.com/sdk-for-php/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli

# composer.json
Requires:      php(language)               >= %{php_min_ver}
Requires:      php-composer(guzzle/guzzle) >= %{guzzle_min_ver}
Requires:      php-composer(guzzle/guzzle) <  %{guzzle_max_ver}
# composer.json: optional
Requires:      php-openssl
# phpcompatinfo (computed from version 2.8.21)
Requires:      php-curl
Requires:      php-date
Requires:      php-hash
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-simplexml
Requires:      php-spl
# Autoloader
Requires:      php-composer(symfony/class-loader)

# Optional package version checks
Conflicts:     php-composer(doctrine/cache)  <  %{cache_min_ver}
Conflicts:     php-composer(doctrine/cache)  >= %{cache_max_ver}
Conflicts:     php-composer(monolog/monolog) <  %{monolog_min_ver}
Conflicts:     php-composer(monolog/monolog) >= %{monolog_max_ver}
Conflicts:     php-composer(symfony/yaml)    <  %{yaml_min_ver}
Conflicts:     php-composer(symfony/yaml)    >= %{yaml_max_ver}

# Rename
Obsoletes:     php-aws-sdk < 2.8.21
Provides:      php-aws-sdk = %{version}-%{release}
Conflicts:     php-composer(%{composer_vendor}/%{composer_project}) >= 3.0

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# PEAR
Provides:      php-pear(%{pear_channel}/%{pear_name}) = %{version}

%description
Amazon Web Services SDK for PHP enables developers to build solutions for
Amazon Simple Storage Service (Amazon S3), Amazon Elastic Compute Cloud
(Amazon EC2), Amazon SimpleDB, and more.

Optional:
* APC (php-pecl-apcu):
      Allows service description opcode caching, request and response caching,
      and credentials caching
* Doctrine Cache (php-doctrine-cache):
      Adds support for caching of credentials and responses
* Monolog (php-Monolog):
      Adds support for logging HTTP requests and responses
* Symfony YAML (php-symfony-yaml):
      Eases the ability to write manifests for creating jobs in AWS
      Import/Export

**** NOTE: This is major version 2.x of php-aws-sdk.  If you need a newer major
****       version, install php-aws-sdk instead.

%prep
%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/Aws/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 *
 * Created by %{name}-%{version}-%{release}
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($fedoraClassLoader) || !($fedoraClassLoader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '%{phpdir}/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $fedoraClassLoader = new \Symfony\Component\ClassLoader\ClassLoader();
    $fedoraClassLoader->register();
}

$fedoraClassLoader->addPrefix('Aws\\', dirname(__DIR__));

foreach (array(
    '%{phpdir}/Doctrine/Common/Cache/autoload.php',
    '%{phpdir}/Monolog/autoload.php',
    '%{phpdir}/Symfony/Component/Yaml/autoload.php',
) as $dependencyAutoloader) {
    if (file_exists($dependencyAutoloader)) {
        require_once $dependencyAutoloader;
    }
}

// Not all dependency autoloaders exist or are in every dist yet so fallback
// to using include path for dependencies for now
$fedoraClassLoader->setUseIncludePath(true);

return $fedoraClassLoader;
AUTOLOAD


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{phpdir}/AWSSDKforPHP
cp -pr src/* %{buildroot}%{phpdir}/
# Compat directory structure with old PEAR pkg
ln -s ../Aws %{buildroot}%{phpdir}/AWSSDKforPHP/Aws


%check
: Library version value check
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Aws/autoload.php";
    exit(version_compare("%{version}", \Aws\Common\Aws::VERSION, "=") ? 0 : 1);'

# Tests skipped because "Guzzle\Tests\GuzzleTestCase" is not provided by the
# php-guzzle-Guzzle package


%post
# Unregister PEAR pkg (ignore errors if it was not registered)
if [ -x %{_bindir}/pear ]; then
    %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc composer.json
%{phpdir}/Aws
%{phpdir}/AWSSDKforPHP


%changelog
* Sat Sep 19 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.21-1
- Renamed from php-aws-sdk to php-aws-sdk2
- Updated to 2.8.21
- Added library version value check

* Sat Sep 05 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.20-1
- Updated to 2.8.20 (RHBZ #1253094)
- Updated autoloader to load dependencies after self registration

* Tue Aug 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.17-1
- Updated to 2.8.17 (RHBZ #1243181)

* Fri Jul 10 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.13-2
- Use full require paths in autoloader

* Fri Jul 10 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.13-1
- Updated to 2.8.13 (RHBZ #1213030)
- Updated dependencies to use php-composer(*)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 25 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.2-1
- Updated to 2.8.2 (BZ #1213030)

* Sun Apr 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.0-1
- Updated to 2.8.0 (BZ #1192383)

* Thu Jan 29 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.17-1
- Updated to 2.7.17 (BZ #1180500)

* Sun Dec 28 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.12-1
- Updated to 2.7.12 (BZ #1171050)

* Tue Nov 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.6-1
- Updated to 2.7.6 (BZ #1164158)

* Sun Nov 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.3-1
- Updated to 2.7.3 (BZ #1157501)

* Mon Oct 20 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.7.1-1
- Updated to 2.7.1 (BZ #1151012)
- Doctrine Cache, Monolog, and Symfony YAML are now optional

* Tue Sep 23 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6.16-1
- Updated to 2.6.16 (BZ #1142985)

* Sun Aug 17 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6.15-2
- Obsolete php-channel-aws
- Compat direcory structure with old PEAR pkg

* Fri Aug 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6.15-1
- Updated to 2.6.15 (BZ #1126610)
- PEAR install changed to Composer-ish install

* Mon Aug 04 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.6.1-3
- Fix php-guzzle-Guzzle max version (3.9.0 => 3.9.9)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 2.6.1-1
- Update to latest upstream release

* Sun Mar 16 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.3-1
- Update to latest upstream release

* Fri Feb 21 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.2-1
- Update to latest upstream release

* Fri Jan 03 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.0-5
- Remove the aws.phar with other uneaded files on %%install

* Fri Jan 03 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.0-4
- Keep the aws.phar file for workaround on install

* Thu Jan 02 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.0-3
- Fix file installation

* Mon Dec 30 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.0-2
- add php-Monolog-dynamo dependency
- update naming on dependency php-symfony-yaml
- fix max version require on guzzle dependency

* Sun Dec 29 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 2.5.0-1
- update to latest upstrean version

* Mon Nov 18 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 2.4.10-1
- update to latest upstream version
- add php-symfony2-Yaml(version2) and php-Monolog
- remove dependency php-symfony2-YAML(version1)
- set version contraint for php-guzzle-Guzzle dependency

* Mon Sep 09 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 2.4.5-2
- add guzzle dependency.
- remove aws.phar file

* Thu Sep 05 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 2.4.5-1
- Update to 2.4.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 08 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.6.2-5
- unbundle sfyaml
- fix requires
- mark doc in package.xml

* Wed May 01 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 1.6.2-4
- Add dependencies
- Add license clarification

* Tue Apr 30 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 1.6.2-3
- Fix Source, remove empty folder _doc

* Mon Apr 29 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 1.6.2-2
- Fix License, Fix Description, move doc files

* Mon Apr 29 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 1.6.2-1
- initial package
