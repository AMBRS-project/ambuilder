# We download Jeff Pierce's aerosol model and assemble a standalone driver
# script that can be run in a separate process to accommodate its (LGPL) license.

# download and extract the source
set(MPHYS_SOURCE_URL https://github.com/AMBRS-project/mphys-1-moment-sectional/archive/refs/heads/main.zip)
set(MPHYS_SOURCE_ZIP ${CMAKE_SOURCE_DIR}/downloads/mphys-1-moment-sectional.zip)
if (NOT EXISTS ${MPHYS_SOURCE_ZIP})
  file(DOWNLOAD ${MPHYS_SOURCE_URL} ${MPHYS_SOURCE_ZIP}
    STATUS result
  )
  list(GET result 0 status)
  if (NOT ${status} EQUAL 0)
    file(REMOVE ${MPHYS_SOURCE_ZIP})
    list(GET result 1 mesg)
    message(FATAL_ERROR ${mesg})
  endif()
endif()
set(MPHYS_SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/mphys-1-moment-sectional-main)
if (NOT EXISTS ${MPHYS_SOURCE_DIR}/dNdt_coag.py)
  file(ARCHIVE_EXTRACT
    INPUT ${MPHYS_SOURCE_ZIP}
    DESTINATION ${CMAKE_CURRENT_BINARY_DIR}
  )
endif()

# mash everything into a self-contained driver script
set(driver ${CMAKE_CURRENT_BINARY_DIR}/mphys-driver)
file(WRITE ${driver} "#!/usr/bin/env python\n")
file(READ ${CMAKE_CURRENT_SOURCE_DIR}/driver.py driver_py)
file(APPEND ${driver} ${driver_py})
foreach(module
        dNdt_coag.py
        dNdt_cond.py
        dNdt_all.py
        get_coag_kernel.py)
  file(APPEND ${driver} "\n# ${module}\n")
  file(READ ${MPHYS_SOURCE_DIR}/${module} module_src)
  file(APPEND ${driver} "${module_src}")
endforeach()
file(CHMOD ${driver} PERMISSIONS
  OWNER_READ OWNER_WRITE OWNER_EXECUTE
  GROUP_READ GROUP_EXECUTE
  WORLD_READ WORLD_EXECUTE
)

install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/mphys-driver
  DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
)
