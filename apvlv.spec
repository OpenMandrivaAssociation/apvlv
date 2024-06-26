Name:		apvlv
Version:	0.5.0
Release:	1
Summary:	A PDF viewer which behaves like Vim
URL:		https://github.com/naihe2010/apvlv
Group:		Office
License:	GPLv2
Source0:	https://github.com/naihe2010/apvlv/archive/refs/tags/v%{version}-final/%{name}-%{version}-final.tar.gz
Source1:	%{name}.desktop

BuildRequires:	cmake
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	ebook-tools-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	man
BuildRequires:	ghostscript

%description
Apvlv is a PDF viewer which behaves like Vim.

%prep
%autosetup -n %{name}-%{version}-final -p1

%build
%cmake \
	-DAPVLV_WITH_UMD:BOOL=OFF \
	-DDOCDIR=%{_datadir}/%{name}

%make

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_datadir}/applications/
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

%files 
%{_bindir}/%{name}
%{_sysconfdir}/%{name}rc
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/apvlv.1
