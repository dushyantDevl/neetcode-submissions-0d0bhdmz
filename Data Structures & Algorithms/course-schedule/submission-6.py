class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Using Kahn's Algorithm (BFS)
        ## if the graph forms is Directed Acyclic graph then toposort is possible i.e. all courses can be finished

        adjList = {i: [] for i in range(numCourses)} # key:course, value: all its prerequisites
        inDegree = [0]*numCourses
        for course, prerequisite in prerequisites:
            adjList[prerequisite].append(course)
            inDegree[course] += 1

        q = deque([i for i in range(numCourses) if inDegree[i]==0])
        numNodesInToposort = 0
        while q:
            node = q.popleft()
            numNodesInToposort += 1

            for neighbor in adjList[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)


        return numNodesInToposort == numCourses