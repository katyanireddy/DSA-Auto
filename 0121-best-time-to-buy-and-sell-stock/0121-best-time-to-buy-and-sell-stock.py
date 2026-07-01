class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i, num in enumerate(prices):
            if num < buy:
                buy = num
            profit = num - buy
            max_profit = max(max_profit, profit)

        return max_profit