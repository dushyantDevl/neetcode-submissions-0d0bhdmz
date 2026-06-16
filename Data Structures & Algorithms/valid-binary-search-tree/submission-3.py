# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inValidRange(node: Optional[TreeNode], greatestLowerBound, leastUpperBound) -> bool:
            if not node:
                return True
            
            # If the current node is not in valid range
            if not greatestLowerBound < node.val < leastUpperBound:
                return False
            
            return (
                    # value of left child (node.left) should be less than its parent (node.val)
                    inValidRange(node.left, greatestLowerBound, node.val) 
                        and
                    # value of right child (node.right) should be greater than its parent (node.val)
                    inValidRange(node.right, node.val, leastUpperBound)
                )

        return inValidRange(root, float('-inf'), float('inf'))
                