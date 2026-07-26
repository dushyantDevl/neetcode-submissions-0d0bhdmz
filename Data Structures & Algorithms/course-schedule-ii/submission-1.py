class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # This problem is based on topological sort
        adjacencyList = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adjacencyList[crs].append(pre)

        # A course has 3 possible states:
        ## visited -> crs has been added to output
        ## visiting -> crs not added to output, but added to cycle
        ## unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            # no need to check for already visited course since we've checked it and added in required output order
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in adjacencyList[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output