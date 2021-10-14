Name:           scurl
Version:        1.1.0
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

BuildArch:      noarch

BuildRequires:  gzip python3-docutils
Requires:       curl


%description
scurl is a wrapper around curl that enforces TLSv1.3.
scurl-download is a wrapper around scurl optimized to download files.


%prep
cp %{SOURCE2} %{SOURCE3} %{_builddir}
printenv | grep RPM


%build
rst2man scurl.1.rst | gzip -9 > scurl.1.gz
rst2man scurl-download.1.rst | gzip -9 > scurl-download.1.gz
rst2man scurl-tor.1.rst | gzip -9 > scurl-tor.1.gz


%install
install -Dm0644 %{SOURCE5} %{buildroot}/etc/sysconfig/scurl-tor
install -Dm0755 -t %{buildroot}%{_bindir} %{SOURCE0} %{SOURCE1} %{SOURCE4}
install -Dm0644 -t %{buildroot}%{_mandir}/man1 scurl.1.gz scurl-download.1.gz scurl-tor.1.gz


%files
%config(noreplace) /etc/sysconfig/scurl-tor
%{_bindir}/scurl
%{_bindir}/scurl-download
%{_bindir}/scurl-tor
%{_mandir}/man1/scurl.1.gz
%{_mandir}/man1/scurl-download.1.gz
%{_mandir}/man1/scurl-tor.1.gz


%changelog
* Thu Oct 14 2021 rusty-snake 1.1.0-1
- Add scurl-tor
- Drop --help message from scurl and scurl-download
- Manpage fixes

* Sun Sep 19 2021 rusty-snake - 1.0-1
- Initial scurl spec
