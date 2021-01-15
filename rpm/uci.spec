Name:			uci
Summary:		UCI
Version:		0.0.1
Release:		1%{?dist}
License:		CPL
Group:			DX
URL:			https://github.com/soft-way/uci
Source:			https://github.com/soft-way/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:		autoconf automake


%description
UCI

%prep
%setup -q -n %{name}-%{version}

%build
cmake3 CMakeLists.txt -DBUILD_LUA=OFF

%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%preun

%post

%pre

%postun

%files
%dir %attr(755, root, root)
%{_libdir}/*.*
%{_bindir}/*

%changelog
* Fri Jan 15 2021 Samuel Chen
- initial file created

