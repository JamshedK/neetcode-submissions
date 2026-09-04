class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        while r < len(nums) - 1:
            temp_r = r
            # iterate through l until r, and keep expanding r
            while l <= temp_r:
                r = max(r, l + nums[l])
                l += 1
            # print(l, r)
            count += 1

        return count

