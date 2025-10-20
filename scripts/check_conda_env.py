#!/usr/bin/env python3
"""
Check that the recommended Conda environment is active.

Usage:
  - Optionally set AMB_CONDA_ENV env var to the expected env name.
  - Run this script before building to ensure you're in the correct env:

    python3 scripts/check_conda_env.py

Exit codes:
  0 - expected conda env is active
  1 - no conda env active or mismatch

Notes:
  This script does NOT activate environments (can't be done from a child
  process to affect the parent shell). It only checks and prints guidance.
"""
import os
import sys

def main():
  expected = os.environ.get('AMB_CONDA_ENV', 'ambrs')
  active = os.environ.get('CONDA_DEFAULT_ENV')

  if not active:
    print('No Conda environment appears active (CONDA_DEFAULT_ENV not set).')
    print(f'Recommended: create and activate the environment named "{expected}" before proceeding.')
    print('\nExample:')
    print('  conda env create -f scripts/environment.yml -n ' + expected)
    print('  conda activate ' + expected)
    sys.exit(1)

  if active != expected:
    print(f'Active Conda env: "{active}" (expected: "{expected}").')
    print('It is recommended to use the same conda env for ambuilder and ambrs workflows.')
    print('\nOptions:')
    print(f'  1) Activate the expected env: conda activate {expected}')
    print(f'  2) Or export AMB_CONDA_ENV={active} to accept the current env for this session')
    sys.exit(1)

  print(f'Conda environment check OK: active env = "{active}"')
  sys.exit(0)

if __name__ == '__main__':
    main()
