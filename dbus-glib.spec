%define api	1
%define major	2
%define libname	%mklibname dbus-glib- %{api} %{major}
%define devname	%mklibname dbus-glib- %{api} -d

%define git_url git://git.freedesktop.org/git/dbus/dbus-glib
%bcond_with	crosscompile

Summary:	D-Bus message bus
Name:		dbus-glib
Version:	0.100.2
Release:	6
License:	AFL and GPLv2
Group:		System/Libraries
Url:		http://www.freedesktop.org/Software/dbus
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description 
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{libname}
Summary:	D-Bus GLib-based library
Group:		System/Libraries
Provides:	dbus-glib = %{version}-%{release}

%description -n %{libname}
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package -n %{devname}
Summary:	D-Bus headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers libraries for D-Bus.

%prep
%setup -q
#fix build with new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*
autoreconf -fi

%build
%if %{with crosscompile}
export ac_cv_have_abstract_sockets=yes
export ac_cv_func_posix_getpwnam_r=yes
export have_abstract_sockets=yes
%endif
%configure2_5x  \
	--disable-static \
	--disable-tests \
	--disable-verbose-mode \
%if %{with crosscompile}
	--with-dbus-binding-tool=/usr/bin/dbus-binding-tool \
%endif
	--disable-asserts

%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdbus-glib-%{api}.so.%{major}*

%files -n %{devname}
%{_bindir}/dbus-binding-tool
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libdir}/dbus-bash-completion-helper
%{_libdir}/libdbus-glib-%{api}.so
%{_libdir}/pkgconfig/dbus-glib-%{api}.pc
%{_includedir}/dbus-1.0/dbus/*.h
%{_datadir}/gtk-doc/html/dbus-glib/
%{_mandir}/man1/*
