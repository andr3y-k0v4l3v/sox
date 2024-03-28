%def_with pulse

Name: sox
Version: 14.4.2
Release: alt4

Summary: A general purpose sound file conversion tool
#Summary(ru_RU.KOI8-R): Универсальный проигрыватель и конвертер звуковых файлов.
License: GPLv2+ and LGPLv2+ and MIT
Group: Sound

Packager: Denis Smirnov <mithraen@altlinux.org>

Url: http://%name.sourceforge.net/
Source: %name-%version.tar
Source1: soxeffect
Patch: %name.dyn.patch

Requires: sox-play = %version-%release
Requires: sox-base = %version-%release
Requires: libsox-fmt-alsa = %version-%release
Requires: libsox-fmt-ao = %version-%release
Requires: libsox-fmt-caf = %version-%release
Requires: libsox-fmt-fap = %version-%release
Requires: libsox-fmt-flac = %version-%release
Requires: libsox-fmt-gsm = %version-%release
Requires: libsox-fmt-lpc10 = %version-%release
Requires: libsox-fmt-mat4 = %version-%release
Requires: libsox-fmt-mat5 = %version-%release
Requires: libsox-fmt-mp3 = %version-%release
Requires: libsox-fmt-oss = %version-%release
Requires: libsox-fmt-opus = %version-%release
Requires: libsox-fmt-paf = %version-%release
%if_with pulse
Requires: libsox-fmt-pulseaudio = %version-%release
%endif
Requires: libsox-fmt-pvf = %version-%release
Requires: libsox-fmt-sd2 = %version-%release
Requires: libsox-fmt-sndfile = %version-%release
Requires: libsox-fmt-vorbis = %version-%release
Requires: libsox-fmt-w64 = %version-%release
Requires: libsox-fmt-wavpack = %version-%release
Requires: libsox-fmt-xi = %version-%release
Requires: libsox-fmt-caf = %version-%release
Requires: libsox-fmt-fap = %version-%release

# Automatically added by buildreq on Thu Feb 26 2015
# optimized out: gnu-config libogg-devel libopencore-amrnb0 libopencore-amrwb0 libopus-devel libssl-devel pkg-config zlib-devel
BuildRequires: glibc-devel-static libalsa-devel libao-devel libflac-devel libgomp-devel libgsm-devel libid3tag-devel liblame-devel libltdl7-devel libmad-devel libmagic-devel libopencore-amrnb-devel libopencore-amrwb-devel libopusfile-devel libpng-devel libsndfile-devel libvorbis-devel libwavpack-devel
%{?_with_pulse:BuildRequires: libpulseaudio-devel}

%description
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.

Install the %name package if you'd like to convert sound file formats
or manipulate some sounds.

#%description -l ru_RU.KOI8-R
#SOX - консольная программа для преобразования, записи и проигрывания
#звуковых файлов, поддерживает множество форматов.

%prep
%setup
%patch -p2
sed -i 's,\-I/lib/modules/`uname -r`/build/include,,' configure*
%ifarch %e2k
# still unsupported as of lcc 1.21.24
sed -i 's,-Wtraditional-conversion,,' configure*
%endif

%build
%autoreconf
%configure \
           --with-dyn-default \
           --enable-dl-amrnb \
           --enable-dl-amrwb \
           --enable-dl-sndfile

%make_build

%install
%makeinstall install

install %SOURCE1 %buildroot%_bindir/soxeffect
sed -i 's,\(/usr/\)local/,\1,' %buildroot%_bindir/soxeffect

rm -f %buildroot%_bindir/rec
ln -s play %buildroot%_bindir/rec

cat << EOF >%buildroot%_bindir/%{name}play
#!/bin/sh
%_bindir/%name \$1 -t .au - >/dev/audio
EOF
chmod 755 %buildroot%_bindir/%{name}play

%files
%doc ChangeLog README

%changelog
* Sat Dec 26 2020 Dmitry V. Levin <ldv@altlinux.org> 14.4.2-alt4
- NMU.
- spec: fixed License tag.
- spec: removed bogus "%%set_automake_version 1.14".

* Fri Mar 01 2019 Dmitry V. Levin <ldv@altlinux.org> 14.4.2-alt3
- NMU: removed bogus Provides from libsox3.

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 14.4.2-alt2
- E2K: avoid lcc-unsupported option properly

* Wed Mar 15 2017 Michael Shigorin <mike@altlinux.org> 14.4.2-alt1.1
- BOOTSTRAP: introduce pulse knob (on by default)

* Thu Feb 26 2015 Denis Smirnov <mithraen@altlinux.ru> 14.4.2-alt1
- 14.4.2

* Tue Jan 21 2014 Denis Smirnov <mithraen@altlinux.ru> 14.4.1-alt2
- disable build ffmpeg module by default

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.4.1-alt1.1
- Fixed build

* Wed Feb 20 2013 Denis Smirnov <mithraen@altlinux.ru> 14.4.1-alt1
- 14.4.1

* Fri Oct 12 2012 Denis Smirnov <mithraen@altlinux.ru> 14.4.0-alt1
- 14.4.0

* Wed May 23 2012 Denis Smirnov <mithraen@altlinux.ru> 14.3.2-alt2
- fix build
- build more subpackages
- some cleanups

* Fri Aug 12 2011 Denis Smirnov <mithraen@altlinux.ru> 14.3.2-alt1
- 14.3.2

* Mon Jan 17 2011 Denis Smirnov <mithraen@altlinux.ru> 14.3.1-alt2
- fix package %_libdir/sox

* Wed Nov 17 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.1-alt1
- 14.3.1

* Fri May 07 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt5
- add Provides sox-devel to libsox-devel

* Sun Feb 21 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt4
- conflicts sox-base with sox < %%version-%%release (closes: #23001)

* Fri Jan 22 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt3
- reimport changes by ldv@ (closes: #21321)

* Tue Jan 19 2010 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt2
- add sox-play subpackage (ALT #21728)

* Wed Sep 02 2009 Dmitry V. Levin <ldv@altlinux.org> 14.3.0-alt1.1
- NMU.
- Moved %%_pkgconfigdir/* files to -devel subpackage (closes: #21321).

* Wed Jul 01 2009 Denis Smirnov <mithraen@altlinux.ru> 14.3.0-alt1
- update to 14.3.0
- move additional formats to subpackages

* Tue Feb 10 2009 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt4
- fix build with new ffmpeg (thanks to shrek@)

* Sun Aug 10 2008 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt3
- fix build in hasher
- spec cleanup

* Tue Apr 01 2008 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt2
- move devel to separate package

* Sun Feb 03 2008 Denis Smirnov <mithraen@altlinux.ru> 14.0.1-alt1
- Update to 14.0.1

* Sun Oct 07 2007 Denis Smirnov <mithraen@altlinux.ru> 13.0.0-alt3
- fix typo in Packager field

* Tue Apr 24 2007 Denis Smirnov <mithraen@altlinux.ru> 13.0.0-alt2
- add requires sox-devel -> sox (fix #11602)

* Fri Feb 16 2007 Denis Smirnov <mithraen@altlinux.ru> 13.0.0-alt1
- 13.0.0
- multiple changes, that affects scripts that used sox!
  Please see changelog for  details
- build dynamic libst (and don't build static)

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 12.18.2-alt2
- build with external libgsm

* Sat Oct 14 2006 Denis Smirnov <mithraen@altlinux.ru> 12.18.2-alt1
- 12.18.2

* Wed May 03 2006 Denis Smirnov <mithraen@altlinux.ru> 12.17.9-alt1
- 12.17.9

* Tue Dec 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 12.17.7-alt1
- 12.17.7

* Thu Oct 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 12.17.6-alt1
- 12.17.6

* Mon Sep 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 12.17.5-alt1
- new version.
- security fix for previous release applied in upstream.

* Mon Aug 02 2004 Stanislav Ievlev <inger@altlinux.org> 12.17.4-alt1.1
- NMU: security fix

* Tue Mar 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 12.17.4-alt1
- new version.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 12.17.3-alt2
- Rebuild with gcc-3.2.
- Alsa dsp support disabled.

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 12.17.3-alt1.1
- rebuild with new vorbis

* Mon Dec 17 2001 Yuri N. Sedunov <aris@altlinux.ru> 12.17.3-alt1
- Updated to 12.7.3, major fix in the spec.

* Wed Dec 12 2001 Yuri N. Sedunov <aris@altlinux.ru> 12.17.2-alt1
- Updated to 12.7.2, built with gsmlib.

* Wed Apr 10 2001 Rider <rider@altlinux.ru> 12.17.1-alt1
- 12.17.1

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 12.17-ipl1mdk
- RE adaptions.

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 12.17-1mdk
- new and shiny version.
- fix the build.

* Wed Aug 30 2000 Enzo Maggi <enzo@mandrakesoft.com> 12.16-9mdk
- minor fix in the spec

* Tue Aug 29 2000 Enzo Maggi <enzo@mandrakesoft.com> 12.16-8mdk
- simplified the installation

* Mon Aug 28 2000 Enzo Maggi <enzo@mandrakesoft.com> 12.16-7mdk
- fixed installation directories

* Fri Apr 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 12.16-6mdk
- fixed groups

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix dangling symlinks (use rpmlint luke).

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP check/build

* Sat Aug 07 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- -DHAVE_SYS_SOUNDCARD_H=1, cause configure is slightly broken

* Thu Jul 22 1999 Gregus <gregus@etudiant.net>
- fr locale

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- A new life for the spec file :).
- 12.16.
- Removed obsoletes patchs.

* Tue Jun 01 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Cleanup from Mandrake adaptions

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Jan 20 1999 Bill Nottingham <notting@redhat.com>
- allow spaces in filenames for play/rec

* Wed Dec  9 1998 Bill Nottingham <notting@redhat.com>
- fix docs

* Mon Nov 23 1998 Bill Nottingham <notting@redhat.com>
- update to 12.15

* Sat Oct 10 1998 Michael Maher <mike@redhat.com>
- fixed broken spec file

* Mon Jul 13 1998 Michael Maher <mike@redhat.com>
- updated source from Chris Bagwell.

* Wed Jun 23 1998 Michael Maher <mike@redhat.com>
- made patch to fix the '-e' option. BUG 580
- added buildroot

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Nov 06 1997 Erik Troan <ewt@redhat.com>
- built against glibc
