# Instead of using CMake's find_library, which introduces ridiculous externalities,
# we simply pass in the relevant paths as regular CMake variables. -JNJ
if(NETCDF_FORTRAN_LIB)
  set(NETCDF_LIBS ${NETCDF_FORTRAN_LIB} ${NETCDF_FORTRAN_LIB} ${NETCDF_C_LIB} ${HDF5_HL_LIB} ${HDF5_LIB} ${Z_LIB})
endif()
include_directories(${NETCDF_INCLUDE_DIR})
