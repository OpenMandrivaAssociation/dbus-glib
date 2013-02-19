%define major 2
%define api 1
%define libname %mklibname dbus-glib- %{api} %{major}
%define develname %mklibname dbus-glib- %{api} -d

%define git_url git://git.freedesktop.org/git/dbus/dbus-glib


Summary:	D-Bus message bus
Name:		dbus-glib
Version:	0.100.1
Release:	1
License:	AFL and GPLv2
Group:		System/Libraries
URL:		http://www.freedesktop.org/Software/dbus
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	expat-devel
BuildRequires:	pkgconfig(dbus-1) >= 0.94
BuildRequires:	pkgconfig(glib-2.0) >= 2.6.0
BuildRequires:	pkgconfig(libxml-2.0)

%description 
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{libname}
Summary:	D-Bus GLib-based library
Group:		System/Libraries
Provides:	dbus-glib = %{version}-%{release}
# keep this provides to be able Mdv 2007.0 using urpmi
Provides:	libdbus-glib = %{version}-%{release}

%description -n %{libname}
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{develname}
Summary:	D-Bus headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}dbus-glib-1_2-devel < 0.98

%description -n %{develname}
Headers libraries for D-Bus.

%prep
%setup -q

%build
%configure2_5x  \
    --disable-static \
    --disable-tests \
    --disable-verbose-mode \
    --disable-asserts

%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*glib*.so.%{major}*

%files -n %{develname}
%{_bindir}/dbus-binding-tool
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libdir}/dbus-bash-completion-helper
%{_libdir}/libdbus-glib-%{api}.so
%{_libdir}/pkgconfig/dbus-glib-%{api}.pc
%{_includedir}/dbus-1.0/dbus/*.h
%{_datadir}/gtk-doc/html/dbus-glib/
%{_mandir}/man1/*


%changelog
* Tue Apr 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.98-4
+ Revision: 793231
- rebuild
- cleaned up spec

* Mon Dec 05 2011 ZÃ© <ze@mandriva.org> 0.98-3
+ Revision: 737992
- -rebuild
- set require to release due to rebuild against glib2
- fix description and summary

* Sat Nov 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.98-2
+ Revision: 733488
- cleaned up BRs
- rebuild
- cleaned up spec
- removed defattr
- disabled static build
- removed old ldconfig scriptlets
- removed clean section
- dropped major from devel pkg
- converted BRs to pkgconfig provides
- remove cooker section
- removed mkrel & BuildRoot

* Sat Oct 01 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.98-1
+ Revision: 702208
- new version
- fix a format string warning

* Fri Sep 23 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.96-1
+ Revision: 701062
- new version
- drop patch

* Wed Jul 20 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.94-2
+ Revision: 690744
- add a Debian patch to help with bug #63728

* Thu Jun 02 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.94-1
+ Revision: 682424
- new version
- update file list

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.92-4
+ Revision: 663757
- mass rebuild

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.92-3
+ Revision: 640264
- rebuild to obsolete old packages

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 0.92-2
+ Revision: 633652
- rebuild

* Mon Jan 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.92-1
+ Revision: 632476
- new version
- update file list

* Tue Aug 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.88-1mdv2011.0
+ Revision: 570899
- update to new version 0.88

* Thu Mar 25 2010 Frederic Crozat <fcrozat@mandriva.com> 0.86-1mdv2010.1
+ Revision: 527399
- Release 0.86

* Thu Jan 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.84-1mdv2010.1
+ Revision: 497523
- Release 0.84
- Remove source1, no longer needed
- Remove patch0, merged upstream

* Fri Jan 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-3mdv2010.1
+ Revision: 491757
- add debian patch allowing duplicate object registrations

* Fri Jan 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.82-2mdv2010.1
+ Revision: 491730
- add ListActivatableNames (bug #57068)

* Fri Jul 24 2009 Frederic Crozat <fcrozat@mandriva.com> 0.82-1mdv2010.0
+ Revision: 399304
- Release 0.82
- Remove patch1, merged upstream

* Tue Feb 03 2009 Frederic Crozat <fcrozat@mandriva.com> 0.80-1mdv2009.1
+ Revision: 336903
- Release 0.80
- Remove patch0 (merged upstream)
- Patch0: fix format-security error

* Fri Dec 05 2008 Frederic Crozat <fcrozat@mandriva.com> 0.78-1mdv2009.1
+ Revision: 310746
- Fix buildrequires
- Release 0.78
- Remove patch0 (merged upstream)
- Patch0: fix linking with expat

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.76-2mdv2009.0
+ Revision: 264400
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 09 2008 Frederic Crozat <fcrozat@mandriva.com> 0.76-1mdv2009.0
+ Revision: 217037
- Release 0.76
- Remove patches 0, 1, 2 (merged upstream)
- Patch0 (GIT): wincaps-to-uscore property names for GetAll() (fd.o bug #16114)

* Tue Mar 18 2008 Frederic Crozat <fcrozat@mandriva.com> 0.74-4mdv2008.1
+ Revision: 188466
- Add back old provides in lib package to fix upgrade from 2007.0 using urpmi

* Tue Mar 18 2008 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.74-3mdv2008.1
+ Revision: 188447
- Ignore namespaces in introspection XML (P2, fixes FD.obz #14429)

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 16 2007 Frederic Crozat <fcrozat@mandriva.com> 0.74-2mdv2008.1
+ Revision: 109059
- Replace patch0 with source0 (Fedora), allowing build without dbus running
- Patch0 (GIT): fix introspection (fd.o #8607)
- Patch1: Dispatch NameOwnerChanged signals to proxies only once (fdo #12505)

* Thu Jul 05 2007 Frederic Crozat <fcrozat@mandriva.com> 0.74-1mdv2008.0
+ Revision: 48555
- Release 0.74

* Fri Jun 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.73-2mdv2008.0
+ Revision: 37262
- rebuild for expat
- spec file clean


* Thu Feb 15 2007 Frederic Crozat <fcrozat@mandriva.com> 0.73-1mdv2007.0
+ Revision: 121292
- Release 0.73

* Wed Dec 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.72-2mdv2007.1
+ Revision: 96159
- fix library provides

* Thu Nov 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.72-1mdv2007.1
+ Revision: 75200
- Import dbus-glib

* Thu Nov 02 2006 Götz Waschk <waschk@mandriva.org> 0.72-1mdv2007.1
- bump deps
- add gtk-docs
- unpack patch
- fix source URL
- new version

* Sat Aug 19 2006 Frederic Crozat <fcrozat@mandriva.com> 0.71-5mdv2007.0
- Fix lib package provides on x86-64

* Tue Aug 08 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.71-4
- add BuildRequires: libexpat-devel

* Sat Aug 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.71-3mdv2007.0
- fix buildrequires

* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.71-2mdv2007.0
- Fix requires of devel package

* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.71-1mdv2007.0
- Initial package
- Patch0 (Fedora): don't require running bus to build

