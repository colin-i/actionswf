
Name: actionswf
Version: 1.153
Release: 0
License: GPLv3
Summary: ActionSwf compiler
Url: https://github.com/colin-i/actionswf
Source0: %{name}-%{version}.tar.gz

BuildRequires: ocompiler make gcc
Requires: python3

%description
ActionSwf compiler and dev files.

%package devel
Summary: ActionSwf dev files
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description devel
This package contains necessary header files for actionswf development.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup
touch include_dev

%build
linkerflags="-O3 -g" make  # -g here is important if wanting to have debuginfo and debugsource packages

%install
install_number=64 %make_install

#-- FILES ---------------------------------------------------------------------#
%files
%attr(0644, root, root) "%{_libdir}/libactionswf.so"
%attr(0644, root, root) "%{_libdir}/liboadbgdata.so"
%attr(0755, root, root) "%{_bindir}/oaalternative.sh"
%attr(0755, root, root) "%{_bindir}/oaalternative.py"

%files devel
%attr(0644, root, root) "%{_includedir}/%{name}/oadbgdatas.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/oadbgdata.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/oadbgdatas.h"
%attr(0644, root, root) "%{_includedir}/%{name}/oadbgdata.h"
%attr(0644, root, root) "%{_includedir}/%{name}/flags.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/flagss.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/importf.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/import.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/flags.h"
%attr(0644, root, root) "%{_includedir}/%{name}/flagss.h"
%attr(0644, root, root) "%{_includedir}/%{name}/actionswf.oh"
%attr(0644, root, root) "%{_includedir}/%{name}/actionswf.h"

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Mon Sep 29 2025 Costin Botescu <costin.botescu@gmail.com> 1.153-0
- python 3.6 (costin.botescu@gmail.com)
- 1.152 (costin.b.84@gmail.com)
- test at deb src (costin.botescu@gmail.com)
- verbose .x peak (costin.botescu@gmail.com)
- makes (costin.botescu@gmail.com)
- deobfuscator at always break loop (costin.botescu@gmail.com)
- while(true) deobfuscator (costin.botescu@gmail.com)
- info (costin.botescu@gmail.com)

* Mon Sep 29 2025 Costin Botescu <costin.botescu@gmail.com> 1.152-0
- test at deb src (costin.botescu@gmail.com)
- verbose .x peak (costin.botescu@gmail.com)
- makes (costin.botescu@gmail.com)
- deobfuscator at always break loop (costin.botescu@gmail.com)
- while(true) deobfuscator (costin.botescu@gmail.com)
- info (costin.botescu@gmail.com)

* Thu Sep 18 2025 Costin Botescu <costin.botescu@gmail.com> 1.151-0
- mover (costin.botescu@gmail.com)
- line ending comments (costin.botescu@gmail.com)
- extra break detection (costin.botescu@gmail.com)
- info (costin.botescu@gmail.com)

* Mon Sep 08 2025 Costin Botescu <costin.botescu@gmail.com> 1.150-0
- extern ffdec test (costin.botescu@gmail.com)
- cmps (costin.botescu@gmail.com)
- remove ffdec obfuscation (costin.botescu@gmail.com)
- value (costin.botescu@gmail.com)
- accepting utf8 2 bytes as variable (for alt for..in break recognition)
  (costin.botescu@gmail.com)
- oalt: exports when _ and another case when ' ' (costin.botescu@gmail.com)
- rest of includes from src to dev (costin.botescu@gmail.com)
- local .h (costin.botescu@gmail.com)

* Mon Sep 01 2025 Costin Botescu <costin.botescu@gmail.com> 1.149-0
- exit from doaction step (costin.botescu@gmail.com)
- oalt optimizations (costin.botescu@gmail.com)
- button spaced export (costin.botescu@gmail.com)
- oalt exports (costin.botescu@gmail.com)
- oalt scripts exports 1/4 (costin.botescu@gmail.com)
- exports at oalt (costin.botescu@gmail.com)
- oalt export redefined (costin.botescu@gmail.com)
- find optimization (costin.botescu@gmail.com)
- filter no action buttons (costin.botescu@gmail.com)
- fixes at oalt (costin.botescu@gmail.com)
- flagss at makewin (costin.botescu@gmail.com)

* Wed Aug 27 2025 Costin Botescu <costin.botescu@gmail.com> 1.148-0
- fix related to constant unsigned at int c open return
  (costin.botescu@gmail.com)
- at oalt: for not exported sprites (costin.botescu@gmail.com)
- flagss (costin.botescu@gmail.com)
- avoid sigsev (costin.botescu@gmail.com)
- another actionparse valid .x commit (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- another case for =- call() (costin.botescu@gmail.com)
- spaces at = - x (costin.botescu@gmail.com)

* Wed Aug 20 2025 Costin Botescu <costin.botescu@gmail.com> 1.147-0
- read_done (costin.botescu@gmail.com)
- must separate flag_pool_read from flag_pool_read_unlink for easiness at .xx
  yes or no (costin.botescu@gmail.com)
- =-x   ,   .log for alt with .x for regrab (costin.botescu@gmail.com)
- minus a jump (costin.botescu@gmail.com)
- no warning when dbl from img. flag_verbose (costin.botescu@gmail.com)
- img[_ex]/imagex[_ex] to do: warning off (costin.botescu@gmail.com)
- and noDup at var (costin.botescu@gmail.com)
- noDup at incdec member (costin.botescu@gmail.com)
- no duplicate for mixt member (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- fix builtin .x run (costin.botescu@gmail.com)
- more parse spaces (costin.botescu@gmail.com)
- oaalt 3 parts (costin.botescu@gmail.com)
- keep alt scripts (costin.botescu@gmail.com)
- new ffdec updates (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- readme (costin.botescu@gmail.com)
- pkgs one push (costin.botescu@gmail.com)

* Wed Jul 23 2025 Costin Botescu <costin.botescu@gmail.com> 1.146-0
- new tag standards at pkg (costin.botescu@gmail.com)
- change src Makefile for ld new version (costin.botescu@gmail.com)
- test strip (costin.botescu@gmail.com)
- callrets (costin.botescu@gmail.com)
- clipped/repeating (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- "up" (costin.botescu@gmail.com)
- that gcc was not the solution (costin.botescu@gmail.com)
- fixes for suse i586 (costin.botescu@gmail.com)
- readme and pub (costin.botescu@gmail.com)

* Mon May 26 2025 Costin Botescu <costin.botescu@gmail.com> 1.143-2
- 

* Mon May 26 2025 Costin Botescu <costin.botescu@gmail.com> 1.143-1
- "sync" (costin.b.84@gmail.com)
- "sync" (costin.b.84@gmail.com)
- "sync" (costin.b.84@gmail.com)
- "$@" (costin.botescu@gmail.com)
- +x (costin.botescu@gmail.com)
- pub win oaalternative (costin.botescu@gmail.com)
- test (costin.botescu@gmail.com)
- test (costin.botescu@gmail.com)
- .cmd file (costin.botescu@gmail.com)
- test (costin.botescu@gmail.com)
- bash? powershell? (costin.botescu@gmail.com)
- in case ffdec is provided somewhere else (costin.botescu@gmail.com)
- "sync" (costin.b.84@gmail.com)
- to not route what_m twice (costin.botescu@gmail.com)
- some one time calls with what_m logic (costin.botescu@gmail.com)
- win rename will not overwrite (costin.botescu@gmail.com)
- "tests" (costin.b.84@gmail.com)
- win oadata tests, still need to fix rename (costin.botescu@gmail.com)
- with the new o will remove one & (costin.botescu@gmail.com)
- at windows a 64bit long is long long (costin.botescu@gmail.com)
- can point straight at function at declare/arg1 but the linker will do more
  work, can be an option if wanting (costin.botescu@gmail.com)
- preparing for liboadbgdata win build (costin.botescu@gmail.com)
- "sync" (costin.b.84@gmail.com)
- rel has overwrite (costin.botescu@gmail.com)
- "sync" (costin.b.84@gmail.com)
- ignore more files at deb package (costin.botescu@gmail.com)
- -dev with main package same version req (costin.botescu@gmail.com)
- fedora copr (costin.botescu@gmail.com)

* Sun May 11 2025 Costin Botescu <costin.botescu@gmail.com> 1.143-0
- new package built with tito

