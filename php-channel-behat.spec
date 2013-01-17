%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}

%global pear_channel pear.behat.org

Name:             php-channel-behat
Version:          1.3
Release:          1%{?dist}
Summary:          Adds %{pear_channel} channel to PEAR

Group:            Development/Libraries
License:          Public Domain
URL:              http://%{pear_channel}
Source0:          http://%{pear_channel}/channel.xml

BuildArch:        noarch
BuildRequires:    php-pear(PEAR)

Requires:         php-pear(PEAR)
Requires(post):   %{__pear}
Requires(postun): %{__pear}

Provides:         php-channel(%{pear_channel})

%description
This package adds the %{pear_channel} channel which allows PEAR packages
from this channel to be installed.


%prep
%setup -q -c -T


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{SOURCE0} %{buildroot}%{pear_xmldir}/%{name}.xml


%post
if [ $1 -eq  1 ] ; then
   %{__pear} channel-add %{pear_xmldir}/%{name}.xml > /dev/null || :
else
   %{__pear} channel-update %{pear_xmldir}/%{name}.xml > /dev/null || :
fi


%postun
if [ $1 -eq 0 ] ; then
   %{__pear} channel-delete %{pear_channel} > /dev/null || :
fi


%files
%{pear_xmldir}/%{name}.xml


%changelog
* Sun Jan 13 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.3-1
- Initial package (version matches channel REST version)
