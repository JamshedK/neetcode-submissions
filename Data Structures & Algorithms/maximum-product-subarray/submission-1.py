class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val, max_val = nums[0], nums[0]
        res = max(nums)
        for num in nums[1:]:
            temp = min_val
            min_val = min(num, max_val * num, min_val * num)
            max_val = max(num, temp * num, max_val * num)
            res = max(res, max_val)
        return res 