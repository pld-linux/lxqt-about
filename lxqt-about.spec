#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	About application for LXQt desktop suite
Summary(pl.UTF-8):	Informacje o środowisku graficznym LXQt
Name:		lxqt-about
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-about/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e6046469ea8838b65b5622d52bb280c1
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 3.18.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
About application for LXQt desktop suite.

%description -l pl.UTF-8
Aplikacja wyświetlająca informacje o środowisku graficznym LXQt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-about
%{_desktopdir}/lxqt-about.desktop
%{_iconsdir}/hicolor/scalable/apps/lxqt-about.svg
# required for the lang files
%%dir %{_datadir}/lxqt/translations/%{name}
