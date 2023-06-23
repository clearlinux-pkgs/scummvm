#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scummvm
Version  : 2.7.0
Release  : 25
URL      : https://github.com/scummvm/scummvm/archive/v2.7.0/scummvm-2.7.0.tar.gz
Source0  : https://github.com/scummvm/scummvm/archive/v2.7.0/scummvm-2.7.0.tar.gz
Summary  : Allows you to run certain classic graphical point-and-click adventure games.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-3.0 GPL-3.0 ISC LGPL-2.1 MIT OFL-1.1 PostgreSQL Zlib
Requires: scummvm-bin = %{version}-%{release}
Requires: scummvm-data = %{version}-%{release}
Requires: scummvm-license = %{version}-%{release}
Requires: scummvm-man = %{version}-%{release}
BuildRequires : SDL-dev
BuildRequires : SDL_net-dev
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : curl-dev
BuildRequires : flac-dev
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libtheora-dev
BuildRequires : libvorbis-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Make-configure-errors-non-fatal.patch
Patch2: CVE-2014-5461.patch

%description
ScummVM is an interpreter that will play many graphic adventure games,
including LucasArts SCUMM games (such as Monkey Island 1-3, Day of the
Tentacle, Sam & Max, ...), many of Sierra's AGI and SCI games (such as King's
Quest 1-6, Space Quest 1-5, ...), Discworld 1 and 2, Simon the Sorcerer 1 and
2, Beneath A Steel Sky, Lure of the Temptress, Broken Sword 1 and 2, Flight of
the Amazon Queen, Gobliiins 1-3, The Legend of Kyrandia 1-3, many of Humongous
Entertainment's children's SCUMM games (including Freddi Fish and Putt Putt
games) and many more. See https://www.scummvm.org for a full compatibility list.

%package bin
Summary: bin components for the scummvm package.
Group: Binaries
Requires: scummvm-data = %{version}-%{release}
Requires: scummvm-license = %{version}-%{release}

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
%setup -q -n scummvm-2.7.0
cd %{_builddir}/scummvm-2.7.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676333875
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --datadir=/usr/share/scummvm \
--enable-release
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1676333875
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scummvm
cp %{_builddir}/scummvm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/scummvm/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.BSD %{buildroot}/usr/share/package-licenses/scummvm/da895920d4a7d4f0920fade3570969cf4d5fafd6 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.FREEFONT %{buildroot}/usr/share/package-licenses/scummvm/e58874a433eec4f975f35cb34379712d3b932f9e || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.GLAD %{buildroot}/usr/share/package-licenses/scummvm/179b231da21a2a00584e3fbe905eaa8aeb659176 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.ISC %{buildroot}/usr/share/package-licenses/scummvm/1ee6945db9b441059627e2e4a6fd39d0ac1c0d70 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.LGPL %{buildroot}/usr/share/package-licenses/scummvm/091c8f65dffdd24bf8c803d8b97c365d2981bdf5 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.MIT %{buildroot}/usr/share/package-licenses/scummvm/ed5455704a0e5e46657530521515574dab455cd4 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.OFL %{buildroot}/usr/share/package-licenses/scummvm/ea3155a0218b1c5cb952b1a18f2b601795ba8569 || :
cp %{_builddir}/scummvm-%{version}/LICENSES/COPYING.TINYGL %{buildroot}/usr/share/package-licenses/scummvm/579527fce9662f931f71819e0cc9df0d04a6330a || :
cp %{_builddir}/scummvm-%{version}/audio/soundfont/VGMTrans_LICENSE.txt %{buildroot}/usr/share/package-licenses/scummvm/14e89807e531a116c2d9d79e5284f195655713b2 || :
cp %{_builddir}/scummvm-%{version}/common/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/scummvm/52144cf874618949f7857eb5adb964bf3cd7938f || :
cp %{_builddir}/scummvm-%{version}/devtools/tasmrecover/dreamweb/LICENSE %{buildroot}/usr/share/package-licenses/scummvm/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/scummvm-%{version}/dists/debian/copyright %{buildroot}/usr/share/package-licenses/scummvm/c57e74e2f28fade261732ed7974b22b5b34fb80e || :
cp %{_builddir}/scummvm-%{version}/dists/snap/LICENSE %{buildroot}/usr/share/package-licenses/scummvm/25053a3b2190049c9d407b00c3a2ff001a7c066a || :
cp %{_builddir}/scummvm-%{version}/graphics/nanosvg/LICENSE.txt %{buildroot}/usr/share/package-licenses/scummvm/130fa43ba54e80bfa36404a32ba5e33e55d47d58 || :
cp %{_builddir}/scummvm-%{version}/graphics/tinygl/LICENSE %{buildroot}/usr/share/package-licenses/scummvm/65203578a020880c05562ee6e25851a1dc45071f || :
cp %{_builddir}/scummvm-%{version}/gui/themes/fonts/LICENSE.mplus %{buildroot}/usr/share/package-licenses/scummvm/a70b05899e79e96734d62e59093e646812eba2db || :
cp %{_builddir}/scummvm-%{version}/test/cxxtest/COPYING %{buildroot}/usr/share/package-licenses/scummvm/dd4547c72e04fd16fd675556993abb945491a69c || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/scummvm

%files data
%defattr(-,root,root,-)
/usr/share/applications/scummvm.desktop
/usr/share/icons/hicolor/scalable/apps/scummvm.svg
/usr/share/metainfo/scummvm.appdata.xml
/usr/share/pixmaps/scummvm.xpm
/usr/share/scummvm/access.dat
/usr/share/scummvm/achievements.dat
/usr/share/scummvm/cryomni3d.dat
/usr/share/scummvm/drascula.dat
/usr/share/scummvm/encoding.dat
/usr/share/scummvm/fonts.dat
/usr/share/scummvm/freescape.dat
/usr/share/scummvm/grim-patch.lab
/usr/share/scummvm/gui-icons.dat
/usr/share/scummvm/hadesch_translations.dat
/usr/share/scummvm/hugo.dat
/usr/share/scummvm/kyra.dat
/usr/share/scummvm/lure.dat
/usr/share/scummvm/macgui.dat
/usr/share/scummvm/mort.dat
/usr/share/scummvm/myst3.dat
/usr/share/scummvm/neverhood.dat
/usr/share/scummvm/pred.dic
/usr/share/scummvm/queen.tbl
/usr/share/scummvm/residualvm.zip
/usr/share/scummvm/scummclassic.zip
/usr/share/scummvm/scummmodern.zip
/usr/share/scummvm/scummremastered.zip
/usr/share/scummvm/shaders.dat
/usr/share/scummvm/shaders/emi_actor.fragment
/usr/share/scummvm/shaders/emi_actor.vertex
/usr/share/scummvm/shaders/emi_actorlights.fragment
/usr/share/scummvm/shaders/emi_actorlights.vertex
/usr/share/scummvm/shaders/emi_background.fragment
/usr/share/scummvm/shaders/emi_background.vertex
/usr/share/scummvm/shaders/emi_dimplane.fragment
/usr/share/scummvm/shaders/emi_dimplane.vertex
/usr/share/scummvm/shaders/emi_sprite.fragment
/usr/share/scummvm/shaders/emi_sprite.vertex
/usr/share/scummvm/shaders/grim_actor.fragment
/usr/share/scummvm/shaders/grim_actor.vertex
/usr/share/scummvm/shaders/grim_actorlights.fragment
/usr/share/scummvm/shaders/grim_actorlights.vertex
/usr/share/scummvm/shaders/grim_background.fragment
/usr/share/scummvm/shaders/grim_background.vertex
/usr/share/scummvm/shaders/grim_dim.fragment
/usr/share/scummvm/shaders/grim_dim.vertex
/usr/share/scummvm/shaders/grim_emerg.fragment
/usr/share/scummvm/shaders/grim_emerg.vertex
/usr/share/scummvm/shaders/grim_primitive.fragment
/usr/share/scummvm/shaders/grim_primitive.vertex
/usr/share/scummvm/shaders/grim_shadowplane.fragment
/usr/share/scummvm/shaders/grim_shadowplane.vertex
/usr/share/scummvm/shaders/grim_smush.fragment
/usr/share/scummvm/shaders/grim_smush.vertex
/usr/share/scummvm/shaders/grim_text.fragment
/usr/share/scummvm/shaders/grim_text.vertex
/usr/share/scummvm/shaders/myst3_box.fragment
/usr/share/scummvm/shaders/myst3_box.vertex
/usr/share/scummvm/shaders/myst3_cube.fragment
/usr/share/scummvm/shaders/myst3_cube.vertex
/usr/share/scummvm/shaders/myst3_text.fragment
/usr/share/scummvm/shaders/myst3_text.vertex
/usr/share/scummvm/shaders/stark_actor.fragment
/usr/share/scummvm/shaders/stark_actor.vertex
/usr/share/scummvm/shaders/stark_fade.fragment
/usr/share/scummvm/shaders/stark_fade.vertex
/usr/share/scummvm/shaders/stark_prop.fragment
/usr/share/scummvm/shaders/stark_prop.vertex
/usr/share/scummvm/shaders/stark_shadow.fragment
/usr/share/scummvm/shaders/stark_shadow.vertex
/usr/share/scummvm/shaders/stark_surface.fragment
/usr/share/scummvm/shaders/stark_surface.vertex
/usr/share/scummvm/shaders/wme_fade.fragment
/usr/share/scummvm/shaders/wme_fade.vertex
/usr/share/scummvm/shaders/wme_flat_shadow_mask.fragment
/usr/share/scummvm/shaders/wme_flat_shadow_mask.vertex
/usr/share/scummvm/shaders/wme_flat_shadow_modelx.fragment
/usr/share/scummvm/shaders/wme_flat_shadow_modelx.vertex
/usr/share/scummvm/shaders/wme_geometry.fragment
/usr/share/scummvm/shaders/wme_geometry.vertex
/usr/share/scummvm/shaders/wme_line.fragment
/usr/share/scummvm/shaders/wme_line.vertex
/usr/share/scummvm/shaders/wme_modelx.fragment
/usr/share/scummvm/shaders/wme_modelx.vertex
/usr/share/scummvm/shaders/wme_shadow_mask.fragment
/usr/share/scummvm/shaders/wme_shadow_mask.vertex
/usr/share/scummvm/shaders/wme_shadow_volume.fragment
/usr/share/scummvm/shaders/wme_shadow_volume.vertex
/usr/share/scummvm/shaders/wme_sprite.fragment
/usr/share/scummvm/shaders/wme_sprite.vertex
/usr/share/scummvm/sky.cpt
/usr/share/scummvm/supernova.dat
/usr/share/scummvm/teenagent.dat
/usr/share/scummvm/tony.dat
/usr/share/scummvm/toon.dat
/usr/share/scummvm/translations.dat
/usr/share/scummvm/ultima.dat
/usr/share/scummvm/wintermute.zip
/usr/share/scummvm/wwwroot.zip
/usr/share/scummvm/xeen.ccs

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/scummvm/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scummvm/091c8f65dffdd24bf8c803d8b97c365d2981bdf5
/usr/share/package-licenses/scummvm/130fa43ba54e80bfa36404a32ba5e33e55d47d58
/usr/share/package-licenses/scummvm/14e89807e531a116c2d9d79e5284f195655713b2
/usr/share/package-licenses/scummvm/179b231da21a2a00584e3fbe905eaa8aeb659176
/usr/share/package-licenses/scummvm/1ee6945db9b441059627e2e4a6fd39d0ac1c0d70
/usr/share/package-licenses/scummvm/25053a3b2190049c9d407b00c3a2ff001a7c066a
/usr/share/package-licenses/scummvm/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/scummvm/52144cf874618949f7857eb5adb964bf3cd7938f
/usr/share/package-licenses/scummvm/579527fce9662f931f71819e0cc9df0d04a6330a
/usr/share/package-licenses/scummvm/65203578a020880c05562ee6e25851a1dc45071f
/usr/share/package-licenses/scummvm/a70b05899e79e96734d62e59093e646812eba2db
/usr/share/package-licenses/scummvm/c57e74e2f28fade261732ed7974b22b5b34fb80e
/usr/share/package-licenses/scummvm/da895920d4a7d4f0920fade3570969cf4d5fafd6
/usr/share/package-licenses/scummvm/dd4547c72e04fd16fd675556993abb945491a69c
/usr/share/package-licenses/scummvm/e58874a433eec4f975f35cb34379712d3b932f9e
/usr/share/package-licenses/scummvm/ea3155a0218b1c5cb952b1a18f2b601795ba8569
/usr/share/package-licenses/scummvm/ed5455704a0e5e46657530521515574dab455cd4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/scummvm.6
