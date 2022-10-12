Name:       sailfish-locale

Summary:    Locale definitions
Version:    0
Release:    1
URL:        https://bitbucket.org/jolla/base-sailfish-locale
License:    Proprietary
Source0:    %{name}-%{version}.tar.bz2
Provides:   locale
Conflicts:  jolla-settings-system <= 1.1.65
BuildRequires:  glibc-common

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -m 0644 -D -t %{buildroot}%{_datadir}/jolla-supported-languages/ language/*.conf

# Replace locale archive with one that has only supported locales
mkdir -p  %{buildroot}%{_prefix}/lib/locale/
# unconditionally include en_US.UTF-8
localedef --replace -i en_US -f UTF-8 en_US.utf8 --prefix=%{buildroot}/
find language/ -type f -name '*.conf' \
    |xargs grep -h Locale |cut -d=  -f2 |cut -d. -f1 \
    |xargs -t -n1 -I@@ localedef --replace -i @@ -f UTF-8 @@.utf8 --prefix=%{buildroot}/

%files
%defattr(-,root,root,-)
%{_datadir}/jolla-supported-languages/
%{_prefix}/lib/locale/locale-archive
