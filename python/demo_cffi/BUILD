load("@dbx_build_tools//build_tools/py:py.bzl", "dbx_py_binary")
load("@dbx_build_tools//build_tools/py:cffi.bzl", "dbx_cffi_module")

dbx_py_binary(
    name = "cffi_test",
    main = "cffi_test.py",
    autogen_deps = False,
    srcs = [
        "cffi_test.py",
    ],
    deps = [
        ":cffi_example",
    ]
)

dbx_cffi_module(
    name = "cffi_example",
    module_name = "cffi_example",
    cdef = ":cmult.h",
    source = ":cffi_c_header_source.c",
    libraries = ["cmult"],
    deps = [
        ":cmult.h",
        ":libcmult.so",
    ],
    linkopts=["-Wl,--export-dynamic",]
)

cc_library(
    name = "libcmult.so",
    linkstatic=True, 
    srcs = [
        "cmult.c",
        "cmult.h",
    ],
)