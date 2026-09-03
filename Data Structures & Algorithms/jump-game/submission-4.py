class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(target - 1, -1, -1):
            # if target can be reached for i, then update target
            max_step = nums[i]
            # print(f"{i}, {max_step}, {target}")
            if i + max_step >= target:
                # print(f"can reach {target} from {i} ")
                target = i
            
        return target == 0