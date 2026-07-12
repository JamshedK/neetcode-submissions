class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set minimum to the first day
        # set max_profit to 0
        min_price, max_profit = prices[0], 0
        for price in prices[1:]: 
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit