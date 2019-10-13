#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kconfigwidgets
Version  : 5.63.0
Release  : 26
URL      : https://download.kde.org/stable/frameworks/5.63/kconfigwidgets-5.63.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.63/kconfigwidgets-5.63.0.tar.xz
Source1 : https://download.kde.org/stable/frameworks/5.63/kconfigwidgets-5.63.0.tar.xz.sig
Summary  : Widgets for KConfig
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kconfigwidgets-data = %{version}-%{release}
Requires: kconfigwidgets-lib = %{version}-%{release}
Requires: kconfigwidgets-license = %{version}-%{release}
Requires: kconfigwidgets-locales = %{version}-%{release}
Requires: kconfigwidgets-man = %{version}-%{release}
BuildRequires : appstream-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-xml
BuildRequires : kauth
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : qtbase-dev mesa-dev

%description
# KConfigWidgets
Widgets for configuration dialogs
## Introduction
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package data
Summary: data components for the kconfigwidgets package.
Group: Data

%description data
data components for the kconfigwidgets package.


%package dev
Summary: dev components for the kconfigwidgets package.
Group: Development
Requires: kconfigwidgets-lib = %{version}-%{release}
Requires: kconfigwidgets-data = %{version}-%{release}
Provides: kconfigwidgets-devel = %{version}-%{release}
Requires: kconfigwidgets = %{version}-%{release}
Requires: kconfigwidgets = %{version}-%{release}

%description dev
dev components for the kconfigwidgets package.


%package extras
Summary: extras components for the kconfigwidgets package.
Group: Default

%description extras
extras components for the kconfigwidgets package.


%package lib
Summary: lib components for the kconfigwidgets package.
Group: Libraries
Requires: kconfigwidgets-data = %{version}-%{release}
Requires: kconfigwidgets-license = %{version}-%{release}

%description lib
lib components for the kconfigwidgets package.


%package license
Summary: license components for the kconfigwidgets package.
Group: Default

%description license
license components for the kconfigwidgets package.


%package locales
Summary: locales components for the kconfigwidgets package.
Group: Default

%description locales
locales components for the kconfigwidgets package.


%package man
Summary: man components for the kconfigwidgets package.
Group: Default

%description man
man components for the kconfigwidgets package.


%prep
%setup -q -n kconfigwidgets-5.63.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570928917
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570928917
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kconfigwidgets
cp COPYING %{buildroot}/usr/share/package-licenses/kconfigwidgets/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kconfigwidgets/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kconfigwidgets5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/kf5_entry.desktop
/usr/share/locale/ar/kf5_entry.desktop
/usr/share/locale/as/kf5_entry.desktop
/usr/share/locale/be/kf5_entry.desktop
/usr/share/locale/be@latin/kf5_entry.desktop
/usr/share/locale/bg/kf5_entry.desktop
/usr/share/locale/bn/kf5_entry.desktop
/usr/share/locale/bn_IN/kf5_entry.desktop
/usr/share/locale/br/kf5_entry.desktop
/usr/share/locale/bs/kf5_entry.desktop
/usr/share/locale/ca/kf5_entry.desktop
/usr/share/locale/ca@valencia/kf5_entry.desktop
/usr/share/locale/crh/kf5_entry.desktop
/usr/share/locale/cs/kf5_entry.desktop
/usr/share/locale/csb/kf5_entry.desktop
/usr/share/locale/cy/kf5_entry.desktop
/usr/share/locale/da/kf5_entry.desktop
/usr/share/locale/de/kf5_entry.desktop
/usr/share/locale/el/kf5_entry.desktop
/usr/share/locale/en_GB/kf5_entry.desktop
/usr/share/locale/en_US/kf5_entry.desktop
/usr/share/locale/eo/kf5_entry.desktop
/usr/share/locale/es/kf5_entry.desktop
/usr/share/locale/et/kf5_entry.desktop
/usr/share/locale/eu/kf5_entry.desktop
/usr/share/locale/fa/kf5_entry.desktop
/usr/share/locale/fi/kf5_entry.desktop
/usr/share/locale/fr/kf5_entry.desktop
/usr/share/locale/fy/kf5_entry.desktop
/usr/share/locale/ga/kf5_entry.desktop
/usr/share/locale/gl/kf5_entry.desktop
/usr/share/locale/gu/kf5_entry.desktop
/usr/share/locale/ha/kf5_entry.desktop
/usr/share/locale/he/kf5_entry.desktop
/usr/share/locale/hi/kf5_entry.desktop
/usr/share/locale/hne/kf5_entry.desktop
/usr/share/locale/hr/kf5_entry.desktop
/usr/share/locale/hsb/kf5_entry.desktop
/usr/share/locale/hu/kf5_entry.desktop
/usr/share/locale/hy/kf5_entry.desktop
/usr/share/locale/ia/kf5_entry.desktop
/usr/share/locale/id/kf5_entry.desktop
/usr/share/locale/is/kf5_entry.desktop
/usr/share/locale/it/kf5_entry.desktop
/usr/share/locale/ja/kf5_entry.desktop
/usr/share/locale/ka/kf5_entry.desktop
/usr/share/locale/kk/kf5_entry.desktop
/usr/share/locale/km/kf5_entry.desktop
/usr/share/locale/kn/kf5_entry.desktop
/usr/share/locale/ko/kf5_entry.desktop
/usr/share/locale/ku/kf5_entry.desktop
/usr/share/locale/lb/kf5_entry.desktop
/usr/share/locale/lt/kf5_entry.desktop
/usr/share/locale/lv/kf5_entry.desktop
/usr/share/locale/mai/kf5_entry.desktop
/usr/share/locale/mk/kf5_entry.desktop
/usr/share/locale/ml/kf5_entry.desktop
/usr/share/locale/mr/kf5_entry.desktop
/usr/share/locale/ms/kf5_entry.desktop
/usr/share/locale/nb/kf5_entry.desktop
/usr/share/locale/nds/kf5_entry.desktop
/usr/share/locale/ne/kf5_entry.desktop
/usr/share/locale/nl/kf5_entry.desktop
/usr/share/locale/nn/kf5_entry.desktop
/usr/share/locale/or/kf5_entry.desktop
/usr/share/locale/pa/kf5_entry.desktop
/usr/share/locale/pl/kf5_entry.desktop
/usr/share/locale/ps/kf5_entry.desktop
/usr/share/locale/pt/kf5_entry.desktop
/usr/share/locale/pt_BR/kf5_entry.desktop
/usr/share/locale/ro/kf5_entry.desktop
/usr/share/locale/ru/kf5_entry.desktop
/usr/share/locale/se/kf5_entry.desktop
/usr/share/locale/si/kf5_entry.desktop
/usr/share/locale/sk/kf5_entry.desktop
/usr/share/locale/sl/kf5_entry.desktop
/usr/share/locale/sq/kf5_entry.desktop
/usr/share/locale/sr/kf5_entry.desktop
/usr/share/locale/sr@ijekavian/kf5_entry.desktop
/usr/share/locale/sr@ijekavianlatin/kf5_entry.desktop
/usr/share/locale/sr@latin/kf5_entry.desktop
/usr/share/locale/sv/kf5_entry.desktop
/usr/share/locale/ta/kf5_entry.desktop
/usr/share/locale/te/kf5_entry.desktop
/usr/share/locale/tg/kf5_entry.desktop
/usr/share/locale/th/kf5_entry.desktop
/usr/share/locale/tr/kf5_entry.desktop
/usr/share/locale/tt/kf5_entry.desktop
/usr/share/locale/ug/kf5_entry.desktop
/usr/share/locale/uk/kf5_entry.desktop
/usr/share/locale/uz/kf5_entry.desktop
/usr/share/locale/uz@cyrillic/kf5_entry.desktop
/usr/share/locale/vi/kf5_entry.desktop
/usr/share/locale/wa/kf5_entry.desktop
/usr/share/locale/xh/kf5_entry.desktop
/usr/share/locale/zh_CN/kf5_entry.desktop
/usr/share/locale/zh_HK/kf5_entry.desktop
/usr/share/locale/zh_TW/kf5_entry.desktop
/usr/share/qlogging-categories5/kconfigwidgets.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KConfigWidgets/KCModule
/usr/include/KF5/KConfigWidgets/KCodecAction
/usr/include/KF5/KConfigWidgets/KColorScheme
/usr/include/KF5/KConfigWidgets/KColorSchemeManager
/usr/include/KF5/KConfigWidgets/KConfigDialog
/usr/include/KF5/KConfigWidgets/KConfigDialogManager
/usr/include/KF5/KConfigWidgets/KConfigViewStateSaver
/usr/include/KF5/KConfigWidgets/KHelpClient
/usr/include/KF5/KConfigWidgets/KLanguageButton
/usr/include/KF5/KConfigWidgets/KLanguageName
/usr/include/KF5/KConfigWidgets/KPasteTextAction
/usr/include/KF5/KConfigWidgets/KRecentFilesAction
/usr/include/KF5/KConfigWidgets/KStandardAction
/usr/include/KF5/KConfigWidgets/KTipDialog
/usr/include/KF5/KConfigWidgets/KViewStateMaintainer
/usr/include/KF5/KConfigWidgets/kcmodule.h
/usr/include/KF5/KConfigWidgets/kcodecaction.h
/usr/include/KF5/KConfigWidgets/kcolorscheme.h
/usr/include/KF5/KConfigWidgets/kcolorschememanager.h
/usr/include/KF5/KConfigWidgets/kconfigdialog.h
/usr/include/KF5/KConfigWidgets/kconfigdialogmanager.h
/usr/include/KF5/KConfigWidgets/kconfigviewstatesaver.h
/usr/include/KF5/KConfigWidgets/kconfigwidgets_export.h
/usr/include/KF5/KConfigWidgets/khelpclient.h
/usr/include/KF5/KConfigWidgets/klanguagebutton.h
/usr/include/KF5/KConfigWidgets/klanguagename.h
/usr/include/KF5/KConfigWidgets/kpastetextaction.h
/usr/include/KF5/KConfigWidgets/krecentfilesaction.h
/usr/include/KF5/KConfigWidgets/kstandardaction.h
/usr/include/KF5/KConfigWidgets/ktip.h
/usr/include/KF5/KConfigWidgets/ktipdialog.h
/usr/include/KF5/KConfigWidgets/kviewstatemaintainer.h
/usr/include/KF5/kconfigwidgets_version.h
/usr/lib64/cmake/KF5ConfigWidgets/KF5ConfigWidgetsConfig.cmake
/usr/lib64/cmake/KF5ConfigWidgets/KF5ConfigWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF5ConfigWidgets/KF5ConfigWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ConfigWidgets/KF5ConfigWidgetsTargets.cmake
/usr/lib64/libKF5ConfigWidgets.so
/usr/lib64/qt5/mkspecs/modules/qt_KConfigWidgets.pri

%files extras
%defattr(-,root,root,-)
/usr/bin/preparetips5

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5ConfigWidgets.so.5
/usr/lib64/libKF5ConfigWidgets.so.5.63.0
/usr/lib64/qt5/plugins/designer/kconfigwidgets5widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kconfigwidgets/COPYING
/usr/share/package-licenses/kconfigwidgets/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/preparetips5.1
/usr/share/man/de/man1/preparetips5.1
/usr/share/man/es/man1/preparetips5.1
/usr/share/man/it/man1/preparetips5.1
/usr/share/man/man1/preparetips5.1
/usr/share/man/nl/man1/preparetips5.1
/usr/share/man/pt/man1/preparetips5.1
/usr/share/man/pt_BR/man1/preparetips5.1
/usr/share/man/ru/man1/preparetips5.1
/usr/share/man/sv/man1/preparetips5.1
/usr/share/man/uk/man1/preparetips5.1

%files locales -f kconfigwidgets5.lang
%defattr(-,root,root,-)

