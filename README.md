# dapper-dark

##About
The Dapper Dark package contains the gnome-shell theme used in Dapper Linux. The shell theme is a heavily modified version of hdni's phosphene shell theme, and the GTK theme is a derivative of arc-dark.


##Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file dapper-dark.spec in the SPECS directory, and rename the dapper-dark directory to dapper-dark-3.22 and compress it:
```bash
$ mv dapper-dark.spec ~/rpmbuild/SPECS/
$ mv dapper-dark dapper-dark-3.22
$ tar -czvf dapper-dark-3.22.tar.gz dapper-dark-3.22
$ mv dapper-dark-3.22.tar.gz ~/rpmbuild/SOURCES/
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba dapper-dark.spec
```


