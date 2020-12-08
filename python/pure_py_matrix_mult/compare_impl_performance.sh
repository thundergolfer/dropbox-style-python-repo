#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail


info() {
  echo "$(date '+[%Y-%m-%d %H:%M:%S]'): INFO: $*"
}

main() {
    info "Building Pure-Python Matrix Multiplication Benchmark Program"
    bazel build //python/pure_py_matrix_mult:benchmark
    info "Running Pure-Python Benchmark Program"
    time ./bazel-bin/python/pure_py_matrix_mult/benchmark

    // TODO(Jonathon): Build and time the C-bindings powered Matrix Mult Program
}

main "$@"