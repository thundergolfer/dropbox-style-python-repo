"""
A pure-python implementation of matrix operations for use in demonstrating the
performance impact of moving expensive computations on large matrices out of Python
and into C/C++ code.
"""

def mult(a, b):
    b_cols = list(zip(*b))
    return [
        [
            sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) 
            for col_b in b_cols
        ]
        for row_a in a
    ]

