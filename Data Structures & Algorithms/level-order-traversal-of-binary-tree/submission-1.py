# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, lvl):
            if not node:
                return None

            if len(res) == lvl: # add empty list only when the particular node is at new level
                res.append([])
            
            ## store the current node's value before going to next level, it'll take care of
            ## appending left node first since we traverse to left and then right subtree in 
            ## recursion calls 
            res[lvl].append(node.val) 

            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)

        dfs(root, 0)
        return res