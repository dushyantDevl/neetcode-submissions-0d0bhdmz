# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # Element Found
            # When key's node has either one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # When key's node has 2 children
            ## either replace the node with 1st inorder successor or 1st inorder predecessor
            else:
                successor = self.getSuccessor(root)
                root.val = successor.val
                # now delete successor node
                ## pass root.right to know the parent or some grand parent of successor
                root.right = self.deleteNode(root.right, successor.val)

        return root

    def getSuccessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # One step right then keep going left\
        curr = root.right
        while curr and curr.left:
            curr = curr.left
        return curr