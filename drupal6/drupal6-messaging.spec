%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name messaging

Name:      drupal6-%{module_name}
Version:   2.4
Release:   1%{?dist}
Summary:   Messaging Framework to allow message sending in an independent way

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
# phpci
Requires:  php-date
Requires:  php-ereg
Requires:  php-pcre

Provides:  drupal6(%{module_name}) = %{version}
Provides:  drupal6(%{module_name}_debug) = %{version}
Provides:  drupal6(%{module_name}_mail) = %{version}
Provides:  drupal6(%{module_name}_mime_mail) = %{version}
Provides:  drupal6(%{module_name}_phpmailer) = %{version}
Provides:  drupal6(%{module_name}_privatemsg) = %{version}
Provides:  drupal6(%{module_name}_simple) = %{version}
Provides:  drupal6(%{module_name}_sms) = %{version}
Provides:  drupal6(%{module_name}_twitter) = %{version}
Provides:  drupal6(%{module_name}_xmpp) = %{version}

%description
This is a Messaging Framework to allow message sending in a channel independent
way. It will provide a common API for message composition and sending while
allowing plug-ins for multiple messaging methods.

When using this framework, you won't send e-mails to users anymore. You will
send them 'messages' and they will decide how they want to get them delivered,
that may be by mail, IM, SMS, depending on user's preferences.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_debug
* %{module_name}_mail
* %{module_name}_mime_mail (NOTE: Requires manual install of the mimemail module)
* %{module_name}_phpmailer
* %{module_name}_privatemsg (NOTE: Requires manual install of the privatemsg module)
* %{module_name}_simple
* %{module_name}_sms (NOTE: Requires manual install of the smsframework module)
* %{module_name}_twitter (NOTE: Requires manual install of the twitter module)
* %{module_name}_xmpp (NOTE: Requires manual install of the xmppframework module)


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.4-1
- Initial package
