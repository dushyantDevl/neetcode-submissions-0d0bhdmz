class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courseOrder = self.topoSort(numCourses, prerequisites)
        res = []
        for a,b in queries:
            a_loc = courseOrder.index(a)
            b_loc = courseOrder.index(b)
            res.append(a_loc < b_loc)
        
        return res

    def topoSort(self, V:int, edges:List[List[int]]):
        adj = {i:[] for i in range(V)}

        indegrees = [0]*V
        for u,v in edges:
            adj[u].append(v)
            indegrees[v] += 1
        
        q = deque()
        for i in range(V):
            if indegrees[i] == 0:
                q.append(i)

        res = []
          
        while q:
            node = q.popleft()
            res.append(node)
            
            ## node is in toposort (res) now, so remove it from indegree
            ## i.e. decrement its indegree by 1
            for neighbor in adj[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
            
        return res