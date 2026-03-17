%global spaversion 0.2
%global __meson_auto_features disabled

Name:       pipewire-libs-extra
Summary:    PipeWire extra plugins
Version:    1.6.2
Release:    1%{?dist}
License:    MIT
URL:        https://pipewire.org/

Source0:    https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz
# Update to LC3plus 1.8.0 APIs
Patch0:     pipewire-lc3plus-api.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  meson >= 0.49.0
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  liblc3plus-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(bluez) >= 4.101
BuildRequires:  pkgconfig(libfreeaptx)
BuildRequires:  pkgconfig(glib-2.0)
#BuildRequires:  pkgconfig(ldacBT-dec)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  sbc-devel

Requires:       pipewire >= %{version}

%description
PipeWire media server Bluetooth aptX codec plugin.

%prep
%autosetup -p1 -n pipewire-%{version}

%build
%meson \
  -D examples=disabled \
  -D bluez5=enabled \
  -D bluez5-codec-aptx=enabled \
  -D bluez5-codec-ldac-dec=disabled \
  -D bluez5-codec-lc3plus=enabled \
  -D ffmpeg=enabled \
  -D lv2=enabled \
  -D session-managers=[]

%meson_build \
    spa-codec-bluez5-aptx \
    spa-codec-bluez5-lc3plus \
    spa-ffmpeg

%install
install -pm 0755 -D %{_vpath_builddir}/spa/plugins/bluez5/libspa-codec-bluez5-aptx.so \
    %{buildroot}%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-aptx.so
install -pm 0755 -D %{_vpath_builddir}/spa/plugins/bluez5/libspa-codec-bluez5-lc3plus.so \
    %{buildroot}%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-lc3plus.so
install -pm 0755 -D %{_vpath_builddir}/spa/plugins/ffmpeg/libspa-ffmpeg.so \
    %{buildroot}%{_libdir}/spa-%{spaversion}/ffmpeg/libspa-ffmpeg.so

%files
%license COPYING
%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-aptx.so
%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-lc3plus.so
%dir %{_libdir}/spa-%{spaversion}/ffmpeg
%{_libdir}/spa-%{spaversion}/ffmpeg/libspa-ffmpeg.so

%changelog
* Tue Mar 17 2026 Simone Caronni <negativo17@gmail.com> - 1.6.2-1
- Update to 1.6.2.
- Re-enable LC3plus with a patch for the new API.

* Sat Feb 14 2026 Simone Caronni <negativo17@gmail.com> - 1.5.85-1
- Update to 1.5.85.

* Sun Jan 18 2026 Simone Caronni <negativo17@gmail.com> - 1.4.10-1
- Update to 1.4.10.

* Wed Oct 15 2025 Simone Caronni <negativo17@gmail.com> - 1.4.9-1
- Update to 1.4.9.

* Wed Sep 17 2025 Simone Caronni <negativo17@gmail.com> - 1.4.8-1
- Update to 1.4.8.

* Thu Jul 24 2025 Simone Caronni <negativo17@gmail.com> - 1.4.7-1
- Update to 1.4.7.

* Tue Jul 01 2025 Simone Caronni <negativo17@gmail.com> - 1.4.6-1
- Update to 1.4.6.

* Mon Jun 09 2025 Simone Caronni <negativo17@gmail.com> - 1.4.5-1
- Update to 1.4.5.

* Thu Mar 27 2025 Simone Caronni <negativo17@gmail.com> - 1.4.1-2
- Drop ebur128 support again.

* Wed Mar 26 2025 Simone Caronni <negativo17@gmail.com> - 1.4.1-1
- Update to 1.4.1.
- Enable ebur128.

* Wed Mar 26 2025 Simone Caronni <negativo17@gmail.com> - 1.2.7-2
- Make lc3plus conditional, does not currently build with version 1.5.1.

* Wed Nov 27 2024 Simone Caronni <negativo17@gmail.com> - 1.2.7-1
- Update to 1.2.7.

* Mon Oct 28 2024 Simone Caronni <negativo17@gmail.com> - 1.2.6-1
- Update to 1.2.6.

* Tue Oct 01 2024 Simone Caronni <negativo17@gmail.com> - 1.2.5-1
- Update to 1.2.5.
- Trim changelog.

* Tue Sep 24 2024 Simone Caronni <negativo17@gmail.com> - 1.0.8-1
- Update to 1.0.8.

* Mon May 27 2024 Simone Caronni <negativo17@gmail.com> - 1.0.7-1
- Update to 1.0.7.

* Mon May 13 2024 Simone Caronni <negativo17@gmail.com> - 1.0.6-1
- Update to 1.0.6.

* Sat Apr 27 2024 Simone Caronni <negativo17@gmail.com> - 1.0.5-1
- Update to 1.0.5.

* Fri Mar 15 2024 Simone Caronni <negativo17@gmail.com> - 1.0.4-1
- Update to 1.0.4.

* Mon Feb 05 2024 Simone Caronni <negativo17@gmail.com> - 1.0.3-1
- Update to 1.0.3.
- Enable LC3plus support.

* Wed Jan 31 2024 Simone Caronni <negativo17@gmail.com> - 1.0.2-1
- Update to 1.0.2.

* Mon Jan 15 2024 Simone Caronni <negativo17@gmail.com> - 1.0.1-1
- Update to 1.0.1.
