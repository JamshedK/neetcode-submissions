# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        l, r = dummy, dummy
        
        for i in range(n):
            r = r.next
        
        # now move until r.next is not null
        while r.next is not None:
            r = r.next
            l = l.next
        
        # update the pointers
        l.next = l.next.next

        return dummy.next
