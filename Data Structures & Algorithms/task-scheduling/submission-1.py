import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Goal: Schedule the most frequent task, greedy
        # Use maxheap and queue
        # convert tasks into count, and add counts as maxheap
        # at every iteration, we pop from maxheap, calculate when it it's available
        # add to queue (count, available_time)
        # if a task is available, we add to the queue
        count = {}
        for task in tasks: 
            count[task] = count.get(task, 0) + 1
        maxheap = [-val for val in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque()
        while q or maxheap:
            # possible that maxheap is empty or a task is available from queue
            if not maxheap or (q and q[0][1] == time):
                count, available_time = q.popleft() 
                time += available_time - time # if task not available, force cooldown
                heapq.heappush(maxheap, count)
            # pop the top from maxheap
            count = heapq.heappop(maxheap)
            count += 1
            # increase time
            time += 1
            if count != 0:
                q.append([count, time + n])
        
        return time

            
            
