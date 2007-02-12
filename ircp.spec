Summary:	A utility for sending and retrieving files using the IrXfer protocol
Summary(pl.UTF-8):   Program do wysyłania i pobierania plików przez protokół IrXfer
Name:		ircp
Version:	0.3
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/openobex/%{name}-%{version}.tar.gz
# Source0-md5:	a77124e7efa6b31369404371485179b2
Patch0:		%{name}-path.patch
URL:		http://sourceforge.net/projects/openobex/
BuildRequires:	openobex-devel >= 0.9.8
Requires:	openobex >= 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility for sending and retrieving files using the IrXfer protocol.

%description -l pl.UTF-8
Program do wysyłania i pobierania plików przez protokół IrXfer.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
