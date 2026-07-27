class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.topoSort(numCourses, prerequisites)
    
    def topoSort(self, V, edges):
        adj = {i:[] for i in range(V)}
        
        # Kahn Algorithm (BFS)
        indegree = [0] * V
        for u,v in edges:
            adj[v].append(u)
            indegree[u] += 1
            
        q = deque()
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
          
        while q:
            node = q.popleft()
            res.append(node)
            
            ## node is in toposort (res) now, so remove it from indegree
            ## i.e. decrement its indegree by 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            
        
        return res