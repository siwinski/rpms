%global github_owner   symfony
%global github_name    symfony
%global github_version 2.3.1
%global github_commit  0902c606b4df1161f5b786ae89f37b71380b1f23

%global symfony_dir    %{_datadir}/php/Symfony
%global pear_channel   pear.symfony.com
%global php_min_ver    5.3.3

Name:      php-symfony2
Version:   %{github_version}
Release:   1%{dist}
Summary:   PHP full-stack web framework

Group:     Development/Libraries
License:   MIT
URL:       http://symfony.com
Source0:   https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch

# Bridges
Requires:  %{name}-DoctrineBridge      = %{version}-%{release}
Requires:  %{name}-MonologBridge       = %{version}-%{release}
Requires:  %{name}-Propel1Bridge       = %{version}-%{release}
Requires:  %{name}-ProxyManagerBridge  = %{version}-%{release}
Requires:  %{name}-SwiftmailerBridge   = %{version}-%{release}
Requires:  %{name}-TwigBridge          = %{version}-%{release}

# Bundles
Requires:  %{name}-FrameworkBundle     = %{version}-%{release}
Requires:  %{name}-SecurityBundle      = %{version}-%{release}
Requires:  %{name}-TwigBundle          = %{version}-%{release}
Requires:  %{name}-WebProfilerBundle   = %{version}-%{release}

# Components
Requires:  %{name}-BrowserKit          = %{version}-%{release}
Requires:  %{name}-ClassLoader         = %{version}-%{release}
Requires:  %{name}-Config              = %{version}-%{release}
Requires:  %{name}-Console             = %{version}-%{release}
Requires:  %{name}-CssSelector         = %{version}-%{release}
Requires:  %{name}-Debug               = %{version}-%{release}
Requires:  %{name}-DependencyInjection = %{version}-%{release}
Requires:  %{name}-DomCrawler          = %{version}-%{release}
Requires:  %{name}-EventDispatcher     = %{version}-%{release}
Requires:  %{name}-Filesystem          = %{version}-%{release}
Requires:  %{name}-Finder              = %{version}-%{release}
Requires:  %{name}-Form                = %{version}-%{release}
Requires:  %{name}-HttpFoundation      = %{version}-%{release}
Requires:  %{name}-HttpKernel          = %{version}-%{release}
Requires:  %{name}-Intl                = %{version}-%{release}
Requires:  %{name}-Locale              = %{version}-%{release}
Requires:  %{name}-OptionsResolver     = %{version}-%{release}
Requires:  %{name}-Process             = %{version}-%{release}
Requires:  %{name}-PropertyAccess      = %{version}-%{release}
Requires:  %{name}-Routing             = %{version}-%{release}
Requires:  %{name}-Security            = %{version}-%{release}
Requires:  %{name}-Serializer          = %{version}-%{release}
Requires:  %{name}-Stopwatch           = %{version}-%{release}
Requires:  %{name}-Templating          = %{version}-%{release}
Requires:  %{name}-Translation         = %{version}-%{release}
Requires:  %{name}-Validator           = %{version}-%{release}
Requires:  %{name}-Yaml                = %{version}-%{release}

%description
%{summary}

# ##############################################################################

%package       common

Summary:       Symfony2 common files

# For tests
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)

Requires:      php(language) >= %{php_min_ver}

%description common
%{summary}

# ------------------------------------------------------------------------------

%package   DoctrineBridge

Summary:   Symfony2 Doctrine Bridge
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Doctrine) = %{version}

%description DoctrineBridge
%{summary}

# ------------------------------------------------------------------------------

%package   MonologBridge

Summary:   Symfony2 Monolog Bridge
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Monolog) = %{version}

%description MonologBridge
%{summary}

# ------------------------------------------------------------------------------

%package   Propel1Bridge

Summary:   Symfony2 Propel1 Bridge
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Propel1) = %{version}

%description Propel1Bridge
%{summary}

# ------------------------------------------------------------------------------

%package   ProxyManagerBridge

Summary:   Symfony2 ProxyManager Bridge
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/ProxyManager) = %{version}

%description ProxyManagerBridge
%{summary}

# ------------------------------------------------------------------------------

%package   SwiftmailerBridge

Summary:   Symfony2 Swiftmailer Bridge
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Swiftmailer) = %{version}

%description SwiftmailerBridge
%{summary}

# ------------------------------------------------------------------------------

%package   TwigBridge

Summary:   Symfony2 Twig Bridge
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Twig) = %{version}

%description TwigBridge
%{summary}

# ------------------------------------------------------------------------------

%package   FrameworkBundle

Summary:   Symfony2 FrameworkBundle Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/FrameworkBundle) = %{version}

%description FrameworkBundle
%{summary}

# ------------------------------------------------------------------------------

%package   SecurityBundle

Summary:   Symfony2 SecurityBundle Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/SecurityBundle) = %{version}

%description SecurityBundle
%{summary}

# ------------------------------------------------------------------------------

%package   TwigBundle

Summary:   Symfony2 TwigBundle Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/TwigBundle) = %{version}

%description TwigBundle
%{summary}

# ------------------------------------------------------------------------------

%package   WebProfilerBundle

Summary:   Symfony2 WebProfilerBundle Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/WebProfilerBundle) = %{version}

%description WebProfilerBundle
%{summary}

# ------------------------------------------------------------------------------

%package   BrowserKit

Summary:   Symfony2 BrowserKit Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/BrowserKit) = %{version}

%description BrowserKit
%{summary}

# ------------------------------------------------------------------------------

%package   ClassLoader

Summary:   Symfony2 ClassLoader Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/ClassLoader) = %{version}

%description ClassLoader
%{summary}

# ------------------------------------------------------------------------------

%package   Config

Summary:   Symfony2 Config Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Config) = %{version}

%description Config
%{summary}

# ------------------------------------------------------------------------------

%package   Console

Summary:   Symfony2 Console Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Console) = %{version}

%description Console
%{summary}

# ------------------------------------------------------------------------------

%package   CssSelector

Summary:   Symfony2 CssSelector Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/CssSelector) = %{version}

%description CssSelector
%{summary}

# ------------------------------------------------------------------------------

%package   Debug

Summary:   Symfony2 Debug Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Debug) = %{version}

%description Debug
%{summary}

# ------------------------------------------------------------------------------

%package   DependencyInjection

Summary:   Symfony2 DependencyInjection Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/DependencyInjection) = %{version}

%description DependencyInjection
%{summary}

# ------------------------------------------------------------------------------

%package   DomCrawler

Summary:   Symfony2 DomCrawler Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/DomCrawler) = %{version}

%description DomCrawler
%{summary}

# ------------------------------------------------------------------------------

%package   EventDispatcher

Summary:   Symfony2 EventDispatcher Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/EventDispatcher) = %{version}

%description EventDispatcher
%{summary}

# ------------------------------------------------------------------------------

%package   Filesystem

Summary:   Symfony2 Filesystem Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Filesystem) = %{version}

%description Filesystem
%{summary}

# ------------------------------------------------------------------------------

%package   Finder

Summary:   Symfony2 Finder Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Finder) = %{version}

%description Finder
%{summary}

# ------------------------------------------------------------------------------

%package   Form

Summary:   Symfony2 Form Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Form) = %{version}

%description Form
%{summary}

# ------------------------------------------------------------------------------

%package   HttpFoundation

Summary:   Symfony2 HttpFoundation Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/HttpFoundation) = %{version}

%description HttpFoundation
%{summary}

# ------------------------------------------------------------------------------

%package   HttpKernel

Summary:   Symfony2 HttpKernel Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/HttpKernel) = %{version}

%description HttpKernel
%{summary}

# ------------------------------------------------------------------------------

%package   Intl

Summary:   Symfony2 Intl Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Intl) = %{version}

%description Intl
%{summary}

# ------------------------------------------------------------------------------

%package   Locale

Summary:   Symfony2 Locale Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Locale) = %{version}

%description Locale
%{summary}

# ------------------------------------------------------------------------------

%package   OptionsResolver

Summary:   Symfony2 OptionsResolver Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/OptionsResolver) = %{version}

%description OptionsResolver
%{summary}

# ------------------------------------------------------------------------------

%package   Process

Summary:   Symfony2 Process Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Process) = %{version}

%description Process
%{summary}

# ------------------------------------------------------------------------------

%package   PropertyAccess

Summary:   Symfony2 PropertyAccess Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/PropertyAccess) = %{version}

%description PropertyAccess
%{summary}

# ------------------------------------------------------------------------------

%package   Routing

Summary:   Symfony2 Routing Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Routing) = %{version}

%description Routing
%{summary}

# ------------------------------------------------------------------------------

%package   Security

Summary:   Symfony2 Security Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Security) = %{version}

%description Security
%{summary}

# ------------------------------------------------------------------------------

%package   Serializer

Summary:   Symfony2 Serializer Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Serializer) = %{version}

%description Serializer
%{summary}

# ------------------------------------------------------------------------------

%package   Stopwatch

Summary:   Symfony2 Stopwatch Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Stopwatch) = %{version}

%description Stopwatch
%{summary}

# ------------------------------------------------------------------------------

%package   Templating

Summary:   Symfony2 Templating Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Templating) = %{version}

%description Templating
%{summary}

# ------------------------------------------------------------------------------

%package   Translation

Summary:   Symfony2 Translation Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Translation) = %{version}

%description Translation
%{summary}

# ------------------------------------------------------------------------------

%package   Validator

Summary:   Symfony2 Validator Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Validator) = %{version}

%description Validator
%{summary}

# ------------------------------------------------------------------------------

%package   Yaml

Summary:   Symfony2 Yaml Component
URL:       xyzxyzxyzxyzxyzxyzxyzxyzxyz

Requires:  %{name}-common = %{version}-%{release}
Requires:  %{name}- = %{version}-%{release}
# Optional
Requires:  %{name}- = %{version}-%{release}
# phpci
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-
Requires:  php-

Provides:  php-pear(%{pear_channel}/Yaml) = %{version}

%description Yaml
%{summary}

# ##############################################################################


%prep
%setup -q -n %{github_name}-%{github_commit}

# Remove unnecessary files
find src -name '.git*' -delete


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{symfony_dir}
cp -rp src/Symfony/* %{buildroot}%{symfony_dir}/

mkdir -p %{buildroot}%{_docdir}
ln -s %{name}-common-%{version} %{buildroot}%{_docdir}/%{name}-%{version}


%check
# TODO


%files
# Empty files section, included in sub-package "common"


# ##############################################################################

%files common

%doc LICENSE *.md composer.*
%doc %{_docdir}/%{name}-%{version}

%dir %{symfony_dir}

# ------------------------------------------------------------------------------

%files DoctrineBridge

%doc src/Symfony/Bridge/Doctrine/LICENSE
%doc src/Symfony/Bridge/Doctrine/*.md
%doc src/Symfony/Bridge/Doctrine/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Doctrine
%exclude %{symfony_dir}/Bridge/Doctrine/LICENSE
%exclude %{symfony_dir}/Bridge/Doctrine/*.md
%exclude %{symfony_dir}/Bridge/Doctrine/composer.*
%exclude %{symfony_dir}/Bridge/Doctrine/phpunit.*
%exclude %{symfony_dir}/Bridge/Doctrine/Tests

# ------------------------------------------------------------------------------

%files MonologBridge

%doc src/Symfony/Bridge/Monolog/LICENSE
%doc src/Symfony/Bridge/Monolog/*.md
%doc src/Symfony/Bridge/Monolog/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Monolog
%exclude %{symfony_dir}/Bridge/Monolog/LICENSE
%exclude %{symfony_dir}/Bridge/Monolog/*.md
%exclude %{symfony_dir}/Bridge/Monolog/composer.*
%exclude %{symfony_dir}/Bridge/Monolog/phpunit.*
%exclude %{symfony_dir}/Bridge/Monolog/Tests

# ------------------------------------------------------------------------------

%files Propel1Bridge

%doc src/Symfony/Bridge/Propel1/LICENSE
%doc src/Symfony/Bridge/Propel1/*.md
%doc src/Symfony/Bridge/Propel1/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Propel1
%exclude %{symfony_dir}/Bridge/Propel1/LICENSE
%exclude %{symfony_dir}/Bridge/Propel1/*.md
%exclude %{symfony_dir}/Bridge/Propel1/composer.*
%exclude %{symfony_dir}/Bridge/Propel1/phpunit.*
%exclude %{symfony_dir}/Bridge/Propel1/Tests

# ------------------------------------------------------------------------------

%files ProxyManagerBridge

%doc src/Symfony/Bridge/ProxyManager/LICENSE
%doc src/Symfony/Bridge/ProxyManager/*.md
%doc src/Symfony/Bridge/ProxyManager/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/ProxyManager
%exclude %{symfony_dir}/Bridge/ProxyManager/LICENSE
%exclude %{symfony_dir}/Bridge/ProxyManager/*.md
%exclude %{symfony_dir}/Bridge/ProxyManager/composer.*
%exclude %{symfony_dir}/Bridge/ProxyManager/phpunit.*
%exclude %{symfony_dir}/Bridge/ProxyManager/Tests

# ------------------------------------------------------------------------------

%files SwiftmailerBridge

%doc src/Symfony/Bridge/Swiftmailer/LICENSE
%doc src/Symfony/Bridge/Swiftmailer/*.md
%doc src/Symfony/Bridge/Swiftmailer/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Swiftmailer
%exclude %{symfony_dir}/Bridge/Swiftmailer/LICENSE
%exclude %{symfony_dir}/Bridge/Swiftmailer/*.md
%exclude %{symfony_dir}/Bridge/Swiftmailer/composer.*
%exclude %{symfony_dir}/Bridge/Swiftmailer/phpunit.*
%exclude %{symfony_dir}/Bridge/Swiftmailer/Tests

# ------------------------------------------------------------------------------

%files TwigBridge

%doc src/Symfony/Bridge/Twig/LICENSE
%doc src/Symfony/Bridge/Twig/*.md
%doc src/Symfony/Bridge/Twig/composer.*

%dir     %{symfony_dir}/Bridge
         %{symfony_dir}/Bridge/Twig
%exclude %{symfony_dir}/Bridge/Twig/LICENSE
%exclude %{symfony_dir}/Bridge/Twig/*.md
%exclude %{symfony_dir}/Bridge/Twig/composer.*
%exclude %{symfony_dir}/Bridge/Twig/phpunit.*
%exclude %{symfony_dir}/Bridge/Twig/Tests

# ------------------------------------------------------------------------------

%files FrameworkBundle

%doc src/Symfony/Bundle/FrameworkBundle/LICENSE
%doc src/Symfony/Bundle/FrameworkBundle/*.md
%doc src/Symfony/Bundle/FrameworkBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/FrameworkBundle
%exclude %{symfony_dir}/Bundle/FrameworkBundle/LICENSE
%exclude %{symfony_dir}/Bundle/FrameworkBundle/*.md
%exclude %{symfony_dir}/Bundle/FrameworkBundle/composer.*
%exclude %{symfony_dir}/Bundle/FrameworkBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/FrameworkBundle/Tests

# ------------------------------------------------------------------------------

%files SecurityBundle

%doc src/Symfony/Bundle/SecurityBundle/LICENSE
%doc src/Symfony/Bundle/SecurityBundle/*.md
%doc src/Symfony/Bundle/SecurityBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/SecurityBundle
%exclude %{symfony_dir}/Bundle/SecurityBundle/LICENSE
%exclude %{symfony_dir}/Bundle/SecurityBundle/*.md
%exclude %{symfony_dir}/Bundle/SecurityBundle/composer.*
%exclude %{symfony_dir}/Bundle/SecurityBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/SecurityBundle/Tests

# ------------------------------------------------------------------------------

%files TwigBundle

%doc src/Symfony/Bundle/TwigBundle/LICENSE
%doc src/Symfony/Bundle/TwigBundle/*.md
%doc src/Symfony/Bundle/TwigBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/TwigBundle
%exclude %{symfony_dir}/Bundle/TwigBundle/LICENSE
%exclude %{symfony_dir}/Bundle/TwigBundle/*.md
%exclude %{symfony_dir}/Bundle/TwigBundle/composer.*
%exclude %{symfony_dir}/Bundle/TwigBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/TwigBundle/Tests

# ------------------------------------------------------------------------------

%files WebProfilerBundle

%doc src/Symfony/Bundle/WebProfilerBundle/LICENSE
%doc src/Symfony/Bundle/WebProfilerBundle/*.md
%doc src/Symfony/Bundle/WebProfilerBundle/composer.*

%dir     %{symfony_dir}/Bundle
         %{symfony_dir}/Bundle/WebProfilerBundle
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/LICENSE
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/*.md
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/composer.*
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/phpunit.*
%exclude %{symfony_dir}/Bundle/WebProfilerBundle/Tests

# ------------------------------------------------------------------------------

%files BrowserKit

%doc src/Symfony/Component/BrowserKit/LICENSE
%doc src/Symfony/Component/BrowserKit/*.md
%doc src/Symfony/Component/BrowserKit/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/BrowserKit
%exclude %{symfony_dir}/Component/BrowserKit/LICENSE
%exclude %{symfony_dir}/Component/BrowserKit/*.md
%exclude %{symfony_dir}/Component/BrowserKit/composer.*
%exclude %{symfony_dir}/Component/BrowserKit/phpunit.*
%exclude %{symfony_dir}/Component/BrowserKit/Tests

# ------------------------------------------------------------------------------

%files ClassLoader

%doc src/Symfony/Component/ClassLoader/LICENSE
%doc src/Symfony/Component/ClassLoader/*.md
%doc src/Symfony/Component/ClassLoader/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/ClassLoader
%exclude %{symfony_dir}/Component/ClassLoader/LICENSE
%exclude %{symfony_dir}/Component/ClassLoader/*.md
%exclude %{symfony_dir}/Component/ClassLoader/composer.*
%exclude %{symfony_dir}/Component/ClassLoader/phpunit.*
%exclude %{symfony_dir}/Component/ClassLoader/Tests

# ------------------------------------------------------------------------------

%files Config

%doc src/Symfony/Component/Config/LICENSE
%doc src/Symfony/Component/Config/*.md
%doc src/Symfony/Component/Config/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Config
%exclude %{symfony_dir}/Component/Config/LICENSE
%exclude %{symfony_dir}/Component/Config/*.md
%exclude %{symfony_dir}/Component/Config/composer.*
%exclude %{symfony_dir}/Component/Config/phpunit.*
%exclude %{symfony_dir}/Component/Config/Tests

# ------------------------------------------------------------------------------

%files Console

%doc src/Symfony/Component/Console/LICENSE
%doc src/Symfony/Component/Console/*.md
%doc src/Symfony/Component/Console/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Console
%exclude %{symfony_dir}/Component/Console/LICENSE
%exclude %{symfony_dir}/Component/Console/*.md
%exclude %{symfony_dir}/Component/Console/composer.*
%exclude %{symfony_dir}/Component/Console/phpunit.*
%exclude %{symfony_dir}/Component/Console/Tests

# ------------------------------------------------------------------------------

%files CssSelector

%doc src/Symfony/Component/CssSelector/LICENSE
%doc src/Symfony/Component/CssSelector/*.md
%doc src/Symfony/Component/CssSelector/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/CssSelector
%exclude %{symfony_dir}/Component/CssSelector/LICENSE
%exclude %{symfony_dir}/Component/CssSelector/*.md
%exclude %{symfony_dir}/Component/CssSelector/composer.*
%exclude %{symfony_dir}/Component/CssSelector/phpunit.*
%exclude %{symfony_dir}/Component/CssSelector/Tests

# ------------------------------------------------------------------------------

%files Debug

%doc src/Symfony/Component/Debug/LICENSE
%doc src/Symfony/Component/Debug/*.md
%doc src/Symfony/Component/Debug/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Debug
%exclude %{symfony_dir}/Component/Debug/LICENSE
%exclude %{symfony_dir}/Component/Debug/*.md
%exclude %{symfony_dir}/Component/Debug/composer.*
%exclude %{symfony_dir}/Component/Debug/phpunit.*
%exclude %{symfony_dir}/Component/Debug/Tests

# ------------------------------------------------------------------------------

%files DependencyInjection

%doc src/Symfony/Component/DependencyInjection/LICENSE
%doc src/Symfony/Component/DependencyInjection/*.md
%doc src/Symfony/Component/DependencyInjection/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/DependencyInjection
%exclude %{symfony_dir}/Component/DependencyInjection/LICENSE
%exclude %{symfony_dir}/Component/DependencyInjection/*.md
%exclude %{symfony_dir}/Component/DependencyInjection/composer.*
%exclude %{symfony_dir}/Component/DependencyInjection/phpunit.*
%exclude %{symfony_dir}/Component/DependencyInjection/Tests

# ------------------------------------------------------------------------------

%files DomCrawler

%doc src/Symfony/Component/DomCrawler/LICENSE
%doc src/Symfony/Component/DomCrawler/*.md
%doc src/Symfony/Component/DomCrawler/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/DomCrawler
%exclude %{symfony_dir}/Component/DomCrawler/LICENSE
%exclude %{symfony_dir}/Component/DomCrawler/*.md
%exclude %{symfony_dir}/Component/DomCrawler/composer.*
%exclude %{symfony_dir}/Component/DomCrawler/phpunit.*
%exclude %{symfony_dir}/Component/DomCrawler/Tests

# ------------------------------------------------------------------------------

%files EventDispatcher

%doc src/Symfony/Component/EventDispatcher/LICENSE
%doc src/Symfony/Component/EventDispatcher/*.md
%doc src/Symfony/Component/EventDispatcher/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/EventDispatcher
%exclude %{symfony_dir}/Component/EventDispatcher/LICENSE
%exclude %{symfony_dir}/Component/EventDispatcher/*.md
%exclude %{symfony_dir}/Component/EventDispatcher/composer.*
%exclude %{symfony_dir}/Component/EventDispatcher/phpunit.*
%exclude %{symfony_dir}/Component/EventDispatcher/Tests

# ------------------------------------------------------------------------------

%files Filesystem

%doc src/Symfony/Component/Filesystem/LICENSE
%doc src/Symfony/Component/Filesystem/*.md
%doc src/Symfony/Component/Filesystem/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Filesystem
%exclude %{symfony_dir}/Component/Filesystem/LICENSE
%exclude %{symfony_dir}/Component/Filesystem/*.md
%exclude %{symfony_dir}/Component/Filesystem/composer.*
%exclude %{symfony_dir}/Component/Filesystem/phpunit.*
%exclude %{symfony_dir}/Component/Filesystem/Tests

# ------------------------------------------------------------------------------

%files Finder

%doc src/Symfony/Component/Finder/LICENSE
%doc src/Symfony/Component/Finder/*.md
%doc src/Symfony/Component/Finder/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Finder
%exclude %{symfony_dir}/Component/Finder/LICENSE
%exclude %{symfony_dir}/Component/Finder/*.md
%exclude %{symfony_dir}/Component/Finder/composer.*
%exclude %{symfony_dir}/Component/Finder/phpunit.*
%exclude %{symfony_dir}/Component/Finder/Tests

# ------------------------------------------------------------------------------

%files Form

%doc src/Symfony/Component/Form/LICENSE
%doc src/Symfony/Component/Form/*.md
%doc src/Symfony/Component/Form/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Form
%exclude %{symfony_dir}/Component/Form/LICENSE
%exclude %{symfony_dir}/Component/Form/*.md
%exclude %{symfony_dir}/Component/Form/composer.*
%exclude %{symfony_dir}/Component/Form/phpunit.*
%exclude %{symfony_dir}/Component/Form/Tests

# ------------------------------------------------------------------------------

%files HttpFoundation

%doc src/Symfony/Component/HttpFoundation/LICENSE
%doc src/Symfony/Component/HttpFoundation/*.md
%doc src/Symfony/Component/HttpFoundation/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/HttpFoundation
%exclude %{symfony_dir}/Component/HttpFoundation/LICENSE
%exclude %{symfony_dir}/Component/HttpFoundation/*.md
%exclude %{symfony_dir}/Component/HttpFoundation/composer.*
%exclude %{symfony_dir}/Component/HttpFoundation/phpunit.*
%exclude %{symfony_dir}/Component/HttpFoundation/Tests

# ------------------------------------------------------------------------------

%files HttpKernel

%doc src/Symfony/Component/HttpKernel/LICENSE
%doc src/Symfony/Component/HttpKernel/*.md
%doc src/Symfony/Component/HttpKernel/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/HttpKernel
%exclude %{symfony_dir}/Component/HttpKernel/LICENSE
%exclude %{symfony_dir}/Component/HttpKernel/*.md
%exclude %{symfony_dir}/Component/HttpKernel/composer.*
%exclude %{symfony_dir}/Component/HttpKernel/phpunit.*
%exclude %{symfony_dir}/Component/HttpKernel/Tests

# ------------------------------------------------------------------------------

%files Intl

%doc src/Symfony/Component/Intl/LICENSE
%doc src/Symfony/Component/Intl/*.md
%doc src/Symfony/Component/Intl/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Intl
%exclude %{symfony_dir}/Component/Intl/LICENSE
%exclude %{symfony_dir}/Component/Intl/*.md
%exclude %{symfony_dir}/Component/Intl/composer.*
%exclude %{symfony_dir}/Component/Intl/phpunit.*
%exclude %{symfony_dir}/Component/Intl/Tests

# ------------------------------------------------------------------------------

%files Locale

%doc src/Symfony/Component/Locale/LICENSE
%doc src/Symfony/Component/Locale/*.md
%doc src/Symfony/Component/Locale/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Locale
%exclude %{symfony_dir}/Component/Locale/LICENSE
%exclude %{symfony_dir}/Component/Locale/*.md
%exclude %{symfony_dir}/Component/Locale/composer.*
%exclude %{symfony_dir}/Component/Locale/phpunit.*
%exclude %{symfony_dir}/Component/Locale/Tests

# ------------------------------------------------------------------------------

%files OptionsResolver

%doc src/Symfony/Component/OptionsResolver/LICENSE
%doc src/Symfony/Component/OptionsResolver/*.md
%doc src/Symfony/Component/OptionsResolver/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/OptionsResolver
%exclude %{symfony_dir}/Component/OptionsResolver/LICENSE
%exclude %{symfony_dir}/Component/OptionsResolver/*.md
%exclude %{symfony_dir}/Component/OptionsResolver/composer.*
%exclude %{symfony_dir}/Component/OptionsResolver/phpunit.*
%exclude %{symfony_dir}/Component/OptionsResolver/Tests

# ------------------------------------------------------------------------------

%files Process

%doc src/Symfony/Component/Process/LICENSE
%doc src/Symfony/Component/Process/*.md
%doc src/Symfony/Component/Process/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Process
%exclude %{symfony_dir}/Component/Process/LICENSE
%exclude %{symfony_dir}/Component/Process/*.md
%exclude %{symfony_dir}/Component/Process/composer.*
%exclude %{symfony_dir}/Component/Process/phpunit.*
%exclude %{symfony_dir}/Component/Process/Tests

# ------------------------------------------------------------------------------

%files PropertyAccess

%doc src/Symfony/Component/PropertyAccess/LICENSE
%doc src/Symfony/Component/PropertyAccess/*.md
%doc src/Symfony/Component/PropertyAccess/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/PropertyAccess
%exclude %{symfony_dir}/Component/PropertyAccess/LICENSE
%exclude %{symfony_dir}/Component/PropertyAccess/*.md
%exclude %{symfony_dir}/Component/PropertyAccess/composer.*
%exclude %{symfony_dir}/Component/PropertyAccess/phpunit.*
%exclude %{symfony_dir}/Component/PropertyAccess/Tests

# ------------------------------------------------------------------------------

%files Routing

%doc src/Symfony/Component/Routing/LICENSE
%doc src/Symfony/Component/Routing/*.md
%doc src/Symfony/Component/Routing/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Routing
%exclude %{symfony_dir}/Component/Routing/LICENSE
%exclude %{symfony_dir}/Component/Routing/*.md
%exclude %{symfony_dir}/Component/Routing/composer.*
%exclude %{symfony_dir}/Component/Routing/phpunit.*
%exclude %{symfony_dir}/Component/Routing/Tests

# ------------------------------------------------------------------------------

%files Security

%doc src/Symfony/Component/Security/LICENSE
%doc src/Symfony/Component/Security/*.md
%doc src/Symfony/Component/Security/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Security
%exclude %{symfony_dir}/Component/Security/LICENSE
%exclude %{symfony_dir}/Component/Security/*.md
%exclude %{symfony_dir}/Component/Security/composer.*
%exclude %{symfony_dir}/Component/Security/phpunit.*
%exclude %{symfony_dir}/Component/Security/Tests

# ------------------------------------------------------------------------------

%files Serializer

%doc src/Symfony/Component/Serializer/LICENSE
%doc src/Symfony/Component/Serializer/*.md
%doc src/Symfony/Component/Serializer/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Serializer
%exclude %{symfony_dir}/Component/Serializer/LICENSE
%exclude %{symfony_dir}/Component/Serializer/*.md
%exclude %{symfony_dir}/Component/Serializer/composer.*
%exclude %{symfony_dir}/Component/Serializer/phpunit.*
%exclude %{symfony_dir}/Component/Serializer/Tests

# ------------------------------------------------------------------------------

%files Stopwatch

%doc src/Symfony/Component/Stopwatch/LICENSE
%doc src/Symfony/Component/Stopwatch/*.md
%doc src/Symfony/Component/Stopwatch/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Stopwatch
%exclude %{symfony_dir}/Component/Stopwatch/LICENSE
%exclude %{symfony_dir}/Component/Stopwatch/*.md
%exclude %{symfony_dir}/Component/Stopwatch/composer.*
%exclude %{symfony_dir}/Component/Stopwatch/phpunit.*
%exclude %{symfony_dir}/Component/Stopwatch/Tests

# ------------------------------------------------------------------------------

%files Templating

%doc src/Symfony/Component/Templating/LICENSE
%doc src/Symfony/Component/Templating/*.md
%doc src/Symfony/Component/Templating/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Templating
%exclude %{symfony_dir}/Component/Templating/LICENSE
%exclude %{symfony_dir}/Component/Templating/*.md
%exclude %{symfony_dir}/Component/Templating/composer.*
%exclude %{symfony_dir}/Component/Templating/phpunit.*
%exclude %{symfony_dir}/Component/Templating/Tests

# ------------------------------------------------------------------------------

%files Translation

%doc src/Symfony/Component/Translation/LICENSE
%doc src/Symfony/Component/Translation/*.md
%doc src/Symfony/Component/Translation/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Translation
%exclude %{symfony_dir}/Component/Translation/LICENSE
%exclude %{symfony_dir}/Component/Translation/*.md
%exclude %{symfony_dir}/Component/Translation/composer.*
%exclude %{symfony_dir}/Component/Translation/phpunit.*
%exclude %{symfony_dir}/Component/Translation/Tests

# ------------------------------------------------------------------------------

%files Validator

%doc src/Symfony/Component/Validator/LICENSE
%doc src/Symfony/Component/Validator/*.md
%doc src/Symfony/Component/Validator/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Validator
%exclude %{symfony_dir}/Component/Validator/LICENSE
%exclude %{symfony_dir}/Component/Validator/*.md
%exclude %{symfony_dir}/Component/Validator/composer.*
%exclude %{symfony_dir}/Component/Validator/phpunit.*
%exclude %{symfony_dir}/Component/Validator/Tests

# ------------------------------------------------------------------------------

%files Yaml

%doc src/Symfony/Component/Yaml/LICENSE
%doc src/Symfony/Component/Yaml/*.md
%doc src/Symfony/Component/Yaml/composer.*

%dir     %{symfony_dir}/Component
         %{symfony_dir}/Component/Yaml
%exclude %{symfony_dir}/Component/Yaml/LICENSE
%exclude %{symfony_dir}/Component/Yaml/*.md
%exclude %{symfony_dir}/Component/Yaml/composer.*
%exclude %{symfony_dir}/Component/Yaml/phpunit.*
%exclude %{symfony_dir}/Component/Yaml/Tests

# ##############################################################################

%changelog
* Thu Jul 11 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.3.1-1
- Initial package
