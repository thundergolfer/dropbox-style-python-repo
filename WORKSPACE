workspace(name = "dropbox_style_python_repo")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

dbx_build_tools_version = "cf20924b088261df13cffd1cfb05b850614d0ebc"

# NOTE: These rules are for build and test of applications for "Linux servers", so they're not OSX compatible.
http_archive(
    name = "dbx_build_tools",
    urls = ["https://github.com/dropbox/dbx_build_tools/archive/{version}.tar.gz".format(version = dbx_build_tools_version)],
    sha256 = "eef383d2fa9193ba13c088416e00822c8270bc0db27df62562186baa6f92b8ec",
    strip_prefix = "dbx_build_tools-{version}".format(version = dbx_build_tools_version),
)

load('@dbx_build_tools//build_tools/bazel:external_workspace.bzl', 'drte_deps')

drte_deps()

register_toolchains(
    "@dbx_build_tools//thirdparty/cpython:drte-off-27-toolchain",
    "@dbx_build_tools//thirdparty/cpython:drte-off-38-toolchain",
)
