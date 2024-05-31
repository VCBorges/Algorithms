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
        return recursive_binary_search(arr[midpoint + 1:], key, start + midpoint + 1)
    
    return recursive_binary_search(arr[:midpoint], key, start)

input = [1,2,3,4,5,6,7,8,9,10]

print(recursive_binary_search(input, 10))