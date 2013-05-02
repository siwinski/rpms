%global theme_name zen

Name:          drupal7-theme-%{theme_name}
Version:       5.1
Release:       2%{?dist}
Summary:       Zen is a powerful, yet simple, HTML5 starting theme

Group:         Applications/Publishing
# Drupal theme itself is licensed under GPL
# js/html5.js and js/html5-respond.js are dual-licensed under MIT or GPL
License:       GPLv2 and MIT
URL:           http://drupal.org/project/%{theme_name}
Source0:       http://ftp.drupal.org/files/projects/%{theme_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild

Requires:      drupal7
# phpci
Requires:      php-pcre

Provides:      drupal7(%{theme_name}) = %{version}

%description
Zen is a powerful, yet simple, HTML5 starting theme with a responsive,
mobile-first grid design. If you are building your own standards-compliant
theme, you will find it much easier to start with Zen than to start with
Garland or Stark. This theme has fantastic online documentation
(http://drupal.org/node/193318) and tons of helpful code comments
in its' PHP, HTML, CSS and Sass.


%prep
%setup -q -n %{theme_name}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal7_themes}/%{theme_name}
cp -pr * %{buildroot}%{drupal7_themes}/%{theme_name}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_themes}/%{theme_name}
%exclude %{drupal7_themes}/%{theme_name}/*.txt


%changelog
* Thu May 02 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 5.1-2
- Fixed license

* Thu Mar 28 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 5.1-1
- Initial package
