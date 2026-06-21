# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        traversal = []
        
        def dfs(root):
            if root:
                dfs(root.left)
                traversal.append(root.val)
                dfs(root.right)
        
        dfs(root)

        res = float('-inf')
        for i in range(len(traversal)):
            currSum = 0
            for j in range(i, len(traversal)):
                currSum += traversal[j]
                res = max(res, currSum)
        
        return res
