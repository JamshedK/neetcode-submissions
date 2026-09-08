class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  
        if not nums: 
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        # for every permutation in perms, add num in every position
        for p in perms: 
            # for every position in the current permutation
            for i in range(0, len(p) + 1):
                # make a copy
                new_copy = p.copy()
                new_copy.insert(i, nums[0])
                res.append(new_copy)

        return res
