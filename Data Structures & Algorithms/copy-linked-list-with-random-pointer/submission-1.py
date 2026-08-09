"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # go through the head and then create an array [Node, random]

        curr = head
        hashmap = {None: None}
        dummy = Node(0, None, None)
        prev = dummy
        # first iteration, create copies of the nodes without random pointer
        while curr: 
            node = Node(curr.val, None, None)
            hashmap[curr] = node
            # update pointers
            prev.next = node
            prev = node
            curr = curr.next
        
        # now update random pointers
        original = head
        copy = dummy.next
        while original: 
            # update the random pointer for the newly copied nodes
            copy.random = hashmap[original.random]
            # update both original and copy pointers
            original = original.next
            copy = copy.next

        return dummy.next
            