# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            temp = curr.next
            if prev == dummy:
                prev.next = None
                curr.next = None
            else:
                curr.next = prev
            prev = curr
            curr = temp
        return prev