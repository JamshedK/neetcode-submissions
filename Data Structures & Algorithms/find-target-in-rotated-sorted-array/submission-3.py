class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            print(nums[l], nums[mid], nums[r])
            # the left is sorted
            if nums[l] <= nums[mid]:
                print('I am called')
                # if target within the range of (l, mid), search this (l, mid - 1)
                if (nums[l] <= target and target < nums[mid]):
                    r = mid - 1
                    print('right updated')
                # else search the right side
                else:
                    l = mid + 1
                    print('Left updated ' + str(l))
            # the right is sorted
            else:
                # if target within the range of (mid, r), serach (mid + 1, r)
                if (nums[mid] < target and target <= nums[r]):
                    l = mid + 1
                # else search the left side 
                else:
                    r = mid - 1
        return - 1