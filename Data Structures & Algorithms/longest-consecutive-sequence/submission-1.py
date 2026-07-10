class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2,20,4,10,3,4,5 -> 2, 3, 4, 5
        # put it all into a hashmap, find the smallest element
        # keep removing until you stop 

        hashset = set(nums)
        max_count = 0
        for num in nums:
            # find a possible starting point for hashset:
            if num - 1 not in hashset:
                count = 1
                while num + 1 in hashset:
                    count += 1
                    num = num + 1
                max_count = max(count, max_count)
        return max_count
