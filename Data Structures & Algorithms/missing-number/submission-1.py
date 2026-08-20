class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= (i ^ nums[i])
        # print(res)
        return res ^ len(nums)