#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_val = 2**32
        for i in range(len(prices)):
            if prices[i] <  min_val:
                min_val = min(prices[i], min_val)
            else:
                if prices[i] - min_val > profit:
                    profit = prices[i] - min_val
        return profit
