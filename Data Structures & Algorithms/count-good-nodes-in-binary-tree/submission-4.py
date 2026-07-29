# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, current_max):
            if root is None:
                return 0


            left = dfs(root.left, max(current_max, root.val))
            right = dfs(root.right, max(current_max, root.val))

            node_valid = 1 if root.val >= current_max else 0

            return left + right + node_valid
        return dfs(root, float('-inf'))