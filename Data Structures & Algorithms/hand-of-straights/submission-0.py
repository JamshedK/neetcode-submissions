from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base case, return false is len(hand) % groupSize != 0
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        
        while count:
            # get the curr max 
            curr_max = max(count.keys())
            # keep looping groupSize times
            n = curr_max
            for i in range(groupSize):
                if n not in count: 
                    return False
                if n in count: 
                    count[n] -= 1
                if count[n] == 0:
                    del count[n]
                n -= 1
        return True


