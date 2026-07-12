# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # construct the path
        # store nodes between path
        if root is None:
            return 0
        self.count = 0
        self._goodNodes(root, root.val)
        return self.count


        # pass in count variable
        # pass in a current max height variable
        
    def _goodNodes(self, root, maxAbove):
        # base case 
        if root is None:
            return 

        if root.val >= maxAbove:
            self.count += 1
        
        maxAbove = max(root.val, maxAbove)
        
        self._goodNodes(root.left, maxAbove)
        self._goodNodes(root.right, maxAbove)
        return

        