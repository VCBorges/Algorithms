def linear_search(arr: list[int], key: int) -> int | None:
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return None
