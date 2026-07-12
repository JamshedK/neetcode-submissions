class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array  O(NlogN) and it becomes a two sum problem
        nums = sorted(nums)
        last_index = len(nums) - 1
        final_list = []
        # start with the first element
        for i in range(last_index + 1):
            # skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # run a two sum right after element i
            l, r = i + 1, last_index
            target = 0 - nums[i]
            while l < r:
                res = (nums[l] + nums[r])
                # if result is equal, add to result, increase move both l and r
                if res == target:
                    final_list.append([nums[i], nums[l], nums[r]])
                    # skip duplicates and move both l and r
                    
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    # move both l, r 
                    l += 1
                    r -= 1
                # if result is small, move left  
                elif res < target:
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    # move left
                    l += 1
                # else move right
                else: 
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    # move r 
                    r -= 1
            
        return final_list

