import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1: 
            # pop 2 elements
            y = 0 - heapq.heappop(heap)
            x = 0 - heapq.heappop(heap)
            if x < y: 
                y = y - x
                heapq.heappush(heap, -y)

        if len(heap) == 1:
            return 0 - heap[0]
        return 0