Name:           typst
Version:        0.11.0
Release:        1%{?dist}
Summary:        A new markup-based typesetting system that is powerful and easy to learn

License:        Apache-2.0
URL:            https://github.com/typst/typst
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24


%description
Typst is a new markup-based typesetting system that is designed to be as
powerful as LaTeX while being much easier to learn and use.


%prep
%autosetup -p1
%{__cargo} vendor --versioned-dirs vendor/
%cargo_prep -v vendor/
cat >> .cargo/config << EOF
[source."git+https://github.com/typst/typst-dev-assets?tag=v0.11.0"]
git = "https://github.com/typst/typst-dev-assets"
tag = "v0.11.0"
replace-with = "vendored-sources"

EOF


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
* Thu Mar 21 2024 rusty-snake - 0.11.0-1
- typst 0.11.0
- fix some rpmlint reports

* Sat Feb 17 2024 rusty-snake - 0.10.0-1
- Initial typst spec
