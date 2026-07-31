class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {i:[] for i in range(n)}
        for u,v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)
        vis = set()
        def dfs(node):
            vis.add(node)
            for neighbors in adjacencyList[node]:
                if neighbors not in vis:
                    dfs(neighbors)

        res = 0

        for i in range(n):
            if i in vis: continue
            res += 1
            dfs(i)

        return res
            