# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal
        values = []
        self.in_order_traversal(root, values)
        print(values)
        return self.is_sorted(values)

    


    def in_order_traversal(self, root, values):
        # process left prodess current process right 
        if root is None:
            return None

        self.in_order_traversal(root.left, values)
        
        values.append(root.val)

        self.in_order_traversal(root.right, values)

        return

    def is_sorted(self, values):
        for i in range(0, len(values) - 1):
            if values[i] >= values[i + 1]:
                return False
        return True
        
        

        
        