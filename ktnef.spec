Summary:        KTNEF - an API for handling TNEF data
Name:           ktnef
Version:	17.04.0
Release:	2
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

%define ktnef_major 5
%define libktnef %mklibname KF5Tnef %{ktnef_major}

Requires: %{libktnef} = %{EVRD}

%description
KTNEF - an API for handling TNEF data.

#--------------------------------------------------------------------

%package -n %{libktnef}
Summary:      KTNEF - an API for handling TNEF data
Group:        System/Libraries
Obsoletes:    %mklibname kf5tnef 4
Obsoletes:    %mklibname kf5tnef 5
Requires:     %{name} = %{EVRD}

%description -n %{libktnef}
KTNEF - an API for handling TNEF data

%files -n %{libktnef}
%{_libdir}/libKF5Tnef.so.%{ktnef_major}*

#--------------------------------------------------------------------

%define ktnef_devel %mklibname KF5Tnef -d

%package -n %ktnef_devel

Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{libktnef} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
Obsoletes:	%mklibname kf5tnef -d

%description -n %{ktnef_devel}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{ktnef_devel}
%{_includedir}/KF5/KTNEF
%{_includedir}/KF5/*.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5Tnef
%{_libdir}/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libktnef5

%files -f libktnef5.lang
