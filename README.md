<p align="center">
  <img src="https://user-images.githubusercontent.com/12058921/100537908-754b3d80-3280-11eb-8c7f-c51afbf39c57.png" height="225px"/>
</p>

# 'Dropbox Style' Python Repo [![CI](https://github.com/thundergolfer/dropbox-style-python-repo/workflows/CI/badge.svg)](https://github.com/thundergolfer/dropbox-style-python-repo/actions/)

Learning how the [`github.com/dropbox/dbx_build_tools`](https://github.com/dropbox/dbx_build_tools/) rules work for Python monorepos. I currently maintain the official Python rules for Bazel, [`bazelbuild/rules_python`](https://github.com/bazelbuild/rules_python), and think those rules have much to learn from what Dropbox have implemented in their rules. 

----

## Contents

### 'Python binding to C/C++' - Native Libs Demos

A very basic example of integrating C/C++ code into Python Bazel targets. Created to start learning how C-bindings work in Python. Originally based on the [Real Python - Python Bindings: Calling C or C++ From Python](https://realpython.com/python-bindings-overview/) tutorial.

### Basic 'Pure-Python' vs. 'C-Bindings Powered' Matrix Multiplication Benchmark

A very basic example of the performance impact of offloading expensive computations from Python to C.
See `python/pure_py_matrix_mult/compare_impl_performance.sh`.

(_Work In Progress_ 🚧)

----

## Development

⚠️ Development within this repository is only known to work on _Linux_, due to restrictions of the Dropbox Bazel rules (or perhaps just my inability to get the rules working on OSX). 

### Github Codespaces

The `.devcontainer/` folder defines a [Github _Codespaces_](https://github.com/features/codespaces) compatible
development container that is automatically setup by Codespaces when you create a codespace for this repository.

The development container has a version of Python (`3.9.0`) and `gcc` (`gcc (Debian 8.3.0-6) 8.3.0`) that are compatible with the Dropbox Bazel rules.

### Build

`bazel build //...`

#### Generating `BUILD` files.

The [Dropbox Bazel rules](https://github.com/dropbox/dbx_build_tools/) come with a `BUILD` file generator that tranforms `BUILD.in` files into complete `BUILD` files. See the Dropbox rules' README for short instructions on how to set up the generator. 

(In some places I've not used a `BUILD.in` file and the generator, and stuck to the plain-jane manual `BUILD` file, because the generator wasn't behaving as I expected or was otherwise getting in the way)

**Example `BUILD` file generation cmd:** `bzl gen //pythonl/...`

### Test

`bazel test //...`
