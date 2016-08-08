%{?drupal7_find_provides_and_requires}

%global module uuid
%global pre_release beta2

Name:          drupal7-%{module}
Version:       1.0
Release:       0.1%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Adds support for universally unique identifiers

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3

Requires:      drupal7(node)
Requires:      drupal7(user)
# phpcompatinfo (computed from version 1.0-beta2)
Requires:      php-pcre

%description
This module provides an API for adding universally unique identifiers (UUID) to
Drupal objects, most notably entities.


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%clean
rm -rf %{buildroot}


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Mon Aug 08 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.beta2
- Initial package
