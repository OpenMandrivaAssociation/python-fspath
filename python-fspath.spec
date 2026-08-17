Name:		python-fspath
Version:	20230629
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fspath/fspath-%{version}.tar.gz
Summary:	semantic path names and more
URL:		https://pypi.org/project/fspath/
License:	AGPLv3
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
semantic path names and more

%files
%{_bindir}/fspath
%{_bindir}/which.py
%{py_sitedir}/fspath
%{py_sitedir}/fspath-*.*-info
