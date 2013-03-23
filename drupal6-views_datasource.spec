%{!?drupal6: %global drupal6 %{_datadir}/drupal6}
%{!?drupal6_modules: %global drupal6_modules %{drupal6}/sites/all/modules}

%global module_name views_datasource
%global pre_release beta2

Name:      drupal6-%{module_name}
Version:   1.0
Release:   0.1.%{pre_release}%{?dist}
Summary:   Plugins for Drupal Views for rendering content in a number formats

Group:     Applications/Publishing
License:   GPLv2
URL:       http://drupal.org/project/%{module_name}
Source0:   http://ftp.drupal.org/files/projects/%{module_name}-6.x-%{version}-%{pre_release}.tar.gz
Source1:   %{name}-RPM-README.txt

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  drupal6
Requires:  drupal6-views
#Requires:  drupal6(views)
# phpci
Requires:  php-date
Requires:  php-json
Requires:  php-pcre

Provides:  drupal6(views_json) = %{version}
Provides:  drupal6(views_rdf) = %{version}
Provides:  drupal6(views_xhtml) = %{version}
Provides:  drupal6(views_xml) = %{version}

%description
Views Datasource is a set of plugins for Drupal Views for rendering content in
a number of shareable, reusable formats based on XML, JSON and XHTML. These
formats allow content in a Drupal site to be easily used as data sources for
Semantic Web clients and web mash-ups. Views Datasource plugins output content
from node lists created in the Drupal Views interface in a variety of formats -
XML data documents using schemas like OPML and Atom, RDF data documents using a
vocabulary like FOAF, JSON data documents in a format like Exhibit JSON, and
XHTML data documents using a microformat like hCard.

Views Datasource can be thought of as a userland complement to the work going on
in the Services and RDF APIs as a site operator only needs to know Views to be
able to create datasources in the different formats.

The project consists of 4 Views style plugins (and related row plugins):
* views_xml - Output as raw XML, OPML, and Atom;
* views_json - Output as Simile/Exhibit JSON, Canonical JSON, JSONP/JSON in
               script;
* views_rdf- Output as FOAF, SIOC, and DOAP;
* views_xhtml - Output as hCard, hCalendar, and Geo.

This package provides the following Drupal modules:
* views_json
* views_rdf
* views_xhtml
* views_xml


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
* Fri Mar 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-0.1.beta2
- Initial package
