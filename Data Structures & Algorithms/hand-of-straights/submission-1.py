from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base case, return false is len(hand) % groupSize != 0
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        hand = sorted(hand)
        for num in hand:
            # get the curr min
            if num not in count: 
                continue
            # keep looping groupSize times
            for i in range(groupSize):
                if num not in count: 
                    return False
                if num in count: 
                    count[num] -= 1
                if count[num] == 0:
                    del count[num]
                num += 1
        return True


