#
# Fedora spec file for php-react-promise-stream
#
# Copyright (c) 2018 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      promise-stream
%global github_version   1.1.1
%global github_commit    00e269d611e9c9a29356aef64c07f7e513e73dc9

%global composer_vendor  react
%global composer_project promise-stream

# "php": ">=5.3"
%global php_min_ver 5.3
# "clue/block-react": "^1.0"
%global clue_block_react_min_ver 1.0
%global clue_block_react_max_ver 2.0
# "react/event-loop": "^1.0 || ^0.5 || ^0.4 || ^0.3"
%global react_event_loop_min_ver 0.3
%global react_event_loop_max_ver 2.0
# "react/promise": "^2.1 || ^1.2"
%global react_promise_min_ver 1.2
%global react_promise_max_ver 3.0
# "react/promise-timer": "^1.0"
%global react_promise_timer_min_ver 1.0
%global react_promise_timer_max_ver 2.0
# "react/stream": "^1.0 || ^0.7 || ^0.6 || ^0.5 || ^0.4 || ^0.3"
%global react_stream_min_ver 0.3
%global react_stream_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%if 0%{?fedora}
%global with_phpunit6 1
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       The missing link between Promise-land and Stream-land for ReactPHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(clue/block-react) >= %{clue_block_react_min_ver} with php-composer(clue/block-react) < %{clue_block_react_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
BuildRequires: php-composer(clue/block-react) <  %{clue_block_react_max_ver}
BuildRequires: php-composer(clue/block-react) >= %{clue_block_react_min_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
BuildRequires: php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
BuildRequires: php-composer(react/stream) <  %{react_stream_max_ver}
BuildRequires: php-composer(react/stream) >= %{react_stream_min_ver}
%endif
### Dual PHPUnit stacks
BuildRequires: php-composer(phpunit/phpunit)
%if 0%{?with_phpunit6}
BuildRequires: phpunit6
%endif
## phpcompatinfo for version 1.1.1
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
Requires:      php-composer(react/stream) <  %{react_stream_max_ver}
Requires:      php-composer(react/stream) >= %{react_stream_min_ver}
%endif
# phpcompatinfo for version 1.1.1
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
The missing link between Promise-land and Stream-land for ReactPHP [1].

Autoloader: %{phpdir}/React/Promise/Stream/autoload.php

[1] https://reactphp.org/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Promise\\Stream\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
    __DIR__.'/functions_include.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React/Promise
cp -rp src %{buildroot}%{phpdir}/React/Promise/Stream


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/Promise/Stream/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Promise\\Stream\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Clue/React/Block/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/Timer/autoload.php',
));
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHPUNIT in phpunit %{?with_phpunit6:phpunit6}; do
    PHPUNIT=$(which $PHPUNIT)
    for PHP_EXEC in php %{?rhel:php54 php55} php56 php70 php71 php72; do
        if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
            $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
        fi
    done
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/React/Promise/Stream


%changelog
* Sat Apr 21 2018 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-2
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Wed Jan 03 2018 Shawn Iwinski <shawn@iwin.ski> - 1.1.1-1
- Initial package
