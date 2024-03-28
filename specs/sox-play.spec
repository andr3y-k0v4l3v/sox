Summary: A general purpose sound file conversion tool
#Summary(ru_RU.KOI8-R): Универсальный проигрыватель и конвертер звуковых файлов.
License: GPLv2+ and LGPLv2+ and MIT
Group: Sound
BuildArch: noarch

Requires: sox-base = %version-%release
Requires: libsox-fmt-oss = %version-%release
Requires: libsox-fmt-alsa = %version-%release
Requires: libsox-fmt-vorbis = %version-%release
#Requires: libsox-fmt-sndfile = %version-%release

%description
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.

Install the %name package if you'd like to convert sound file formats
or manipulate some sounds.

%files
