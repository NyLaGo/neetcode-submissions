class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')

        for num in prices:
            min_price = min(min_price, num)
            profit = max(profit, num - min_price)

        return profit