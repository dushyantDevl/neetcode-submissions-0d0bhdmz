# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # returns list containing 2 elements: [if tree/subtree is balance or not, height of tree/subtree]
        def helper(root):
            if not root: 
                return [True, 0]
            
            traverseLeft, traverseRight = helper(root.left), helper(root.right)
            # check if tree/subtree is balance or not returns false immediately if either one side returns false
            isBalance = (
                            traverseLeft[0] and
                            traverseRight[0] and
                            abs(traverseRight[1] - traverseLeft[1]) <= 1
                        )
            
            return [isBalance, 1 + max(traverseLeft[1], traverseRight[1])]
        
        return helper(root)[0]
            