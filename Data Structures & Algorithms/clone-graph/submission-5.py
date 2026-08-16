"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # add the first node to the qeuee, with neighbors None and parent None
        # goal is: when you iterate to neighbors, you create a copy for each neighbor and parent.neighbors.append(curr_node)
        # once you created all the neighbors, add the parent to visited
        # each queue item is (node, parent)
        if not node: 
            return None
        q = deque([node])
        visited = set()
        hashmap = defaultdict()
        def dfs(node):
            if node in visited: 
                return 
            visited.add(node)
            hashmap[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)
        dfs(node)
        # set the parent node for return function
        res_node = hashmap[node]
        visited = set([node])
        while q: 
            # pop
            node = q.popleft()
            # add all neighbors to the queue 
            for nei in node.neighbors: 
                # add nei to the queue
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

            # loop through the neibors, and add them to the list of parents neighbors
            copy_node = hashmap[node]
            # print(f"current node: {copy_node.val} \nneighbors: ")
            for nei in node.neighbors:
                # print(nei.val)
                copy_node.neighbors.append(hashmap[nei])
        # because it's undirected
        return res_node
        

        