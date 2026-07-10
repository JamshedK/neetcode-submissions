class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # if total is bigger, move right
                if total <  0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates for l
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # skip duplicates for r
                    while r > l and r < len(nums) -1 and nums[r] == nums[r+1]:
                        r += 1
        return res