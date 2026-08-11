# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Goal: Keep an interval, if we move left, update max
        # if we move right, update min, because everything needs to be greater 
        # resursive parameters, pass min, max, 
        # base case: return true
        # recursive case: 
            # if we moved left, update min
            # if we moved right, update max

        def dfs(root, minVal, maxVal):
            if not root:
                return True
            return (minVal < root.val and root.val < maxVal  
                and dfs(root.left, minVal, root.val)  
                and dfs(root.right, root.val, maxVal) )
        return dfs(root, float('-inf'), float('inf')) 
