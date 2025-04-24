from typing import List

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

def maxProfit(prices: List[int]) -> int:
    ans = 0
    min_value_so_far = prices[0]

    for index, price in enumerate(prices):
        profit = price - min_value_so_far
        if (profit > ans):
            ans = profit
        if (price < min_value_so_far):
            min_value_so_far = price

    return ans

print(maxProfit(prices1))
print(maxProfit(prices2))