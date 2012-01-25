Name:		apvlv
Version:	0.1.2
Release:	1
Summary:	A PDF viewer which behaves like Vim
URL:		http://naihe2010.github.com/apvlv/
Group:		Office
License:	GPLv2
Source0:	https://github.com/downloads/naihe2010/apvlv/%{name}-%{version}-Source.tar.gz
Source1:	%{name}.desktop
Patch0:		apvlv-poppler015.patch
# fedora patch but rediff'd for 0.1.2
Patch1:		apvlv-poppler017.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(poppler-glib)

%description
Apvlv is a PDF viewer which behaves like Vim.

%prep
%setup -qn %{name}-%{version}-Source
%apply_patches

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
%doc %{_datadir}/%{name}/Startup.pdf
%doc %{_datadir}/%{name}/Startup.tex
%doc %{_datadir}/%{name}/apvlvrc.example
%{_datadir}/%{name}/icons/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

