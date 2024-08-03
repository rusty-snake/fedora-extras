Name:           typos-lsp
Version:        0.1.22
Release:        1%{?dist}
Summary:        Source code spell checker for Visual Studio Code and LSP clients

License:        MIT
URL:            https://github.com/tekumara/typos-lsp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24


%description
typos is a low false-positive source code spell checker. This project
exposes typos via a Language Server Protocol (LSP) server and Visual
Studio Code extension to provide a fast, low memory, in-editor spell
checker.


%prep
%autosetup -p1
%{__cargo} vendor --versioned-dirs vendor/
%cargo_prep -v vendor/


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%define cargo_install_lib 0
cd crates/typos-lsp
%cargo_install


%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md CHANGELOG.md
%{_bindir}/typos-lsp


%changelog
* Sat Aug 3 2024 rusty-snake - 0.1.22-1
- typos-lsp 0.1.22

* Sat Jul 13 2024 rusty-snake - 0.1.21-1
- typos-lsp 0.1.21

* Sat Jul 6 2024 rusty-snake - 0.1.20-1
- typos-lsp 0.1.20

* Sun Jun 16 2024 rusty-snake - 0.1.19-1
- typos-lsp 0.1.19

* Thu May 02 2024 rusty-snake - 0.1.18-1
- typos-lsp 0.1.18

* Tue Apr 09 2024 rusty-snake - 0.1.17-1
- typos-lsp 0.1.17

* Tue Mar 26 2024 rusty-snake - 0.1.16-1
- typos-lsp 0.1.16

* Sun Mar 03 2024 rusty-snake - 0.1.15-1
- Initial typos-lsp spec
