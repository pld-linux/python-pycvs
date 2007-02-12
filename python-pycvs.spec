
%define		module	pycvs

Summary:	CVS support for Python
Summary(pl.UTF-8):   Obsługa CVSu dla Pythona
Name:		python-%{module}
Version:	0.1
Release:	3
License:	GNU
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pycvs/%{module}-%{version}.tar.gz
# Source0-md5:	3abf7c9d6d67a760190692071a476edc
URL:		http://pycvs.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyCVS is a Python library/module for the CVS (Concurrent Versions
System) protocol. It supports asynchronous and synchronous handling of
CVS servers.

%description -l pl.UTF-8
pyCVS jest biblioteką/modułem Pythona do obsługi protokołu CVS
(Concurrent Versions System). Obsługuje asynchroniczną i synchroniczną
obsługę serwerów CVS.

%prep
%setup -q -n %{module}-%{version}

%build
python -c "import compiler;compiler.compileFile('library/pycvs.py')"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install clients/client.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install library/pycvs.pyc $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{py_sitedir}/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
