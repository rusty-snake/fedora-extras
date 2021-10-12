%global commit 7c4c765671ce5c76d9486894b3ea36b306621008
%global commitdate 20211012
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libaslrmalloc
Version:        1.0.0~alpha
Release:        0.2.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Malloc replacement library for maximum ASLR

License:        LGPLv2+ or BSD
URL:            https://github.com/topimiettinen/libaslrmalloc
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  meson >= 0.52.1


%description
libaslrmalloc is a LD_PRELOADed library which replaces malloc() and other
memory allocation functions from C library. The main design goal is not
performance or memory consumption but to increase address space layout
randomization (ASLR), hence the name. This is achieved by not trying to keep
the pages together, forcing the kernel to map pages at random addresses and
unmapping old memory immediately when possible.


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install
strip %{buildroot}%{_libdir}/libaslrmalloc.so.1.0.0


%check
%meson_test


%files
%doc README.md DESIGN.md
%{_libdir}/libaslrmalloc.so
%{_libdir}/libaslrmalloc.so.1
%{_libdir}/libaslrmalloc.so.1.0.0


%changelog
* Tue Oct 12 2021 rusty-snake - 1.0.0~alpha-0.2.20211012git7c4c765
- Update to latest commit

* Tue Oct 12 2021 rusty-snake - 1.0.0~alpha-0.2.20211011git6dfeb74
- Update to latest commit

* Mon Oct 11 2021 rusty-snake - 1.0.0~alpha-0.2.20211010gitd094658
- Update to latest commit

* Sat Oct 09 2021 rusty-snake - 1.0.0~alpha-0.2.20211009git098f91c
- Update to latest commit

* Fri Oct 08 2021 rusty-snake - 1.0.0~alpha-0.2.20211008git9abdb7b
- Update to latest commit

* Thu Oct 07 2021 rusty-snake - 1.0.0~alpha-0.2.20211007git2c70360
- Update to latest commit

* Thu Oct 07 2021 rusty-snake - 1.0.0~alpha-0.1.20211007gitb6c03a4
- Update to latest commit

* Wed Oct 06 2021 rusty-snake - 0-1.20211006git1f0beff
- Update to latest commit

* Wed Oct 06 2021 rusty-snake - 0-1.20211005git468e3e9
- Update to latest commit

* Fri Oct 01 2021 rusty-snake - 0-1.20211001gitacea54c
- Adopt meson as build system

* Thu Sep 30 2021 rusty-snake - 0-1.20210927gita04fa0b
- Initial libaslrmalloc spec
