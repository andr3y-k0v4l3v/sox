Summary: A general purpose sound file conversion tool
#Summary(ru_RU.KOI8-R): Универсальный проигрыватель и конвертер звуковых файлов.
License: GPLv2+ and LGPLv2+ and MIT
Group: Sound

Conflicts: sox < %version-%release

%description
SoX (Sound eXchange) is a sound file format converter for Linux,
UNIX and DOS PCs. The self-described 'Swiss Army knife of sound
tools,' SoX can convert between many different digitized sound
formats and perform simple sound manipulation functions,
including sound effects.

Install the %name package if you'd like to convert sound file formats
or manipulate some sounds.

%files
%_bindir/*
%_man1dir/sox.*
%_man1dir/play.*
%_man1dir/rec.*
%_man1dir/soxi.*
%_man7dir/*
