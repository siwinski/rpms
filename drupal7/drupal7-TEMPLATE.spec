%{?drupal7_find_provides_and_requires}

%global module __MODULE__

Name:          drupal7-%{module}
Version:       __VERSION__
Release:       1%{?dist}
Summary:       __SUMMARY__

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.23-3

# phpcompatinfo (computed from version __VERSION__)
#Requires:      php-

%description
__DESCRIPTION__

This package provides the following Drupal module(s):
* %{module}


%prep
%setup -qn %{module}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%doc *.txt
%{drupal7_modules}/%{module}
%exclude %{drupal7_modules}/%{module}/*.txt


%changelog
* ddd MMM DD YYYY Shawn Iwinski <shawn.iwinski@gmail.com> __VERSION__-1
- Initial package
