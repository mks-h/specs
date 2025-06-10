Name:           flood
Version:        4.9.5
Release:        %autorelease -b 2
Summary:        A modern web UI for various torrent clients with a Node.js backend and React frontend

License:        GPL-3.0-only
URL:            https://flood.js.org/
Source0:        https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/jesec/%{name}/refs/tags/v%{version}/distribution/shared/flood%40.service

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} nodejs

BuildRequires:  systemd-rpm-macros
Requires:       nodejs

%description
Flood is a monitoring service for various torrent clients. It's a Node.js
service that communicates with your favorite torrent client and serves a decent
web UI for administration.

%prep
%setup -q -b 0 -n package/


%build


%install
install -m 0755 -vd %{buildroot}/%{_datadir}/%{name}
cp -r %{_builddir}/package/dist/assets %{buildroot}/%{_datadir}/%{name}/
install -m 0755 -vD %{_builddir}/package/dist/index.js %{buildroot}/%{_bindir}/%{name}
install -m 0644 -vD %{SOURCE1} %{buildroot}/%{_unitdir}/flood@.service

%check

%files
%{_datadir}/%{name}/
%{_bindir}/%{name}
%config %{_unitdir}/flood@.service

%post
%systemd_post flood@.service

%preun
%systemd_preun flood@.service

%postun
%systemd_postun_with_restart flood@.service

%changelog
* Wed Jun 11 2025 Maksym Hazevych <mhazevych@proton.me> - 4.9.5-2
- Include systemd service template

* Tue Jun 10 2025 Maksym Hazevych <mhazevych@proton.me> - 4.9.5-1
- Initial package
