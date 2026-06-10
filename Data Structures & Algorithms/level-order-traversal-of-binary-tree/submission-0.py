# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q, res = deque(), []
        q.append(root)

        while q:
            lvl = []
            lvlSize = len(q) # no. of nodes on certain level
            for _ in range(lvlSize):
                curr = q.popleft()
                # append curr node's child if exist (for traversing the next level in next iteration)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                lvl.append(curr.val)
            res.append(lvl)
            
        return res