Name:           hardened_malloc
Version:        13
Release:        1%{?dist}
Summary:        Hardened allocator designed for modern systems

License:        MIT
URL:            https://github.com/GrapheneOS/hardened_malloc
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

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
cp config/default.mk config/pkey.mk
sed -i 's/CONFIG_SEAL_METADATA := false/CONFIG_SEAL_METADATA := true/' config/pkey.mk


%build
make
make VARIANT=light
make VARIANT=pkey


%install
install -Dm4644 -s out/libhardened_malloc.so %{buildroot}%{_libdir}/libhardened_malloc.so
install -Dm4644 -s out-light/libhardened_malloc-light.so %{buildroot}%{_libdir}/libhardened_malloc-light.so
install -Dm4644 -s out-pkey/libhardened_malloc-pkey.so %{buildroot}%{_libdir}/libhardened_malloc-pkey.so


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
%{_libdir}/libhardened_malloc.so
%{_libdir}/libhardened_malloc-light.so
%{_libdir}/libhardened_malloc-pkey.so


%changelog
* Mon Oct 14 2024 rusty-snake - 13-1
- hardened_malloc 13

* Tue Dec 12 2023 rusty-snake - 12-5
- hardened_malloc.so: 4755 -> 4644

* Sun Dec 10 2023 rusty-snake - 12-4
- Set set-user-id bit on libhardened_malloc.so.
  Thanks to Tad for the finding and reporting.
  Fixes #2

* Sat Dec 09 2023 rusty-snake - 12-3
- Remove 30-hardened_malloc.conf, Fedora 39 does this by default

* Sat Dec 09 2023 rusty-snake - 12-2
- Add pkey variant

* Fri Sep 29 2023 rusty-snake - 12-1
- Update to version 12

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
