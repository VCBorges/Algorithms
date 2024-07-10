def fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(2, n + 1):
        current, previous = (current + previous), current
    return current


def recursive_fibonacci_number(n: int) -> int:
    if n <= 1:
        return n
    return recursive_fibonacci_number(n - 1) + recursive_fibonacci_number(n - 2)


def fibonacci_sequence(n: int) -> list[int]:
    if n <= 1:
        return n

    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def naive_memoized_recursive_fibonacci_number(
    n: int,
    memo: dict = {},
) -> int:
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = naive_memoized_recursive_fibonacci_number(
        n - 1
    ) + naive_memoized_recursive_fibonacci_number(n - 2)

    return memo[n]


if __name__ == "__main__":
    print(naive_memoized_recursive_fibonacci_number(10))
