%global module_name transliteration

Name:          drupal7-%{module_name}
Version:       3.1
Release:       1%{?dist}
Summary:       Converts non-Latin text to US-ASCII and sanitizes file names

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
# phpci
Requires:      php-pcre

Provides:      drupal7(%{module_name}) = %{version}

%description
Provides one-way string transliteration (romanization) and cleans file names
during upload by replacing unwanted characters.

Generally spoken, it takes Unicode text and tries to represent it in US-ASCII
characters (universally displayable, unaccented characters) by attempting to
transliterate the pronunciation expressed by the text in some other writing
system to Roman letters.

This package provides the following Drupal modules:
* %{module_name}


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .


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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 3.1-1
- Initial package
