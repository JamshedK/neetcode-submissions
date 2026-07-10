class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            # check if the array is sorted
            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            # inflection point is on the right, means left is sorted
            if nums[l] <= nums[mid]:
                # left is sorted, check mid + 1 is less than mid
                if nums[mid+1] < nums[mid]:
                    return nums[mid + 1]
                # otherwise check the right side
                l = mid + 1
            # check if inflection point is on the left, right is sorted
            else:
                # right is sorted, mid - 1 if greater, return mid
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                # otherwise, check the left
                l = mid - 1
        return 0