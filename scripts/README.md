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
