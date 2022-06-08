Name:           bubblejail
Version:        0.6.1
Release:        1%{?dist}
Summary:        Bubblewrap based sandboxing for desktop applications

License:        GPLv3+
URL:            https://github.com/igo95862/bubblejail
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  m4
BuildRequires:  python3-sphinx
Requires:       python3 >= 3.9
Requires:       python3-pyxdg
Requires:       python3-tomli
Requires:       python3-tomli-w
Requires:       bubblewrap >= 0.5.0
Requires:       xdg-dbus-proxy
Requires:       python3-qt5-base
Requires:       libseccomp
Recommends:     desktop-file-utils
Recommends:     libnotify
Suggests:       bash-completion
Suggests:       fish


%description
Bubblejail is a bubblewrap-based alternative to Firejail.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


# bubblejail's testsuit tries to access files
# in $HOME and fails if they don't exist.
#%%check
#%%meson_test


%files
%license COPYING
%doc README.md docs/breaking_changes.md
%_bindir/bubblejail
%_bindir/bubblejail-config
%_libdir/bubblejail
%_datadir/applications/bubblejail-config.desktop
%_datadir/bash-completion/completions/bubblejail
%_datadir/bubblejail
%_datadir/fish/vendor_completions.d/bubblejail.fish
%_datadir/icons/hicolor/48x48/apps/bubblejail-config.png
%_datadir/icons/hicolor/scalable/apps/bubblejail-config.svg
%_mandir/man1/bubblejail.1.gz


%changelog
* Wed Jun 08 2022 rusty-snake - 0.6.1-1
- Update to 0.6.1

* Mon May 23 2022 rusty-snake - 0.6.0-1
- Update to 0.6.0

* Thu Apr 19 2022 rusty-snake - 0.5.3-1
- Update to 0.5.3

* Wed Apr 06 2022 rusty-snake - 0.5.2-1
- Update to 0.5.2

* Sun Feb 13 2022 rusty-snake - 0.5.1-1
- Update to 0.5.1

* Mon Jan 31 2022 rusty-snake - 0.5.0-1
- Update to 0.5.0

* Mon Oct 11 2021 rusty-snake - 0.4.2-1
- Initial bubblejail spec
