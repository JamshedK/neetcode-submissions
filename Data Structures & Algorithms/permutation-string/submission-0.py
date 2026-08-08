from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        windowLen = len(s1)
        l, r = 0, windowLen - 1
        while r < len(s2):
            # print(s2[l:r+1])
            count2 = Counter(s2[l:r+1])
            if count1 == count2:
                return True
            l += 1
            r = l + windowLen - 1

        return False