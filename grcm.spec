Summary:	Gnome Remote Connection Manager
Name:		grcm
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://grcm.sf.net/
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	dmalloc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Remote Connection Manager is a Gnome application that stores
information about remote connections. It gives you a GUI program to
launch applications like telnet, ssh or rdesktop. It is highly
configurable as to what type of applications it launches, so you are
not limited to the three listed. For example, I never thought of using
it for ftp, but it would be easy to setup.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/grcm
