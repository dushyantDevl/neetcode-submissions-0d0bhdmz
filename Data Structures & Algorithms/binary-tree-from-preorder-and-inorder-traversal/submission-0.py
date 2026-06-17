# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        ## first node will always be root in preorder at any instance in between of recursion 
        ## calls too since we're sending sublist in recursion (not the whole traversal lists)
        root = TreeNode(val=preorder[0])
        subRootIdx = inorder.index(root.val) # node that separate left and right subtree (parent) 

        # sublists of preorder and inorder here contains all the nodes required to make left subtree
        root.left = self.buildTree(preorder[1:subRootIdx+1], inorder[:subRootIdx])
        # sublists of preorder and inorder here contains all the nodes required to make right subtree
        root.right = self.buildTree(preorder[subRootIdx+1:], inorder[subRootIdx+1:])

        return root