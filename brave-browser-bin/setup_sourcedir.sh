# Credits go to https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=brave-bin
VERSION="$(curl -s https://brave-browser-downloads.s3.brave.com/latest/release.version)"
[[ $VERSION =~ ^1\.[0-9]+\.[0-9]+$ ]] || exit 10
sed -i "s/@VERSION@/$VERSION/" "$SPECDIR"/brave-browser-bin.spec

spectool -C "$SOURCEDIR" --gf "$SPECDIR"/brave-browser-bin.spec
cp brave-browser.desktop "$SOURCEDIR"
cp brave-browser-launcher "$SOURCEDIR"
