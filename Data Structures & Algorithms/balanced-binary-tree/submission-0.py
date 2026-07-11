# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.tree_height(root) < 0:
            return False
        return True

    def tree_height(self, root):
        if root is None:
            return 0
        
        left_balanced = self.tree_height(root.left)
        right_balanced = self.tree_height(root.right)
        difference = abs(left_balanced - right_balanced)

        if difference > 1:
            return -1
        if left_balanced == -1 or right_balanced  == -1:
            return -1

        return max(left_balanced, right_balanced) + 1

        

        
        
        