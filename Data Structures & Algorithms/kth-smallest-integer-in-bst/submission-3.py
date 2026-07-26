# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        def in_order(root, k):
            nonlocal count

            if root is None:
                return None
            

            left = in_order(root.left, k)
            if left:
                return left
           
            count += 1
            if count == k:
                return root.val

            right = in_order(root.right, k)
            if right: 
                return right
        return in_order(root, k)

            



