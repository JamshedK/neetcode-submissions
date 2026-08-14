import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Goal: Use a k-sized heap
        # Minheap or maxheap?: The top needs to be the smallest item, because we need k'th largest
        # How to insert: 
            # if heapsize is < k: just keep adding
            # other if the new number is bigger than top of heap, pop top and then insert
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            elif minheap[0] < num: 
                heapq.heappop(minheap)
                heapq.heappush(minheap, num)

        return minheap[0]
