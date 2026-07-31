class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # for a connected undirected graph with no self loop and no cycle it must've
        ## n nodes
        ## n-1 edges
        # if this graph has n edges then it implies it has will contain cycle, 
        # therfore to solve this we've to do cycle detection

        # Using Union Find method:
        ## We don't even need the rank array for this problem, since we traverse the edges 
        ## and assign parents with path compression, it is guaranteed the first path where 
        ## the rank is greater will be the cycle, so we can return False from there itself

        E = len(edges)
        parent = [i for i in range(E+1)] # initially, each node is its own parent 
        
        def findRootParent(node):
            if parent[node] != node:
                parent[node] = findRootParent(parent[node])
            return parent[node]

        def union(u, v):
            uParent, vParent = findRootParent(u), findRootParent(v)

            if uParent == vParent:
                return False

            parent[uParent] = vParent

            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]

        return []