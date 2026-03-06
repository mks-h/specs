Name:           flood
Version:        4.13.0
Release:        2%dist
Summary:        A modern web UI for various torrent clients

License:        GPL-3.0-only AND MIT AND ISC AND BSD-3-Clause AND Unlicense 0BSD
URL:            https://flood.js.org/
Source0:        https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/jesec/%{name}/refs/tags/v%{version}/distribution/shared/flood%40.service
Source2:        %{name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} nodejs

BuildRequires:  systemd-rpm-macros
Requires:       nodejs
Recommends:     mediainfo

%description
Flood is a monitoring service for various torrent clients. It's a Node.js
service that communicates with your favorite torrent client and serves a decent
web UI for administration.

%prep
%setup -q -b 0 -n package/
cp %{SOURCE2} .


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
%{_unitdir}/flood@.service
%license LICENSE %{name}-%{version}-bundled-licenses.txt

%post
%systemd_post flood@.service

%preun
%systemd_preun flood@.service

%postun
%systemd_postun_with_restart flood@*.service

%changelog
* Sat Mar 7 2026 Maksym Hazevych <mhazevych@mailbox.org> - 4.13.0-2
- Include all required licensing information in the package

* Sun Feb 22 2026 Maksym Hazevych <mhazevych@mailbox.org> - 4.13.0-1
- Support info hash as a magnet link
- Support searching torrents by info hash
- Fix API when no authentication is used
- Fix sidebar toggle on desktop
- Update some UI strings
- Update IP geolocation database

* Wed Feb 11 2026 Maksym Hazevych <mhazevych@mailbox.org> - 4.12.6-1
- Update package summary
- Update IP geolocation database
- Fix: relax the schema to allow unknown field and fix setting schema

* Sun Feb 8 2026 Maksym Hazevych <mhazevych@mailbox.org> - 4.12.5-1
- Fix systemd services not restarting on package update
- Update dependencies
- rTorrent: ignore sequential download input when unsupported
- rTorrent: preserve extra files in directory when moving
- qBittorrent: set ETA to -1 when not downloading
- Add OpenAPI support

* Sat Dec 27 2025 Maksym Hazevych <mhazevych@mailbox.org> - 4.11.0-2
- Specify weak dependency on mediainfo

* Sun Oct 19 2025 Maksym Hazevych <mhazevych@mailbox.org> - 4.11.0-1
- Show size for status filter
- Fix: improve server startup message

* Sun Oct 19 2025 Maksym Hazevych <mhazevych@mailbox.org> - 4.10.0-1
- Add optional Last Activity column to torrent list
- Add units of measure to throttle speeds
- Show 2 decimal in size usage
- Fix: LoadingOverlay sometimes does not hide after login/logout
- Fix: log authentication failed reasons
- Update translations

* Wed Jun 11 2025 Maksym Hazevych <mhazevych@proton.me> - 4.9.5-2
- Include systemd service template

* Tue Jun 10 2025 Maksym Hazevych <mhazevych@proton.me> - 4.9.5-1
- Initial package
- Update translations
