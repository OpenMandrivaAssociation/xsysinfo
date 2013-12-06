%define name	xsysinfo
%define version	1.7
Summary:	An X Window System kernel parameter monitoring tool
Name:		%{name}
Version:	%{version}
Release:	32
License:	MIT
Group:		Monitoring
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/xsysinfo-%{version}.tar.bz2
Source1:	%{name}
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		xsysinfo-1.7-imake.patch
Patch1:		xsysinfo-1.7-xf4.patch
Patch2:		xsysinfo-1.7-includes.patch
BuildRequires:	imake
BuildRequires:	pkgconfig(x11)
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)

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
%make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%ldflags"

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

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7-26mdv2011.0
+ Revision: 671370
- mass rebuild

* Tue Dec 21 2010 Funda Wang <fwang@mandriva.org> 1.7-25mdv2011.0
+ Revision: 623573
- update BR
- use our own flag

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-24mdv2010.1
+ Revision: 524472
- rebuilt for 2010.1

* Wed Mar 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-23mdv2009.1
+ Revision: 361187
- rediff fuzzy patch
- decompress all patches

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.7-20mdv2009.0
+ Revision: 226089
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.7-19mdv2008.1
+ Revision: 179464
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Jun 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.7-18mdv2008.0
+ Revision: 40738
- new X layout; trim buildrequires; xdg menu; fd.o icons; rebuild for new era
- Import xsysinfo



* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 1.7-17mdk
- rebuild

* Tue Jun 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.7-16mdk
- fix unpackaged files
- convert icons to png
- generate menu during %%install in stead

* Fri Sep 26 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.7-15mdk
- lib64 & includes fixes

* Thu Sep 04 2003 Aurelien Lemaire <alemaire@mandrakesoft.com> 1.7-14mdk
- Fix buildrequires with vitual providing name on libxpm-devel
- Macroize the %%config files
- Clean spec file

* Sun Jul 13 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.7-13mdk
- macroize
- fix unpackaged files

* Fri Sep 06 2002 Aurelien Lemaire <alemaire@mandraksoft.com> 1.7-12mdk
- Rebuild for new g++3.2

* Thu Aug 30 2001 Etienne Faure  <etienne@mandraksoft.com> 1.7-11mdk
- rebuild

* Thu Jan 11 2001 David BAUDENS <baudens@mandrakesoft.com> 1.7-10mdk
- BuildRequires: libxpm4-devel

* Sat Dec 16 2000 Etienne Faure  <etienne@mandraksoft.com> 1.7-9mdk
- cleaned menu entry
- macros
- normal and large icons

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.7-8mdk
- automatically added BuildRequires

* Mon Jul 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.7-7mdk
- macro-ize
- use _menudir just as titi commands me :)

* Wed Jul 18 2000 Etienne Faure <etienne@mandrakesoft.com> 1.7-6mdk
- Added file 'CHANGES' to doc

* Fri May 26 2000 Adam Lebsack <adam@mandrakesoft.com> 1.7-5mdk
- Imake bugfix for XFree86 4.0

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.7-4mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.7-3mdk
- Added menu entry.

* Tue Mar 28 2000 dam's <damien@mandrakesoft.com> 1.7-2mdk
- Release.

* Wed Nov 03 1999 Jerome Martin <jerome@mandrakesoft.com>
- Updated to version 1.7 with SMP support
- Specfile cleanup
- Rebuild for new distribution

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Fri Dec 20 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
