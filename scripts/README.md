# CAMP presence checks

Two small diagnostic scripts help confirm whether CAMP is available to PartMC and MAM in this workspace.

Files
- `check_camp_partmc.py`: verifies CMake cache, CAMP headers and library, and the `partmc` binary.
- `check_camp_mam.py`: verifies CMake cache, CAMP headers and library, and presence of `mam4` sources or libs.

Usage
1. Run a CMake configure with CAMP enabled (recommended):

```bash
mkdir -p build
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=$(pwd)/build/install -DENABLE_CAMP=ON -DCMAKE_BUILD_TYPE=Release
```

2. Run the checks:

```bash
python3 scripts/check_camp_partmc.py
python3 scripts/check_camp_mam.py
```

Exit codes: 0 = all checks passed; 1 = one or more checks failed.

Notes
- These are lightweight sanity checks and do not run compilations or PartMC/MAM. They look for expected installed files and CMake cache flags.
- For a full validation, perform `make install` from the build directory and then run a short PartMC PPE using the provided configs.

Conda environment (required)
---------------------------------
This project expects you to use a dedicated Conda environment for ambuilder/ambrs workflows. Always activate the environment before running the configure/build/check scripts.

1. Create the recommended environment (first time):

```bash
conda env create -f scripts/environment.yml -n ambrs
```

2. Activate it before doing anything else in this repo:

```bash
conda activate ambrs
python3 scripts/check_conda_env.py
```

If your environment has a different name, set `AMB_CONDA_ENV` in your shell to the name you use:

```bash
export AMB_CONDA_ENV=myenv
python3 scripts/check_conda_env.py
```
