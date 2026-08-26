class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set target as the last element
        # right pointer, starts from one below target, keep iterating until you can reach the target
        # if the target is reachable, the current poitner becomes the new target
        # if target == 0, then it's reachable. Otherwise, return false
        target = len(nums) - 1
        curr_idx = target - 1
        
        while curr_idx >= 0:
            max_jump = nums[curr_idx]
            if (curr_idx + max_jump) >= target:
                target = curr_idx
            curr_idx -= 1
        
        return target == 0
            

            
