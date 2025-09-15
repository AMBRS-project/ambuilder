# AMBuilder

AMBuilder is a CMake setup that builds the box models used by the AMBRS
Project in configurations of interest. Supported box models are:

* CARMA
* MAM4
* PartMC

## Calling CMake Directly

To use CMake to build the box models and install them to a given folder
(shown here as `<prefix>`, with a `bin` subfolder), use the following commands:

```
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=<prefix> [options]
cd build
make
make install
```

### Configuration options

Additional options can be passed to CMake using the `-D` flag:

* `CMAKE_BUILD_TYPE={Debug,Release}`: builds debuggable or optimized versions
  of libraries and aerosol box models (default: `Release`)
* `CMAKE_C_COMPILER=/path/to/c-compiler`: sets the C compiler used to build
  libraries and/or aerosol box models
* `CMAKE_Fortran_COMPILER=/path/to/fortran-compiler`: sets the Fortran compiler
  used to build libraries and/or aerosol box models
* `CMAKE_INSTALL_PREFIX=/path/to/install`: sets the top-level directory under
  which supported aerosol box models are installed (in a `bin` subdirectory)
* `ENABLE_CAMP={ON,OFF}`: enables support for CAMP chemistry in relevant aerosol
  box models (default: `OFF`)
* `MOSAIC_SOURCE_DIR=/path/to/mosaic`: enables MOSAIC in relevant aerosol box
  models, building it from the source in the given directory (default: none)
