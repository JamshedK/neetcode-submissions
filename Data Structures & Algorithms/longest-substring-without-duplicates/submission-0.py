class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l, r = 0, 0
        max_len = 0
        while r < len(s):
            # check if current character not in hashset
            if s[r] not in hashset:
                # keep expanding, add r to hashset and calculate the new max_len
                max_len = max(max_len, r - l + 1)
                hashset.add(s[r])
                r += 1
            # else means current character in hashset
            else:
                # keep expanding l until you remove the element from hashset
                while l < r and s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                # then add r to hashset and increment r
                hashset.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
        return max_len
