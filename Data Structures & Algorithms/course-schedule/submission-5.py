class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)} # key:course, value: all its prerequisites
        for course,prerequisite in prerequisites:
            adjList[course].append(prerequisite)

        visited = [False] * numCourses

        def dfs(course):
            if visited[course]:
                return False
            
            if not adjList[course]: # if course has no prerequisites
                return True

            visited[course] = True

            for prerequisite in adjList[course]:
                if not dfs(prerequisite):
                    return False

            visited[course] = False
            adjList[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
