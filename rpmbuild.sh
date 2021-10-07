#!/bin/bash

set -e

shopt -s nullglob

cd -P -- "$(readlink -e "$(dirname "$0")")"

REQUIRED_PROGRAMS=(rpmbuild rpmlint spectool)
for program in "${REQUIRED_PROGRAMS[@]}"; do
	if ! command -v $program >&-; then
		echo "rpmbuild.sh: Please install $program: sudo dnf install \"\$(dnf repoquery --whatprovides /usr/bin/\"$package\" 2>/dev/null)\""
		exit 5
	fi
done

while getopts "lns" opt; do
	case $opt in
		l)
			RBS_LINT=true
		;;
		n)
			RBS_NODEPS=true
		;;
		s)
			RBS_NOSANDBOX=true
		;;
		*)
			exit 2
		;;
	esac
done

PACKAGE="${!OPTIND}"

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
(cd "$PACKAGE" && source ./setup_sourcedir.sh)

BWRAP_ARGS=(
	--die-with-parent
	--unshare-all
	--new-session
	--cap-drop all
	--proc /proc
	--dev /dev
	--ro-bind /usr /usr
	--symlink /usr/bin /bin
	--symlink /usr/lib /lib
	--symlink /usr/lib64 /lib64
	--symlink /usr/sbin /sbin
	--tmpfs /tmp
	--ro-bind-try /etc/alternatives /etc/alternatives
	--ro-bind-try /etc/dnf /etc/dnf
	--ro-bind-try /etc/rpm /etc/rpm
	--ro-bind-try /etc/rpmrc /etc/rpmrc
	--ro-bind-try /etc/yum.repos.d /etc/yum.repos.d
	--ro-bind-try /var/cache/dnf /var/cache/dnf
	--ro-bind-try /var/lib/dnf /var/lib/dnf
	--ro-bind-try /var/lib/rpm /var/lib/rpm
	--tmpfs /var/tmp
	--bind "$TOPDIR" "$TOPDIR"
)
RPMBUILD_ARGS=(
	--nodebuginfo
	--define "_topdir $TOPDIR"
)

if [[ -n "$RBS_NODEPS" ]]; then
	RPMBUILD_ARGS+=(--nodeps)
fi

echo ${RPMBUILD_ARGS[@]}

if [[ -n "$RBS_NOSANDBOX" ]]; then
	rpmbuild "${RPMBUILD_ARGS[@]}" -bb "$SPECDIR/$PACKAGE.spec"
else
	bwrap "${BWRAP_ARGS[@]}" -- rpmbuild "${RPMBUILD_ARGS[@]}" -bb "$SPECDIR/$PACKAGE.spec"
fi

if [[ -n "$RBS_LINT" ]]; then
	echo ""
	echo "==========="
	echo "= rpmlint ="
	echo "==========="
	echo ""
	rpmlint -i "$SPECDIR"/*.spec "$RPMDIR"/*/*.rpm "$SRPMDIR"/*.rpm ||:
fi

cp "$RPMDIR"/*/*.rpm "$SRPMDIR"/*.rpm .
