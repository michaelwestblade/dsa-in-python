from typing import List

list1 = [2,3,-2,4]
list2 = [-2,0,-1]

def max_product_subarray(nums: List[int]) -> int:
    result = nums[0]
    max_product = nums[0]
    min_product = nums[0]

    for index in range(1, len(nums)):
        if nums[index] >= 0:
            max_product = max(max_product*nums[index], nums[index])
            min_product = min(min_product*nums[index], nums[index])
        else:
            temp = max_product
            max_product = max(min_product*nums[index], nums[index])
            min_product = min(temp*nums[index], nums[index])
        result = max(max_product, result)
    return result

print(max_product_subarray(list1))
print(max_product_subarray(list2))