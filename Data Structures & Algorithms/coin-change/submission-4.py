class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        for i in range(0, amount + 1):
            dp[i] = 0

        # dfs(i) returns the minimum number of coints needed to make up the target amount
        # base case, if amount < 0, return 0
        # recursive case: 
            # loop through all possible coins, subtract
        # def dfs(amount):
        #     if amount in dp: 
        #         return dp[amount]
        #     if i < 0:
        #         return 0
        #     min_coins = 1
        #     for coin in coins:
        #         dfs(amount - coin)
        for i in range(1, amount + 1):
            # dp[i] = 1 + min(dp[i - coin])
            curr_min = float("inf")
            for coin in coins: 
                if i >= coin: 
                    # print(f"coin: {coin}, i: {i}")
                    curr_min = min(curr_min, dp[i - coin])
                    # print(curr_min)
                dp[i] = curr_min + 1
                # print(f"i = {i}, {dp[i]}")
        return dp[amount] if dp[amount] != float('inf') else -1