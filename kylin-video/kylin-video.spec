%global debug_package %{nil}

Name:           kylin-video
Version:        2.1.1.1
Release:        1
Summary:        A powerful video player

License:        LGPL-2.0-only and LGPL-2.1-only and GPL-2.0-only and LGPL-2.0-or-later and GPL-2.0-or-later and BSD and LGPL-3.0-only and GPL-3.0-only
URL:            https://www.ubuntukylin.com/applications/26-cn.html
Source0:        https://github.com/UbuntuKylin/kylin-video/kylin-video-2.1.1.1.tar.gz
Patch1:         fix-lrelease.patch

BuildRequires:  qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(xext)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme



%{?kf5_kinit_requires}

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Kylin Video utilizes MPV and MPlayer as background play engine (use MPV by default). Its GUI front end is written by Qt5. Plus, it supports both x86 and ARM platform. As a powerful video player, Kylin Video supports most of the audio and video formats. Functions of shortcut keys/ preview/ screenshot/ sound settings/ subtitles and so on are provided. Users can even customize settings as they like.



%prep
%autosetup -p1


%build
%{qmake_qt5}
%make_build


%install
cd %{_builddir}/%{name}-%{version}
%make_install  PREFIX=%{_prefix} INSTALL_ROOT=%{buildroot} 


%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datarootdir}/*



%changelog   
* Fri Aug 20 2021 tongzong <2505108658@qq.com> - 2.1.1.1-1   
- package init

