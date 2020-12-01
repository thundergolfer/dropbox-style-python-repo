from python.pure_py_matrix_mult import matrix

def test_matrix_mult():
    x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    y = [[1,2],[1,2],[3,4]]

    actual = matrix.mult(x, y)
    expected = [
        [12, 18],
        [27, 42],
        [42, 66],
        [57, 90],
    ]
    assert expected == actual