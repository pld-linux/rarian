Summary:	Rarian - a documentation meta-data library
Summary(pl.UTF-8):	Rarian - biblioteka metadanych dokumentacji
Name:		rarian
Version:	0.8.1
Release:	5
License:	LGPL v2.1+ (library), GPL v2+ (utilities)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rarian/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	75091185e13da67a0ff4279de1757b94
Patch0:		%{name}-am.patch
URL:		http://rarian.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
Requires:	coreutils
Requires:	gawk
Requires:	libxslt
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rarian is a documentation meta-data library that allows access to
documents, man pages and info pages. It was designed as a replacement
for scrollkeeper.

%description -l pl.UTF-8
Rarian to biblioteka metadanych dokumentacji pozwalająca na dostęp do
dokumentów oraz stron manuala i info. Została zaprojektowana jako
zamiennik scrollkeepera.

%package compat
Summary:	Extra files for compatibility with scrollkeeper
Summary(pl.UTF-8):	Dodatkowe pliki dla kompatybilności ze scrollkeeperem
License:	GPL v2+
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
Provides:	scrollkeeper
Obsoletes:	scrollkeeper <= 1:0.3.14

%description compat
This package contains files needed to maintain backward-compatibility
with scrollkeeper.

%description compat -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do zachowania wstecznej zgodności
ze scrollkeeperem.

%package devel
Summary:	Development files for Rarian
Summary(pl.UTF-8):	Pliki programistyczne Rariana
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains files required to develop applications that use
the Rarian library ("librarian").

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do tworzenia aplikacji
wykorzystujących bibliotekę Rarian (librarian).

%package static
Summary:	Static Rarian library
Summary(pl.UTF-8):	Statyczna biblioteka Rarian
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Rarian library (librarian).

%description static -l pl.UTF-8
Statyczna biblioteka Rarian (librarian).

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-omf-read \
	--disable-skdb-update

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/omf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsolted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librarian.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post compat
%{_bindir}/rarian-sk-update

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/rarian-example
%attr(755,root,root) %{_libdir}/librarian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librarian.so.0
%{_datadir}/librarian
%{_datadir}/help/rarian.document

%files compat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rarian-sk-*
%attr(755,root,root) %{_bindir}/scrollkeeper-*
%dir %{_datadir}/omf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librarian.so
%{_includedir}/rarian
%{_pkgconfigdir}/rarian.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librarian.a
