Name:           typst-lsp
Version:        0.13.0
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
cat >> .cargo/config << EOF
[source."git+https://github.com/astrale-sharp/typstfmt?tag=0.2.7"]
git = "https://github.com/astrale-sharp/typstfmt"
tag = "0.2.7"
replace-with = "vendored-sources"

[source."git+https://github.com/typst/typst.git?tag=v0.7.0"]
git = "https://github.com/typst/typst.git"
tag = "v0.7.0"
replace-with = "vendored-sources"

EOF


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
* Thu Mar 21 2024 rusty-snake - 0.13.0-1
- typst-lsp 0.13.0

* Sat Feb 17 2024 rusty-snake - 0.12.1-1
- Initial typst-lsp spec
