class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        # # stores the prerequisite of each course in set (for faster search)
        isPrereq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                isPrereq[neighbor].add(node)
                # Add the prerequisite of node also bcoz before going to its neighbor
                # you also have to go through the prerequisite of the node itself
                # e.g course '3' can have a course '1' as prerequisite but to complete the '1'
                # itself you might have to complete course '0' too (or can be any other course)
                isPrereq[neighbor].update(isPrereq[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return [u in isPrereq[v] for u, v in queries]