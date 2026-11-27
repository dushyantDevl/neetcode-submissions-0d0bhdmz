"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        ogToClone = {} # keep track of cloned node (to avoid duplicate by not visiting same node again)

        def bfs(ogNode: Optional['Node']):
            clonedNode = Node(val=ogNode.val)
            ogToClone[ogNode] = clonedNode
            
            # put the og node in queue to also visit its neighbors (to make thier clones)
            q = deque([ogNode]) 

            while q:
                currClonedNode = q.popleft()

                for neighbor in currClonedNode.neighbors:
                    # append in queue only if its not yet visited and also make their clone
                    if neighbor not in ogToClone:
                        ogToClone[neighbor] = Node(val=neighbor.val) # mark visited
                        q.append(neighbor)
                    
                    ## add neighbors of cloned node too, irrespective of if they are visited 
                    ## before or not bcoz here we're just adding neighbors of a node and 
                    ## neighbors can be common among nodes in graph
                    ogToClone[currClonedNode].neighbors.append(ogToClone[neighbor])
        
        bfs(node)
        return ogToClone[node]


