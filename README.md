# 'Dropbox Style' Python Repo

Learning how the `github.com/dropbox/dbx_build_tools work` for Python monorepos.

----

## Contents

### Python + C/C++ Native Libs Demo

A very basic example of integrating C/C++ code into Python Bazel targets. Created to start learning how C-bindings work in Python.

----

## Development

⚠️ Development within this repository is only known to work on _Linux_, due to restrictions of the Dropbox Bazel rules (or perhaps just my inability to get the rules working on OSX). 

### Github Codespaces

The `.devcontainer/` folder defines a [Github _Codespaces_](https://github.com/features/codespaces) compatible
development container that is automatically setup by Codespaces when you create a codespace for this repository.

The development container has a version of Python (`3.9.0`) and `gcc` (`gcc (Debian 8.3.0-6) 8.3.0`) that are compatible with the Dropbox Bazel rules.

### Build

`bazel build //...`

### Test

`bazel test //...`