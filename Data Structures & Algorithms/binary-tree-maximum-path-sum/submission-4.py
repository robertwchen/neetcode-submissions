# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # recursively at each node look left and right
        self.maxSum = float('-inf')

        # return max of left and max or right
        self. _maxPathSum(root)
        return self.maxSum

    def _maxPathSum(self, root):
        # base case if 0 return 0
        if root is None:
            return 0
        
        leftSum = self._maxPathSum(root.left)
        rightSum = self._maxPathSum(root.right)
        leftGain = max(0, leftSum)
        rightGain = max(0, rightSum)
        current = root.val
        currentSum = root.val + leftGain + rightGain
        if currentSum > self.maxSum:
            self.maxSum = currentSum
        return max(leftGain, rightGain) + root.val
