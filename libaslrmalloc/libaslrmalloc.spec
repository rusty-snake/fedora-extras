%global commit a04fa0bedec3f5170ba2982fdbb4004a0ebd8503
%global commitdate 20210927
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libaslrmalloc
Version:        0
Release:        1.%{commitdate}git%{shortcommit}%{?dist}
Summary:        LD_PRELOADed library to randomize malloc and friends

License:        LGPLv2+ or BSD
URL:            https://github.com/topimiettinen/libaslrmalloc
Source0:        %{url}/archive/%{commit}.tar.gz


%description
libaslrmalloc is a LD_PRELOADed library which replaces malloc(), free(),
realloc() and calloc() from C library. The main design goal is not
performance or memory consumption but to increase address space layout
randomization (ASLR).


%prep
%autosetup -n %{name}-%{commit}


%build
gcc -o libaslrmalloc.so libaslrmalloc.c -fPIC -Wall -g -nostdlib -shared -O


%install
install -Dm0755 libaslrmalloc.so %{buildroot}%{_libdir}/libaslrmalloc.so
strip %{buildroot}%{_libdir}/libaslrmalloc.so


%files
%doc README.md DESIGN.md
%{_libdir}/libaslrmalloc.so


%changelog
* Thu Sep 30 2021 rusty-snake - 0-1.20210927gita04fa0b
- Initial libaslrmalloc spec
