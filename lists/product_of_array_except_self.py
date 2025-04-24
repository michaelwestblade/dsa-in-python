from typing import List

input1 = [1,2,3,4]
input2 = [-1,1,0,-3,3]

def product_of_array_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    left_array = [1]*n
    right_array = [1]*n

    for index in range(1, n):
        left_array[index] = left_array[index - 1]*nums[index - 1]
    for index in range(n-2, -1, -1):
        right_array[index] = right_array[index + 1]*nums[index+1]

    output = []

    for index in range(0,n):
        output.append(left_array[index] * right_array[index])

    return output

print(product_of_array_except_self(input1))
print(product_of_array_except_self(input2))