def iterative_fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        current, previous = (current + previous), current
    return current


def recursive_fibonacci_number(n: int) -> int:
    if n <= 1:
        return n
    return recursive_fibonacci_number(n - 1) + recursive_fibonacci_number(n - 2)


def iterative_fibonacci_sequence(n: int) -> list[int]:
    if n <= 1:
        return n

    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def memoized_recursive_fibonacci_number(
    n: int,
    memo: dict = {},
) -> int:
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = memoized_recursive_fibonacci_number(n - 1) + memoized_recursive_fibonacci_number(n - 2) # fmt: skip

    return memo[n]


if __name__ == "__main__":
    print(memoized_recursive_fibonacci_number(10))
