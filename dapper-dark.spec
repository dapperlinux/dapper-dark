Name:    dapper-dark
Version: 3.22
Release: 1%{?dist}
Summary: Dapper Linux Dark Theme
URL:     https://github.com/dapperlinux/dapper-dark
License: GPLv3+
BuildArch: noarch
Source0: %{name}-%{version}.tar.xz
Requires: gtk-murrine-engine

%description
Dapper Dark is a Gnome-Shell theme for the Dapper Linux operating system.
The shell theme is based on hdni's Phosphene, and the GTK theme is based
on Arc-Dark. 

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/usr/share/themes/
cp -r %{name} %{buildroot}/usr/share/themes/

%files
/usr/share/themes/%{name}/*

%changelog
* Fri Nov 4 2016 Matthew Ruffell
- 3.22 Updating for F25

* Sat Oct 1 2016 Matthew Ruffell
- 3.20 r1 Initial Packaging
