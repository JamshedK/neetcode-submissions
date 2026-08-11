# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Goal: Everytime you iterate, pass on the maximum value seen so far
        # set a default max, a global res variable
        # dfs iteration
        # base case: if not null, return None
        # recursive case: start from the root, update maxSoFar and res if needed
        # go to left subtree, pass maxSoFar 
        # go to right subtree, pass maxSoFar
        maxSoFar = -200
        res = 0
        def dfs(root, maxSoFar):
            nonlocal res 
            if not root:
                return None
            if root.val >= maxSoFar:
                res += 1
            maxSoFar = max(maxSoFar, root.val)
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)
        
        dfs(root, maxSoFar)
        return res
        