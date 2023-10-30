Name:           scurl
Version:        2.0.3
Release:        1%{?dist}
Summary:        Secure curl

License:        MIT
URL:            https://github.com/rusty-snake/fedora-extras/tree/main/scurl
Source0:        scurl
Source1:        scurl-download
Source2:        scurl.1.rst
Source3:        scurl-download.1.rst
Source4:        scurl-tor
Source5:        scurl-tor.conf
Source6:        scurl-tor.1.rst
Source7:        scurl-download.conf

BuildArch:      noarch
BuildRequires:  python3-docutils
Requires:       curl


%description
scurl is a wrapper around curl that enforces TLSv1.3.
scurl-download is a wrapper around scurl optimized to download files.


%prep
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{_builddir}


%build
rst2man scurl.1.rst scurl.1
rst2man scurl-download.1.rst scurl-download.1
rst2man scurl-tor.1.rst scurl-tor.1


%install
install -Dm0644 %{SOURCE5} %{buildroot}/etc/sysconfig/scurl-tor
install -Dm0644 %{SOURCE7} %{buildroot}/etc/sysconfig/scurl-download
install -Dm0755 -t %{buildroot}%{_bindir} scurl scurl-download scurl-tor
install -Dm0644 -t %{buildroot}%{_mandir}/man1 scurl.1 scurl-download.1 scurl-tor.1


%files
%config(noreplace) /etc/sysconfig/scurl-tor
%config(noreplace) /etc/sysconfig/scurl-download
%{_bindir}/scurl
%{_bindir}/scurl-download
%{_bindir}/scurl-tor
%{_mandir}/man1/scurl.1.gz
%{_mandir}/man1/scurl-download.1.gz
%{_mandir}/man1/scurl-tor.1.gz


%changelog
* Mon Oct 30 2023 rusty-snake - 2.0.3-1
- Update USER_AGENT in scurl-tor.conf

* Sat Aug 05 2023 rusty-snake - 2.0.2-1
- Update USER_AGENT in scurl-download.conf

* Tue Mar 28 2023 rusty-snake - 2.0.1-1
- Update USER_AGENT strings

* Thu Nov 18 2021 rusty-snake - 2.0.0-1
- Do not gzip manpages during %%build
- scurl-download: Fake the UA
- scurl-download: Use --compressed

* Thu Oct 14 2021 rusty-snake - 1.1.0-2
- Fix building of scurl-tor manpage

* Thu Oct 14 2021 rusty-snake - 1.1.0-1
- Add scurl-tor
- Drop --help message from scurl and scurl-download
- Manpage fixes

* Sun Sep 19 2021 rusty-snake - 1.0-1
- Initial scurl spec
