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

# 1.
# When trying BUILD.in `bzl gen` seemed to skip this target and not copy it into the final BUILD file.
# TODO(Jonathon): Create Github issue for the above problem.
#
# 2. 
# This rule is not documented at all in the Dropbox rules' README, nor anywhere else on the internet, so was a little tricky to figure out.
# TODO(Jonathon): Contribute some docs back to the Dropbox rules repo.
dbx_cffi_module(
    name = "cffi_example",
    module_name = "cffi_example",
    cdef = ":cmult.h",
    source = ":cffi_c_header_source.c",  # Note: The contents of this file are inserted into the CFFI generated .c file.
    libraries = ["cmult"],
    deps = [
        ":cmult.h",
        ":libcmult.so",
    ],
    linkopts=["-Wl,--export-dynamic",] # TODO(Jonathon): May not actually need this.
)

# Note: Has to be a cc_library not a cc_binary, as I think the latter doesn't export symbols.
cc_library(
    name = "libcmult.so",
    linkstatic=True, 
    srcs = [
        "cmult.c",
        "cmult.h",
    ],
)