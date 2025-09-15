cmake_minimum_required (VERSION 3.24.0)

# Adjust CMake's module path.
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")

#----------
# Settings
#----------

option(ENABLE_CAMP "Enables support for CAMP chemistry in relevant aerosol models" OFF)

set(MOSAIC_SOURCE_DIR "" CACHE PATH "source directory for Mosaic")
if (MOSAIC_SOURCE_DIR)
  set(ENABLE_MOSAIC ON CACHE BOOL "MOSAIC support (determined by MOSAIC_SOURCE_DIR)")
else()
  set(ENABLE_MOSAIC OFF CACHE BOOL "MOSAIC support (determined by MOSAIC_SOURCE_DIR)")
endif()

project(ambuilder)
enable_language(C)
enable_language(Fortran)

message(STATUS "Generating project files in build directory: ${PROJECT_BINARY_DIR}")
message(STATUS "C compiler is ${CMAKE_C_COMPILER} (${CMAKE_C_COMPILER_ID} ${CMAKE_C_COMPILER_VERSION})")
message(STATUS "Fortran compiler is ${CMAKE_Fortran_COMPILER} (${CMAKE_Fortran_COMPILER_ID} ${CMAKE_Fortran_COMPILER_VERSION})")

message(STATUS "Configuring Aerosol box models")

# We build static libraries only.
set(BUILD_SHARED_LIBS OFF)

# Figure out the system type.
if (APPLE)
  set(SYS_FLAGS "-DAPPLE=1")
  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -framework Accelerate")
  set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -framework Accelerate")
  message(STATUS "Configuring on Mac.")
elseif(LINUX)
  set(SYS_FLAGS "-DLINUX=1")
  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pthread")
  message(STATUS "Configuring on Linux.")
else()
  message(FATAL_ERROR "Unknown system type! Currently only Mac and Linux are supported")
endif ()

# Fortran compiler flags
set(CMAKE_Fortran_FLAGS "-cpp")
if (CMAKE_Fortran_COMPILER_ID STREQUAL "GNU")
  if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fbacktrace")
  endif()
  set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Wall -ffree-form -ffree-line-length-0")
  set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Wno-unused-dummy-argument")
  set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Wno-unused-variable")
  #set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Wno-maybe-uninitialized")
  #set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Wno-target-lifetime")
  #set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Werror=tabs")
  #set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fno-range-check") # <-- we shouldn't need this!
  #set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -Wno-line-truncation") # <-- we shouldn't need this!
  # This is a hack to make our non-standard inf/nan values work with
  # recent, picky versions of GFortran.
  if (${CMAKE_Fortran_COMPILER_VERSION} GREATER_EQUAL 10)
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-invalid-boz")
    message(STATUS "BOZ literal hack enabled")
    # we also need this guy
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-argument-mismatch")
  endif()
elseif (CMAKE_Fortran_COMPILER_ID STREQUAL "Intel")
  if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -traceback")
  endif()
endif()

# C compiler flags
set(CMAKE_C_FLAGS "-fPIC")
if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-format-truncation -Wfloat-equal")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-unknown-pragmas")
  if (HAVE_DOUBLE_PRECISION)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wfloat-conversion")
  endif()

  if (LINUX)
    # Pass some more needed flags to the compiler.
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pthread")
  endif()
elseif (CMAKE_C_COMPILER_ID MATCHES "Clang")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-unknown-pragmas")

  # Clang proper behaves differently from Apple Clang. Each require
  # specific suppressions.
  if (CMAKE_C_COMPILER_ID MATCHES "AppleClang")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-implicit-function-declaration")
  else()
    # tolower() is a recursive macro, which causes issues.
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-disabled-macro-expansion")
  endif()
elseif (CMAKE_C_COMPILER_ID STREQUAL "Intel")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall")
endif()
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${SYS_FLAGS}")

# Report the installation prefix.
message(STATUS "Installation prefix is ${CMAKE_INSTALL_PREFIX}")

# supporting libraries
add_subdirectory(libraries)

# Include the binary directory in the header file search path,
# since it's where we place the third-party libraries.
include_directories("${PROJECT_BINARY_DIR}")
include_directories("${PROJECT_BINARY_DIR}/include")
link_directories("${PROJECT_BINARY_DIR}/lib")
link_directories("${PROJECT_BINARY_DIR}/lib64")

# the box models
add_subdirectory(mam4)
add_subdirectory(partmc)
#add_subdirectory(carma)
add_subdirectory(mphys-1-moment-sectional)
