class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursion
        # dfs(n) returns x ^ n  
        # recurrence if number is odd, dfs(n) = dfs(n / 2) * dfs(n / 2)
        # if number is even dfs(1) * dfs(n / 2) * dfs(n / 2)
        dp = {1: x, 0: 1 }
        def dfs(n):
            if n in dp:
                return dp[n]
            # if even
            if n % 2 == 0:
                half = dfs(n // 2)
                dp[n] = half * half
            else:
                half = dfs(n // 2)
                dp[n] = half * half * x
            return dp[n]
        res = dfs(abs(n))
        if n < 0: 
            return 1 / res
        return res