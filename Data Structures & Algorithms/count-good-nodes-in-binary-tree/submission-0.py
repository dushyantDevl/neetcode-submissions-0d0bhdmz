# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Root node is also considered as good node since there aren't any node greater than root
        # on its path (its the only node in path)
        
        # preorder traversal but instead of storing node value, update the max Value at each path
        def dfs(node, maxSoFar):
            if not node:
                return 0

            res = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            res += dfs(node.left, maxSoFar)
            res += dfs(node.right, maxSoFar)

            return res

        return dfs(root, root.val)