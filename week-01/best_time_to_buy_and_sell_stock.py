from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        min_price = prices[0]

        for i in range(1, n):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit


# Time Complexity: O(n)
# Space Complexity: O(1)