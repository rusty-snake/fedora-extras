%global commit 4634c0523c020a59c43e1544a17f91eee1e2905a
%global commitdate 20211118
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libaslrmalloc
Version:        1.0.0~alpha
Release:        0.1.%{commitdate}git%{shortcommit}%{?dist}
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
%meson -Dstrip=true
%meson_build


%install
%meson_install


%check
%meson_test


%files
%doc README.md DESIGN.md
%{_bindir}/libaslrmallocrun
%{_libdir}/libaslrmalloc.so
%{_libdir}/libaslrmalloc.so.1
%{_libdir}/libaslrmalloc.so.1.0.0


%changelog
* Thu Nov 18 2021 rusty-snake - 1.0.0~alpha-0.1.20211118git4634c05
- Update to latest commit

* Thu Sep 30 2021 rusty-snake - 0-1.20210927gita04fa0b
- Initial libaslrmalloc spec
