Name:           hardened_malloc
Version:        8
Release:        1%{?dist}
Summary:        Hardened allocator designed for modern systems

License:        MIT
URL:            https://github.com/GrapheneOS/hardened_malloc
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        30-hardened_malloc.conf


%description
Hardened allocator designed for modern systems.

It has integration into Android's Bionic libc and can be used externally with
musl and glibc as a dynamic library for use on other Linux-based platforms. It
will gain more portability / integration over time.


%prep
%autosetup


%build
make


%install
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysctl.d/30-hardened_malloc.conf
install -Dm0755 libhardened_malloc.so %{buildroot}%{_libdir}/libhardened_malloc.so
strip %{buildroot}%{_libdir}/libhardened_malloc.so


%check
make test


%post
if ! grep -q "%{_libdir}/libhardened_malloc.so" /etc/ld.so.preload; then
    echo " %{_libdir}/libhardened_malloc.so " >> /etc/ld.so.preload
fi


%preun
if [[ $1 == 0 ]]; then
    sed -i "s|%{_libdir}/libhardened_malloc.so||g" /etc/ld.so.preload
fi


%files
%license LICENSE CREDITS
%doc README.md
%{_sysconfdir}/sysctl.d/30-hardened_malloc.conf
%{_libdir}/libhardened_malloc.so


%changelog
* Sat Sep 18 2021 rusty-snake - 8-1
- Initial hardened_malloc spec
