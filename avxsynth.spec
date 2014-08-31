Summary:	Linux Port of Avisynth
Name:		avxsynth
Version:	4.0
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	https://github.com/avxsynth/avxsynth/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	9df808e436aad27a14af29af9ea03c8f
URL:		http://www.avxsynth.org/
BuildRequires:	QtCore-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	ffms2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	log4cpp-devel
#BuildRequires:	mplayer
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	yasm
Obsoletes:	avisynth < 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AvxSynth is a Linux port of the AviSynth toolkit. The objective of the
porting effort was to bring the power of AviSynth into the Linux
world. In particular, we are interested in AviSynth as a frame server
front-end to the encode step of our media pipeline.

%package devel
Summary:	Development Headers for Avxsynth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
AvxSynth is a Linux port of the AviSynth toolkit. The objective of the
porting effort was to bring the power of AviSynth into the Linux
world. In particular, we are interested in AviSynth as a frame server
front-end to the encode step of our media pipeline.

This package provides development headers for avxsynth.

%prep
%setup -qc
mv %{name}-*/* .

%build
autoreconf -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Fix Documentation
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# Clear .la files
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md debian/changelog debian/copyright plugins/autocrop/AutoCrop.txt
%attr(755,root,root) %{_bindir}/avxFrameServer
%attr(755,root,root) %{_libdir}/libavxsynth.so.*.*.*
%ghost %{_libdir}/libavxsynth.so.0
%attr(755,root,root) %{_libdir}/libavxutils.so.*.*.*
%ghost %{_libdir}/libavxutils.so.0
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libautocrop.so
%attr(755,root,root) %{_libdir}/%{name}/libavxffms2.so
%attr(755,root,root) %{_libdir}/%{name}/libavxframecapture.so
%attr(755,root,root) %{_libdir}/%{name}/libavxsubtitle.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/libavxsynth.so
%{_libdir}/libavxutils.so
%{_pkgconfigdir}/%{name}.pc
%{_pkgconfigdir}/avxutils.pc
