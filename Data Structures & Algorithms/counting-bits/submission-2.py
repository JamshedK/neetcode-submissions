class Solution:
    def countBits(self, n: int) -> List[int]:
        if n < 1:
            return [0]
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1): 
            temp = i >> 1
            # if number if odd
            if i & 1 == 1:
                print(f"i = {i} and shift right {i >> 1}")
                dp[i] = dp[1] + dp[temp]
            # if number is even
            else:
                dp[i] = dp[temp]
        
        return dp
