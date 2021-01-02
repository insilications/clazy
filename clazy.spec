#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : clazy
Version  : 1.8
Release  : 69
URL      : file:///insilications/build/clearlinux/packages/clazy/clazy-v1.8.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/clazy/clazy-v1.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0+
Requires: clazy-bin = %{version}-%{release}
Requires: clazy-data = %{version}-%{release}
Requires: clazy-man = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : binutils-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : gcc-dev
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : llvm11
BuildRequires : llvm11-bin
BuildRequires : llvm11-data
BuildRequires : llvm11-dev
BuildRequires : llvm11-lib
BuildRequires : llvm11-libexec
BuildRequires : llvm11-staticdev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libedit)
BuildRequires : pkgconfig(libffi)
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : valgrind-dev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Clazy-STATIC-build.patch
Patch2: 0002-Fix1.patch
Patch3: 0003-New2.patch

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


%package staticdev
Summary: staticdev components for the clazy package.
Group: Default
Requires: clazy-dev = %{version}-%{release}

%description staticdev
staticdev components for the clazy package.


%prep
%setup -q -n clazy
cd %{_builddir}/clazy
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609573677
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-O3 -march=native -mtune=native -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -falign-functions=32 -flimit-function-alignment -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -Wno-error -pipe -ffat-lto-objects -fPIC -pthread -static-libstdc++ -static-libgcc -std=c17"
#  -Wl,--as-needed  -Wl,--hash-style=gnu  -Wl,-z,now -Wl,-z,relro  -fasynchronous-unwind-tables -fdevirtualize-at-ltrans  -fno-semantic-interposition  -fipa-pta -flto=16  -fgraphite-identity
export CXXFLAGS="-O3 -march=native -mtune=native -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -falign-functions=32 -flimit-function-alignment -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -Wno-error -pipe -ffat-lto-objects -fPIC -pthread -static-libstdc++ -static-libgcc -std=c++17"
#  -fvisibility-inlines-hidden  -Wl,-sort-common
export LDFLAGS="-O3 -march=native -mtune=native -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -falign-functions=32 -flimit-function-alignment -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -Wno-error -pipe -ffat-lto-objects -fPIC -pthread -static-libstdc++ -static-libgcc"
#
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export MAKEFLAGS="-j16"
export DEBUG_FIX_IT_EXPORTER=1
## altflags1 end
%cmake .. -DCMAKE_BUILD_TYPE=Release \
-DLINK_CLAZY_TO_LLVM:BOOL=OFF \
-DCLANG_CLANG-CPP_LIB:BOOL=OFF \
-DCLAZY_LINK_CLANG_DYLIB:BOOL=OFF \
-DDEBUG_FIX_IT_EXPORTER:BOOL=ON
make  %{?_smp_mflags}  V=1 VERBOSE=1
## ccache stats
ccache -s
## ccache stats
popd

%install
export SOURCE_DATE_EPOCH=1609573677
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

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/clazy/*

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clazy.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/ClazyPlugin.a
