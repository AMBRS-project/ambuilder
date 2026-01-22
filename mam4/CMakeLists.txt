# We download the MAM box model and build it directly as an executable here,
# since it doesn't have a reasonable build system.

# download and extract the source for MAM4
set(MAM4_SOURCE_URL https://github.com/Duncan-Quevedo/MAM_box_model_dq/archive/refs/heads/dev_mac.zip)
set(MAM4_SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/MAM_box_model_dq-dev_mac)
if (NOT EXISTS ${MAM4_SOURCE_DIR})
  file(DOWNLOAD ${MAM4_SOURCE_URL} ${CMAKE_SOURCE_DIR}/downloads/mam4.zip)
  file(ARCHIVE_EXTRACT INPUT ${CMAKE_SOURCE_DIR}/downloads/mam4.zip)
endif()

# build the box model
add_executable(mam4
  ${MAM4_SOURCE_DIR}/e3sm_src/shr_kind_mod.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/shr_const_mod.F90

  ${MAM4_SOURCE_DIR}/box_model_utils/cam_logfile.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/spmd_utils.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/abortutils.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/cam_abortutils.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/ppgrid.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/pmgrid.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/constituents.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/radconstants.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/physconst.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/cam_history.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/units.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/ref_pres.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/dyn_grid.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/buffer.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/physics_buffer.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/physics_types.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/phys_control.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/mo_constants.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/chem_mods.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/mo_tracname.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/mo_chem_utls.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/gffgch.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/wv_saturation.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/error_function.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/shr_spfn_mod.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/infnan.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/seasalt_model.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/time_manager.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/aerodep_flx.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/modal_aero_convproc.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/modal_aero_deposition.F90

  ${MAM4_SOURCE_DIR}/e3sm_src/modal_aero_data.F90

  ${MAM4_SOURCE_DIR}/box_model_utils/rad_constituents.F90

  ${MAM4_SOURCE_DIR}/e3sm_src_modified/modal_aero_wateruptake.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/modal_aero_rename.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/modal_aero_calcsize.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/modal_aero_gasaerexch.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/modal_aero_newnuc.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/modal_aero_coag.F90
  ${MAM4_SOURCE_DIR}/e3sm_src_modified/modal_aero_amicphys.F90
  ${MAM4_SOURCE_DIR}/e3sm_src/modal_aero_initialize_data.F90

  ${MAM4_SOURCE_DIR}/box_model_utils/gaschem_simple.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/cloudchem_simple.F90
  ${MAM4_SOURCE_DIR}/test_drivers/driver.F90
  ${MAM4_SOURCE_DIR}/test_drivers/camp_interface.F90
  ${MAM4_SOURCE_DIR}/test_drivers/set_state.F90
  ${MAM4_SOURCE_DIR}/box_model_utils/main.F90
)

if(ENABLE_CAMP)
    target_link_libraries(mam4 camp netcdff netcdf hdf5_hl hdf5 dl z)
    set_target_properties(mam4 PROPERTIES
        BUILD_RPATH "${CMAKE_BINARY_DIR}/lib"
        INSTALL_RPATH "${CMAKE_BINARY_DIR}/lib")
else()
    target_link_libraries(mam4 netcdff netcdf hdf5_hl hdf5 dl z)
endif()

# These macros are defined in ${MAM4_SOURCE_DIR}/test_drivers/cambox_config.cpp.in.
target_compile_definitions(mam4 PRIVATE CAMBOX_ACTIVATE_THIS;CAMBOX_DEACTIVATE_THIS;MODAL_AERO;MODAL_AERO_4MODE_MOM;RAIN_EVAP_TO_COARSE_AERO;PCNST=35;PCOLS=1;PVER=1;NBC=1;NPOA=1;NSOA=1)
if (ENABLE_CAMP)
  add_definitions(-DMAM4_USE_CAMP)
endif()

install(
  TARGETS mam4
  DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
)
