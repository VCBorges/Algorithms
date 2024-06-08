from typing import MutableSequence
from rich import print


def merge_and_count_split_inversions(
    left_arr: list[int],
    right_arr: list[int],
) -> tuple[list[int], int]:
    merged_arr = []
    right_idx, left_idx = 0, 0
    inversions = 0
    while right_idx <= len(right_arr) - 1 and left_idx <= len(left_arr) - 1:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1
            inversions += len(left_arr) - left_idx

    merged_arr.extend(right_arr[right_idx:])
    merged_arr.extend(left_arr[left_idx:])
    return merged_arr, inversions


def sort_and_count_inversions(arr: list[int]) -> tuple[list[int], int]:
    length = len(arr)
    if length <= 1:
        return arr, 0

    middle_idx = length // 2
    left_arr, left_inv = sort_and_count_inversions(arr[:middle_idx])
    right_arr, right_inv = sort_and_count_inversions(arr[middle_idx:])

    merged_arr, split_inv = merge_and_count_split_inversions(
        left_arr=left_arr,
        right_arr=right_arr,
    )
    return merged_arr, split_inv + left_inv + right_inv


input = [6, 5, 4, 4, 3, 2, 1]

print(sort_and_count_inversions(input))
