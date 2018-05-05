Name:    dapper-dark
Version: 3.28
Release: 1
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
%license LICENSE
/usr/share/themes/%{name}/*

%changelog
* Sat May  5 2018 Matthew Ruffell
- 3.28 Updating for DL28

* Thu Aug 10 2017 Matthew Ruffell
- 3.26 Updating for DL27

* Thu Aug 10 2017 Matthew Ruffell
- 3.24 Updating for DL26

* Fri Nov 4 2016 Matthew Ruffell
- 3.22 Updating for DL25

* Sat Oct 1 2016 Matthew Ruffell
- 3.20 Initial Packaging
