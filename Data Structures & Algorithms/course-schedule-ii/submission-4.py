class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # We just have to find a valid Toposort order

        # Using Kahn's algorithm (BFS)   
        adjList = {i:[] for i in range(numCourses)}
        inDegree = [0]*numCourses

        for course, prerequisite in prerequisites:
            adjList[prerequisite].append(course)
            inDegree[course] += 1

        q = deque([course for course in range(numCourses) if inDegree[course]==0])
        res = []
        
        while q:
            prerequisite = q.popleft()
            res.append(prerequisite)

            for course in adjList[prerequisite]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    q.append(course)

        return res