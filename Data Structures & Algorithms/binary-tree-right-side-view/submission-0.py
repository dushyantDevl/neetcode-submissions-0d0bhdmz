# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
            # append only the last element of the level which is the rightmost node of any level
            res.append(lvl[-1])
            
        return res
        