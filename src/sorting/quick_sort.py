def partition(arr: list[int]) -> list[int]:
    pivot = arr[0]
    j = 0
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[0], arr[j] = arr[j], arr[0]
    return j


def quick_sort(arr: list[int]) -> list[int]:
    sorted_arr = []
    return sorted_arr
