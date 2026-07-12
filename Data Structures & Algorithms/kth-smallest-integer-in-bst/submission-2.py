# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        #count = 0

        while cur or stack:
            # save all nodes inbetween
            # visit as far left
            while cur:
                stack.append(cur)
                cur = cur.left

            # process current
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val

            cur = cur.right

            # go right
