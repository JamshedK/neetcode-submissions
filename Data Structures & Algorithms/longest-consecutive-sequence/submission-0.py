class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2,20,4,10,3,4,5 -> 2, 3, 4, 5
        # put it all into a hashmap, find the smallest element
        # keep removing until you stop 

        hashset = set(nums)
        max_count = 0
        while hashset:
            smallest = min(hashset)
            original = smallest
            # keep removing until the stop condition is met
            count = 1
            while smallest + 1 in hashset:
                hashset.remove(smallest + 1)
                count += 1
                smallest = smallest + 1
            # remove the current element from hashset
            hashset.remove(original)
            # update the count
            max_count = max(count, max_count)
            
        return max_count