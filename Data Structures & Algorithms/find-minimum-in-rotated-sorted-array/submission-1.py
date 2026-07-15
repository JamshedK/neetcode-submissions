class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # check if array already sorted, return l
            if nums[l] <= nums[r]:
                return nums[l]
            # otherwise, get the middle and check which side is sorted
            mid = (l + r) // 2
            # check if l is smaller than middle, means left is sorted
            if nums[l] <= nums[mid]:
                # left is sorted, so we need to search right
                l = mid + 1
            # otherwise, right is sorted, need to search left
            else: 
                # right is sorted, search left
                r = mid 

