%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name user_badges

Name:      drupal6-%{module_name}
Version:   1.6
Release:   1%{?dist}
Summary:   Enables assignment of graphical badges to users and roles

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
# phpci
Requires:  php-pcre

%description
The User Badges module allows each user to be assigned 'badges' which can be
displayed as a series of iconic images.

A common use will probably be to display the badges along with the user's
information within forums, comments, or node postings. These badges can be
assigned individually by the administrator or attached to a role so that,
for example, all users in the 'admin' role will show the 'Administrator'
badge which could display as a graphic letter 'A'.

Any badge can optionally be associated to a URL that links the image to a
description page. If a user has more than one badge, there is also a mechanism
that allows administrators to only show the highest-level badge. You can also
set a special badge for blocked users and even override their role badges with
this one.

User Badges can be used as a way to establish trust (in the same way as eBay's
star graphics), or as an incentive for users. They can also be a quick way to
identify moderators, administrators, or anyone with a given role.


%prep
%setup -qn %{module_name}

cp -p %{SOURCE1} .


%build
# Empty build section, nothing required


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{drupal6_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal6_modules}/%{module_name}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal6_modules}/%{module_name}
%exclude %{drupal6_modules}/%{module_name}/*.txt


%changelog
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.6-1
- Initial package
