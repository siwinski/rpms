%global github_owner          symfony
%global github_name           Icu
%global github_version        1.1.0
%global github_commit         b4081efff21a8a85c57789a39f454fed244f8e46

%global php_min_ver           5.3.3
# "symfony/intl": "~2.3" (composer.json)
%global symfony_intl_min_ver  2.3
%global symfony_intl_max_ver  3.0
# "lib-ICU": ">=3.8" (composer.json)
%global libicu_min_ver        3.8

%global symfony_dir           %{_datadir}/php/Symfony

Name:           php-symfony2-icu
Version:        %{github_version}
Release:        1%{dist}
Summary:        Symfony2 Icu Component

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/symfony/Icu
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(icu%{!?el6:-i18n})

Requires:       php(language)     >= %{php_min_ver}
Requires:       php-symfony2-intl >= %{symfony_intl_min_ver}
Requires:       php-symfony2-intl <  %{symfony_intl_max_ver}
# phpcompatinfo
Requires:       php-ctype
Requires:       php-intl

%description
Contains data of the ICU library.

You should not directly use this component. Use it through the API of the Intl
component instead.


%prep
%setup -q -n %{github_name}-%{github_commit}


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}%{symfony_dir}/Component/Icu
cp -rp *.php Resources %{buildroot}%{symfony_dir}/Component/Icu/

# Lang files
for res_file in \
    %{buildroot}%{symfony_dir}/Component/Icu/Resources/data/*/*.res
do
    res_file_lang=$(basename $res_file | sed 's#\(_.*\)*\.res##')
    if [ "root" != "$res_file_lang" ] && \
       [ "supplementaldata" != "$res_file_lang" ]
    then
        echo "%lang($res_file_lang) $res_file"
    else
        echo "$res_file"
    fi
done > %{name}.lang
sed -i "s#%{buildroot}##" %{name}.lang


%check
pkg-config icu%{!?el6:-i18n} --atleast-version=%{libicu_min_ver} || exit 1

# NOTE: PHPUnit tests will be run when the required php-symfony2-intl pkg
# version is available


%files -f %{name}.lang
%doc LICENSE *.md composer.json
%doc Resources/data/*.txt

%dir %{symfony_dir}/Component/Icu
     %{symfony_dir}/Component/Icu/*.php
%dir %{symfony_dir}/Component/Icu/Resources
%dir %{symfony_dir}/Component/Icu/Resources/data
%dir %{symfony_dir}/Component/Icu/Resources/data/curr
%dir %{symfony_dir}/Component/Icu/Resources/data/lang
%dir %{symfony_dir}/Component/Icu/Resources/data/locales
%dir %{symfony_dir}/Component/Icu/Resources/data/region
%exclude %{symfony_dir}/Component/Icu/Resources/data/*.txt


%changelog
* Sun Nov 17 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.1.0-1
- Initial package