Name:		apvlv
Version:	0.7.0
Release:	1
Summary:	A PDF viewer which behaves like Vim
URL:		https://github.com/naihe2010/apvlv
Group:		Office
License:	GPLv2
Source0:	https://github.com/naihe2010/apvlv/archive/refs/tags/v%{version}-final/%{name}-%{version}-final.tar.gz
Source1:	%{name}.desktop

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	ebook-tools-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(quazip1-qt6)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Pdf)
BuildRequires:	cmake(Qt6PdfWidgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(libcmark)
BuildRequires:	man
BuildRequires:	ghostscript

%description
Apvlv is a PDF viewer which behaves like Vim.

%prep
%autosetup -n apvlv-0.7.0-final -p1
# lrelease writes the qm file before cmake creates this directory.
mkdir -p share/doc/apvlv/translations

%build
%cmake \
	-DAPVLV_WITH_UMD:BOOL=OFF \
	-DAPVLV_WITH_MUPDF:BOOL=OFF \
	-DAPVLV_WITH_OFFICE:BOOL=OFF \
	-DAPVLV_WITH_OCR:BOOL=OFF \
	-DDOCDIR=%{_datadir}/%{name}

%make

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_datadir}/applications/
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/
# The viewer loads SYSCONFDIR/apvlvrc, and ships the defaults as the example.
install -m0644 %{buildroot}%{_sysconfdir}/apvlvrc.example %{buildroot}%{_sysconfdir}/apvlvrc

%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/apvlvrc
%config(noreplace) %{_sysconfdir}/apvlvrc.example
%dir %{_datadir}/scripts
%{_datadir}/scripts/internal.js
%{_datadir}/doc/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/apvlv.1
