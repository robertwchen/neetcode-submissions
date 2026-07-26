# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(root):
            if not root:
                return 0

            nonlocal max_sum

            left = dfs(root.left) # retursn me the max length
            right = dfs(root.right) 

            max_left = max(0, left)
            max_right = max(0, right)
            max_sum = max(max_sum, root.val + max_left + max_right)

            return root.val + max(left, right, 0)
        dfs(root)
        return max_sum