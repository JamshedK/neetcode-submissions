# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2:
                return  True
            if root1 and root2 and root1.val == root2.val:
                return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
            else:
                return False
        res = []
        def isSubtree(root, subRoot):
            nonlocal res
            # do a dfs and check whether each root is the same as subroot
            if not root:
                return 
            res.append(sameTree(root, subRoot))
            isSubtree(root.left, subRoot)
            isSubtree(root.right, subRoot)
        isSubtree(root, subRoot)
        for flag in res:
            if flag == True:
                return True
        return False