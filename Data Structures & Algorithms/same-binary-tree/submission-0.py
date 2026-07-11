# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # same root
        # same left
        # same right
        if p is None and q is None:
            return True

        if p is None:
            return False

        if q is None:
            return False
            
        isTreeLeft = self.isSameTree(p.left, q.left)
        isTreeRight = self.isSameTree(p.right, q.right)

        if p.val != q.val:
            return False

        if not isTreeLeft: 
            return False
        
        if not isTreeRight:
            return False

        return True

        
        