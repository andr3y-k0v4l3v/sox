Requires: %name = %version-%release
Obsoletes: sox-devel
Summary: The SoX sound file format converter headers files and libraries
Group: Sound

%description
This package contains the headers and library needed for compiling
applications which will use the SoX sound file format converter.

Install %name-devel if you want to develop applications which will use SoX.

%files
%_libdir/sox/*.a
%exclude %_libdir/sox/*.la
