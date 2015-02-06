Name:		cboard
Version:	0.7.1
Release:	2
Summary:	Console frontend of gnuchess
License:	GPLv2
Group:		Games/Boards
URL:		http://benkibbey.wordpress.com/cboard/
Source0:	http://sourceforge.net/projects/c-board/files/0.7.1/%{name}-%{version}.tar.bz2
Patch0:		cboard-0.6-mode.patch
BuildRequires:	pkgconfig(ncursesw)
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
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/man?/*
