# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.in_order_traversal(root, values)

        return values[k - 1]

    
    def in_order_traversal(self, root, values):
        if root is None:
            return None
        
        self.in_order_traversal(root.left, values)

        values.append(root.val)

        self.in_order_traversal(root.right, values)
        return


        