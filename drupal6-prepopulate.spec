%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name prepopulate

Name:      drupal6-%{module_name}
Version:   2.2
Release:   1%{?dist}
Summary:   Allows form elements to be pre-populated from the URL

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6

Provides:  drupal6(%{module_name}) = %{version}

%description
The Prepopulate module allows fields in most forms to be pre-populated from
the $_REQUEST variable.

For example, the following URL:

http://www.example.com/node/add/blog?edit[title]=this is the title

will automatically fill the Title field on a new blog post with the words
"this is the title". Any field can be pre-populated this way, including taxonomy
and CCK fields. You can prepopulate more than one field at a time as well.
Prepopulate is excellent for creating bookmarklets. For examples on usage for
all of these cases, please read the USAGE.txt file that comes with the module
or you can read the online handbook page (http://drupal.org/node/228167).

This package provides the following Drupal modules:
* %{module_name}


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.2-1
- Initial package
