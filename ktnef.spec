#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        KTNEF - an API for handling TNEF data
Name:           ktnef
Version: 15.08.0
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/


BuildRequires:  kf5-macros

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)

BuildRequires:  kf5-macros
BuildRequires:  kdelibs4support-devel >= 5.12.0
BuildRequires:  kcalcore-devel >= 4.79.0
BuildRequires:  kcalutils-devel >= 4.79.0
BuildRequires:  kcontacts-devel >= 4.91.0

BuildRequires:  boost-devel

BuildRequires:  pkgconfig(libsasl2)

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
KTNEF - an API for handling TNEF data

#--------------------------------------------------------------------

%define ktnef_major 4
%define libktnef %mklibname kf5tnef %{ktnef_major}

%package -n %libktnef
Summary:      KTNEF - an API for handling TNEF data
Group:        System/Libraries


%description -n %libktnef
KTNEF - an API for handling TNEF data

%files -n %libktnef
%_kf5_libdir/libKF5Tnef.so.%{ktnef_major}*
%_kf5_libdir/libKF5Tnef.so.5

#--------------------------------------------------------------------

%define ktnef_devel %mklibname kf5tnef -d

%package -n %ktnef_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libktnef = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %ktnef_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %ktnef_devel
%_kf5_includedir/KTNEF
%_kf5_includedir/*.h
%_kf5_libdir/*.so
%_kf5_libdir/cmake/KF5Tnef
%_qt5_prefix/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build

%find_lang --all %{name}5



%changelog
* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865972
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863725
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 861785
- New version 15.07.90

* Wed Jul 29 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 858839
- imported package ktnef

