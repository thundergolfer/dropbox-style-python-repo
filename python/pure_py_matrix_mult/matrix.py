def mult(a, b):
    b_cols = list(zip(*b))
    return [
        [
            sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) 
            for col_b in b_cols
        ]
        for row_a in a
    ]

