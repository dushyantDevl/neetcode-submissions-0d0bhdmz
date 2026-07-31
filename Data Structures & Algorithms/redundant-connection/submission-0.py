from abc import update_abstractmethods
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # for a connected undirected graph with no self loop and no cycle it must've
        ## n nodes
        ## n-1 edges
        # if this graph has n edges then it implies it has will contain cycle, 
        # therfore to solve this we've to do cycle detection

        # Using Union Find method:
        E = len(edges)
        parent = [i for i in range(E+1)] # initially, each node is its own parent 
        rank = [1] * (E+1) # more rank means above in heirarchy
        
        def findRootParent(node):
            if parent[node] != node:
                parent[node] = findRootParent(parent[node])
            return parent[node]

        def union(u, v):
            uParent, vParent = findRootParent(u), findRootParent(v)
            if uParent == vParent: # either a root node or topmost hierarchical node
                return False

            if rank[uParent] > rank[vParent]:
                parent[vParent] = uParent
                rank[uParent] += rank[vParent]
            else:
                parent[uParent] = vParent
                rank[vParent] += rank[uParent]

            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]

        return []