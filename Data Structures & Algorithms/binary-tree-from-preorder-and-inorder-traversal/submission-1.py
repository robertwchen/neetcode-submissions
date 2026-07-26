# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [1 2 3] pre
# [2 1 3] in
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self._buildTree(preorder, inorder)




    def _buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None

        val = preorder[0]
        root = TreeNode(val)
        mid = inorder.index(val)
        left_in_order = inorder[:mid]
        right_in_order = inorder[mid + 1:]
        left_size = len(left_in_order)
        left_pre_order = preorder[1: 1 + left_size]
        right_pre_order = preorder[1 + left_size:]
        root.left = self._buildTree(left_pre_order, left_in_order)
        root.right = self._buildTree(right_pre_order, right_in_order)
        return root
        
        