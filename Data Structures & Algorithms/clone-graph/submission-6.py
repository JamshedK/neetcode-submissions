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
        # you can also make it in one DFS
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            # create a copy of this node
            copy_node = Node(node.val)
            oldToNew[node] = copy_node
            for nei in node.neighbors: 
                oldToNew[node].neighbors.append(dfs(nei))
            # return the copy of the original node
            return oldToNew[node]
        
        return dfs(node) if node is not None else None
        
        
        

        