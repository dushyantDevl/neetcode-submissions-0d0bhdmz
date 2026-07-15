class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [[0,0]] * (n+1)
        for pair in trust:
            ai, bi = pair[0], pair[1]
            
            inDegree, outDegree = degree[ai]
            outDegree += 1
            degree[ai] = [inDegree, outDegree]

            inDegree, outDegree = degree[bi]
            inDegree += 1
            degree[bi] = [inDegree, outDegree]

        for i in range(n+1):
            if degree[i][0] == n-1 and degree[i][1] == 0:
                return i
        
        return -1