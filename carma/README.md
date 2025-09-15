# CARMA "box model"

We build a CARMA "box model" from [CARMA's base source](https://github.com/AMBRS-project/CARMA_base), creating an executable with a few source files copied from the
[CARMA standalone repository](https://github.com/ESCOMP/CARMA):

* [`atmosphere_mod.F90`](https://github.com/ESCOMP/CARMA/blob/main/tests/atmosphere_mod.F90)
* [`carma_testutils.F90`](https://github.com/ESCOMP/CARMA/blob/main/tests/carma_testutils.F90)

The source for the executable program itself, `carma.F90`, has been adapted from
[camra_sulfate_vehkamaki_test.F90](https://github.com/ESCOMP/CARMA/blob/main/tests/carma_sulfate_vehkamaki_test.F90).


