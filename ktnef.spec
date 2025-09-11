#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6Tnef
%define devname %mklibname KPim6Tnef -d

Summary:	KTNEF - an API for handling TNEF data
Name:		ktnef
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/ktnef/-/archive/%{gitbranch}/ktnef-%{gitbranchd}.tar.bz2#/ktnef-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/ktnef-%{version}.tar.xz
%endif
URL:		https://www.kde.org/
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
BuildRequires:	qt6-qttools-assistant
Requires:	%{libname} >= %{version}
# Renamed 2025-05-25 after 6.0
%rename plasma6-ktnef
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KTNEF - an API for handling TNEF data.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	KTNEF - an API for handling TNEF data
Group:		System/Libraries
Requires:	%{name} >= %{version}
# Not a 1:1 replacement, but we need to get rid of old cruft...
Obsoletes:	%{mklibname KF5Tnef 5}
Obsoletes:	%{mklibname KPim5Tnef}

%description -n %{libname}
KTNEF - an API for handling TNEF data.

%files -n %{libname}
%{_libdir}/libKPim6Tnef.so*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft...
Obsoletes:	%{mklibname -d KPim5Tnef}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KPim6/KTNEF
%{_libdir}/cmake/KPim6Tnef

#--------------------------------------------------------------------

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/ktnef.categories
%{_datadir}/qlogging-categories6/ktnef.renamecategories
