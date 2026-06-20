# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Postorder traversal so that we go from leaf to root (and not the other way around)
        # and it also take care of deleting the parent node if somehow it becomes a target 
        # leaf node after deleting the laef node which was its child
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.left == root.right == None and root.val == target:
            return None # convert the target node to NULL

        return root