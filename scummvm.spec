#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scummvm
Version  : 2.0.0
Release  : 1
URL      : https://github.com/scummvm/scummvm/archive/v2.0.0.tar.gz
Source0  : https://github.com/scummvm/scummvm/archive/v2.0.0.tar.gz
Summary  : CxxTest Testing Framework for C++
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: scummvm-bin = %{version}-%{release}
Requires: scummvm-data = %{version}-%{release}
Requires: scummvm-license = %{version}-%{release}
Requires: scummvm-man = %{version}-%{release}
BuildRequires : SDL-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(x11)

%description
CxxTest is a JUnit/CppUnit/xUnit-like framework for C++.
Its advantages over existing alternatives are that it:
 - Doesn't require RTTI
 - Doesn't require member template functions
 - Doesn't require exception handling
 - Doesn't require any external libraries (including memory management, 
   file/console I/O, graphics libraries)

%package bin
Summary: bin components for the scummvm package.
Group: Binaries
Requires: scummvm-data = %{version}-%{release}
Requires: scummvm-license = %{version}-%{release}
Requires: scummvm-man = %{version}-%{release}

%description bin
bin components for the scummvm package.


%package data
Summary: data components for the scummvm package.
Group: Data

%description data
data components for the scummvm package.


%package doc
Summary: doc components for the scummvm package.
Group: Documentation
Requires: scummvm-man = %{version}-%{release}

%description doc
doc components for the scummvm package.


%package license
Summary: license components for the scummvm package.
Group: Default

%description license
license components for the scummvm package.


%package man
Summary: man components for the scummvm package.
Group: Default

%description man
man components for the scummvm package.


%prep
%setup -q -n scummvm-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548801464
%configure --disable-static || ./configure --host=x86_64-generic-linux-gnu --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --datadir=/usr/share --libdir=/usr/lib64 --mandir=/usr/share/man
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1548801464
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scummvm
cp COPYING %{buildroot}/usr/share/package-licenses/scummvm/COPYING
cp devtools/tasmrecover/dreamweb/LICENSE %{buildroot}/usr/share/package-licenses/scummvm/devtools_tasmrecover_dreamweb_LICENSE
cp engines/sword25/util/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/scummvm/engines_sword25_util_lua_COPYRIGHT
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scummvm

%files data
%defattr(-,root,root,-)
/usr/share/access.dat
/usr/share/appdata/scummvm.appdata.xml
/usr/share/applications/scummvm.desktop
/usr/share/drascula.dat
/usr/share/hugo.dat
/usr/share/icons/hicolor/scalable/apps/scummvm.svg
/usr/share/kyra.dat
/usr/share/lure.dat
/usr/share/mort.dat
/usr/share/neverhood.dat
/usr/share/pixmaps/scummvm.xpm
/usr/share/pred.dic
/usr/share/queen.tbl
/usr/share/scummclassic.zip
/usr/share/scummmodern.zip
/usr/share/sky.cpt
/usr/share/teenagent.dat
/usr/share/tony.dat
/usr/share/toon.dat
/usr/share/translations.dat

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/scummvm/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scummvm/COPYING
/usr/share/package-licenses/scummvm/devtools_tasmrecover_dreamweb_LICENSE
/usr/share/package-licenses/scummvm/engines_sword25_util_lua_COPYRIGHT

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/scummvm.6
