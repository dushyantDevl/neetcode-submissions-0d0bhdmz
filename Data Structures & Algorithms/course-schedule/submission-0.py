class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make a adjacency list using prerequisites to make course-prerequisites graph
        prerequisiteMap = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisiteMap[course].append(prerequisite)

        vis = set()

        def dfs(course):
            if course in vis: # back to the same graph again
                return False

            if prerequisiteMap[course] == []: # course with no prerequisites
                return True

            vis.add(course)
            for prerequisite in prerequisiteMap[course]:
                if not dfs(prerequisite):
                    return False
            
            vis.remove(course)
            prerequisiteMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True