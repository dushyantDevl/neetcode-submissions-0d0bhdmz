"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNewMap = {}

        def dfs(node):
            if node in oldToNewMap: # Already made a clone of the node (Also work as visited map)
                return oldToNewMap[node]

            nodeClone = Node(val=node.val) # just a value clone of node (doesn't have neighbors yet)
            oldToNewMap[node] = nodeClone

            # check for neighbors of old node to add in new cloned one
            for neighbor in node.neighbors:
                nodeClone.neighbors.append(dfs(neighbor))

            return nodeClone

        return dfs(node) if node else None
