# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # Goal: the breaking point, that is the LCA
        # assume p < q, we can find this out pretty easily
        # case 1: p < q < root.val, then we need to search the left subtree
        # case 2: root.val > p > q, then we need to search the rigth subtree
        # otherwise, the current root is LCA
        p, q = min(p.val, q.val), max(p.val, q.val)
        
        while root: 
            if p < root.val and q < root.val:
                root = root.left
            elif p > root.val and q > root.val:
                root = root.right
            else:
                return root
