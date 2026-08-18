# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Goal: pointer for each linkedlist, compare add the smallest one and then increment that point
        # use a minheap, push all the top 
        minheap = []
        for i, node in enumerate(lists):
            if node is not None: 
                minheap.append((node.val, i, node))
        
        heapq.heapify(minheap)

        dummy = ListNode(0)
        curr = dummy

        while len(minheap) > 0: 
            # pop the top of the heap
            val, i, node = heapq.heappop(minheap)
            # make curr.next point to the node we popped out
            temp = node.next
            curr.next = node
            node.next = None
            # update curr
            curr = node 
            # if temp is not None, add to heapq
            if temp is not None: 
                heapq.heappush(minheap, (temp.val, i, temp))
    
        return dummy.next