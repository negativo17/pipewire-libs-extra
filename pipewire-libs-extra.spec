%global spaversion 0.2
%global __meson_auto_features disabled

Name:       pipewire-libs-extra
Summary:    PipeWire extra plugins
Version:    1.0.8
Release:    1%{?dist}
License:    MIT
URL:        https://pipewire.org/

Source0:    https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  meson >= 0.49.0
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  liblc3plus-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(bluez) >= 4.101
BuildRequires:  pkgconfig(libfreeaptx)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libavcodec)
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
  -D bluez5-codec-lc3plus=enabled \
  -D ffmpeg=enabled \
  -D session-managers=[]

%meson_build spa-codec-bluez5-aptx spa-ffmpeg

%install
install -pm 0755 -D %{_vpath_builddir}/spa/plugins/bluez5/libspa-codec-bluez5-aptx.so \
   %{buildroot}%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-aptx.so
install -pm 0755 -D %{_vpath_builddir}/spa/plugins/ffmpeg/libspa-ffmpeg.so \
   %{buildroot}%{_libdir}/spa-%{spaversion}/ffmpeg/libspa-ffmpeg.so

%files
%license COPYING
%{_libdir}/spa-%{spaversion}/bluez5/libspa-codec-bluez5-aptx.so
%{_libdir}/spa-%{spaversion}/ffmpeg

%changelog
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

* Mon Dec 04 2023 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Fri Nov 10 2023 Simone Caronni <negativo17@gmail.com> - 0.3.84-1
- Update to 0.3.84.

* Tue Oct 17 2023 Simone Caronni <negativo17@gmail.com> - 0.3.82-1
- Update to 0.3.82.

* Fri Sep 22 2023 Simone Caronni <negativo17@gmail.com> - 0.3.80-1
- Update to 0.3.80.

* Wed Aug 23 2023 Simone Caronni <negativo17@gmail.com> - 0.3.78-1
- Update to 0.3.78.

* Mon Aug 07 2023 Simone Caronni <negativo17@gmail.com> - 0.3.77-1
- Update to 0.3.77.

* Wed Jun 28 2023 Simone Caronni <negativo17@gmail.com> - 0.3.72-1
- Update to 0.3.72.

* Thu May 11 2023 Simone Caronni <negativo17@gmail.com> - 0.3.70-1
- Update to 0.3.70.

* Wed Apr 12 2023 Simone Caronni <negativo17@gmail.com> - 0.3.68-1
- Update to 0.3.68.

* Thu Mar 16 2023 Simone Caronni <negativo17@gmail.com> - 0.3.67-1
- Update to 0.3.67.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 0.3.64-1
- Update to 0.3.64.

* Tue Dec 20 2022 Simone Caronni <negativo17@gmail.com> - 0.3.63-1
- Update to 0.3.63.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 0.3.62-1
- Update to 0.3.62.

* Mon Nov 28 2022 Simone Caronni <negativo17@gmail.com> - 0.3.61-1
- Update to 0.3.61.

* Mon Nov 21 2022 Simone Caronni <negativo17@gmail.com> - 0.3.60-1
- Update to 0.3.60.

* Tue Oct 11 2022 Simone Caronni <negativo17@gmail.com> - 0.3.59-1
- Update to 0.3.59.

* Sat Sep 17 2022 Simone Caronni <negativo17@gmail.com> - 0.3.58-1
- Update to 0.3.58.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 0.3.57-1
- Update to 0.3.57.

* Tue Jul 05 2022 Simone Caronni <negativo17@gmail.com> - 0.3.53-1
- Update to 0.3.53.

* Fri Jun 17 2022 Simone Caronni <negativo17@gmail.com> - 0.3.52-1
- Update to 0.3.52.

* Tue May 03 2022 Simone Caronni <negativo17@gmail.com> - 0.3.51-1
- Update to 0.3.51.

* Wed Apr 06 2022 Simone Caronni <negativo17@gmail.com> - 0.3.49-1
- Update to 0.3.49.

* Fri Mar 11 2022 Simone Caronni <negativo17@gmail.com> - 0.3.48-1
- Update to 0.3.48.

* Sun Feb 06 2022 Simone Caronni <negativo17@gmail.com> - 0.3.45-1
- Update to 0.3.45.

* Fri Jan 21 2022 Simone Caronni <negativo17@gmail.com> - 0.3.43-1
- Update to 0.3.43.

* Mon Dec 13 2021 Simone Caronni <negativo17@gmail.com> - 0.3.40-1
- Update to 0.3.40.

* Fri Oct 29 2021 Simone Caronni <negativo17@gmail.com> - 0.3.39-1
- Update to 0.3.39.

* Fri Oct 01 2021 Simone Caronni <negativo17@gmail.com> - 0.3.38-1
- Update to 0.3.38.

* Thu Sep 23 2021 Simone Caronni <negativo17@gmail.com> - 0.3.36-1
- First build.
