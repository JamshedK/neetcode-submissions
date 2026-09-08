class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  
        # base case: if curr = len(3)
        # recursive case: loop through all availabel items, add them to curr 
        res = []
        def dfs(curr, curr_set):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums: 
                if num in curr_set:
                    curr.append(num)
                    curr_set.remove(num)
                    dfs(curr, curr_set)
                    curr.pop()
                    curr_set.add(num)
        
        curr_set = set([num for num in nums])
        dfs([], curr_set)
        
        return res
