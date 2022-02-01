Name:           scala3-bin
Version:        3.1.0
Release:        1%{?dist}
Summary:        The Scala 3 compiler, also known as Dotty

License:        ASL 2.0
URL:            https://dotty.epfl.ch
Source0:        https://github.com/lampepfl/dotty/releases/download/%{version}/scala3-%{version}.tar.gz

BuildArch:      noarch


%description
The Scala 3 compiler, also known as Dotty


%prep
%autosetup -n scala3-%{version}


%build
rm bin/*.bat


%install
mkdir -m 0755 -p %{buildroot}/opt %{buildroot}%{_bindir}
cp -a . %{buildroot}/opt/scala3
ln -s /opt/scala3/bin/scala %{buildroot}%{_bindir}/scala
ln -s /opt/scala3/bin/scalac %{buildroot}%{_bindir}/scalac
ln -s /opt/scala3/bin/scaladoc %{buildroot}%{_bindir}/scaladoc


%files
%_bindir/scala
%_bindir/scalac
%_bindir/scaladoc
/opt/scala3


%changelog
* Tue Feb 1 2022 rusty-snake - 3.1.0-1
- Initial scala3-bin spec
