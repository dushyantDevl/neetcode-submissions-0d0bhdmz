# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pAncestors, qAncestors = [], []
        self.nodeAncestor(root, p, pAncestors)
        self.nodeAncestor(root, q, qAncestors)

        for i in range(len(pAncestors)-1,-1,-1):
            if pAncestors[i] in qAncestors:
                return pAncestors[i]


    def nodeAncestor(self, root: TreeNode, node:TreeNode, stk:list[TreeNode]):
        if not root:
            return
        stk.append(root)
        if root.val > node.val:
            self.nodeAncestor(root.left, node, stk)
        if root.val < node.val:
            self.nodeAncestor(root.right, node, stk)
