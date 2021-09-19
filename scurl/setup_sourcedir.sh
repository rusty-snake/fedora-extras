SOURCE_FILES=(scurl scurl-download scurl.1.rst scurl-download.1.rst)
for file in "${SOURCE_FILES[@]}"; do
	cp "$file" "$SOURCEDIR/$file"
done
