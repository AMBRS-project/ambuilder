# We download CARMA and build a configurable box model version directly.

# download and extract the source
set(CARMA_SOURCE_URL https://github.com/AMBRS-project/CARMA_base/archive/refs/heads/main.zip)
set(CARMA_SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/CARMA_base-main)
if (NOT EXISTS ${CARMA_SOURCE_DIR})
  file(DOWNLOAD ${CARMA_SOURCE_URL} ${CMAKE_SOURCE_DIR}/downloads/CARMA.zip)
  file(ARCHIVE_EXTRACT INPUT ${CMAKE_SOURCE_DIR}/downloads/CARMA.zip)
endif()

# build the box model
add_executable(carma
  ${CARMA_SOURCE_DIR}/actdropl.F90
  ${CARMA_SOURCE_DIR}/adgaquad_types_mod.F90
  ${CARMA_SOURCE_DIR}/adgaquad_mod.F90
  ${CARMA_SOURCE_DIR}/bhmie.F90
  ${CARMA_SOURCE_DIR}/calcrs.F90
  ${CARMA_SOURCE_DIR}/carma_constants_mod.F90
  ${CARMA_SOURCE_DIR}/carma_enums_mod.F90
  ${CARMA_SOURCE_DIR}/carma_mod.F90
  ${CARMA_SOURCE_DIR}/carma_precision_mod.F90
  ${CARMA_SOURCE_DIR}/carma_types_mod.F90
  ${CARMA_SOURCE_DIR}/carmaelement_mod.F90
  ${CARMA_SOURCE_DIR}/carmagas_mod.F90
  ${CARMA_SOURCE_DIR}/carmagroup_mod.F90
  ${CARMA_SOURCE_DIR}/carmasolute_mod.F90
  ${CARMA_SOURCE_DIR}/carmastate_mod.F90
  ${CARMA_SOURCE_DIR}/coagl.F90
  ${CARMA_SOURCE_DIR}/coagp.F90
  ${CARMA_SOURCE_DIR}/coremasscheck.F90
  ${CARMA_SOURCE_DIR}/csolve.F90
  ${CARMA_SOURCE_DIR}/downgevapply.F90
  ${CARMA_SOURCE_DIR}/downgxfer.F90
  ${CARMA_SOURCE_DIR}/evapp.F90
  ${CARMA_SOURCE_DIR}/evap_ingrp.F90
  ${CARMA_SOURCE_DIR}/evap_mono.F90
  ${CARMA_SOURCE_DIR}/evap_poly.F90
  ${CARMA_SOURCE_DIR}/fixcorecol.F90
  ${CARMA_SOURCE_DIR}/fractal_meanfield_mod.F90
  ${CARMA_SOURCE_DIR}/freezaerl_koop2000.F90
  ${CARMA_SOURCE_DIR}/freezaerl_mohler2010.F90
  ${CARMA_SOURCE_DIR}/freezaerl_tabazadeh2000.F90
  ${CARMA_SOURCE_DIR}/freezdropl.F90
  ${CARMA_SOURCE_DIR}/freezglaerl_murray2010.F90
  ${CARMA_SOURCE_DIR}/growevapl.F90
  ${CARMA_SOURCE_DIR}/growp.F90
  ${CARMA_SOURCE_DIR}/gsolve.F90
  ${CARMA_SOURCE_DIR}/hetnucl.F90
  ${CARMA_SOURCE_DIR}/hygroscopicity.F90
  ${CARMA_SOURCE_DIR}/lusolvec_mod.F90
  ${CARMA_SOURCE_DIR}/maxconc.F90
  ${CARMA_SOURCE_DIR}/melticel.F90
  ${CARMA_SOURCE_DIR}/microfast.F90
  ${CARMA_SOURCE_DIR}/microslow.F90
  ${CARMA_SOURCE_DIR}/mie.F90
  ${CARMA_SOURCE_DIR}/miess.F90
  ${CARMA_SOURCE_DIR}/newstate.F90
  ${CARMA_SOURCE_DIR}/newstate_calc.F90
  ${CARMA_SOURCE_DIR}/nsubsteps.F90
  ${CARMA_SOURCE_DIR}/pheat.F90
  ${CARMA_SOURCE_DIR}/planck.F90
  ${CARMA_SOURCE_DIR}/prestep.F90
  ${CARMA_SOURCE_DIR}/psolve.F90
  ${CARMA_SOURCE_DIR}/rhopart.F90
  ${CARMA_SOURCE_DIR}/setupatm.F90
  ${CARMA_SOURCE_DIR}/setupbdif.F90
  ${CARMA_SOURCE_DIR}/setupbins.F90
  ${CARMA_SOURCE_DIR}/setupckern.F90
  ${CARMA_SOURCE_DIR}/setupcoag.F90
  ${CARMA_SOURCE_DIR}/setupgkern.F90
  ${CARMA_SOURCE_DIR}/setupgrow.F90
  ${CARMA_SOURCE_DIR}/setupnuc.F90
  ${CARMA_SOURCE_DIR}/setupvdry.F90
  ${CARMA_SOURCE_DIR}/setupvf.F90
  ${CARMA_SOURCE_DIR}/setupvf_heymsfield2010.F90
  ${CARMA_SOURCE_DIR}/setupvf_std.F90
  ${CARMA_SOURCE_DIR}/setupvf_std_shape.F90
  ${CARMA_SOURCE_DIR}/smallconc.F90
  ${CARMA_SOURCE_DIR}/step.F90
  ${CARMA_SOURCE_DIR}/sulfate_utils.F90
  ${CARMA_SOURCE_DIR}/sulfhetnucrate.F90
  ${CARMA_SOURCE_DIR}/sulfnuc.F90
  ${CARMA_SOURCE_DIR}/sulfnucrate.F90
  ${CARMA_SOURCE_DIR}/supersat.F90
  ${CARMA_SOURCE_DIR}/totalcondensate.F90
  ${CARMA_SOURCE_DIR}/tsolve.F90
  ${CARMA_SOURCE_DIR}/upgxfer.F90
  ${CARMA_SOURCE_DIR}/vaporp.F90
  ${CARMA_SOURCE_DIR}/vaporp_h2o_buck1981.F90
  ${CARMA_SOURCE_DIR}/vaporp_h2o_goff1946.F90
  ${CARMA_SOURCE_DIR}/vaporp_h2o_murphy2005.F90
  ${CARMA_SOURCE_DIR}/vaporp_h2so4_ayers1980.F90
  ${CARMA_SOURCE_DIR}/versol.F90
  ${CARMA_SOURCE_DIR}/versub.F90
  ${CARMA_SOURCE_DIR}/vertadv.F90
  ${CARMA_SOURCE_DIR}/vertdif.F90
  ${CARMA_SOURCE_DIR}/vertical.F90
  ${CARMA_SOURCE_DIR}/wetr.F90
  ${CARMA_SOURCE_DIR}/zeromicro.F90

  atmosphere_mod.F90
  carma_testutils.F90
  carma.F90
)

install(
  TARGETS carma
  DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
)
