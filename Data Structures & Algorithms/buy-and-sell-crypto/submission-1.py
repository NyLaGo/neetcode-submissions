class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')

        for num in prices:
            if num < min_price:
                min_price = num
            
            if num - min_price > profit:
                profit = num - min_price

        return profit