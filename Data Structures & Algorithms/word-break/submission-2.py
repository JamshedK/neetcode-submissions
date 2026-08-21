class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # First find the longest word in wordDict O(m * n)
        # store wordDict in a hashmap
        # Keep going through the string s until
            # you run out of space
            # go beyond the longest word
            # found a word that exists in wordDict
        # if you found a word in wordDict, call the same function on wordBreak(l + 1) pointer
        # if you reach the end, and that is a word, return True
        # otherwise, return False

        hashset = set(wordDict)
        dp = [None] * len(s)
        def dfs(i):
            # if we reach end of string, return True
            if i == len(s):
                return True
            if dp[i] is not None: 
                return dp[i]
            for j in range(i + 1, len(s) + 1):
                if str(s[i:j]) in hashset: 
                    res = dfs(j)
                    if res == True:
                        dp[i] = True 
                        return True
            dp[i] = False
            return False
        return dfs(0)

            