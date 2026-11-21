class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # assume trust list as the graph node edges list, we can find out outdegree and indegree of these
        # nodes here by representing person's trust to edge going to other person i.e. for `trust[i] = [ai, bi]`
        # if a1 trusts b1 that means there's direct edge from person 'ai' to 'bi'.
        # Judge will be someon with indegree=n-1 and outdegree=0

        inDegreeMap, outDegreeMap = [0]*(n+1), [0]*(n+1)

        for ai,bi in trust:
            inDegreeMap[bi] += 1
            outDegreeMap[ai] += 1

        for i in range(n+1):
            if i != 0 and inDegreeMap[i] == n-1 and outDegreeMap[i] == 0:
                return i

        return -1