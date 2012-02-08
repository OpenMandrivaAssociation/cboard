Name:		cboard
Version:	0.6
Release:	%mkrel 1
Summary:	Console frontend of gnuchess
License:	GPLv2
Group:		Games/Boards
URL:		http://benkibbey.wordpress.com/cboard/
Source0:	http://downloads.sourceforge.net/c-board/%{name}-%{version}.tar.bz2
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


