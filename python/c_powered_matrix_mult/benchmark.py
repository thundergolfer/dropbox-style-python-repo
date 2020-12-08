# IDE complains with "no module found" here, even when it exists (because it is generated within Bazel).
import c_matrix

if __name__ == "__main__":
    # TODO(Jonathon): Multiply two huge matrices to demo performance compared to pure-Python mmult
    c_matrix.lib.multiply_random_matrices(
        2,
        2,
        2,
        5,
    )