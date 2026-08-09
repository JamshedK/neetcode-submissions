# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # go halfway through
        second = head
        prev = None
        for i in range((n + 1) // 2):
            prev = second
            second = second.next
        
        # split into two lists
        prev.next = None

        # reverse the second list
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first, second = head, prev
        # now do the replacements
        for i in range(n//2):
            temp_first, temp_second = first.next, second.next 
            first.next = second # 0.next = n-1
            second.next = temp_first  # n-1.next = 0.next
            first = temp_first
            second = temp_second
        

        




        

