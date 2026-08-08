from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,r = 0, 0
        longest = 0
        while r < len(s): 
            # add r to count
            count[s[r]] = 1 + count.get(s[r], 0)

            # check if window invalid
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest