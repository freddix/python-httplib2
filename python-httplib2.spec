Summary:	A comprehensive HTTP client library
Name:		python-httplib2
Version:	0.7.6
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://httplib2.googlecode.com/files/httplib2-%{version}.tar.gz
# Source0-md5:	65ff252c621e382cbaf10b43f28891b9
URL:		http://code.google.com/p/httplib2
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A comprehensive HTTP client library, httplib2.py supports many
features left out of other HTTP libraries.

%prep
%setup -qn httplib2-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/httplib2
%{py_sitescriptdir}/httplib2/*.py[co]
%{py_sitescriptdir}/httplib2/cacerts.txt

