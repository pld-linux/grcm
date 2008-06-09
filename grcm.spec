Summary:	GNOME Remote Connection Manager
Summary(pl.UTF-8):	GNOME Remote Connection Manager - zarządca zdalnych połączeń dla GNOME
Name:		grcm
Version:	0.1.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/grcm/%{name}-%{version}.tar.bz2
# Source0-md5:	74ee03719fdfde1140a8a5b01a85db42
Patch0:		%{name}-makefile.patch
URL:		http://grcm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dmalloc
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Remote Connection Manager is a GNOME application that stores
information about remote connections. It gives you a GUI program to
launch applications like telnet, ssh or rdesktop. It is highly
configurable as to what type of applications it launches, so you are
not limited to the three listed. For example, I never thought of using
it for ftp, but it would be easy to setup.

%description -l pl.UTF-8
GNOME Remote Connection Manager (zarządca zdalnych połączeń dla GNOME)
to aplikacja przechowująca informacje o zdalnych połączeniach.
Udostępnia program z graficznym interfejsem użytkownika do
uruchamiania aplikacji typu telnet, ssh czy rdesktop. Jest wysoko
konfigurowalny co do rodzaju aplikacji, które uruchamia, więc nie
ogranicza do tych trzech wymienionych wyżej. Na przykład, autor nigdy
nie myślał o używaniu go do ftp, ale byłoby to łatwe w konfiguracji.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_pixmapsdir}/grcm
%{_pixmapsdir}/grcm/*.png
%{_pixmapsdir}/grcm/*.xpm
%{_omf_dest_dir}/%{name}
%{_desktopdir}/%{name}.desktop
