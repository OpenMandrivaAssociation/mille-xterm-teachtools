%define svn 2137

Summary:	Teacher Tools for the MILLE-XTERM project
Name:		mille-xterm-teachtools
Version:	1.0
Release:	%mkrel 0.%{svn}.1
License:	GPL
Group:		System/Servers
URL:		http://www.revolutionlinux.com/mille-xterm
Source:		mille-xterm-teachtools-%{version}.tar.bz2
Requires:	python >= 2.4.1 tkinter
BuildRequires:	python-devel >= 2.4.1
BuildArch:	noarch

%define py_ver %(python -c "import sys; v=sys.version_info[:2]; print '%%d.%%d'%%v" 2>/dev/null || echo PYTHON-NOT-FOUND)
%define py_prefix %(python -c "import sys; print sys.prefix" 2>/dev/null || echo PYTHON-NOT-FOUND)
%define py_libdir %{py_prefix}/lib/python%{py_ver}

%description
Teacher Tools for the MILLE-XTERM project.

%prep

%setup -q

%build 

%install
rm -fr %{buildroot}

install -d %{buildroot}%{_datadir}/locale/en/LC_MESSAGES
install -d %{buildroot}/lib/python%{py_ver}/site-packages

pushd src
    python setup.py install --prefix=%{buildroot}
popd

chmod 755 %{buildroot}%{_datadir}/mille-xterm/MilleTeachTools/*.sh
mv %{buildroot}%{_bindir}/MilleTeachTools.py %{buildroot}%{_bindir}/MilleTeachTools
chmod 755 %{buildroot}%{_bindir}/MilleTeachTools

# cleanup
rm -rf %{buildroot}/lib/python%{py_ver}/site-packages

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README.fr
%{_datadir}/mille-xterm/MilleTeachTools/*
%{_datadir}/mille-xterm/MilleTeachTools/locale/*/LC_MESSAGES/*
%{_bindir}/MilleTeachTools


