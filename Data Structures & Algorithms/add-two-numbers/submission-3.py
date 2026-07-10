# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0 
            total = val1 + val2 + carry
            if total >= 10:
                # update the total
                total -= 10
                carry = 1
            else:
                carry = 0
            # print(total)
            # create a new node
            node = ListNode(total)
            curr.next = node
            curr = node
            # update l1 and l2
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry:
            node = ListNode(carry)
            curr.next = node
        return dummy.next
