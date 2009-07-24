%define glib2_version           2.6.0
%define dbus_version		0.94

%define lib_major 2
%define lib_api 1
%define lib_name %mklibname dbus-glib- %{lib_api} %{lib_major}

%define git_url git://git.freedesktop.org/git/dbus/dbus-glib


Summary: D-Bus message bus
Name: dbus-glib
Version: 0.82
Release: %mkrel 1
URL: http://www.freedesktop.org/Software/dbus
Source0: http://dbus.freedesktop.org/releases/%name/%{name}-%{version}.tar.gz
# (fc) 0.71-1mdv don't require running bus to build (Fedora)
Source1: dbus-bus-introspect.xml

License: AFL and GPLv2
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libxml2-devel
BuildRequires: libexpat-devel
# needed by patch0
BuildRequires: gtk-doc

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

%build

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

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*glib*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/dbus-binding-tool
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libdir}/dbus-bash-completion-helper
%{_libdir}/libdbus-glib-%{lib_api}.a
%{_libdir}/libdbus-glib-%{lib_api}.so
%{_libdir}/pkgconfig/dbus-glib-%{lib_api}.pc
%{_includedir}/dbus-1.0/dbus/dbus-glib-bindings.h
%{_includedir}/dbus-1.0/dbus/dbus-gtype-specialized.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-error-enum.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-lowlevel.h
%{_includedir}/dbus-1.0/dbus/dbus-glib.h
%{_datadir}/gtk-doc/html/dbus-glib/
%{_mandir}/man1/*
