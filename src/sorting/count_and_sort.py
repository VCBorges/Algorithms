from rich import print


def count_and_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    M = max(arr) + 1
    counter = [0] * M

    for i in arr:
        counter[i] += 1

    position = [0] * M
    for i in range(2, M):
        position[i] = position[i - 1] + counter[i - 1]

    sorted_arr = [0] * len(arr)
    for i in range(1, len(arr)):
        sorted_arr[position[arr[i]]] = arr[i]
        position[arr[i]] += 1

    return sorted_arr


input = [2, 2, 2, 1, 1, 1, 3, 3]
