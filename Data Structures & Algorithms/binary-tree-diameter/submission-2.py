# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# where am I
    # at some point on the binary tree
# what am I doing
    # returning depth, comparing to global diameter max
# what do I return
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        def longest_length(root):
            if not root:
                return 0
            print(root.val)
            nonlocal diameter

            left = longest_length(root.left)
            right = longest_length(root.right)

            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        longest_length(root)
        return diameter

        