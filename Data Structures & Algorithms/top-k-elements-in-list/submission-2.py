from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        last_index = len(nums)
        array = [None] * (last_index + 2)
        for (key, value) in count.items():
            if array[value] is None: 
                array[value] = [key]
            else:
                array[value].append(key)
        res = []
        last_index = len(array) - 1
        for i in range(last_index, 0, -1):
            if array[i] != None:
                for j in array[i]:
                    res.append(j)
                    if len(res) == k: 
                        return res            

            