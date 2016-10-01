Name:    dapper-dark
Version: 3.20
Release: 1%{?dist}
Summary: Dapper Linux Dark Theme
URL:     https://github.com/dapperlinux/dapper-dark
License: GPLv3+
BuildArch: noarch
Source0: https://github.com/dapperlinux/dapper-dark/archive/3.20.tar.gz
Requires: gtk-murrine-engine

%description
Dapper Dark is a Gnome-Shell theme for the Dapper Linux operating system.
The shell theme is based on hdni's Phosphene, and the GTK theme is based
on Arc-Dark. 

%prep
%autosetup -n %{version}

%build

%install
mkdir -p %{buildroot}/usr/share/themes/
cp -r %{name} %{buildroot}/usr/share/themes/

%files
/usr/share/themes/%{name}/*

%changelog
* Sat Oct 1 2016 Matthew Ruffell
- 3.20 r1 Initial Packaging
