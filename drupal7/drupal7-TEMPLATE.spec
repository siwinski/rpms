%{?drupal7_find_provides_and_requires}

%global module __MODULE__

Name:          drupal7-%{module}
Version:       __VERSION__
Release:       1%{?pre_release:.%{pre_release}}%{?dist}
Summary:       __SUMMARY__

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3

# phpcompatinfo (computed from version __VERSION__)
#Requires:      php-

%description
__DESCRIPTION__

This package provides the following Drupal 7 modules:
* %{module}


%prep
%setup -qn %{module}


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.txt
%{drupal7_modules}/%{module}
%exclude %{drupal7_modules}/%{module}/*.txt


%changelog
