%{?drupal7_find_provides_and_requires}

%global module_name color_field

Name:          drupal7-%{module_name}
Version:       1.6
Release:       1%{?dist}
Summary:       Color Field using a hexadecimal notation (HEX)

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3

Requires:      drupal7-libraries
#Requires:      drupal7(libraries)
# phpcompatinfo
Requires:      php-pcre

%description
Color Field is simple field that use a hexadecimal notation (HEX) for the
combination of Red, Green, and Blue color values (RGB).

This package provides the following Drupal module:
* %{module_name}


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .

# Remove executable bit from all JS/CSS files
find . -name '*.js'  | xargs chmod a-x
find . -name '*.css' | xargs chmod a-x

# Remove empty file
rm -f color_field.test


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt


%changelog
* Tue Nov 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.6-1
- Initial package
