# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = []
        def dfs(root):
            if not root: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # compare if difference is 1
            if abs(left - right) <= 1:
                res.append(True)
            else:
                res.append(False)
            return 1 + max(left, right)
        dfs(root)
        for b in res:
            if b == False:
                return False

        return True
