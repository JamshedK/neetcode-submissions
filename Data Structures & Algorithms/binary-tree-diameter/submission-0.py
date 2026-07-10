# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return 1 + max(height(root.left), height(root.right))
        maxCount = [0]
        def diameter(root):
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            maxCount[0] = max(maxCount[0], leftHeight + rightHeight)
            diameter(root.left)
            diameter(root.right)
        diameter(root)
        return maxCount[0]

