%{?drupal7_find_provides_and_requires}

%global module_name fences

Name:          drupal7-%{module_name}
Version:       1.0
Release:       2%{?dist}
Summary:       Configurable field wrappers

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.22-5

Requires:      drupal7(field)

%description
Fences is a an easy-to-use tool to specify an HTML element for each field. This
element choice will propagate everywhere the field is used, such as teasers, RSS
feeds and Views. You don't have to keep re-configuring the same HTML element
over and over again every time you display the field.

Best of all, Fences provides leaner markup than Drupal 7 core! And can get rid
of the extraneous classes too!

This kind of tool is needed in order to create semantic HTML5 output from
Drupal. Without such a tool, you have to create custom field templates in your
theme for every field. :(

Similar projects include Semantic fields [1], Field Wrappers [2] and a tool
inside the Display Suite [3] extras.

This package provides the following Drupal module:
* %{module_name}

[1] http://drupal.org/project/semantic_fields
[2] http://drupal.org/project/field_wrappers
[3] http://drupal.org/project/ds


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
* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2
- Updated for drupal7-rpmbuild 7.22-5

* Tue Apr 02 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
