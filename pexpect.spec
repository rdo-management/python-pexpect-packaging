%define pyver %(python -c 'import sys ; print sys.version[:3]')
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Expect module for Python
Name: pexpect
Version: 2.0
Release: 1%{?dist}

License: PSF
Group: Development/Languages
URL: http://pexpect.sf.net
Source: http://dl.sf.net/pexpect/%{name}-%{version}.tgz
Source1: http://dl.sf.net/pexpect/pexpect-doc.tgz
Source2: http://dl.sf.net/pexpect/pexpect-%{version}-examples.tgz
Source10: LICENSE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-abi = %{pyver}
BuildRequires: python
BuildArch: noarch

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for
duplicating software package installations on different servers. It can be
used for automated software testing. Pexpect is in the spirit of Don Libes'
Expect, but Pexpect is pure Python. Unlike other Expect-like modules for
Python, Pexpect does not require TCL or Expect nor does it require C
extensions to be compiled. It should work on any platform that supports the
standard Python pty module.

%prep
%setup -q -a1 -a2
rm -rf $(find . -type d -name CVS)
cp %{SOURCE10} .

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# These are apparently works in progress and thus not installed.  But they are
# needed by the chess* examples.... Moving them to examples for now.
cp -p screen.py ANSI.py FSM.py pxssh.py examples
find examples -type f -exec chmod a-x \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/pexpect.py
%{python_sitelib}/pexpect.pyc
%ghost %{python_sitelib}/pexpect.pyo

%doc README doc examples LICENSE

%changelog
* Thu Nov 17 2005 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.0-1
- Update to 2.0.

* Sat Sep 3 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0.99999b-2
- Add LICENSE File.
- Make noarch.
- Remove executable permissions from the modules copied to examples.
  
* Fri Sep  2 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0.99999b
- Update to version 0.99999b.
- Add dist tag. 

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb 03 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0.999-2
- Use python_sitelib macro to resolve build issues on x86_64.
- %%ghost *.pyo
- Install ANSI.py, screen.py, and FSM.py into the examples.  These are intended
  to suplement pexpect eventually but they are currently much less robust and
  not installed to by default.  But they are needed by some examples.
- Use __python macro in build/install for consistency.
- Add --skip-build to the invocation of setup.py in install.

* Mon May 31 2004 Panu Matilainen <pmatilai@welho.com> 0.999-0.fdr.1
- get rid of distrel munging, buildsys does that...
- update to 0.999
- update doc and example tarballs
- fix build on python <> 2.2
- use -O1 in install to generate .pyo files instead of manually creating the files
- require python-abi = pyver to get dependencies right

* Sun Jul 27 2003 Panu Matilainen <pmatilai@welho.com> 0.98-0.fdr.3
- own .pyo files too as suggested by Ville (#517)

* Sat Jul 26 2003 Panu Matilainen <pmatilai@welho.com> 0.98-0.fdr.2
- fixes by Ville (bug #517) applied

* Sat Jul 26 2003 Panu Matilainen <pmatilai@welho.com>
- Initial Fedora packaging

