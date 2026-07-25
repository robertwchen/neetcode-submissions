# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        first = self.find_node(root, p)
        second = set(self.find_node(root, q))
        
        for root in first:
            if root in second:
                return root
        return None


        # first find left and find right 
        
    def find_node(self, root, target):

        if not root:
            return None 

        if root.val == target.val:
            return [ root ]


        left = self.find_node(root.left, target)
        right = self.find_node(root.right, target)
        
        if left is not None:
            return [*left, root]
        if right is not None:
            return [*right, root]
        
        return None
        

            