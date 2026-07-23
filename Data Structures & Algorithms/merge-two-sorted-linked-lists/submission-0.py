# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        root = ListNode()
        curr = root

        while list1 or list2: 
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')
            
            if val1 < val2:
                min_val = val1
                if list1: 
                    list1 = list1.next
            else: 
                min_val = val2
                if list2: 
                    list2 = list2.next
            # create a new node from min_val
            new_node = ListNode(min_val)
            curr.next = new_node
            curr = new_node

        return root.next