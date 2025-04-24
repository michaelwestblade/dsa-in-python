from typing import List

list1 = [1,2,3,4,5,6,7]
list2 = [-1,-100,3,99]

def rotate_array(arr: List[int], rotations) -> List[int]:
    k = rotations % len(arr)
    n = len(arr)
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    return arr

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


print(rotate_array(list1, 3))
print(rotate_array(list2, 2))