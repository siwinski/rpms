%global github_owner      symfony-cmf
%global github_name       Routing
%global github_version    1.0.0
%global github_prerelease alpha4
%global github_commit     92ee467ea2ed1797acd630c9576543d2120ca97a

%global php_min_ver       5.3.2

Name:          php-SymfonyCmfRouting
Version:       %{github_version}
Release:       0.1.%{github_prerelease}%{?dist}
Summary:       Extends the Symfony2 routing component for dynamic routes and chaining several routers

Group:         Development/Libraries
License:       MIT
URL:           http://symfony.com/doc/master/cmf/components/routing.html
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_prerelease}-%{github_commit}.tar.gz

BuildArch:     noarch
# Test build requires
BuildRequires: php-common >= %{php_min_ver}
BuildRequires: php-pear(pear.phpunit.de/PHPUnit)
# Test build requires: phpci
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl

Requires:      php-common >= %{php_min_ver}
Requires:      php-pear(pear.symfony.com/Routing) >= 2.1.0
Requires:      php-pear(pear.symfony.com/Routing) <  2.3.0
Requires:      php-pear(pear.symfony.com/HttpKernel) >= 2.1.0
Requires:      php-pear(pear.symfony.com/HttpKernel) <  2.3.0
# phpci requires
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

%description
The Symfony CMF Routing component library extends the Symfony2 core routing
component. Even though it has Symfony in its name, it does not need the full
Symfony2 framework and can be used in standalone projects. For integration
with Symfony we provide RoutingExtraBundle.

At the core of the Symfony CMF Routing component is the ChainRouter, that is
used instead of the Symfony2's default routing system. The ChainRouter can
chain several RouterInterface implementations, one after the other, to determine
what should handle each request. The default Symfony2 router can be added to
this chain, so the standard routing mechanism can still be used.

Additionally, this component is meant to provide useful implementations of the
routing interfaces. Currently, it provides the DynamicRouter, which uses a
RequestMatcherInterface to dynamically load Routes, and can apply
RouteEnhancerInterface strategies in order to manipulate them. The provided
NestedMatcher can dynamically retrieve Symfony2 Route objects from a
RouteProviderInterface. This interfaces abstracts a collection of Routes,
that can be stored in a database, like Doctrine PHPCR-ODM or Doctrine ORM.
The DynamicRouter also uses a UrlGenerator instance to generate Routes and
an implementation is provided under ProviderBasedGenerator that can generate
routes loaded from a RouteProviderInterface instance, and the
ContentAwareGenerator on top of it to determine the route object from a
content object.


%package tests
Summary:  Test suite for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description tests
%{summary}.


%prep
%setup -q -n %{github_name}-%{github_commit}

# TODO: Update tests bootstrap

sed -e 's:Tests/bootstrap.php:./bootstrap.php:' \
    -e 's:<directory>\.\?/\?:<directory>%{_datadir}/php/Symfony/Cmf/Component/Routing/:' \
    -i phpunit.xml.dist


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/Symfony/Cmf/Component/Routing
cp -rp * %{buildroot}%{_datadir}/php/Symfony/Cmf/Component/Routing/

mkdir -p -m 755 %{buildroot}%{_datadir}/tests/%{name}
mv %{buildroot}%{_datadir}/php/Symfony/Cmf/Component/Routing/phpunit.xml.dist \
   %{buildroot}%{_datadir}/php/Symfony/Cmf/Component/Routing/Tests/bootstrap.php \
   %{buildroot}%{_datadir}/tests/%{name}/


%check
# TODO: Run tests
#%{_bindir}/phpunit \
#    -d include_path="./src:./tests:.:%{pear_phpdir}:%{_datadir}/php" \
#    -c tests/phpunit.xml.dist


%files
%doc LICENSE README.md composer.json
%dir %{_datadir}/php/Symfony/Cmf
%dir %{_datadir}/php/Symfony/Cmf/Component
     %{_datadir}/php/Symfony/Cmf/Component/Routing
%exclude %{_datadir}/php/Symfony/Cmf/Component/Routing/LICENSE
%exclude %{_datadir}/php/Symfony/Cmf/Component/Routing/README.md
%exclude %{_datadir}/php/Symfony/Cmf/Component/Routing/composer.json
%exclude %{_datadir}/php/Symfony/Cmf/Component/Routing/Test
%exclude %{_datadir}/php/Symfony/Cmf/Component/Routing/Tests

%files tests
%dir %{_datadir}/tests
     %{_datadir}/tests/%{name}
%{_datadir}/php/Symfony/Cmf/Component/Routing/Test
%{_datadir}/php/Symfony/Cmf/Component/Routing/Tests


%changelog
* Thu Jan 31 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.0-0.1.alpha4
- Initial package
