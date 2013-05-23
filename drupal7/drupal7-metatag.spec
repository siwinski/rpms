%{?drupal7_find_provides_and_requires}

%global module_name metatag
%global pre_release beta7

Name:          drupal7-%{module_name}
Version:       1.0
Release:       0.2.%{pre_release}%{?dist}
Summary:       Adds support and an API to implement meta tags

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}-%{pre_release}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# For macros and auto-provides
BuildRequires: drupal7-rpmbuild >= 7.22-4

Requires:      drupal7
Requires:      drupal7-ctools
Requires:      drupal7-token
Requires:      drupal7-views
#Requires:      drupal7(ctools)
#Requires:      drupal7(token)
#Requires:      drupal7(views)
# phpci
Requires:      php-hash
Requires:      php-pcre

%description
The Metatag module allows you to automatically provide structured metadata,
aka "meta tags", about your website. In the context of search engine
optimization, when people refer to meta tags they are usually referring to
the meta description tag and the meta keywords tag that may help improve
the rankings and display of your site in search engine results.

Meta tags have additional uses like the Open Graph Protocol used by Facebook,
specifying the canonical location [2] of content across multiple URLs or
domains.

This project is the designated Drupal 7 a from-the-ground-up rewrite and
successor of the Nodewords module.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_context
* %{module_name}_dc
* %{module_name}_opengraph
* %{module_name}_panels (NOTE: Requires manual install of the panels module)
* %{module_name}_twitter_cards
* %{module_name}_ui
* %{module_name}_views


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
* Thu May 23 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.2.beta7
- Updated for drupal7-rpmbuild auto-provides

* Sun May 19 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta7
- Initial package
