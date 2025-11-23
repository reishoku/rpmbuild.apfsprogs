Name: apfsprogs
Version: 0.2.1
Release: 1%{?dist}
Summary: Experimental APFS tools for linux

License: GPL-2.0
URL: https://github.com/linux-apfs/apfsprogs
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Apfsprogs is a suite of userland software to work with the Apple File System on Linux.

%prep
%autosetup

%build
for d in "apfs-label" "apfs-snap" "apfsck" "mkapfs" "lib"; do
  %make_build -C "$d"
done

%install
for d in "apfs-label" "apfs-snap" "apfsck" "mkapfs"; do
  %make_install -C "$d" DESTDIR=%{buildroot}%{_prefix}
done
%{__mkdir_p} %{buildroot}%{_libdir}
%{__install} -p -s -m '0644' lib/libapfs.a %{buildroot}%{_libdir}
%{__cp} -pr include/ %{buildroot}%{_includedir}

%check

%files
%{_bindir}/apfs-label
%{_bindir}/apfs-snap
%{_bindir}/apfsck
%{_bindir}/mkapfs
%{_bindir}/fsck.apfs
%{_bindir}/mkfs.apfs
%{_libdir}/libapfs.a
%{_includedir}/apfs
%license LICENSE
%doc
%{_mandir}/man8/apfs-label.8.gz
%{_mandir}/man8/apfs-snap.8.gz
%{_mandir}/man8/apfsck.8.gz
%{_mandir}/man8/fsck.apfs.8.gz
%{_mandir}/man8/mkapfs.8.gz
%{_mandir}/man8/mkfs.apfs.8.gz

%changelog
* Mon Nov 24 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 0.2.1-1
- Initial RPM packaging