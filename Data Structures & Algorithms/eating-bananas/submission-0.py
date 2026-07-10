import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [3,6,7,11], h = 8 
        # 1, 2, 3, 4, 5, 6, 7, 8 => 4
        # 0 + 7 // 2 = 3
        # 3 per hour => min_hours = 10 hours, too long need to increase eating speed
        # l = 4, r = 8
        max_per_hour = max(piles)
        l, r = 1, max_per_hour
        minimum = max_per_hour
        while l <= r and l >= 0:
            mid = (l + r) // 2
            # calculate how many hours it takes with the current b_per_h rate
            min_hours_taken = self.calculateHours(piles, mid)

            # if min_hours_taken is less or equal h, update minimum and r
            if min_hours_taken <= h:
                # update the minimum
                minimum = min(minimum, mid)
                r = mid - 1
            # it's taken too long, need to increase the eating speed
            else:
                l = mid + 1
        return minimum
    
    def calculateHours(self, piles, b_per_h):
        total = 0
        for item in piles:
            min_hours = math.ceil(item/b_per_h)
            total += min_hours
        return total