class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            # for every coin, calculate the minimum it takes
            min_coins = float('inf')
            for coin in coins: 
                if i - coin < 0: 
                    continue
                min_coins =min(min_coins, 1 + dp[i - coin])
            dp[i] = min_coins 
                
        # # tryint the recursive case first
        # def dfs(amount):
        #     if amount < 0: 
        #         return float('inf')
        #     if dp[amount] != -1:
        #         return dp[amount]
        #     if amount == 0: 
        #         return 0
        #     min_val = float('inf')
        #     for coin in coins: 
        #         res = 1 + dfs(amount - coin)
        #         min_val = min(res, min_val)
        #     dp[amount] = min_val
        #     return dp[amount]
        return dp[amount] if dp[amount] != float('inf') else -1
