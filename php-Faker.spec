%global libname Faker

Name:          php-%{libname}
Version:       1.1.0
Release:       1%{?dist}
Summary:       Faker is a PHP library that generates fake data for you

Group:         Development/Libraries
License:       MIT
URL:           https://github.com/fzaninotto/%{libname}
Source0:       %{url}/archive/v%{version}.tar.gz

BuildArch:     noarch

Requires:      php-common >= 5.3.3
# phpci requires
Requires:      php-date
Requires:      php-hash
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl

%description
Faker is a PHP library that generates fake data for you. Whether you need
to bootstrap your database, create good-looking XML documents, fill-in your
persistence to stress test it, or anonymize data taken from a production
service, Faker is for you.

Faker is heavily inspired by Perl's Data::Faker
(http://search.cpan.org/~jasonk/Data-Faker/), and by ruby's Faker
(http://faker.rubyforge.org/).


%prep
%setup -q -n %{libname}-%{version}

# Remove executable bit from all PHP files
# https://github.com/fzaninotto/Faker/pull/84
find . -name '*.php' -executable | xargs chmod a-x


%build
# Empty build section, nothing to build


%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp src/%{libname} %{buildroot}%{_datadir}/php/


%files
%doc LICENSE CHANGELOG readme.md composer.json
%{_datadir}/php/%{libname}


%changelog
* Thu Nov 29 2012 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.0-1
- Initial package
