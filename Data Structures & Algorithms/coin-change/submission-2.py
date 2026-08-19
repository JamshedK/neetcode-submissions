class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        # tryint the recursive case first
        def dfs(amount):
            if amount < 0: 
                return float('inf')
            if dp[amount] != -1:
                return dp[amount]
            if amount == 0: 
                return 0
            min_val = float('inf')
            for coin in coins: 
                res = 1 + dfs(amount - coin)
                min_val = min(res, min_val)
            dp[amount] = min_val
            return dp[amount]
            
        dfs(amount)
        return dp[amount] if dp[amount] != float('inf') else -1  
