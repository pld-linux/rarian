Summary:	Rarian is a documentation meta-data library
Name:		rarian
Version:	0.5.8
Release:	1
License:	LGPL v2+
Group:		Base
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rarian/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	9afee4d25a10bd5310ee21e23a09d659
Patch0:		%{name}-scrollkeeper.patch
URL:		http://rarian.freedesktop.org/
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

%package compat
Summary:	Extra files for compatibility with scrollkeeper
License:	GPL v2+
Group:		Base
Requires:	%{name} = %{version}-%{release}
Provides:	scrollkeeper
Obsoletes:	scrollkeeper <= 0.3.14

%description compat
This package contains files needed to maintain backward-compatibility
with scrollkeeper.

%package devel
Summary:	Development files for Rarian
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains files required to develop applications that use
the Rarian library ("librarian").

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-omf-read \
	--disable-skdb-update

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/omf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/librarian.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%post compat
%{_bindir}/rarian-sk-update

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING COPYING.LIB COPYING.UTILS ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/rarian-example
%attr(755,root,root) %{_libdir}/librarian.so.*.*
%{_datadir}/librarian
%{_datadir}/help

%files compat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rarian-sk-*
%attr(755,root,root) %{_bindir}/scrollkeeper-*
%dir %{_datadir}/omf

%files devel
%defattr(644,root,root,755)
%{_includedir}/rarian
%{_libdir}/librarian.so
%{_libdir}/librarian.la
%{_pkgconfigdir}/rarian.pc
