from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap_list = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap_list)
        res = []
        for i in range(k):
            value, key = heapq.heappop(heap_list)
            res.append(key)
        return res