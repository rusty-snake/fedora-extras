Name:           typst
Version:        0.10.0
Release:        1%{?dist}
Summary:        A new markup-based typesetting system that is powerful and easy to learn.

License:        Apache-2.0
URL:            https://github.com/typst/typst
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24


%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.


%prep
%autosetup -p1
%{__cargo} vendor --versioned-dirs vendor/
%cargo_prep -v vendor/


%build
pushd crates/typst-cli
%cargo_build
popd
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
cd crates/typst-cli
%cargo_install


%files
%license LICENSE
%license NOTICE
%license LICENSE.dependencies
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/typst


%changelog
* Sat Feb 17 2024 rusty-snake - 0.10.0-1
- Initial typst spec
