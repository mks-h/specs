Name:           flood
Version:        4.9.5
Release:        %autorelease
Summary:        A modern web UI for various torrent clients with a Node.js backend and React frontend

License:        GPL-3.0-only
URL:            https://flood.js.org/
Source0:        https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} nodejs

Requires:       nodejs

%description
Flood is a monitoring service for various torrent clients. It's a Node.js
service that communicates with your favorite torrent client and serves a decent
web UI for administration.

%prep
%setup -q -n package/


%build


%install
install -m 0755 -vd %{buildroot}/%{_datadir}/%{name}
cp -r %{_builddir}/package/dist/assets %{buildroot}/%{_datadir}/%{name}/
install -m 0755 -vD %{_builddir}/package/dist/index.js %{buildroot}/%{_bindir}/%{name}

%check

%files
%{_datadir}/%{name}/
%{_bindir}/%{name}

%changelog
* Tue Jun 10 2025 Maksym Hazevych <mhazevych@proton.me> - 4.9.5-1
- Initial package
