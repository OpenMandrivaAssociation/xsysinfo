%define name	xsysinfo
%define version	1.7
%define release	%mkrel 18
Summary:	An X Window System kernel parameter monitoring tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
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
BuildRequires:	imake libx11-devel libxext-devel libxaw-devel libxmu-devel libxt-devel libxp-devel xpm-devel

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

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Xsysinfo
Comment=System information
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Monitor;X-MandrivaLinux-System-Monitoring;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

rm -f $RPM_BUILD_ROOT/%{_prefix}/lib/X11/app-defaults

%post
%{update_menus}
%update_icon_cache hicolor
 
%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{_bindir}/xsysinfo
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XSysinfo
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XSysinfo-color
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
