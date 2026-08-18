class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        def is_palindrome(l, r):
            nonlocal counter
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                counter += 1
        
        for i in range(len(s)):
            # odd strings
            l, r = i, i
            is_palindrome(l, r)
            
            # even strings
            l, r = i, i + 1
            is_palindrome(l, r)
        
        return counter