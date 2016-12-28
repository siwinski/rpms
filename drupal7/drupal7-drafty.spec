%{?drupal7_find_provides_and_requires}

%global module drafty
%global pre_release beta3

Name:          drupal7-%{module}
Version:       1.0
Release:       0.1%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Facilitates handling of draft revisions

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: drupal7-rpmbuild >= 7.23-3

# drafty.info
Requires:      drupal7(entity)
# phpcompatinfo (computed from version 1.0-beta3)
#     <none>

%description
API module for handling drafts of revisions.

This module doesn't provide any workflow handling, but it should provide robust
mechanisms for creating new revisions as drafts, publishing revisions, and
deletion of old drafts.

The goal of drafty is to be a dependency for workflow modules such as Workbench
Moderation [1], CPS [2] (and others). Currently, each of the workflow modules
has their own implementation for saving draft revisions.

[1] https://www.drupal.org/project/workbench_moderation
[2] https://www.drupal.org/project/cps


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.md .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Wed Dec 28 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.beta3
- Initial package
