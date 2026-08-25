class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        best = nums[0]
        for num in nums: 
            currSum = max(num, num + currSum)
            best = max(best, currSum)
        
        return best