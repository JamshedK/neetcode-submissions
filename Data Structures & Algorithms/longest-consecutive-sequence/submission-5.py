class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add everything into set
        # loop through all the elements
        # if element - 1 and element + 1 don't exist, just skip, means there is no sequence
        # if not (element - 1), means it's start of the sequence
        # if not (element + 1), means end of sequence
        # otherwise middle of sequence, we can just skip, because we will find beginning of the sequence at some point
        if not nums:
            return 0
        hashset = set(nums)
        max_length = 1
        for num in nums: 
            if (num - 1) not in hashset and (num + 1) not in hashset: 
                continue
            # beginning of the sequence
            if not (num - 1) in hashset:
                length = 0
                while num in hashset: 
                    length += 1
                    num = num + 1
                max_length = max(length, max_length)
            # end of the sequence
            elif not (num + 1) in hashset:
                length = 0
                while num in hashset: 
                    length += 1
                    num = num - 1
                max_length = max(length, max_length)
            else:
                continue
        return max_length
