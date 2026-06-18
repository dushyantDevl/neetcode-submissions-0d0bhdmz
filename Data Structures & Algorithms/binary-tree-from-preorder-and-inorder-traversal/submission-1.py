# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)): inMap[inorder[i]] = i
        return self.helpBuildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)

    def helpBuildTree(self, preorder, preL, preR, inorder, inL, inR, inMap):
        if preL > preR or inL > inR:
            return None
        
        root = TreeNode(val=preorder[preL]) # current root (first element of the preorder subarray)
        rootIdx = inMap[root.val]
        noOfLeftNodesInorder = rootIdx - inL

        # Form left and right subtree by sending the subarray with which they will going to form
        root.left = self.helpBuildTree(
                        preorder, preL + 1, preL + noOfLeftNodesInorder,
                        inorder, inL, rootIdx - 1,
                        inMap
                    )

        root.right = self.helpBuildTree(
                        preorder, preL + noOfLeftNodesInorder + 1, preR,
                        inorder, rootIdx + 1, inR,
                        inMap
                    )

        return root
