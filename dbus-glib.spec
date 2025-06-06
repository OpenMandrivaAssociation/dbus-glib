%define api 1
%define major 2
%define libname %mklibname dbus-glib- %{api} %{major}
%define devname %mklibname dbus-glib- %{api} -d

%define git_url git://git.freedesktop.org/git/dbus/dbus-glib
%bcond_with crosscompile

Summary:	D-Bus message bus
Name:		dbus-glib
Version:	0.114
Release:	1
License:	AFL and GPLv2+
Group:		System/Libraries
Url:		https://www.freedesktop.org/Software/dbus
Source0:	http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gio-2.0) >= 2.32
BuildRequires:	pkgconfig(gobject-2.0) >= 2.32
BuildRequires:	chrpath

%description
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	D-Bus GLib-based library
Group:		System/Libraries
Provides:	dbus-glib = %{EVRD}

%description -n %{libname}
D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%files -n %{libname}
%{_libdir}/libdbus-glib-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	D-Bus headers
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Headers libraries for D-Bus.

%files -n %{devname}
%{_bindir}/dbus-binding-tool
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libexecdir}/dbus-bash-completion-helper
%{_libdir}/libdbus-glib-%{api}.so
%{_libdir}/pkgconfig/dbus-glib-%{api}.pc
%{_includedir}/dbus-1.0/dbus/*.h
%{_datadir}/gtk-doc/html/dbus-glib/
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%if %{with crosscompile}
export ac_cv_have_abstract_sockets=yes
export ac_cv_func_posix_getpwnam_r=yes
export have_abstract_sockets=yes
%endif
%configure  \
	--disable-static \
	--disable-tests \
	--disable-verbose-mode \
%if %{with crosscompile}
	--with-dbus-binding-tool=/usr/bin/dbus-binding-tool \
%endif
	--disable-asserts

%make_build

%install
%make_install

chrpath --delete %{buildroot}%{_bindir}/dbus-binding-tool
chrpath --delete %{buildroot}%{_libexecdir}/dbus-bash-completion-helper

# Scripts that are sourced should not be executable.
chmod -x %{buildroot}%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh

