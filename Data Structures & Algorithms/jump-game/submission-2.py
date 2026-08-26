class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dfs(i) => whether you can jump to the end from position i
        # base case: i == last_index, return True
        # if nums[i] == 0, return False
        # recurrence for i in range(len(nums[0])): pass each of them to dfs(i)
        dp = [None] * len(nums)
        dp[len(nums) - 1] = True
        def dfs(i):
            if i >= len(nums):
                return False
            if dp[i] is not None: 
                return dp[i]
            if nums[i] == 0:
                return False
            num = nums[i]
            temp = False
            for jump in range(num, 0, - 1):
                res = dfs(i + jump)
                temp = res or temp
            dp[i] = temp
            return dp[i]
        return dfs(0)
            
