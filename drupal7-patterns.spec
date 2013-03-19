%global module_name patterns
%global pre_release rc2

Name:          drupal7-%{module_name}
Version:       2.0
Release:       0.1.%{pre_release}%{?dist}
Summary:       Magically import and export web site configuration and content to files

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
Requires:      drupal7-libraries
Requires:      drupal7-token
# TODO: SPYC
#   * https://github.com/mustangostang/spyc/
#   * https://admin.fedoraproject.org/pkgdb/acls/name/php-spyc
# phpci
Requires:      php-date
Requires:      php-dom
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-simplexml
Requires:      php-xml
Requires:      php-zip

%description
Complex websites and web applications can be created by combining
configurations of Modules, Content Types (CCK,) Views, Panels, Menus, Blocks,
Categories, Roles / Permissions, etc.. This site setup and configuration
process is a very time consuming and repetitive bottleneck.

Patterns module is built to bypass this bottleneck by managing and automating
site configuration. Site configuration is stored in XML or YAML called Patterns
which are easy to read, modify, manage, & share and can be executed manually or
as a part of an automated web site deployment.


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .
chmod +x scripts/setup


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt


%changelog
* Tue Mar 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-0.1.rc2
- Initial package
