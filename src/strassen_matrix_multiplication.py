from rich import print

def matrix_mult(
    a: list[list[int]],
    b: list[list[int]],
) -> list[list[int]]:
    rows_a = len(a)
    rows_b = len(b)
    cols_a = len(a[0])
    cols_b = len(b[0])
    
    if cols_a != rows_b:
        raise ValueError()
    
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result

def strassen_matrix_mult(
    a: list[list[int]],
    b: list[list[int]],
) -> list[list[int]]:
    
    return ...



a = [
    [1,2], 
    [3,4],
]
b = [
    [5,6], 
    [7,8],
]

print(matrix_mult(a,b))