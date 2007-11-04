%define version 0.5
%define release %mkrel 1

Summary:	Console frontend of gnuchess
Name:		cboard
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://arbornet.org/~bjk/cboard/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		%{name}-%{version}.tar.gz

BuildRequires:	ncurses-devel
Requires:	gnuchess

%description
CBoard is a console frontend to GNU Chess, using the ncurses library for
the interface. It can edit PGN tags, annotate moves with NAG, and more.

%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/man?/*


