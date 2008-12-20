Name:           kino
Version:        1.3.2
Release:        3%{?dist}
Summary:        Kino is a non-linear DV editor for GNU/Linux

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.kinodv.org
Source0:        http://dl.sf.net/kino/kino-%{version}.tar.gz
Patch0:         %{name}-udev.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel 
BuildRequires: libraw1394-devel
BuildRequires: libavc1394-devel
BuildRequires: libiec61883-devel
BuildRequires: libdv-devel >= 0.102
BuildRequires: libXv-devel
BuildRequires: libbonoboui-devel
BuildRequires: libquicktime-devel
BuildRequires: ffmpeg-devel
BuildRequires: desktop-file-utils
BuildRequires: libsamplerate-devel
BuildRequires: zlib-devel
BuildRequires: gettext intltool
BuildRequires: perl(XML::Parser)

Requires: ffmpeg
Requires: mjpegtools
Requires: mencoder

%description
Kino is a non-linear DV editor for GNU/Linux. It features excellent
integration with IEEE 1394 for capture, VTR control, and recording
back to the camera. It captures video to disk in AVI format in both
type-1 DV and type-2 DV (separate audio stream) encodings.

%package        devel
Summary:        Files needed to build kino plugins
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
Files needed to build kino plugins

%prep
%setup -q
%patch0 -p1 -b .udev


%build
%configure --enable-quicktime --disable-local-ffmpeg \
           --disable-static \
           --disable-dependency-tracking \

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__make} install DESTDIR=${RPM_BUILD_ROOT}
%{__rm} ${RPM_BUILD_ROOT}%{_libdir}/kino-gtk2/*.la
ln -sf kino ${RPM_BUILD_ROOT}%{_bindir}/kino2raw
%{__rm} ${RPM_BUILD_ROOT}%{_datadir}/applications/Kino.desktop
ln -s Kino.desktop kino.desktop

%find_lang kino

desktop-file-install \
    --vendor=livna \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    --add-category=X-Livna \
    kino.desktop


%check
%{__make} check


%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files -f kino.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README* TODO
%{_bindir}/kino
%{_bindir}/kino2raw
%{_mandir}/man1/*
%{_datadir}/kino
%{_datadir}/applications/*kino.desktop
%{_datadir}/pixmaps/kino.png
%config(noreplace) %{_sysconfdir}/udev/rules.d/kino.rules
%{_datadir}/mime/packages/kino.xml
%{_libdir}/kino-gtk2

%files devel
%defattr(-,root,root,-)
%{_includedir}/kino

%changelog
* Sat Dec 20 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.3.2-3
- rebuild against new ffmpeg

* Sat Nov  1 2008 Dan Horák <dan at danny.cz> - 1.3.2-2
- remove dependency on esound and audiofile
- add dependency on mjpegtools and mencoder

* Mon Aug 25 2008 Dan Horák <dan at danny.cz> - 1.3.2-1
1.3.2

* Wed Aug 13 2008 Dan Horák <dan at danny.cz> - 1.3.1-1
1.3.1
- dropped upstream'd patches

* Mon Aug 11 2008 Dan Horák <dan at danny.cz> - 1.3.0-2
- fix build with new ffmpeg

* Mon Mar 03 2008 Dan Horák <dan at danny.cz> - 1.3.0-1
1.3.0
- dropped upstream'd patches

* Sun Jan 13 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.2.0-1
1.2.0
- fix build against libquicktime (patch by Dan Horák)
- fix building with gcc-4.3

* Sun Nov 25 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.1.1-3
- rebuilt

* Sun Aug 19 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.1.1-2
- require ffmpeg (needed for lots of functions)

* Wed Aug 08 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.1.1-1
1.1.1
- fix build (patch by Dan Horák)

* Tue Jun 19 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0.0-2
- fix up udev rules file
- remove redundant BR

* Thu Jun 07 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0.0-1
1.0.0
- adapt to upstream changes
- fix unowned dirs (#1457)
- fix kino2raw symlink
- drop kino.desktop, upstream ships a good desktop file

* Sun Feb  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9.5-2
- Rebuild.

* Tue Jan 16 2007 Dominik Mierzejewski <rpm at greysector.net> - 0.9.5-1
0.9.5-1
 - dropped upstreamed patches
 - URL update

* Wed Jan 03 2007 Dominik Mierzejewski <rpm at greysector.net> - 0.9.4-1
0.9.4-1
- patch for better plugin linking by Dan Horak
- patch to fix build with libswscale
- clean up BuildRequires
- don't build static libs

* Fri Dec 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.3-2
- Rebuild.

* Mon Nov 06 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.3-1
- version upgrade (#1257)
- plugins are now included the right way (#1193)

* Wed Oct 11 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.9.2-1
- version upgrade

* Thu Mar 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.8.0-2
- fix devel build (#795)

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Wed Jan 25 2006 Adrian Reber <adrian@lisas.de> - 0.8.0-0.lvn.1
- Updated to 0.8.0
- Dropped 0 Epoch
- Changes for modular X

* Tue Sep 27 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- finally fix #502

* Sat Jun 04 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info>
- send error output of lqt-config to /dev/null; fixes building with svn-to-srpm

* Mon May 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.6-0.lvn.2
- Fix #441

* Sun May 22 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.6-0.lvn.1
- Version upgrade
- Add libquicktime fixes and spec cleanups from Ville Skyttä (#437)

* Tue May 10 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.5-2.lvn.3
- Added missing buildrequires for gettext

* Mon May  9 2005 Dams <anvil[AT]livna.org> 
0:0.7.5-2.lvn.2
- Minor details corrections

* Tue Feb 15 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.5-2.lvn.1
- add libquicktime and ffmpeg
- add lvn tag

* Sun Feb 13 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.7.5-1
- drop fdr 
- minor beautifications

* Thu Nov 25 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.5-0.fdr.1
- Version upgrade (0.7.5)

* Tue Jul 27 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de
0:0.7.2-0.fdr.2
- added missing BuildRequires libsamplerate
- require libdv >= 0.102

* Tue Jul 27 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de
0:0.7.2-0.fdr.1
- Version upgrade (0.7.2)

* Mon May 31 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.fdr.1
- Version upgrade (0.7.1)

* Tue Dec 23 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- Initial RPM release.
