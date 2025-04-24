list1 = [-2,1,-3,4,-1,2,1,-5,4]
list2 = [1]
list3 = [5,4,-1,7,8]

def max_sub_array(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for index in range(1, len(nums)):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[index]
        if current_sum > max_sum:
            max_sum = current_sum


    return max_sum

print(max_sub_array(list1))
print(max_sub_array(list2))
print(max_sub_array(list3))
