%global spaversion 0.2
%global __meson_auto_features disabled

Name:       pipewire-libs-extra
Summary:    PipeWire extra plugins
Version:    1.2.5
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
