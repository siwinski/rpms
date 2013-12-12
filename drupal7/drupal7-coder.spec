%{?drupal7_find_provides_and_requires}

%global module_name coder

Name:          drupal7-%{module_name}
Version:       2.0
Release:       1%{?dist}
Summary:       Developer module that assists with code review and version upgrade

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module_name}
Source0:       http://ftp.drupal.org/files/projects/%{module_name}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3
# For PEAR RPM macros
BuildRequires: php-pear(PEAR)

Requires:      php-pear(PHP_CodeSniffer) >= 1.3.5
# phpcompatinfo
Requires:      php-date
Requires:      php-ereg
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-tokenizer

%description
The Coder project includes two developer modules that assist with code review
and code manipulation. Each of the modules supports a plug-in extensible hook
system so contributed modules can define additional review standards and upgrade
routines.

This package provides the following Drupal modules:
* %{module_name}
* %{module_name}_review
* %{module_name}_upgrade


%prep
%setup -q -n %{module_name}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}

# Install Drupal module
mkdir -p -m 0755 %{buildroot}%{drupal7_modules}/%{module_name}
cp -pr * %{buildroot}%{drupal7_modules}/%{module_name}/

# Symlink PHP_CodeSniffer standards
mkdir -p -m 0755 %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/Standards
ln -s %{drupal7_modules}/%{module_name}/coder_sniffer/Drupal \
      %{buildroot}%{pear_phpdir}/PHP/CodeSniffer/Standards/Drupal


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.txt
%{drupal7_modules}/%{module_name}
%exclude %{drupal7_modules}/%{module_name}/*.txt
%{pear_phpdir}/PHP/CodeSniffer/Standards/Drupal


%changelog
* Thu Dec 12 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 2.0-1
- Initial package
