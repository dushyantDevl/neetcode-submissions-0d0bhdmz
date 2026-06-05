# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stk = [], []
        temp = root

        while temp or stk:
            while temp:
                stk.append(temp)
                temp = temp.left
            temp = stk.pop()
            res.append(temp.val)
            temp = temp.right
        
        return res