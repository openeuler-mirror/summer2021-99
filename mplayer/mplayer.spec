%global debug_package %{nil}



Name:           mplayer
Version:        1.4
Release:        1 
Summary:        a test tool 

License:        GPL  
URL:            http://www.gnu.org/software/hello/ 
Source0:        MPlayer-1.4.tar.gz

BuildRequires:  gcc make patch gtk2-devel
Requires:       glibc

%description
The GNU Hello program produces a familiar, friendly greeting. 
Yes, this is another implementation of the classic program that prints “Hello, world!” when you run it.

%prep
%autosetup -n MPlayer-%{version}


%build
#直接%%configure有问题
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --confdir=%{_sysconfdir} \
    --libdir=%{_libdir} \
    --enable-gui  \
    --yasm='' 
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install 




%files
%license LICENSE
%doc README
%{_bindir}/*
%{_datarootdir}/*




%changelog   
* Fri Aug 20 2021 tongzong <2505108658@qq.com> - 1.4-1
- package init