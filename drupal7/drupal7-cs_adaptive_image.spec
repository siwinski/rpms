%{?drupal7_find_provides_and_requires}

%global module_name cs_adaptive_image

Name:          drupal7-%{module_name}
Version:       1.0
Release:       2%{?dist}
Summary:       Client-side adaptive image

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(image)

%description
The Client-side adaptive image module helps build responsive web designs with
fluid images by providing an Image field formatter that allows you to select
appropriate image styles for various client widths. With this module, you can
ensure that for each Image field only the most appropriately sized image gets
downloaded by the client.

You can serve light images to mobile users while still providing the best
quality images to visitors equipped with large screens.

Some highlights:
* Per-field configuration (for each view mode)
* Relies on JavaScript but provides a clean fallback for clients lacking it
* No cookies required
* No external libraries required
* No extra server configuration needed
* Does not attempt to perform any client OS detection
* Reverse proxy cache friendly

This package provides the following Drupal module:
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
* Sat Jun 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2
- Updated for drupal7-rpmbuild 7.22-5

* Sat May 04 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
