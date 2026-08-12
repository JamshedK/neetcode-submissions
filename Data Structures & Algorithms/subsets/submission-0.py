class Solution:        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, index):
            if index < 0:
                res.append(subset)
                # print(subset)
                return 
            dfs((subset + [nums[index-1]]), index - 1)
            dfs(subset, index - 1)
        subset = []
        dfs(subset, len(nums) - 1)
        return res