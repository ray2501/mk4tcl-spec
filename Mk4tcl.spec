%{!?directory:%define directory /usr}

Summary:	Metakit for Tcl extension
Name:		Mk4tcl
Version:	2.4.9.8
Release:	1
License:	MIT
Group:		Development/Languages/Tcl
Source0:	metakit-%{version}.tar.gz
URL:		https://github.com/jcw/metakit
BuildRequires:	autoconf
BuildRequires:	gcc-c++
BuildRequires:	tcl-devel >= 8.5
BuildRequires:	libstdc++-devel
Requires:       tcl >= 8.5
BuildRoot:	%{tmpdir}/metakit-%{version}

%description
Metakit is an embeddable database which runs on Unix, Windows,
Macintosh, and other platforms.  It lets you build applications which
store their data efficiently, in a portable way, and which will not need a
complex runtime installation.  In terms of the data model, Metakit takes
the middle ground between RDBMS, OODBMS, and flat-file databases - yet it
is quite different from each of them.

WHAT IT ISN'T - Metakit is not: 1) an SQL database, 2) multi-user/-threading,
3) scalable to gigabytes, 4) proprietary software, 5) a toy.

Mk4tcl is Metakit for Tcl extension, which allows you to create,
access, and manipulate Metakit datafiles using Tcl.

%prep
%setup -q -n metakit-%{version}

%build
export CC=g++
cd tcl
%configure --with-tcl=%{directory}/%{_lib} --prefix=%{directory} \
	   --exec-prefix=%{directory} \
	   --libdir=%{directory}/%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd tcl
%{__make} install \
        pkglibdir=%{tcl_archdir}/%{name}%{version} \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{tcl_archdir}

