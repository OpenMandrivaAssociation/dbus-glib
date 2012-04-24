%define major 2
%define api 1
%define libname %mklibname dbus-glib- %{api} %{major}
%define develname %mklibname dbus-glib- %{api} -d

%define git_url git://git.freedesktop.org/git/dbus/dbus-glib


Summary: D-Bus message bus
Name: dbus-glib
Version: 0.98
Release: 4
License: AFL and GPLv2
Group: System/Libraries
URL: http://www.freedesktop.org/Software/dbus
Source0: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0: dbus-glib-0.98-format-string.patch

BuildRequires: expat-devel
BuildRequires: pkgconfig(dbus-1) >= 0.94
BuildRequires: pkgconfig(glib-2.0) >= 2.6.0
BuildRequires: pkgconfig(libxml-2.0)

%description 
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{libname}
Summary: D-Bus GLib-based library
Group: System/Libraries
Provides: dbus-glib = %{version}-%{release}
# keep this provides to be able Mdv 2007.0 using urpmi
Provides: libdbus-glib = %{version}-%{release}

%description -n %{libname}
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{develname}
Summary: D-Bus headers
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname %{name}- %{api} %{major} -d

%description -n %{develname}
Headers libraries for D-Bus.

%prep
%setup -q
%apply_patches

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

#remove unpackaged file
rm -f %{buildroot}%{_libdir}/*.la

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
