#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : clazy
Version  : 1.8
Release  : 48
URL      : file:///insilications/build/clearlinux/packages/clazy/clazy-v1.8.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/clazy/clazy-v1.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0+
Requires: clazy-bin = %{version}-%{release}
Requires: clazy-data = %{version}-%{release}
Requires: clazy-man = %{version}-%{release}
BuildRequires : Z3-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : llvm-dev
BuildRequires : mesa-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Designer)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Help)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Script)
BuildRequires : pkgconfig(Qt5Sensors)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This folder is for internal scripts which are only relevant if you're developing clazy itself.

%package bin
Summary: bin components for the clazy package.
Group: Binaries
Requires: clazy-data = %{version}-%{release}

%description bin
bin components for the clazy package.


%package data
Summary: data components for the clazy package.
Group: Data

%description data
data components for the clazy package.


%package dev
Summary: dev components for the clazy package.
Group: Development
Requires: clazy-bin = %{version}-%{release}
Requires: clazy-data = %{version}-%{release}
Provides: clazy-devel = %{version}-%{release}
Requires: clazy = %{version}-%{release}

%description dev
dev components for the clazy package.


%package doc
Summary: doc components for the clazy package.
Group: Documentation
Requires: clazy-man = %{version}-%{release}

%description doc
doc components for the clazy package.


%package man
Summary: man components for the clazy package.
Group: Default

%description man
man components for the clazy package.


%prep
%setup -q -n clazy
cd %{_builddir}/clazy

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607168155
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags1 end
##
%global _lto_cflags 1
##
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607168155
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/lib/qtcreator/libqbscore.prl
rm -f %{buildroot}/usr/lib/qtcreator/libqbsqtprofilesetup.prl

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clazy
/usr/bin/clazy-standalone

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/org.kde.clazy.metainfo.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/ClazyPlugin.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/clazy/*

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clazy.1
