# AMBuilder

AMBuilder is a CMake setup that builds the box models used by the AMBRS
Project in configurations of interest. Supported box models are:

* MAM4 (`mam4`)
* PartMC (`partmc`)
* a 1-moment sectional model from Jeff Pierce at Colorado State U (`mphys-driver`)

## Building and Installing the Models with CMake

To use CMake to build the box models and install them to a given location,
use the following commands:
```
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=<prefix> [options]
cd build
make
make install
```
The `CMAKE_INSTALL_PREFIX` option indicates that the models and supporting
libraries are installed to a folder with `bin/` and `lib/` subdirectories. You
should add `<prefix>/bin` to your `PATH` environment variable so you can
execute the installed models. For example, to run `partmc` after you've run
the above commands, you should be able to type

```
partmc
```

and get a message about a missing input file.

### Configuration options

Additional options can be passed to CMake using the `-D` flag. Angle brackets
(`<`, `>`) surround text that you should type in, while curly braces (`{`, `}`)
indicate valid options.

* `CMAKE_BUILD_TYPE={Debug,Release}`: builds debuggable or optimized versions
  of libraries and aerosol box models (default: `Release`)
* `CMAKE_C_COMPILER=<c-compiler>`: sets the C compiler used to build
  libraries and/or aerosol box models. The compiler should be in your `PATH`.
* `CMAKE_Fortran_COMPILER=<fortran-compiler>`: sets the Fortran compiler
  used to build libraries and/or aerosol box models. The compiler should be in
  your `PATH`.
* `CMAKE_INSTALL_PREFIX=</path/to/install>`: sets the top-level directory under
  which supported aerosol box models are installed (in a `bin` subdirectory)
* `ENABLE_CAMP={ON,OFF}`: enables support for CAMP chemistry in relevant aerosol
  box models (default: `OFF`)
* `MOSAIC_SOURCE_DIR=</path/to/mosaic>`: enables MOSAIC in relevant aerosol box
  models, building it from the source in the given directory (default: none)
