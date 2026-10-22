class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edgeLength = len(edges)

        def detectCycleBFS(src):
            visited[src] = True
            q = deque()
            q.append((src,-1))
            while q:
                node, parent = q.pop()

                for neighbor in adjList[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((neighbor, node))
                    ## visited before but not a parent => cycle (came from different path still met 
                    ## again while traversing)
                    elif parent != neighbor:
                        return True

            return False

        adjList = [[] for _ in range(edgeLength+1)]
        for a1,b1 in edges:
            adjList[a1].append(b1)
            adjList[b1].append(a1)
            visited = [False]*(edgeLength+1)

            if detectCycleBFS(a1):
                ## While adding edges one by one, the first edge that creates a cycle is the redundant connection.
                return [a1,b1]

        return []