Summary:	Multithreaded FTP client for X Window System
Summary(pl):	Wielow±tkowy klient FTP dla systemu X Window
Name:		ftpcube
Version:	0.4.3
Release:	4
License:	Artistic for code, GPL v2 for icons
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/ftpcube/%{name}-%{version}.tar.gz
# Source0-md5:	574d207377a24caf6315866d52326672
Source1:	%{name}.desktop
URL:		http://ftpcube.sourceforge.net/
BuildRequires:	python
%pyrequires_eq	python-libs
Requires:	python-wxPython
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FtpCube is a multi-platform, graphical FTP client written in Python,
using the wxPython graphical tookit. FtpCube's interface is based on
LeechFTP by Jan Debis but its codebase has been developed from scratch
and includes functionality that surpasses the original LeechFTP.

FtpCube aims to provide a high quality user interface, as well as a
rich feature set. The FtpCube project was born out of my search to
find a good, capable unix FTP client that offered an intuitive and
sexy UI. Plus, I liked the idea of having an FTP client written in
Python. So, voila FtpCube.

%description -l pl
FtpCube to wieloplatformowy, graficzny klient FTP napisany w Pythonie,
u¿ywaj±cy biblioteki graficznej wxPython. Interfejs FtpCube jest
oparty na LeechFTP Jana Debisa, ale kod zosta³ stworzony od pocz±tku i
zawiera funkcjonalno¶æ przewy¿szaj±c± orygina³.

FtpCube ma zapewniæ wysokiej jako¶ci interfejs u¿ytkownika, a tak¿e
bogaty zbiór mo¿liwo¶ci. Projekt FtpCube narodzi³ siê z poszukiwañ
dobrego, uniksowego klienta FTP o du¿ych mo¿liwo¶ciach, oferuj±cego
intuicyjny i seksowny interfejs. Autorowi spodoba³a siê idea klienta
FTP napisanego w Pythonie. Tak wiêc, voila FtpCube.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--prefix=%{_prefix} \
	--install-scripts=%{_bindir} \
	--root=$RPM_BUILD_ROOT

install -D %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/libftpcube
%{_desktopdir}/*
%{_pixmapsdir}/*
