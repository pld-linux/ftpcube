Summary:	Multithreaded FTP client for X Window
Name:		ftpcube
Version:	0.4.3
Release:	1
License:	Artistic for code, GPL v2 for icons
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/ftpcube/ftpcube-0.4.3.tar.gz
# Source0-md5:	574d207377a24caf6315866d52326672
URL:		http://ftpcube.sourceforge.net/
BuildRequires:	python
Requires:	python-wxPython
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FtpCube is a multi-platform, graphical FTP client written in Python,
using the wxPython graphical tookit.  FtpCube's interface is based on
LeechFTP by Jan Debis but its codebase has been developed from scratch
and includes functionality that surpasses the original LeechFTP.

FtpCube aims to provide a high quality user interface, as well as a rich
feature set.  The FtpCube project was born out of my search to find a
good, capable unix FTP client that offered an intuitive and sexy UI.
Plus, I liked the idea of having an FTP client written in Python.  So,
voila FtpCube.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --optimize=2 \
	--prefix=%{_prefix} \
	--install-scripts=%{_bindir} \
        --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGELOG
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/libftpcube/
