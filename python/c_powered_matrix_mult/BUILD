load("@dbx_build_tools//build_tools/py:py.bzl", "dbx_py_binary")
load("@dbx_build_tools//build_tools/py:cffi.bzl", "dbx_cffi_module")

dbx_py_binary(
    name = "benchmark",
    main = "benchmark.py",
    autogen_deps = False,
    srcs = [
        "benchmark.py",
    ],
    deps = [
        ":c_matrix",
    ]
)

dbx_cffi_module(
    name = "c_matrix",
    module_name = "c_matrix",
    cdef = ":matrix.h",
    source = ":cffi_c_header_source.c",  # Note: The contents of this file are inserted into the CFFI generated .c file before it's compiled.
    libraries = ["matrix"],
    deps = [
        ":matrix.h",
        ":matrix.so",
    ],
    linkopts=["-Wl,--export-dynamic",] # TODO(Jonathon): May not actually need this.
)

# Note: Has to be a cc_library not a cc_binary, as I think the latter doesn't export symbols.
cc_library(
    name = "matrix.so",
    linkstatic=True, 
    srcs = [
        "matrix.c",
        "matrix.h",
    ],
)