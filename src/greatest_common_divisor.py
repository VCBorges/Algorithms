from rich import print

def greatest_common_divisor(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a

print(greatest_common_divisor(375, 234))