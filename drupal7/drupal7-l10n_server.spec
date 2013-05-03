%global module_name l10n_server

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.1.dev.20130220%{?dist}
Summary:       Localization server

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-1.x-dev.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
Requires:      drupal7(potx)
Requires:      drupal7(l10n_pconfig)
#Requires:      drupal7(locale)
# phpci
Requires:      php-date
Requires:      php-pcre
Requires:      php-simplexml

Provides:      drupal7(l10n_community) = %{version}
Provides:      drupal7(l10n_groups) = %{version}
Provides:      drupal7(l10n_remote) = %{version}
Provides:      drupal7(l10n_packager) = %{version}
Provides:      drupal7(l10n_server) = %{version}
Provides:      drupal7(l10n_drupal) = %{version}
Provides:      drupal7(l10n_gettext) = %{version}

%description
The localization server is a set of Drupal modules powering
http://localize.drupal.org/, https://translate.openatrium.com/,
http://localize.openpublishapp.com/ and even the non-Drupal based
http://translate.musescore.org/ among other translation communities.

It provides a generic translation database back-end with a community
localization user interface, which allows people to collaborate on
translating projects to different languages. It currently contains
tools to translate Drupal projects as well as general Gettext based
sources.

This package provides the following Drupal modules:
* l10n_community
* l10n_groups (NOTE: Requires install of the og module)
* l10n_remote
* l10n_packager
* l10n_server
* l10n_drupal
* l10n_gettext


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
* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.dev.20130220
- Initial package
