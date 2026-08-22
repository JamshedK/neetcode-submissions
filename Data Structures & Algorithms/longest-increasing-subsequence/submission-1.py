class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [None] * len(nums)
        def dfs(i):
            if dp[i] != None: 
                return dp[i]
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            dp[i] = best
            return dp[i]
    
        res = 0
        for i in range(len(nums)):
            res = max(dfs(i), res)
        return res