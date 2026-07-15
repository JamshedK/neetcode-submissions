class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_hours = r 
        def calculate_hours(k):
            total = 0
            for pile in piles: 
                total += math.ceil(pile/k)
            # print(f"k = {k} total: {total}")
            return total 

        while l <= r: 
            # see how long it takes to eat all the bananas
            mid = (l + r) // 2
            hours = calculate_hours(mid)
            # if hours is smaller, then we need to increase l
            if hours > h: 
                # print('Updated l')
                l = mid + 1
            # if hours is bigger or equal, update r and min_hours
            else:
                min_hours = min(min_hours, mid)
                r = mid - 1
        return min_hours
