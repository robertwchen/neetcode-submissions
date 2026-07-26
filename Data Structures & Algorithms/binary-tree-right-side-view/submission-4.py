# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if root is None:
            return []

        stack = [ (root, 1) ]

        while stack:
            current, height = stack.pop()

            if height > len(vals):
                vals.append(current.val)

            if current.left:
                stack.append((current.left, height + 1))
            if current.right:
                stack.append((current.right, height + 1))
        return vals

        