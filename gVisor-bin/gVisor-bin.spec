Name:           gVisor-bin
Version:        20211101
Release:        1%{?dist}
Summary:        Application Kernel for Containers

License:        ASL 2.0
URL:            https://gvisor.dev/
Source0:        https://storage.googleapis.com/gvisor/releases/release/%{version}/x86_64/runsc
Source1:        https://storage.googleapis.com/gvisor/releases/release/%{version}/x86_64/runsc.sha512
Source2:        https://storage.googleapis.com/gvisor/releases/release/%{version}/x86_64/containerd-shim-runsc-v1
Source3:        https://storage.googleapis.com/gvisor/releases/release/%{version}/x86_64/containerd-shim-runsc-v1.sha512

ExclusiveArch:  x86_64


%description
gVisor is an application kernel, written in Go, that implements a substantial
portion of the Linux system surface. It includes an Open Container Initiative
(OCI) runtime called runsc that provides an isolation boundary between the
application and the host kernel. The runsc runtime integrates with Docker and
Kubernetes, making it simple to run sandboxed containers.


%prep
%autosetup -c -T
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%build
sha512sum -c runsc.sha512 -c containerd-shim-runsc-v1.sha512


%install
install -Dm0755 -s -t %{buildroot}%{_bindir} runsc containerd-shim-runsc-v1


%files
%{_bindir}/runsc
%{_bindir}/containerd-shim-runsc-v1


%changelog
* Wed Nov 10 2021 rusty-snake - 20211101-1
- Initial gVisor spec
