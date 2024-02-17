Name:           typst-lsp
Version:        0.12.1
Release:        1%{?dist}
Summary:        A new markup-based typesetting system that is powerful and easy to learn.

License:        MIT
URL:            https://github.com/nvarner/typst-lsp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24


%description
A language server for Typst


%prep
%autosetup -p1
%{__cargo} vendor --versioned-dirs vendor/
%cargo_prep -v vendor/


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%cargo_install


%files
%license LICENSE-Apache-2.0.txt
%license LICENSE-MIT.txt
%license LICENSE.dependencies
%doc README.md
%{_bindir}/typst-lsp


%changelog
* Sat Feb 17 2024 rusty-snake - 0.12.1-1
- Initial typst-lsp spec
