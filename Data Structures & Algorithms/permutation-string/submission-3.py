from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count1, count2 = [0] * 26, [0] * 26

        # populate count1 and count2
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1
        
        # calculate initial number of matches
        matches = 0
        for i in range(len(count1)):
            if count1[i] == count2[i]:
                matches += 1
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            # we are currently adding r, update the indexes and matches
            index = ord(s2[r]) - ord('a')
            # update the index
            count2[index] += 1
            # update matches if there is a mismatch
            if count2[index] == count1[index]:
                matches += 1
            elif count2[index] - 1 == count1[index]:
                matches -= 1
            
            # remove l and update matches
            index = ord(s2[l]) - ord('a')
            count2[index] -= 1
            if count2[index] == count1[index]:
                matches += 1
            elif count2[index] + 1 == count1[index]:
                matches -= 1
            # update l
            l += 1
        return matches == 26




