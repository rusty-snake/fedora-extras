%global commit 468e3e96d9e0c677e090bbfb8c4ce0a0b66f4999
%global commitdate 20211005
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libaslrmalloc
Version:        0
Release:        1.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Malloc replacement library for maximum ASLR

License:        LGPLv2+ or BSD
URL:            https://github.com/topimiettinen/libaslrmalloc
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  meson >= 0.52.1


%description
libaslrmalloc is a LD_PRELOADed library which replaces malloc(), free(),
realloc() and calloc() from C library. The main design goal is not
performance or memory consumption but to increase address space layout
randomization (ASLR).


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install
strip %{buildroot}%{_libdir}/libaslrmalloc.so.1


%check
%meson_test


%files
%doc README.md DESIGN.md
%{_libdir}/libaslrmalloc.so
%{_libdir}/libaslrmalloc.so.1


%changelog
* Wed Oct 06 2021 rusty-snake - 0-1.20211005git468e3e9
- Update to latest commit

* Fri Oct 01 2021 rusty-snake - 0-1.20211001gitacea54c
- Adopt meson as build system

* Thu Sep 30 2021 rusty-snake - 0-1.20210927gita04fa0b
- Initial libaslrmalloc spec
