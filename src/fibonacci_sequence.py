from rich import print

def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_sequence(n: int) -> int:
    if n <= 1:
        return n
    
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]
    
input = 6

# print([fibonacci_recursive(n) for n in range(input + 1)])
print([fibonacci_sequence(n) for n in range(input + 1)])

