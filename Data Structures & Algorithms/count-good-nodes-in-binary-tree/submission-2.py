# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, curr_max):
            if root is None:
                return 0

            count = 0
            if root.val >= curr_max:
                count += 1

            count += dfs(root.left, max(curr_max, root.val)) + dfs(root.right, max(curr_max, root.val))
            return count
        return dfs(root, float('-inf'))
                
        