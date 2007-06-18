Summary:	An X Window System kernel parameter monitoring tool
Name:		xsysinfo
Version:	1.7
Release:	%mkrel 17
License:	MIT
Group:		Monitoring
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/xsysinfo-%{version}.tar.bz2
Source1:	%{name}
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		xsysinfo-imake.patch.bz2
Patch1:		xsysinfo-1.7-xf4.patch.bz2
Patch2:		xsysinfo-1.7-includes.patch.bz2
BuildRequires:	XFree86-devel xpm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters:  CPU load
average, CPU load, memory and swap sizes.

Install the xsysinfo package if you'd like to use a graphical kernel
monitoring tool.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1 -b .includes
make clean

%build
xmkmf
%make CDEBUGFLAGS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

install -d $RPM_BUILD_ROOT%{_menudir}
cat <<EOF >$RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
	needs="X11" \
	section="Applications/Monitoring" \
	title="Xsysinfo" \
	longtitle="System information" \
	command="%{_prefix}/X11R6/bin/%{name}" \
	icon="%{name}.png"
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

rm -f $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

%post
%{update_menus}
 
%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{_prefix}/X11R6/bin/xsysinfo
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XSysinfo
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XSysinfo-color
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
