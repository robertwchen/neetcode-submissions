# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)
        q_set = set(q_path)
        
        for val in p_path:
            if val in q_set:
                return val
        return None

        # make one of them a set
        # if find a match return that value (first time they match)


    def find_path(self, root, target):
        if root is None:
            return None
        
        if root.val == target.val:
            return [ root ]

        left_path = self.find_path(root.left, target)
        if left_path is not None:
            left_path.append(root)
            return left_path
        
        right_path = self.find_path(root.right, target)
        if right_path is not None:
            right_path.append(root)
            return right_path
        
        return None

        