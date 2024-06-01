from rich import print

def naive_selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


input = [8,2,5,7,9,1,3, 1]


print(naive_selection_sort(input))