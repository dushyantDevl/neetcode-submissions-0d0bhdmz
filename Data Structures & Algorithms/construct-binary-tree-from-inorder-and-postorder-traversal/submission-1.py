# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)): inMap[inorder[i]] = i
        return self.helpBuildTree(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, inMap)
    
    def helpBuildTree(self, inorder, inL, inR, postorder, postL, postR, inMap):
        if inL > inR or postL > postR:
            return None
        
        root = TreeNode(val=postorder[postR])
        rootIdx = inMap[root.val]

        root.left = self.helpBuildTree(
                        inorder, inL, rootIdx-1, 
                        postorder, postL, postL+(rootIdx-inL)-1, 
                        inMap
                    )
        root.right = self.helpBuildTree(
                        inorder, rootIdx+1, inR, 
                        postorder, postL+(rootIdx-inL), postR-1,
                        inMap
                    )
        
        return root
