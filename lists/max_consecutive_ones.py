from typing import List

example_1 = [1, 1, 0, 1, 1, 1]  # 3
example_2 = [1, 0, 1, 1, 0, 1]  # 2


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    answer = 0
    currentCount = 0
    for index, element in enumerate(nums):
        if element != 1:
            currentCount = 0
        else:
            currentCount += 1
        if currentCount > answer:
            answer = currentCount

    return answer


print(findMaxConsecutiveOnes(example_1))
print(findMaxConsecutiveOnes(example_2))
