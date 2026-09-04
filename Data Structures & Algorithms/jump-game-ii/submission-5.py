class Solution:
    def jump(self, nums: List[int]) -> int:
        # keep jumping but always jump the maximum 
        res = len(nums)
        last_index = len(nums) - 1
        dp = {last_index:0}
        def dfs(i):
            if i in dp:
                return dp[i]
            if nums[i] == 0:
                return float('inf')
            end = min(last_index, i + nums[i])
            res = float('inf')
            for j in range(i + 1, end + 1):
                res = min(1 + dfs(j), res)
            dp[i] = res
            return res
        return dfs(0) 
