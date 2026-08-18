class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two cases
            # if len(s) is odd, take out the middle one
            # if string is even, split into two
        # two passes, 
        # first pass consider a single string as the middle and then go to l and r side
        # second pass, consider two strings at a time and check if palindrom
        
        def check_palindrome(l, r):
            length = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                length += 2
            return [length, l + 1, r - 1]
        max_len = [0,0,0]
        for i in range(1, len(s)):
            # check palindrome from 
            length, l, r = check_palindrome(i - 1, i + 1)
            if length > max_len[0]:
                max_len = [length, l, r]
        
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                length, l, r = check_palindrome(i, i + 1)
                if length > max_len[0]:
                    max_len = [length, l, r]
        l, r = max_len[1], max_len[2]
        return s[l: r + 1]



