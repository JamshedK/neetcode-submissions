class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums: 
            if n == 0:
                currMin, currMax = 1, 1
                continue
            temp = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * currMin, n * temp, n)  

            res = max(currMax, res)
        return res