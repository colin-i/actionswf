
Name: actionswf
Version: 1.146
Release: 0
License: GPLv3
Summary: ActionSwf compiler
Url: https://github.com/colin-i/actionswf
Source0: %{name}-%{version}.tar.gz

BuildRequires: ocompiler make gcc

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

