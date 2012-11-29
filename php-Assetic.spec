# NOTE: Tests not included because Composer (http://getcomposer.org/) required

%global lib_name          Assetic
%global github_name       assetic
%global github_date       20121127
%global github_hash       deed96bb7ba009d8e05aaeeb1b73c1d67a8f3719
%global github_shorthash  %(expr substr "%{github_hash}" 1 10)
%global php_min_ver       5.3.1

Name:          php-%{lib_name}
Version:       1.0.4
Release:       1.%{github_date}git%{github_shorthash}%{?dist}
Summary:       Asset Management for PHP

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/kriswallsmith/%{github_name}
Source0:       %{url}/archive/%{github_hash}.tar.gz

BuildArch:     noarch

Requires:      php-common >= %{php_min_ver}
Requires:      php-pear(pear.symfony.com/Process) >= 2.1.0
Requires:      php-pear(pear.symfony.com/Process) < 2.3
# phpci requires
Requires:      php-ctype
Requires:      php-date
Requires:      php-fileinfo
Requires:      php-json
Requires:      php-pcre
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-tokenizer
# Optional requires
Requires:      php-pear(pear.twig-project.org/Twig) >= 1.6.0
Requires:      php-pear(pear.twig-project.org/Twig) < 2.0
Requires:      php-lessphp

%description
Assetic is an asset management framework for PHP.


%prep
%setup -q -n %{github_name}-%{github_hash}


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{lib_name}
cp -rp src/%{lib_name}/* %{buildroot}%{_datadir}/php/%{lib_name}/


%files
%doc LICENSE *.md composer.json
%{_datadir}/php/%{lib_name}


%changelog
* Thu Nov 29 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0.4-1
- Initial package
