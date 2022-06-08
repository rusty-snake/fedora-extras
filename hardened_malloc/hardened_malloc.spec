Name:           hardened_malloc
Version:        11
Release:        1%{?dist}
Summary:        Hardened allocator designed for modern systems

License:        MIT
URL:            https://github.com/GrapheneOS/hardened_malloc
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        30-hardened_malloc.conf

BuildRequires:  systemd-rpm-macros


# https://github.com/GrapheneOS/hardened_malloc/issues/200
%global optflags %{optflags} -fno-fat-lto-objects

%description
Hardened allocator designed for modern systems.

It has integration into Android's Bionic libc and can be used externally with
musl and glibc as a dynamic library for use on other Linux-based platforms. It
will gain more portability / integration over time.


%prep
%autosetup


%build
make
make VARIANT=light


%install
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysctldir}/30-hardened_malloc.conf
install -Dm0755 -s out/libhardened_malloc.so %{buildroot}%{_libdir}/libhardened_malloc.so
install -Dm0755 -s out-light/libhardened_malloc-light.so %{buildroot}%{_libdir}/libhardened_malloc-light.so


%check
make test


#%%post
#if ! grep -q "%%{_libdir}/libhardened_malloc.so" /etc/ld.so.preload; then
#    echo " %%{_libdir}/libhardened_malloc.so " >> /etc/ld.so.preload
#fi
#
#
#%%preun
#if [[ $1 == 0 ]]; then
#    sed -i "s|%%{_libdir}/libhardened_malloc.so||g" /etc/ld.so.preload
#fi


%files
%license LICENSE CREDITS
%doc README.md
%{_sysctldir}/30-hardened_malloc.conf
%{_libdir}/libhardened_malloc.so
%{_libdir}/libhardened_malloc-light.so


%changelog
* Sat Jan 22 2022 rusty-snake - 11-1
- Update to version 11

* Thu Jan 13 2022 rusty-snake - 10-1
- Update to version 10
- Add libhardened_malloc-light.so

* Mon Jan 3 2022 rusty-snake - 9-1
- Update to version 9

* Sun Nov 14 2021 rusty-snake - 8-3
- Install 30-hardened_malloc.conf under %%_sysctldir
- Cleanup the specfile

* Thu Sep 30 2021 rusty-snake - 8-2
- Disable the post-transaction scriptlet to insert hardened_malloc
  into `/etc/ld.so.preload

* Sat Sep 18 2021 rusty-snake - 8-1
- Initial hardened_malloc spec
