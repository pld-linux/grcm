Summary:	Gnome Remote Connection Manager
Name:		grcm
Version:	0.1.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
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
%{_datadir}/applications/%{name}.desktop
