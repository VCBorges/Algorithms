from rich import print

def matrix_mult(
    a: list[list[int]],
    b: list[list[int]],
) -> list[list[int]]:
    length = len(a)
    result = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
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

matrix_mult(a,b)