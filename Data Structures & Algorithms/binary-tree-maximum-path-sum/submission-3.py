# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Prerequisite: Find max height and max width of tree
        res = float('-inf')
        
        def maxPathSumDFS(node):
            nonlocal res
            if not node:
                return 0

            # Traverse to left and right subtree
            ## To ignore the left or right max sum with negative value and just take the 
            ## current node itself (not left or right node) we can find max from 0 and node value
            ## since 0 is greater than any negative value coming from left or right path sum
            leftMax = max(0, maxPathSumDFS(node.left))
            rightMax = max(0, maxPathSumDFS(node.right))

            # Now while backtracking update the max path sum
            ## finds the max path going from particular node (at each split curve)
            res = max(res, leftMax + rightMax + node.val)

            # Returns the max path from each node
            ## max(leftMax, rightMax) will make sure it takes the max path sum and not both 
            ## the split path, bcoz then its not defined as path (since it visits nodes more than once)
            return node.val + max(leftMax, rightMax)
        
        maxPathSumDFS(root)
        return res
        