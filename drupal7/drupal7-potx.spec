%global module_name potx

Name:          drupal7-%{module_name}
Version:       1.0
Release:       1%{?dist}
Summary:       Translation template extractor

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
#Requires:      drupal7(locale)
# phpci
Requires:      php-date
Requires:      php-pcre
Requires:      php-tokenizer

Provides:      drupal7(%{module_name}) = %{version}

%description
The Translation template extractor provides a web based and a command line
Gettext translation template extractor interface for Drupal as well as a
reusable API to look for translatable strings and translatability errors.
This tool is used under the hood at http://localize.drupal.org/ as well to
serve as a parsing machine for Drupal.org project releases.

This package provides the following Drupal modules:
* %{module_name}


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .

# Remove executable bits
chmod a-x translations/*


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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package