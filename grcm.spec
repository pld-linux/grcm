Summary:	GNOME Remote Connection Manager
Summary(pl):	GNOME Remote Connection Manager - zarz±dca zdalnych po³±czeñ dla GNOME
Name:		grcm
Version:	0.1.5
Release:	2
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0e4d1d226e51ed1388db191d3b5f965a
Patch0:		%{name}-desktop.patch
URL:		http://grcm.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dmalloc
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Remote Connection Manager is a GNOME application that stores
information about remote connections. It gives you a GUI program to
launch applications like telnet, ssh or rdesktop. It is highly
configurable as to what type of applications it launches, so you are
not limited to the three listed. For example, I never thought of using
it for ftp, but it would be easy to setup.

%description -l pl
GNOME Remote Connection Manager (zarz±dca zdalnych po³±czeñ dla GNOME)
to aplikacja przechowuj±ca informacje o zdalnych po³±czeniach.
Udostêpnia program z graficznym interfejsem u¿ytkownika do
uruchamiania aplikacji typu telnet, ssh czy rdesktop. Jest wysoko
konfigurowalny co do rodzaju aplikacji, które uruchamia, wiêc nie
ogranicza do tych trzech wymienionych wy¿ej. Na przyk³ad, autor nigdy
nie my¶la³ o u¿ywaniu go do ftp, ale by³oby to ³atwe w konfiguracji.

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
%{_pixmapsdir}/grcm
%{_omf_dest_dir}/%{name}
%{_desktopdir}/%{name}.desktop
