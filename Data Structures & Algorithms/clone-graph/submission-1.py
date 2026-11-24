"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # mapping to avoid visiting same node again, bcoz same node can be neighbor of multiple nodes
        oldCopyToNew = {}

        def dfs(node):
            if node in oldCopyToNew:
                return oldCopyToNew[node]

            newCopyNode = Node(val=node.val)
            oldCopyToNew[node] = newCopyNode

            for neighbor in node.neighbors:
                neighborCopy = dfs(neighbor) # this step will make copy of neighbor nodes also
                newCopyNode.neighbors.append(neighborCopy) # append new copied neighbors

            return newCopyNode

        return dfs(node) if node else None