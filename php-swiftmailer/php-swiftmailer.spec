#
# Fedora spec file for php-swiftmailer
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     swiftmailer
%global github_name      swiftmailer
%global github_version   5.4.1
%global github_commit    0697e6aa65c83edf97bb0f23d8763f94e3f11421

%global composer_vendor  swiftmailer
%global composer_project swiftmailer

# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "mockery/mockery": "~0.9.1,<0.9.4"
%global mockery_min_ver 0.9.1

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       Comprehensive mailing tools for PHP

Group:         Development/Libraries
License:       MIT
URL:           http://swiftmailer.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Library version value check
BuildRequires: php-cli
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language)                 >= %{php_min_ver}
BuildRequires: php-composer(mockery/mockery) >= %{mockery_min_ver}
## phpcompatinfo (computed from version 5.4.1)
BuildRequires: php-bcmath
BuildRequires: php-ctype
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-mcrypt
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-simplexml
BuildRequires: php-spl
## Bootstrap/autoloader
BuildRequires: %{_bindir}/phpab
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 5.4.1)
Requires:      php-bcmath
Requires:      php-ctype
Requires:      php-date
Requires:      php-hash
Requires:      php-iconv
Requires:      php-mbstring
Requires:      php-mcrypt
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-simplexml
Requires:      php-spl

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Swift Mailer integrates into any web app written in PHP 5, offering a flexible
and elegant object-oriented approach to sending emails with a multitude of
features:
* Send emails using SMTP, sendmail, postfix or a custom Transport implementation
      of your own
* Support servers that require username & password and/or encryption
* Protect from header injection attacks without stripping request data content
* Send MIME compliant HTML/multipart emails
* Use event-driven plugins to customize the library
* Handle large attachments and inline/embedded images with low memory use


%prep
%setup -qn %{github_name}-%{github_commit}

: Replace Swift::VERSION
sed 's/@SWIFT_VERSION_NUMBER@/%{version}/' -i lib/classes/Swift.php

: Remove uneeded files
rm -f \
    lib/swift_required_pear.php \
    lib/swiftmailer_generate_mimes_config.php


%build
# Empty build section, nothing required


%install
: Everything
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr lib/* %{buildroot}%{_datadir}/%{name}/

: Relocate library
mkdir -p %{buildroot}%{phpdir}
mv %{buildroot}%{_datadir}/%{name}/classes/* %{buildroot}%{phpdir}/
rmdir %{buildroot}%{_datadir}/%{name}/classes
ln -s \
    %(python -c "import os.path; print os.path.relpath('%{phpdir}', '%{_datadir}/%{name}')") \
    %{buildroot}%{_datadir}/%{name}/classes

: Relocate preferences / config
mkdir -p %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/preferences.php %{buildroot}%{_sysconfdir}/%{name}.php
ln -s \
    %(python -c "import os.path; print os.path.relpath('%{_sysconfdir}/%{name}.php', '%{_datadir}/%{name}')") \
    %{buildroot}%{_datadir}/%{name}/preferences.php

: Autoloader
ln -s \
    %(python -c "import os.path; print os.path.relpath('%{_datadir}/%{name}/swift_required.php', '%{phpdir}/Swift/')") \
    %{buildroot}%{phpdir}/Swift/autoload.php



%check
: Library version check
%{_bindir}/php -r 'require_once "%{buildroot}%{phpdir}/Swift/autoload.php";
    exit(version_compare("%{version}", Swift::VERSION, "=") ? 0 : 1);'

%if %{with_tests}
: Create tests bootstrap/autoloader
%{_bindir}/phpab --nolower --output bootstrap.php tests %{phpdir}/Mockery.php %{phpdir}/Mockery
cat <<'BOOTSTRAP' >> bootstrap.php

require_once '%{buildroot}%{phpdir}/Swift/autoload.php';

if (!defined('SWIFT_TMP_DIR')) {
    define('SWIFT_TMP_DIR', sys_get_temp_dir());
}
BOOTSTRAP

: Remove loading of swift_required.php in tests
grep -r --files-with-matches 'swift_required.php' tests \
    | xargs sed -i '/swift_required.php/d'

: Run tests
%{_bindir}/phpunit --verbose --bootstrap bootstrap.php --process-isolation --exclude-group smoke
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGES
%doc README
%doc composer.json
%config(noreplace) %{_sysconfdir}/%{name}.php
%{phpdir}/Swift.php
%{phpdir}/Swift
%{_datadir}/%{name}


%changelog
* Fri Oct 16 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 5.4.1-1
- Initial package
