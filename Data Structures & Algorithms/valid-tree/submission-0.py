class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A graph is a valid tree if:
        ## It has no cycles
        ## It is fully connected
        adjacencyList = {i: [] for i in range(n)}
        for u,v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        visited = set()

        def dfs(currNode, prevNode):
            if currNode in visited:
                return False

            visited.add(currNode)
            for neighbor in adjacencyList[currNode]:
                if neighbor == prevNode:
                    continue

                if not dfs(neighbor, currNode): # If there's any cycle present in graph
                    return False

            return True

        return dfs(0, -1) and n == len(visited)