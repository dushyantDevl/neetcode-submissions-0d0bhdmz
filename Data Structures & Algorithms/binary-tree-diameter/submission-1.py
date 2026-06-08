# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def findMaxHeight(node: Optional[TreeNode]):
            nonlocal res

            if not node:
                return 0
            
            leftHeight = findMaxHeight(node.left)
            rightHeight = findMaxHeight(node.right)

            res = max(res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        findMaxHeight(root)
        return res