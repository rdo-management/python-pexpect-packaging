%{!?rhrel:%define rhrel %(cut -d' ' -f5 /etc/redhat-release )}
%if "%{rhrel}" == "9"
%define distrel rh90
%else
%define distrel rh%(echo %{rhrel} | sed 's/\\.//')
%endif

Summary: Expect module for Python
Name: pexpect
Version: 0.98
Release: 0.fdr.3.%{distrel}
License: PSFL
Group: Development/Languages
URL: http://pexpect.sourceforge.net
Source: http://download.sourceforge.net/pexpect/%{name}-%{version}.tgz
Source1: http://download.sourceforge.net/pexpect/pexpect-doc.tgz
Source2: http://download.sourceforge.net/pexpect/pexpect-examples.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python >= 0:2.2
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
python setup.py install --root $RPM_BUILD_ROOT

touch %{name}-ghost.files
for file in $(find $RPM_BUILD_ROOT -type f -name "*.py"); do
  for suffix in c o; do
    if [ ! -e "$file$suffix" ]; then
      touch "$file$suffix"
      echo "%ghost $file$suffix" | sed "s|$RPM_BUILD_ROOT||" \
        >> %{name}-ghost.files
    fi
  done
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-ghost.files
%defattr(-,root,root,-)
%{_libdir}/python2.2/site-packages/pexpect.py
%{_libdir}/python2.2/site-packages/pexpect.pyc

%doc README.txt doc examples

%changelog
* Sun Jul 27 2003 Panu Matilainen <pmatilai@welho.com> 0.98-0.fdr.3
- own .pyo files too as suggested by Ville (#517)

* Sat Jul 26 2003 Panu Matilainen <pmatilai@welho.com> 0.98-0.fdr.2
- fixes by Ville (bug #517) applied

* Sat Jul 26 2003 Panu Matilainen <pmatilai@welho.com>
- Initial Fedora packaging

