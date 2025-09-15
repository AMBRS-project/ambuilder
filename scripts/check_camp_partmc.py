#!/usr/bin/env python3
"""
Lightweight check for CAMP availability for PartMC.

Checks performed:
- CMake cache for ENABLE_CAMP
- presence of CAMP headers in build/include/camp or install include
- presence of libcamp in build/lib or build/lib64 or install/lib
- presence of partmc binary in common install locations

Exit code 0 when all checks pass, 1 otherwise.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BUILD_DIR = os.path.join(ROOT, 'build')
INSTALL_DIR = os.path.join(BUILD_DIR, 'install')

def read_cmake_cache():
    cache = ''
    path = os.path.join(BUILD_DIR, 'CMakeCache.txt')
    if os.path.exists(path):
        with open(path, 'r') as f:
            cache = f.read()
    return cache

def check_enable_camp(cache):
    if 'ENABLE_CAMP:BOOL=ON' in cache:
        return True
    # also check other encodings
    if 'ENABLE_CAMP:STRING=ON' in cache:
        return True
    return False

def check_camp_headers():
    candidates = [
        os.path.join(BUILD_DIR, 'include', 'camp'),
        os.path.join(INSTALL_DIR, 'include', 'camp'),
        os.path.join(ROOT, 'include', 'camp'),
    ]
    for p in candidates:
        if os.path.isdir(p) and os.listdir(p):
            return p
    return None

def find_libcamp():
    libnames = ['libcamp.a', 'libcamp.so', 'libcamp.dylib']
    search_dirs = [
        os.path.join(BUILD_DIR, 'lib'),
        os.path.join(BUILD_DIR, 'lib64'),
        os.path.join(INSTALL_DIR, 'lib'),
        os.path.join(INSTALL_DIR, 'lib64'),
    ]
    for d in search_dirs:
        if os.path.isdir(d):
            for ln in libnames:
                p = os.path.join(d, ln)
                if os.path.exists(p):
                    return p
    return None

def find_partmc_binary():
    candidates = [
        os.path.join(BUILD_DIR, 'bin', 'partmc'),
        os.path.join(INSTALL_DIR, 'bin', 'partmc'),
        os.path.join(ROOT, 'bin', 'partmc'),
    ]
    for p in candidates:
        if os.path.exists(p) and os.access(p, os.X_OK):
            return p
    return None

def main():
    cache = read_cmake_cache()
    ok = True

    print('Checking CMake cache for ENABLE_CAMP...')
    if check_enable_camp(cache):
        print('  ENABLE_CAMP appears to be ON in CMake cache')
    else:
        print('  ENABLE_CAMP not set to ON in CMake cache')
        ok = False

    hdr = check_camp_headers()
    if hdr:
        print(f'  Found CAMP headers in: {hdr}')
    else:
        print('  CAMP headers not found under build/include or install/include')
        ok = False

    lib = find_libcamp()
    if lib:
        print(f'  Found CAMP library at: {lib}')
    else:
        print('  CAMP library (libcamp.*) not found in build/install lib dirs')
        ok = False

    partmc = find_partmc_binary()
    if partmc:
        print(f'  Found partmc binary at: {partmc}')
    else:
        print('  partmc binary not found in build/install/bin')
        ok = False

    if ok:
        print('\nAll CAMP checks for PartMC PASSED')
        sys.exit(0)
    else:
        print('\nOne or more CAMP checks for PartMC FAILED')
        sys.exit(1)

if __name__ == '__main__':
    main()
