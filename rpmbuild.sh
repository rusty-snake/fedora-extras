#!/bin/bash

set -e

shopt -s nullglob

cd -P -- "$(readlink -e "$(dirname "$0")")"

REQUIRED_PROGRAMS=(rpmbuild rpmlint spectool)
for program in "${REQUIRED_PROGRAMS[@]}"; do
	if ! command -v $program >&-; then
		exit 5
	fi
done

PACKAGE="$1"

TOPDIR="$(mktemp -dt rpmbuild.sh-XXXXXX)"
# shellcheck disable=SC2064
trap "rm -rf '$TOPDIR'" EXIT

BUILDDIR=$(rpm --define "_topdir $TOPDIR" --eval %_builddir)
RPMDIR=$(rpm --define "_topdir $TOPDIR" --eval %_rpmdir)
SOURCEDIR=$(rpm --define "_topdir $TOPDIR" --eval %_sourcedir)
SPECDIR=$(rpm --define "_topdir $TOPDIR" --eval %_specdir)
SRPMDIR=$(rpm --define "_topdir $TOPDIR" --eval %_srcrpmdir)
mkdir -p "$BUILDDIR" "$RPMDIR" "$SOURCEDIR" "$SPECDIR" "$SRPMDIR"

cp "$PACKAGE/$PACKAGE.spec" "$SPECDIR/$PACKAGE.spec"
(cd "$PACKAGE" && ls && source ./setup_sourcedir.sh)

rpmbuild --nodebuginfo --define "_topdir $TOPDIR" -bb "$SPECDIR/$PACKAGE.spec"

if [[ -n "$2" ]]; then
	echo ""
	echo "==========="
	echo "= rpmlint ="
	echo "==========="
	echo ""
	rpmlint -i "$SPECDIR"/*.spec "$RPMDIR"/*/*.rpm "$SRPMDIR"/*.rpm ||:
fi

cp "$RPMDIR"/*/*.rpm "$SRPMDIR"/*.rpm .
