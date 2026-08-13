import heapq
class KthLargest:
    # Goal use heaps, store upto k elements, the top is minimum

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums: 
            # check if heap size does not exceed k 
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            # check if top is smaller than num, then pop it and add value
            elif self.heap[0] < num:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)
            

    def add(self, val: int) -> int:
        # check if heap size does not exceed k 
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # check if top is smaller than num, then pop it and add value
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
