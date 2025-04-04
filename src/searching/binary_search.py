def recursive_binary_search(
    arr: list[int],
    key: int,
    start: int = 0,
) -> int | None:
    if key > arr[-1] or key < arr[0]:
        return None

    midpoint = len(arr) // 2
    if arr[midpoint] == key:
        return midpoint + start

    if arr[midpoint] < key:
        return recursive_binary_search(
            arr=arr[midpoint + 1 :],
            key=key,
            start=start + midpoint + 1,
        )

    return recursive_binary_search(
        arr=arr[:midpoint],
        key=key,
        start=start,
    )


def iterative_binary_search(
    arr: list[int],
    key: int,
) -> int | None:
    high = len(arr) - 1
    low = 0
    while low <= high:
        midpoint = low + ((high - low) // 2)
        if key == arr[midpoint]:
            return midpoint

        elif key < arr[midpoint]:
            high = midpoint - 1

        else:
            low = midpoint + 1

    return None