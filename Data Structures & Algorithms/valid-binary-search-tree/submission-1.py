# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # traverse to the left and right 
        def dfs(root, start, end):
            # base case:
            if root is None:
                return True
            
            if root.val >= end or start >= root.val:
                return False

            left = dfs(root.left, start, root.val)
            right = dfs(root.right, root.val, end)

            return left and right

        return dfs(root, float('-inf'), float('inf'))
        
        