# Copied from https://github.com/dropbox/dbx_build_tools/blob/78c3052646c6934d930905e94b1372ce3284158a/pip/pycparse/BUILD
# TODO(Jonathon): I shouldn't need to copy it. I have to because one of Dropbox's rules refs' //pip/cffi instead of @dbx_buil...//pip/cffi
package(default_visibility = ["//visibility:public"])

load("@dbx_build_tools//build_tools/py:py.bzl", "dbx_py_pypi_piplib")

licenses(["notice"])  # BSD

dbx_py_pypi_piplib(
    name = "pycparser",
    pip_version = "2.20",
)