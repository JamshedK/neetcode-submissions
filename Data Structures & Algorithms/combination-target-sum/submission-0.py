class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Goal: backtracking, at every step we make n decisions, to include each number separately

        # base case: if current path sum == target, add the subset and then return 
        # if sum != target, we also stop
        # recursive case, loop through every element in nums and call dfs
        res = []
        def dfs(subset, curr_sum, i):
            if curr_sum == target:
                res.append(subset.copy())
                return 
            if i >= len(nums) or curr_sum > target:
                return 
            # include that number 
            subset.append(nums[i])
            dfs(subset, curr_sum + nums[i], i)
            # exclude that number
            subset.pop()
            dfs(subset, curr_sum, i + 1)

        dfs([], 0, 0)
        return res