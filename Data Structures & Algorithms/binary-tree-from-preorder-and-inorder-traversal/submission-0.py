# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # construct pre and inorder
        if len(preorder) == 0:
            return None

        val = preorder[0]
        root = TreeNode(val)
        mid = inorder.index(val)
        left_len = len(inorder[0:mid])

        root.left = self.buildTree(preorder[1: left_len + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[left_len + 1:], inorder[mid + 1:])
        return root
        