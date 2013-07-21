Name:		cboard
Version:	0.6.1
Release:	1
Summary:	Console frontend of gnuchess
License:	GPLv2
Group:		Games/Boards
URL:		http://benkibbey.wordpress.com/cboard/
Source0:	http://sourceforge.net/projects/c-board/files/0.6.1/%{name}-%{version}.tar.bz2
Patch0:		cboard-0.6-mode.patch
BuildRequires:	ncurses-devel
Requires:	gnuchess

%description
CBoard is a console frontend to GNU Chess, using the ncurses library for
the interface. It can edit PGN tags, annotate moves with NAG, and more.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/man?/*




%changelog
* Wed Feb 08 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6-1mdv2011.0
+ Revision: 771891
- New version 0.6, new URL, spec cleanup

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.5-2mdv2008.1
+ Revision: 109292
- rebuild for new lzma

* Sun Nov 04 2007 Olivier Thauvin <nanardon@mandriva.org> 0.5-1mdv2008.1
+ Revision: 105715
- 0.5


* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:38:28 (52991)
- 0.2.4
- remove menu entry (is text application)

* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:31:49 (52920)
Import cboard

* Sun May 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.2.3-1mdk
- New release 0.2.3

* Thu May 04 2006 Jerome Soyer <saispo@mandriva.org> 0.2.2-1mdk
- New release 0.2.2

* Wed Apr 26 2006 Lenny Cartier <lenny@mandriva.com> 0.2.1-1mdk
- rebuild

* Sat Dec 31 2005 Olivier Thauvin <nanardon@mandriva.org> 0.1.6-4mdk
- rebuild

* Mon Dec 20 2004 Abel Cheung <deaddog@mandrake.org> 0.1.6-3mdk
- Rebuild

* Mon Nov 03 2003 Abel Cheung <deaddog@deaddog.org> 0.1.6-2mdk
- Move binaries and data files to games dir

* Fri Sep 19 2003 Abel Cheung <maddog@linux.org.hk> 0.1.6-1mdk
- First Mandrake package
- Patch0: Fix compilation with newest gcc


