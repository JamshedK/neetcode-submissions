# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(height(root.left), height(root.right))
        height(root)
        return self.res
