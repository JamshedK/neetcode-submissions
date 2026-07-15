class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # get the middle index
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if l and mid are sorted
            if nums[l] <= nums[mid]:
                # print('left sorted')
                # if target smaller than middle, search left side
                if nums[l] <= target < nums[mid]:
                    # print('checking left side')
                    r = mid - 1
                # otherwise, search right side
                else: 
                    # print('checking right side')
                    l = mid + 1
            # else, right side is sorted
            else: 
                # if target is bigger than middle, search right
                if nums[mid] < target <= nums[r]: 
                    l = mid + 1
                # otherwise, search the left
                else:
                    r = mid - 1
        return -1 