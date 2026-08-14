class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Goal at each backtracking step, include everything except the current number
        # base case: if the new array size == len(nums), add to res and return 
        # recursive case, loop through, ignore all the ones that have been seen

        
        res = []
        seen = set([])
        def dfs(curr, seen):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            
            for num in nums:
                # skip numbers that have already been seen
                if num in seen: 
                    continue
                # process
                seen.add(num)
                curr.append(num)
                dfs(curr, seen)
                # backtrack
                seen.remove(num)
                curr.pop()
                # dfs(curr, seen)
        
        dfs([], seen)
        return res
                
                