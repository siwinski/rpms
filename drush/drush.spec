#
# RPM spec file for drush
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     drush-ops
%global github_name      drush
%global github_version   6.6.0
%global github_commit    1779c6c37d56235935e99d849bb4c910b632428e

%global composer_vendor  drush
%global composer_project drush

# "php": ">=5.3.0"
%global php_min_ver  5.3.0

%global drush_dir    %{_datadir}/drush
%global pear_channel pear.drush.org
%global pear_name    drush

%global git_min_ver  1.7

# Build using "--with tests" to enable tests
# TODO: Figure out test issues and enable by default
%global with_tests 0%{?_with_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          %{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Command line shell and scripting interface for Drupal

Group:         Development/Libraries
License:       GPLv2+
URL:           http://www.drush.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
%if %{with_tests}
BuildRequires: git >= %{git_min_ver}
BuildRequires: patch
BuildRequires: php-symfony-yaml
# composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 6.6.0)
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-dom
BuildRequires: php-fileinfo
BuildRequires: php-filter
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-pdo
BuildRequires: php-posix
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
%endif

Requires:      git >= %{git_min_ver}
Requires:      patch
Requires:      php-symfony-yaml
# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 6.6.0)
Requires:      php-ctype
Requires:      php-date
Requires:      php-dom
Requires:      php-fileinfo
Requires:      php-filter
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-posix
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl

Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Obsoletes:     php-drush-drush < %{version}-%{release}
Provides:      php-drush-drush = %{version}-%{release}
Obsoletes:     drupal6-drush < %{version}-%{release}
Provides:      drupal6-drush = %{version}-%{release}
Obsoletes:     drupal7-drush < %{version}-%{release}
Provides:      drupal7-drush = %{version}-%{release}
Provides:      php-pear(%{pear_channel}/%{pear_name}) = %{version}

# This pkg was the only one in this channel so the channel is no longer needed
Obsoletes: php-channel-drush

%description
Drush is a command line shell and Unix scripting interface for Drupal. If you
are unfamiliar with shell scripting, reviewing the documentation for your shell
(e.g. man bash) or reading an online tutorial (e.g. search for "bash tutorial")
will help you get the most out of Drush.

Drush core ships with lots of useful commands for interacting with code like
modules/themes/profiles. Similarly, it runs update.php, executes sql queries
and DB migrations, and misc utilities like run cron or clear cache.


%prep
%setup -qn %{github_name}-%{github_commit}

# Remove bundled Symfony YAML
rm -rf lib/Yaml*
sed -e "s#\$path\s*=\s*.*#\$path = '%{phpdir}/Symfony/Component/Yaml';#" \
    -e '/DRUSH_YAML_VERSION/d' \
    -i commands/core/outputformat/yaml.inc

# Remove drush.bat
rm -f drush.bat

# W: wrong-file-end-of-line-encoding /usr/share/doc/drush/examples/sandwich.txt
sed -i 's/\r$//' examples/sandwich.txt


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{drush_dir}
cp -pr * %{buildroot}%{drush_dir}/

# Bin
mkdir -p %{buildroot}%{_bindir}
ln -s %{drush_dir}/drush %{buildroot}%{_bindir}/drush

# Completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 0644 drush.complete.sh %{buildroot}%{_sysconfdir}/bash_completion.d/


%check
%if %{with_tests}
%{_bindir}/phpunit -c tests/phpunit.xml.dist
%else
: Tests skipped
: Build using "--with tests" to enable tests
%endif


%files
%{!?_licensedir:%global license %%doc}
# %%license
# See https://github.com/drush-ops/drush/pull/319
%doc docs
%doc examples
%doc composer.json
%doc *.md
%{_bindir}/drush
%{drush_dir}
%exclude %{drush_dir}/docs
%exclude %{drush_dir}/examples
%exclude %{drush_dir}/tests
%exclude %{drush_dir}/composer.json
%exclude %{drush_dir}/drush.complete.sh
%exclude %{drush_dir}/*.md
%dir %{_sysconfdir}/bash_completion.d
     %{_sysconfdir}/bash_completion.d/drush.complete.sh


%changelog
* Thu Apr 30 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 6.6.0-1
- Initial package obsoleting php-drush-drush
