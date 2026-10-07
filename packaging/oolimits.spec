Name:           oolimits
Version:        0.1.0
Release:        1%{?dist}
Summary:        Queries and configures POSIX process resource limits (nofile, nproc, stack).
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oolimits
Source0:        oolimits-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oolimits is a sovereign, capability-bounded RLIMIT AUDITOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oolimits
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oolimits-uninstall

%files
/usr/bin/oolimits
/usr/bin/oolimits-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
