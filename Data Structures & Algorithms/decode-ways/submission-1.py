class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1] * len(s)
        def dfs(i):
            # if there is nothing left in string, we return 1
            if i == len(s):
                return 1
            # if i = 0, return 0
            if s[i] == '0': 
                return 0
            if dp[i] != -1:
                return dp[i]
            
            # always take the one digit
            left = dfs(i + 1)
            right = 0 
            if int(s[i:i + 2]) >= 10 and int(s[i:i + 2]) <= 26:
                right = dfs(i + 2)
            dp[i] = left + right

            return dp[i]
        
        return dfs(0)
            
        