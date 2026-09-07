from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        farthest = {}
        for i in range(len(s)):
            farthest[s[i]] = i
        size, end = 0, 0
        res = []
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, farthest[c])
            if end == i: 
                res.append(size)
                size = 0 
        return res



