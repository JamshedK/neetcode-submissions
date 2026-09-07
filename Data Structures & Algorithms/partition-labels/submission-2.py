from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        farthest = {}
        for i in range(len(s)):
            farthest[s[i]] = i
        lastIndex = 0
        res = []
        while l < len(s):
            r = l
            while True:
                # get the current ch 
                ch = s[r]
                # update the farthest 
                lastIndex = max(lastIndex, farthest[ch])
                if lastIndex == r: 
                    res.append(r - l + 1)
                    break
                r += 1
            l = r
            l += 1
        return res



