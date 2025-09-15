#!/usr/bin/env python3
"""
Lightweight check for CAMP availability for MAM integration.

Checks performed:
- CMake cache for ENABLE_CAMP
- presence of CAMP headers in build/include/camp or install include
- presence of MAM module files (check for mam4 directory or lib)
- presence of libcamp as above

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
    if 'ENABLE_CAMP:STRING=ON' in cache:
        return True
    return False

def check_camp_headers():
    candidates = [
        os.path.join(BUILD_DIR, 'include', 'camp'),
        os.path.join(INSTALL_DIR, 'include', 'camp'),
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

def check_mam_presence():
    # Look for a mam4 directory or a mam4 lib
    candidates = [
        os.path.join(ROOT, 'mam4'),
        os.path.join(ROOT, 'mam4', 'CMakeLists.txt'),
        os.path.join(BUILD_DIR, 'lib', 'libmam4.a'),
        os.path.join(BUILD_DIR, 'lib64', 'libmam4.a'),
    ]
    for p in candidates:
        if os.path.exists(p):
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

    mam = check_mam_presence()
    if mam:
        print(f'  Found MAM artifact at: {mam}')
    else:
        print('  MAM (mam4) sources or libraries not found')
        ok = False

    if ok:
        print('\nAll CAMP checks for MAM PASSED')
        sys.exit(0)
    else:
        print('\nOne or more CAMP checks for MAM FAILED')
        sys.exit(1)

if __name__ == '__main__':
    main()
