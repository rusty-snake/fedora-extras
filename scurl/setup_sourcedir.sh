SOURCE_FILES=(
	scurl
	scurl-download
	scurl-tor
	scurl-tor.conf
	scurl.1.rst
	scurl-download.1.rst
	scurl-tor.1.rst
)
for file in "${SOURCE_FILES[@]}"; do
	cp "$file" "$SOURCEDIR/$file"
done
