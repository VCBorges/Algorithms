from rich import print


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(2, n + 1):
        current, previous = (current + previous), current
    return current


def fibonacci_sequence(n: int) -> list[int]:
    if n <= 1:
        return n

    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


input = 6

print(fibonacci_sequence(input))
