# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(val=postorder[-1])
        subRootIdx = inorder.index(root.val)

        root.left = self.buildTree(inorder[:subRootIdx], postorder[:subRootIdx])
        root.right = self.buildTree(inorder[subRootIdx+1:], postorder[subRootIdx:-1])

        return root