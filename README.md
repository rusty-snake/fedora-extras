fedora-extras
=============

Additional package for Fedora, missing in the offical repositories and RPMFusion.

Currently this are:
- brave-browser-bin [abandoned; should still work]
- bubblejail
- gVisor-bin [abandoned]
- hardened_malloc
- libaslrmalloc [abandoned]
- scurl
- typos-lsp
- typst
- typst-lsp

Getting started
---------------

1. Install the necessary programs to build rpms on your system.

```bash
sudo dnf install rpm-build rpmdevtools rpmlint
```

2. Build the package you.

```bash
./rpmbuild.sh [OPTIONS] <PACKAGE>
```

Where `<PACKAGE>` is the name of a directory containing a specfile named `$PACKAGE.spec` and `setup_source.sh` (optional).

`[OPTIONS]` can be `-l` (run `rpmlint`), `-n` (add `--nodeps` to `rpmbuild`) and `-s` (run unsandboxed).

3. Install the package

```bash
sudo dnf install ./<PACKAGE>.rpm
```

Documentation
-------------

 - <https://rpm-packaging-guide.github.io/#setup>
 - <https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch09s04.html#id796983>
 - <https://rpm-software-management.github.io/rpm/manual/autosetup.html>
