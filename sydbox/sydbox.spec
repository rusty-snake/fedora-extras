Name:           sydbox
Version:        3.24.1
Release:        1%{?dist}
Summary:        Rock-solid unikernel

License:        GPLv3
URL:            https://gitlab.exherbo.org/sydbox/sydbox
Source0:        %{url}/-/archive/v%{version}/sydbox-v%{version}.tar.bz2

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  libseccomp-devel
BuildRequires:  scdoc


%description
Syd is a rock-solid unikernel to sandbox applications on Linux>=5.19.
Syd is similar to Bubblewrap, Firejail, GVisor, and minijail. Syd is
secure by default, and intends to provide a simple interface over
various intricate Linux sandboxing mechanisms such as LandLock,
Namespaces, ptrace, and seccomp-{bpf,notify}, most of which have a
reputation of being brittle and difficult to use. You may run Syd as a
regular user, with no extra privileges, and you can even set Syd as
your login shell.


%prep
%autosetup -n %{name}-v%{version}
%{__cargo} vendor --versioned-dirs vendor/
%cargo_prep -v vendor/


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

for manpage in man/*.scd; do
    scdoc < "$manpage" > "${manpage%.scd}"
done


%install
%define cargo_install_lib 0
%cargo_install

for manpage in man/*.1; do
    %{__install} -Dm644 "$manpage" "%{buildroot}%{_mandir}/man1/$(basename "$manpage")"
done
for manpage in man/*.2; do
    %{__install} -Dm644 "$manpage" "%{buildroot}%{_mandir}/man2/$(basename "$manpage")"
done
for manpage in man/*.5; do
    %{__install} -Dm644 "$manpage" "%{buildroot}%{_mandir}/man5/$(basename "$manpage")"
done
for manpage in man/*.7; do
    %{__install} -Dm644 "$manpage" "%{buildroot}%{_mandir}/man7/$(basename "$manpage")"
done

# TODO:
#  * data/*.syd-3
#  * pandora/
#  * src/esyd.sh
#  * time/
#  * vim/


%files
%license COPYING
%license LICENSE.dependencies
%doc ChangeLog.md README.md
%{_bindir}/syd
%{_bindir}/syd-aes
%{_bindir}/syd-cat
%{_bindir}/syd-chk
%{_bindir}/syd-cp
%{_bindir}/syd-cpu
%{_bindir}/syd-elf
%{_bindir}/syd-env
%{_bindir}/syd-err
%{_bindir}/syd-exec
%{_bindir}/syd-fork
%{_bindir}/syd-hex
%{_bindir}/syd-key
%{_bindir}/syd-ldd
%{_bindir}/syd-load
%{_bindir}/syd-lock
%{_bindir}/syd-log
%{_bindir}/syd-ls
%{_bindir}/syd-mdwe
%{_bindir}/syd-mem
%{_bindir}/syd-open
%{_bindir}/syd-path
%{_bindir}/syd-poc
%{_bindir}/syd-read
%{_bindir}/syd-run
%{_bindir}/syd-sha
%{_bindir}/syd-size
%{_bindir}/syd-stat
%{_bindir}/syd-sys
%{_bindir}/syd-test
%{_bindir}/syd-test-do
%{_bindir}/syd-tick
%{_bindir}/syd-tor
%{_bindir}/syd-tty
%{_mandir}/man1/syd-aes.1.gz
%{_mandir}/man1/syd-cat.1.gz
%{_mandir}/man1/syd-chk.1.gz
%{_mandir}/man1/syd-cp.1.gz
%{_mandir}/man1/syd-cpu.1.gz
%{_mandir}/man1/syd-elf.1.gz
%{_mandir}/man1/syd-env.1.gz
%{_mandir}/man1/syd-err.1.gz
%{_mandir}/man1/syd-exec.1.gz
%{_mandir}/man1/syd-fork.1.gz
%{_mandir}/man1/syd-hex.1.gz
%{_mandir}/man1/syd-key.1.gz
%{_mandir}/man1/syd-ldd.1.gz
%{_mandir}/man1/syd-load.1.gz
%{_mandir}/man1/syd-lock.1.gz
%{_mandir}/man1/syd-log.1.gz
%{_mandir}/man1/syd-ls.1.gz
%{_mandir}/man1/syd-mdwe.1.gz
%{_mandir}/man1/syd-mem.1.gz
%{_mandir}/man1/syd-oci.1.gz
%{_mandir}/man1/syd-open.1.gz
%{_mandir}/man1/syd-path.1.gz
%{_mandir}/man1/syd-poc.1.gz
%{_mandir}/man1/syd-read.1.gz
%{_mandir}/man1/syd-run.1.gz
%{_mandir}/man1/syd-sha.1.gz
%{_mandir}/man1/syd-size.1.gz
%{_mandir}/man1/syd-stat.1.gz
%{_mandir}/man1/syd-sys.1.gz
%{_mandir}/man1/syd-test.1.gz
%{_mandir}/man1/syd-tick.1.gz
%{_mandir}/man1/syd-tor.1.gz
%{_mandir}/man1/syd-tty.1.gz
%{_mandir}/man1/syd.1.gz
%{_mandir}/man2/syd.2.gz
%{_mandir}/man5/syd.5.gz
%{_mandir}/man7/syd.7.gz
%{_mandir}/man7/sydtutorial.7.gz

%changelog
* Sat Aug 24 2024 rusty-snake - 3.24.1-1
- Initial sydbox spec
