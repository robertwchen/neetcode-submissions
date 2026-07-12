# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs from right to left
        # initialize stack contains (node.val, height)
        stack = [ (root, 0)]
        results = []
        # add results array
        if root is None:
            return []

        while stack:
            current, height = stack.pop()
            
            if len(results) == height:
                results.append(current.val)
            
            if current.left is not None:
                stack.append((current.left, height + 1))
            if current.right is not None:
                stack.append((current.right, height + 1))
        return results
            # process current
            # if first time see this height then add to the array
            # add left to stack
            # add right to stack

        