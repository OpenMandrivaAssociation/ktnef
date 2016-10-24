Summary:        KTNEF - an API for handling TNEF data
Name:           ktnef
Version:	16.08.2
Release:	1
License:        GPLv2+
Group:          System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
URL:            https://www.kde.org/


BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5KDELibs4Support)

BuildRequires:  boost-devel

BuildRequires:  sasl-devel

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
KTNEF - an API for handling TNEF data

#--------------------------------------------------------------------

%define ktnef_major 5
%define libktnef %mklibname kf5tnef %{ktnef_major}

%package -n %libktnef
Summary:      KTNEF - an API for handling TNEF data
Group:        System/Libraries
Obsoletes:    %mklibname kf5tnef 4


%description -n %libktnef
KTNEF - an API for handling TNEF data

%files -n %libktnef
%_libdir/libKF5Tnef.so.%{ktnef_major}*

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
%_includedir/KF5/KTNEF
%_includedir/KF5/*.h
%_libdir/*.so
%_libdir/cmake/KF5Tnef
%_libdir/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
