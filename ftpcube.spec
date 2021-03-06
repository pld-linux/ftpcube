Summary:	Multithreaded FTP client for X Window System
Summary(pl.UTF-8):	Wielowątkowy klient FTP dla systemu X Window
Name:		ftpcube
Version:	0.5.1
Release:	2
License:	Artistic for code, GPL v2 for icons
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/ftpcube/%{name}-%{version}.tar.gz
# Source0-md5:	3eb93ae44fa552ec50a24b7882198dd1
Source1:	%{name}.desktop
URL:		http://ftpcube.sourceforge.net/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-wxPython
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-libs
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FtpCube is a multi-platform, graphical FTP client written in Python,
using the wxPython graphical tookit. FtpCube's interface is based on
LeechFTP by Jan Debis but its codebase has been developed from scratch
and includes functionality that surpasses the original LeechFTP.

FtpCube aims to provide a high quality user interface, as well as a
rich feature set. The FtpCube project was born out of my search to
find a good, capable Unix FTP client that offered an intuitive and
sexy UI. Plus, I liked the idea of having an FTP client written in
Python. So, voila FtpCube.

%description -l pl.UTF-8
FtpCube to wieloplatformowy, graficzny klient FTP napisany w Pythonie,
używający biblioteki graficznej wxPython. Interfejs FtpCube jest
oparty na LeechFTP Jana Debisa, ale kod został stworzony od początku i
zawiera funkcjonalność przewyższającą oryginał.

FtpCube ma zapewnić wysokiej jakości interfejs użytkownika, a także
bogaty zbiór możliwości. Projekt FtpCube narodził się z poszukiwań
dobrego, uniksowego klienta FTP o dużych możliwościach, oferującego
intuicyjny i seksowny interfejs. Autorowi spodobała się idea klienta
FTP napisanego w Pythonie. Tak więc, voila FtpCube.

%prep
%setup -q

%build
# Extracting program icon from .py
%{__python} -c "import libftpcube.icons.ftpcube as icon; print icon.getData()" > %{name}.png
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
%py_install \
	--prefix=%{_prefix} \
	--install-scripts=%{_bindir} \
	--root=$RPM_BUILD_ROOT

cp -a %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG COPYING COPYING.ICONS
%attr(755,root,root) %{_bindir}/ftpcube
%{py_sitescriptdir}/libftpcube
%{py_sitescriptdir}/ftpcube-*.egg-info
%{_desktopdir}/ftpcube.desktop
%{_pixmapsdir}/ftpcube.png
