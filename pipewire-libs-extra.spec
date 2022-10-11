%global spaversion 0.2
%global __meson_auto_features disabled

Name:       pipewire-libs-extra
Summary:    PipeWire extra plugins
Version:    0.3.59
Release:    1%{?dist}
License:    MIT
URL:        https://pipewire.org/

Source0:    https://gitlab.freedesktop.org/pipewire/pipewire/-/archive/%{version}/pipewire-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  meson >= 0.49.0
BuildRequires:  gcc-c++
BuildRequires:  git
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
