%{?drupal7_find_provides_and_requires}

%global module_name htmLawed

Name:          drupal7-%{module_name}
Version:       3.2
Release:       1%{?dist}
Summary:       htmLawed (X)HTML filter/purifier

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3

Requires:      php-htmLawed
# phpcompatinfo
Requires:      php-pcre

Provides:      drupal7-htmlawed = %{version}-%{release}

%description
Restrict HTML markup and make content secure, and standard- and admin.
policy-compliant

This package provides the following Drupal module:
* %{module_name}


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .

# Remove bundled library
rm -rf htmLawed

# Remove executable bit from files
find . -type f -executable -print0 | xargs -0 chmod -x


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}/

# Link to un-bundled library
ln -s %{_datadir}/php/htmLawed \
      %{buildroot}%{drupal7_modules}/%{module_name}/htmLawed


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt


%changelog
* Tue Dec 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.2-1
- Initial package
