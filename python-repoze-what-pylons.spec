%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		python-repoze-what-pylons
Version:	1.0
Release:	4%{?dist}
Summary:	A plugin providing utilities for Pylons applications using repoze.what
Group:		Development/Languages
License:	BSD
URL:		http://code.gustavonarea.net/repoze.what-pylons/
Source0:	http://pypi.python.org/packages/source/r/repoze.what-pylons/repoze.what-pylons-%{version}.tar.gz
Patch0:		%{name}-setuptools.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools-devel
Requires:	python-repoze-what >= 1.0.4
Requires:	python-pylons >= 0.9.7
Requires:	python-decorator >= 3.0

%description
This plugin provides optional and handy utilities for Pylons applications 
using repoze.what. Some of the features of the plugin include:
* The utilities are ready to use: There’s nothing additional to be configured 
  before using.
* 100% documented. Each component is documented along with code samples.
* The test suite has a coverage of 100% and it will never decrease – if it 
  ever does, report it as a bug!
* TurboGears 2 is officially supported as well.

%prep
%setup -q -n repoze.what-pylons-%{version}
%patch0 -p0 -b .setuptools

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
# Can't do tests due to circular dependencies
# PYTHONPATH=$(pwd) nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-3
- fix rpmlint issues

* Fri Jun 05 2009 Luke Macken <lmacken@redhat.com> - 1.0-2
- Add a patch to ensure we use our own setuptools.

* Wed May  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-1
- Initial package for Fedora
