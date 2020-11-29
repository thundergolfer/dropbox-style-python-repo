load("@dbx_build_tools//build_tools/py:py.bzl", "dbx_py_pypi_piplib")

licenses(["notice"])  # Apache 2.0

# TODO(Jonathon): Maybe don't need this if I can use Cython via pyx_library like this: https://github.com/tensorflow/tensorflow/blob/48f0418e39203cf29c3508721f14062e4c30e0a3/tensorflow/core/platform/default/build_config.bzl
# How to get @cython in WORKSPACE: https://github.com/tensorflow/tensorflow/blob/7a0852a34f91c0e19b56781cce220e1a53efe0ce/tensorflow/workspace.bzl#L894
dbx_py_pypi_piplib(
    name = "cython",
    pip_version = "0.29.21",
    visibility = ["//visibility:public"],
)