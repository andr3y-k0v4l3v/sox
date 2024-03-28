Requires: %name = %version-%release

Obsoletes: sox-devel < %version-%release
Provides:  sox-devel = %version-%release

Summary: The SoX sound file format converter headers files and libraries
Group: Sound

%description
This package contains the headers and library needed for compiling
applications which will use the SoX sound file format converter.

%files
%_includedir/*
%_libdir/libsox.so
%_pkgconfigdir/*.pc
%_man3dir/*
%exclude %_libdir/libsox.a
