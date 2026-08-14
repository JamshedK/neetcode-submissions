import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Goal: use a heap of size n
        # max heap or minheap? => maxheap so we can pop the top and replace
        # when to replace: if the new point is smaller than top
        maxheap = []
        for point in points: 
            x, y = point
            distance = math.sqrt(math.pow((x-0),2) + math.pow((y-0),2))
            print(distance)
            # if maxheap size is smaller than k, just add
            if len(maxheap) < k: 
                heapq.heappush(maxheap, [-distance, point])
            
            # otherwise, if distance is bigger than top, pop the top and add the new point
            elif distance < (0-maxheap[0][0]):
                heapq.heappop(maxheap)
                heapq.heappush(maxheap, [-distance, point])

        return [p for d, p in maxheap] 

