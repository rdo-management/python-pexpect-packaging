%define pyver %(python -c 'import sys ; print sys.version[:3]')

Summary: Expect module for Python
Name: pexpect
Version: 0.999
Release: 1
License: PSFL
Group: Development/Languages
URL: http://pexpect.sourceforge.net
Source: http://download.sourceforge.net/pexpect/%{name}-%{version}.tgz
Source1: http://download.sourceforge.net/pexpect/pexpect-doc.tgz
Source2: http://download.sourceforge.net/pexpect/pexpect-examples.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-abi = %{pyver}
BuildRequires: python-devel >= 0:2.2

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

%build
python setup.py build

%install
python setup.py install -O1 --root $RPM_BUILD_ROOT

#touch %{name}-ghost.files
#for file in $(find $RPM_BUILD_ROOT -type f -name "*.py"); do
#for suffix in c o; do
#if [ ! -e "$file$suffix" ]; then
#touch "$file$suffix"
#echo "%ghost $file$suffix" | sed "s|$RPM_BUILD_ROOT||" \
#>> %{name}-ghost.files
#fi
#done
#done

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}-ghost.files
%files
%defattr(-,root,root,-)
%{_libdir}/python%{pyver}/site-packages/pexpect.*

%doc README.txt doc examples

%changelog
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

