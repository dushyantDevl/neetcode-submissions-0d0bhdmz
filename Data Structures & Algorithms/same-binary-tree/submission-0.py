# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pInorder, qInorder = [], []
        def inorder(node, order):
            if not node:
                return None
            inorder(node.left, order)
            order.append(node.val)
            inorder(node.right, order)
        
        inorder(p, pInorder)
        inorder(q, qInorder)
        
        for i in range(len(pInorder)):
            if pInorder[i] != qInorder[i]:
                return False
            
        return True