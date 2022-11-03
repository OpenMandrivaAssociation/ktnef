%define major 5
%define libname %mklibname KF5Tnef %{major}
%define devname %mklibname KF5Tnef -d

Summary:	KTNEF - an API for handling TNEF data
Name:		ktnef
Version:	22.08.3
Release:	1
Epoch:      3
License:	GPLv2+
Group:		System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
URL:		https://www.kde.org/
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
Requires:	%{libname} >= %{version}

%description
KTNEF - an API for handling TNEF data.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	KTNEF - an API for handling TNEF data
Group:		System/Libraries
Obsoletes:	%{mklibname kf5tnef 4} < 3:17.04.0
Obsoletes:	%{mklibname kf5tnef 5} < 3:17.04.0
Provides:	%{mklibname kf5tnef 5} = 3:17.04.0
Requires:	%{name} >= %{version}

%description -n %{libname}
KTNEF - an API for handling TNEF data.

%files -n %{libname}
%{_libdir}/libKF5Tnef.so.%{major}*

#--------------------------------------------------------------------

%package -n %{devname}

Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname kf5tnef -d} < 3:17.04.0
Provides:	%{mklibname kf5tnef -d} = 3:17.04.0

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KF5/KTNEF
%{_libdir}/*.so
%{_libdir}/cmake/KF5Tnef
%{_libdir}/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libktnef5

%files -f libktnef5.lang
%{_datadir}/qlogging-categories5/ktnef.categories
%{_datadir}/qlogging-categories5/ktnef.renamecategories
