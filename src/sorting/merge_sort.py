from typing import MutableSequence
from rich import print

def merge(
    right_arr: MutableSequence[int], 
    left_arr: MutableSequence[int],
) -> MutableSequence[int]:
    merged_arr = []
    right_idx, left_idx = 0, 0
    while (
        right_idx <= len(right_arr) - 1
        and left_idx <= len(left_arr) - 1
    ):
        if right_arr[right_idx] <= left_arr[left_idx]:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1
        else:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
    
    merged_arr.extend(right_arr[right_idx:])
    merged_arr.extend(left_arr[left_idx:])
    return merged_arr    


def merge_sort(arr: MutableSequence[int]) -> MutableSequence[int]:
    length = len(arr)
    if length <= 1:
        return arr
    
    middle_idx = length // 2
    return merge(
        right_arr=merge_sort(arr[:middle_idx]), 
        left_arr=merge_sort(arr[middle_idx:]),
    )


input = [20, 9, 2 ,6 ,4, 10, 11, 12, 15]

print(merge_sort(input))