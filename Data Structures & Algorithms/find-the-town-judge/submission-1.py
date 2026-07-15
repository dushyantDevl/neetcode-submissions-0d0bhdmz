class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [[0,0]] * (n+1)
        for pair in trust:
            ai, bi = pair[0], pair[1]
            
            # inDegree means a node (person) is trusting someone, 
            ## i.e. forming directive edge towards other node (person)

            # outDegree means node (person) is trusted by someone,
            ## i.e. incoming edge from other node (person)

            inDegree, outDegree = degree[ai]
            outDegree += 1
            degree[ai] = [inDegree, outDegree]

            inDegree, outDegree = degree[bi]
            inDegree += 1
            degree[bi] = [inDegree, outDegree]

        for i in range(n+1):
            # Judge trusted by everyone except him and Judge trusts nobody
            if degree[i][0] == n-1 and degree[i][1] == 0:
                return i
        
        return -1