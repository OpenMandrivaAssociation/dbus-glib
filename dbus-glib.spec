%define glib2_version           2.6.0
%define dbus_version		0.94

%define lib_major 2
%define lib_api 1
%define lib_name %mklibname dbus-glib- %{lib_api} %{lib_major}


Summary: D-Bus message bus
Name: dbus-glib
Version: 0.74
Release: %mkrel 4
URL: http://www.freedesktop.org/Software/dbus
Source0: http://dbus.freedesktop.org/releases/%name/%{name}-%{version}.tar.gz
# (fc) 0.71-1mdv don't require running bus to build (Fedora)
Source1: dbus-bus-introspect.xml
# (fc) 0.74-2mdv fix introspection (fd.o bug #8607) (GIT)
Patch0: dbus-glib-0.74-broken-xml.patch
# (fc) 0.74-2mdv Dispatch NameOwnerChanged signals to proxies only once (fdo #12505)
Patch1: dbus-glib-proxy-signals-once.patch
# (proyvind) https://bugs.freedesktop.org/show_bug.cgi?id=14429
Patch2: dbus-glib-0.73-ignore-namespaces.patch

License: AFL/GPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libxml2-devel
BuildRequires: libexpat-devel

%description 
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{lib_name}
Summary: GLib-based library for using D-Bus
Group: System/Libraries
Provides: dbus-glib = %{version}-%{release}
# keep this provides to be able Mdv 2007.0 using urpmi
Provides: libdbus-glib = %{version}-%{release}

%description -n %{lib_name}
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{lib_name}-devel
Summary: Libraries and headers for D-Bus
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: lib%{name}-1-devel = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
Headers and static libraries for D-Bus.


%prep
%setup -q
%patch0 -p1 -b .broken-xml
%patch1 -p1 -b .proxy-signal-once
%patch2 -p1 -b .ignore-namespaces

%build

%define _localstatedir %{_var}

%configure2_5x  \
    --disable-tests \
    --disable-verbose-mode \
    --disable-asserts \
    --with-introspect-xml=%{SOURCE1}

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged file
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*glib*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/dbus-binding-tool
%{_libdir}/libdbus-glib-%{lib_api}.a
%{_libdir}/libdbus-glib-%{lib_api}.so
%{_libdir}/pkgconfig/dbus-glib-%{lib_api}.pc
%{_includedir}/dbus-1.0/dbus/dbus-glib-bindings.h
%{_includedir}/dbus-1.0/dbus/dbus-gtype-specialized.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-error-enum.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-lowlevel.h
%{_includedir}/dbus-1.0/dbus/dbus-glib.h
%{_datadir}/gtk-doc/html/dbus-glib/
