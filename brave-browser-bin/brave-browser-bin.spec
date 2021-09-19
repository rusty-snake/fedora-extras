Name:           brave-browser-bin
Version:        @VERSION@
Release:        1%{?dist}
Summary:        Brave Browser (binary release)

License:        MPLv2.0
URL:            https://brave.com/
Source0:        https://github.com/brave/brave-browser/releases/download/v%{version}/brave-browser-%{version}-linux-amd64.zip
Source1:        brave-browser.desktop
Source2:        brave-browser-launcher

ExclusiveArch:  x86_64


%description
A browser with your interests at heart.

Browse faster by blocking ads and trackers
that violate your privacy and cost you time and money.


%prep
%autosetup -c -n %{name}-%{version}/brave


%build


%install
cd ..

mkdir -m 0755 -p %{buildroot}/opt %{buildroot}%{_bindir}
cp -a brave %{buildroot}/opt/brave
ln -s /opt/brave/brave-browser %{buildroot}%{_bindir}/brave-browser

install -Dm0755 %{SOURCE2} %{buildroot}%{_bindir}/brave-browser-launcher
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/brave-browser.desktop
install -Dm0644 brave/product_logo_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/brave-browser.png
install -Dm0644 brave/product_logo_24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/brave-browser.png
install -Dm0644 brave/product_logo_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/brave-browser.png
install -Dm0644 brave/product_logo_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/brave-browser.png
install -Dm0644 brave/product_logo_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/brave-browser.png
install -Dm0644 brave/product_logo_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/brave-browser.png
install -Dm0644 brave/product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/brave-browser.png


%files
%license LICENSE
/opt/brave
%_bindir/brave-browser
%_bindir/brave-browser-launcher
%_datadir/applications/brave-browser.desktop
%_datadir/icons/hicolor/*/apps/brave-browser.png


%changelog
* Sun Sep 19 2021 rusty-snake
- Initial brave-browser-bin spec
