Summary:	A utility for sending and retrieving files using the IrXfer protocol
Summary(pl):	Program do wysy³ania i pobierania plików przez protokó³ IrXfer
Name:		ircp
Version:	0.2
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/openobex/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/openobex/
Requires:	openobex >= 0.9.8
BuildRequires:	openobex-devel >= 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility for sending and retrieving files using the IrXfer protocol.

%description -l pl
Program do wysy³ania i pobierania plików przez protokó³ IrXfer.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
./configure --prefix=%{_prefix}

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
