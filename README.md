# Mk4tcl-spec

openSUSE Metakit for Tcl extension (Mk4tcl) RPM spec  

[Metakit](http://equi4.com/metakit/) is an embeddable database which runs on Unix, Windows, Macintosh, and other platforms.

Metakit source code repository:
[https://git.jeelabs.org/jcw/metakit](https://git.jeelabs.org/jcw/metakit)

Metakit provides C++, Python and Tcl interface. However, I only need Metakit for Tcl extension (Mk4tcl).
So I created this RPM spec to create a Mk4tcl RPM file.

And remove install-doc at Maakefile.in (for RPM build).

