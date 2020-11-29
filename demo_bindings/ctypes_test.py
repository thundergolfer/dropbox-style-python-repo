#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
import sys

from dropbox import runfiles


if __name__ == "__main__":
    # Load the shared library into c types.
    if sys.platform.startswith("win"):
        lib_so_path = runfiles.data_path("//demo_bindings/libcmult.dll")
    else:
        lib_so_path = runfiles.data_path("//demo_bindings/libcmult.so")
        # lib_so_path = "/home/vscode/.cache/bazel/_bazel_vscode/ce7fdaa19959a795d41dc5f49a9dba88/execroot/dropbox_style_python_repo/bazel-out/k8-fastbuild/bin/demo_bindings/libcmult.so"

    c_lib = ctypes.CDLL(lib_so_path)

    # Sample data for our call:
    x, y = 6, 2.3

    # This will not work:
    # answer = c_lib.cmult(x, y)

    # This produces a bad answer:
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print()

    # You need tell ctypes that the function returns a float
    c_lib.cmult.restype = ctypes.c_float
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
