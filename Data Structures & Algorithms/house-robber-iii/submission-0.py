# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def maxRobDFS(curr):
            if not curr:
                return (0, 0)
            
            leftPair = maxRobDFS(curr.left)
            rightPair = maxRobDFS(curr.right)

            # After all the recursion calls (i.e starting from leaf nodes then traverse 
            # up to root node) we decide to pick or not pick the current node

            # If we include the current node we're at then then can't pick the one's on 
            # very next/prev level, that's why include the withoutCurrNode
            withCurrNode = curr.val + leftPair[1] + rightPair[1]

            # If we aren't including the current node then we can choose either of left or right
            # pair, so just pick the one with max money
            withoutCurrNode = max(leftPair) + max(rightPair)

            return withCurrNode, withoutCurrNode

        return max(maxRobDFS(root))